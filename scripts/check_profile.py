import re
from pathlib import Path
from urllib.parse import urlparse


README = Path("README.md")
OPEN_SOURCE = Path("OPEN_SOURCE.md")

README_REQUIRED = [
    "Independent software developer",
    "## Owned Work",
    "## Selected Upstream Results",
    "## Technical Focus",
    "## Working Practice",
    "## Contact",
    "https://github.com/moroshani/Dominoyar",
    "https://github.com/moroshani/setadinfo",
    "https://moroshani.github.io/setadinfo/",
    "https://github.com/moroshani/solar-hijri-calendar-component",
    "https://moroshani.github.io/solar-hijri-calendar-component/",
    "https://github.com/pandas-dev/pandas/pull/66600",
    "https://github.com/persian-calendar/persian-calendar/pull/1879",
    "https://github.com/floci-io/floci/pull/2268",
    "https://github.com/influxdata/docs-v2/pull/7524",
    "https://github.com/nanlabs/frontend-reference/pull/139",
    "moroshaniofficial@gmail.com",
    "https://www.linkedin.com/in/moroshaniofficial/",
    "https://t.me/moroshaniofficial",
    "Codex",
]

OPEN_SOURCE_REQUIRED = [
    "## Owned And Maintained",
    "## Merged Upstream Work",
    "## Work Under Review",
    "## Maintainer Handoff",
    "https://github.com/pandas-dev/pandas/pull/66601",
    "https://github.com/pandas-dev/pandas/pull/66603",
    "https://github.com/storybookjs/mcp/pull/366",
    "https://github.com/usemoss/moss/pull/438",
    "https://github.com/apilens/apilens/pull/207",
    "https://github.com/openeverest/openeverest/pull/3002",
    "https://github.com/persian-calendar/persian-calendar/issues/1256",
]

OPEN_WORK_LINKS = [
    "https://github.com/pandas-dev/pandas/pull/66601",
    "https://github.com/pandas-dev/pandas/pull/66603",
    "https://github.com/storybookjs/mcp/pull/366",
    "https://github.com/usemoss/moss/pull/438",
    "https://github.com/apilens/apilens/pull/207",
    "https://github.com/openeverest/openeverest/pull/3002",
]

FORBIDDEN = [
    "gho_",
    "github_pat_",
    "BEGIN OPENSSH PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
    "/mnt/c/Projects",
    "C:\\Projects",
    "Dominoyar-source",
    "TODO",
]

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_required(text: str, required: list[str], label: str) -> list[str]:
    return [f"Missing required {label} text: {item}" for item in required if item not in text]


def check_local_links(path: Path, text: str) -> list[str]:
    failures = []
    for target in MARKDOWN_LINK.findall(text):
        parsed = urlparse(target)
        if parsed.scheme or target.startswith("#"):
            continue
        clean_target = target.split("#", 1)[0]
        if clean_target and not (path.parent / clean_target).exists():
            failures.append(f"Broken local link in {path}: {target}")
    return failures


def main() -> None:
    failures = []
    for path in (README, OPEN_SOURCE):
        if not path.exists():
            failures.append(f"{path} is missing")

    if failures:
        raise SystemExit("\n".join(failures))

    readme_text = README.read_text(encoding="utf-8")
    open_source_text = OPEN_SOURCE.read_text(encoding="utf-8")

    failures.extend(check_required(readme_text, README_REQUIRED, "profile"))
    failures.extend(check_required(open_source_text, OPEN_SOURCE_REQUIRED, "open-source"))

    for item in OPEN_WORK_LINKS:
        if item in readme_text:
            failures.append(f"Open work must not appear in the profile README: {item}")

    for item in FORBIDDEN:
        if item in readme_text or item in open_source_text:
            failures.append(f"Forbidden public profile text found: {item}")

    failures.extend(check_local_links(README, readme_text))
    failures.extend(check_local_links(OPEN_SOURCE, open_source_text))

    if failures:
        raise SystemExit("\n".join(failures))

    print("Profile README check passed.")


if __name__ == "__main__":
    main()
