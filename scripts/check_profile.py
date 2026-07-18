from pathlib import Path


README = Path("README.md")

REQUIRED_TEXT = [
    "https://github.com/moroshani/Dominoyar",
    "https://github.com/moroshani/setadinfo",
    "https://github.com/moroshani/solar-hijri-calendar-component",
    "moroshaniofficial@gmail.com",
    "https://www.linkedin.com/in/moroshaniofficial/",
    "https://t.me/moroshaniofficial",
    "Persian",
    "RTL",
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


def main() -> None:
    if not README.exists():
        raise SystemExit("README.md is missing")

    text = README.read_text(encoding="utf-8")
    failures = []

    for item in REQUIRED_TEXT:
        if item not in text:
            failures.append(f"Missing required profile text: {item}")

    for item in FORBIDDEN_TEXT:
        if item in text:
            failures.append(f"Forbidden public profile text found: {item}")

    if failures:
        raise SystemExit("\n".join(failures))

    print("Profile README check passed.")


if __name__ == "__main__":
    main()
