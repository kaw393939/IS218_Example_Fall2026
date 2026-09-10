"""Check this course's inline Markdown links, fences, and shell syntax."""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def inspect_markdown(path):
    lines = []
    blocks = []
    fence = None
    language = ""
    body = []
    for line in path.read_text().splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker and fence is None:
            fence = marker[1]
            language = marker[2].strip()
            body = []
        elif marker and fence and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
            blocks.append((language, "\n".join(body)))
            fence = None
        elif fence:
            body.append(line)
        else:
            lines.append(line)
    return "\n".join(lines), blocks, fence is not None


def heading_ids(text):
    found = set()
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        candidate = slug
        index = 0
        while candidate in found:
            index += 1
            candidate = f"{slug}-{index}"
        found.add(candidate)
    return found


def check(root):
    paths = sorted(p for p in root.rglob("*.md") if not any(part.startswith(".") for part in p.relative_to(root).parts))
    parsed = {p.resolve(): inspect_markdown(p) for p in paths}
    errors = []
    for path in paths:
        text, blocks, unclosed = parsed[path.resolve()]
        label = path.relative_to(root)
        if unclosed:
            errors.append(f"{label}: unclosed code fence")
        for language, code in blocks:
            if language in {"sh", "bash"}:
                result = subprocess.run(["bash", "-n"], input=code, text=True, capture_output=True)
                if result.returncode:
                    errors.append(f"{label}: shell syntax: {result.stderr.strip()}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            link = urlsplit(target)
            if link.scheme or link.netloc:
                continue
            destination = (path.parent / unquote(link.path)).resolve() if link.path else path.resolve()
            if not destination.exists():
                errors.append(f"{label}: missing target {target}")
            elif link.fragment and destination.suffix == ".md":
                target_text = parsed.get(destination, inspect_markdown(destination))[0]
                if unquote(link.fragment) not in heading_ids(target_text):
                    errors.append(f"{label}: missing heading {target}")
    return paths, errors


if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    paths, errors = check(root)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"Checked {len(paths)} Markdown pages: local links, heading fragments, fences, and shell syntax passed.")
