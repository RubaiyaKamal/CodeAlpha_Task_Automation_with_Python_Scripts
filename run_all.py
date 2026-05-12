"""
Run all three automation tasks in sequence.
"""

import os
import sys

BASE = os.path.dirname(__file__)


def run_task1():
    print("\n=== TASK 1a: Move .jpg files ===")
    sys.path.insert(0, os.path.join(BASE, "task1_move_images"))
    from move_images import move_jpg_files

    source = os.path.join(BASE, "task1_move_images", "sample_folder")
    dest = os.path.join(BASE, "task1_move_images", "images_output")
    count = move_jpg_files(source, dest)
    print(f"Result: {count} file(s) moved.")


def run_task2():
    print("\n=== TASK 1b: Extract emails ===")
    sys.path.insert(0, os.path.join(BASE, "task2_extract_emails"))
    from extract_emails import extract_emails

    inp = os.path.join(BASE, "task2_extract_emails", "sample_emails.txt")
    out = os.path.join(BASE, "task2_extract_emails", "extracted_emails.txt")
    found = extract_emails(inp, out)
    for e in found:
        print(f"  {e}")
    print(f"Result: {len(found)} email(s) extracted.")


def run_task3():
    print("\n=== TASK 1c: Scrape webpage title ===")
    sys.path.insert(0, os.path.join(BASE, "task3_scrape_title"))
    from scrape_title import scrape_title

    out = os.path.join(BASE, "task3_scrape_title", "scraped_title.txt")
    title = scrape_title("https://books.toscrape.com/", out)
    print(f"Result: '{title}'")


if __name__ == "__main__":
    run_task1()
    run_task2()
    run_task3()
    print("\nAll tasks completed.")
