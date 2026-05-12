"""
Task 1c — Scrape the <title> of a fixed webpage and save it to a file.
Uses: requests, re, file handling
"""

import re
import requests


TARGET_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "scraped_title.txt"

TITLE_PATTERN = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def scrape_title(url: str, output_path: str) -> str:
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    match = TITLE_PATTERN.search(response.text)
    title = match.group(1).strip() if match else "No <title> found"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"URL  : {url}\n")
        f.write(f"Title: {title}\n")

    return title


if __name__ == "__main__":
    import os

    output = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)

    print("-" * 40)
    title = scrape_title(TARGET_URL, output)
    print(f"Title: {title}")
    print("-" * 40)
    print(f"Done. Result saved to '{output}'.")
