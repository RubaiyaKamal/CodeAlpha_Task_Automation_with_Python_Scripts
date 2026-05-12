"""
Task 1b — Extract all email addresses from a .txt file and save them to another file.
Uses: re, file handling
"""

import re


EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)


def extract_emails(input_path: str, output_path: str) -> list[str]:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    emails = sorted(set(EMAIL_PATTERN.findall(text)))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(emails) + "\n")

    return emails


if __name__ == "__main__":
    import os

    base = os.path.dirname(__file__)
    input_file = os.path.join(base, "sample_emails.txt")
    output_file = os.path.join(base, "extracted_emails.txt")

    print(f"Input : {input_file}")
    print(f"Output: {output_file}")
    print("-" * 40)

    found = extract_emails(input_file, output_file)

    for email in found:
        print(f"  {email}")

    print("-" * 40)
    print(f"Done. {len(found)} unique email(s) saved to '{output_file}'.")
