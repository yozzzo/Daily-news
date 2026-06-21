#!/usr/bin/env python3
"""
Fetches the latest news from RSS feeds and saves them as JSON files
organized by date under the news/ directory.

Usage:
    python scripts/fetch_news.py [--date YYYY-MM-DD]

If --date is omitted, today's date (UTC) is used.
"""

import argparse
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# RSS feed sources (no API key required)
# ---------------------------------------------------------------------------
RSS_SOURCES = [
    {
        "name": "Reuters Top News",
        "url": "https://feeds.reuters.com/reuters/topNews",
    },
    {
        "name": "BBC News",
        "url": "https://feeds.bbci.co.uk/news/rss.xml",
    },
    {
        "name": "NHK World (English)",
        "url": "https://www3.nhk.or.jp/rss/news/cat0.xml",
    },
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "news")
REQUEST_TIMEOUT = 15  # seconds


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_rss(url: str) -> ET.Element | None:
    """Download and parse an RSS feed. Returns the root element or None."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Daily-news-bot/1.0"},
        )
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            data = resp.read()
        return ET.fromstring(data)
    except Exception as exc:  # noqa: BLE001
        print(f"  [WARN] Failed to fetch {url}: {exc}", file=sys.stderr)
        return None


def parse_items(root: ET.Element, source_name: str) -> list[dict]:
    """Extract news items from an RSS 2.0 root element."""
    articles = []
    channel = root.find("channel")
    if channel is None:
        return articles

    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        description = (item.findtext("description") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()

        if not title:
            continue

        articles.append(
            {
                "title": title,
                "url": link,
                "description": description,
                "published_at": pub_date,
                "source": source_name,
            }
        )

    return articles


def save_news(date_str: str, articles: list[dict]) -> str:
    """Write articles to news/<date_str>.json and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"{date_str}.json")

    payload = {
        "date": date_str,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(articles),
        "articles": articles,
    }

    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    return output_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch daily news from RSS feeds.")
    parser.add_argument(
        "--date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="Target date in YYYY-MM-DD format (default: today UTC)",
    )
    args = parser.parse_args()

    date_str: str = args.date
    print(f"Fetching news for {date_str} …")

    all_articles: list[dict] = []

    for source in RSS_SOURCES:
        print(f"  Fetching from {source['name']} …")
        root = fetch_rss(source["url"])
        if root is None:
            continue
        items = parse_items(root, source["name"])
        print(f"    → {len(items)} articles")
        all_articles.extend(items)

    output_path = save_news(date_str, all_articles)
    print(f"Saved {len(all_articles)} articles to {output_path}")


if __name__ == "__main__":
    main()
