#!/usr/bin/env python3
# HSReplay top deck scraper using Playwright

from playwright.sync_api import sync_playwright
import json

URL = "https://hsreplay.net/decks/"


def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)
        page.wait_for_timeout(3000)

        # Try clicking "Copy Deck" on first deck
        try:
            page.click("text=Copy Deck")
            page.wait_for_timeout(1000)
            deck_code = page.evaluate("navigator.clipboard.readText()")
        except:
            deck_code = None

        result = {
            "deck_code": deck_code
        }

        browser.close()
        return result


if __name__ == "__main__":
    data = scrape()
    print(json.dumps(data, indent=2))
