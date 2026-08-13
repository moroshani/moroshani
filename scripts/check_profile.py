from pathlib import Path


README = Path("README.md")
OPEN_SOURCE = Path("OPEN_SOURCE.md")

REQUIRED_TEXT = [
    "https://github.com/moroshani/Dominoyar",
    "https://github.com/moroshani/setadinfo",
    "https://moroshani.github.io/setadinfo/",
    "https://github.com/moroshani/solar-hijri-calendar-component",
    "https://moroshani.github.io/solar-hijri-calendar-component/",
    "https://github.com/persian-calendar/persian-calendar/pull/1879",
    "https://github.com/pandas-dev/pandas/pull/66600",
    "https://github.com/pandas-dev/pandas/pull/66601",
    "https://github.com/pandas-dev/pandas/pull/66603",
    "https://github.com/floci-io/floci/pull/2268",
    "https://github.com/nanlabs/frontend-reference/pull/139",
    "https://github.com/storybookjs/mcp/pull/366",
    "https://github.com/usemoss/moss/pull/438",
    "https://github.com/apilens/apilens/pull/207",
    "https://github.com/influxdata/docs-v2/pull/7524",
    "moroshaniofficial@gmail.com",
    "https://www.linkedin.com/in/moroshaniofficial/",
    "https://t.me/moroshaniofficial",
    "Codex",
    "AI tools",
    "Persian",
    "RTL",
    "Python",
    "## Projects I Build and Maintain",
    "## Contributions to Other Projects",
]

FORBIDDEN_TEXT = [
    "gho_",
    "github_pat_",
    "BEGIN OPENSSH PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
    "/mnt/c/Projects",
    "C:\\Projects",
    "Dominoyar-source",
    "TODO",
    "Add your preferred contact",
]

OPEN_SOURCE_REQUIRED_TEXT = [
    "Mohammad Mehdi Roshani",
    "https://github.com/moroshani/setadinfo",
    "https://moroshani.github.io/setadinfo/",
    "https://github.com/moroshani/solar-hijri-calendar-component",
    "https://moroshani.github.io/solar-hijri-calendar-component/",
    "https://github.com/persian-calendar/persian-calendar/pull/1879",
    "Codex",
    "no external users",
]


def main() -> None:
    if not README.exists():
        raise SystemExit("README.md is missing")

    text = README.read_text(encoding="utf-8")
    if not OPEN_SOURCE.exists():
        raise SystemExit("OPEN_SOURCE.md is missing")

    open_source_text = OPEN_SOURCE.read_text(encoding="utf-8")
    failures = []

    for item in REQUIRED_TEXT:
        if item not in text:
            failures.append(f"Missing required profile text: {item}")

    for item in FORBIDDEN_TEXT:
        if item in text or item in open_source_text:
            failures.append(f"Forbidden public profile text found: {item}")

    for item in OPEN_SOURCE_REQUIRED_TEXT:
        if item not in open_source_text:
            failures.append(f"Missing required open-source text: {item}")

    if failures:
        raise SystemExit("\n".join(failures))

    print("Profile README check passed.")


if __name__ == "__main__":
    main()
