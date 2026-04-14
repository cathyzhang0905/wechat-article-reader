"""
fetch.py - Fetch and parse WeChat public article content
No authentication required. Works with public share URLs (mp.weixin.qq.com/s/...)
"""
import json
import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 15
CACHE_FILE = Path(__file__).parent / "article_cache.json"


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_cache(cache: dict):
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def get_article_content(url: str) -> dict:
    """
    Fetch a public WeChat article URL and extract its text content.

    Args:
        url: Public WeChat article URL (mp.weixin.qq.com/s/...)

    Returns:
        dict with keys:
            - text: article body (up to 15000 chars)
            - images: list of image URLs (up to 5)
    """
    cache = _load_cache()
    if url in cache:
        logger.info(f"Cache hit: {url[:60]}")
        return cache[url]

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
        }
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        result = _parse_html(resp.text)

        if result.get("text", "").strip():
            cache[url] = result
            _save_cache(cache)

        return result
    except Exception as e:
        logger.error(f"Failed to fetch article: {url} - {e}")
        return {"text": "", "images": []}


def _parse_html(html: str) -> dict:
    """Extract plain text and image URLs from WeChat article HTML."""
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "lxml")

        for tag in soup(["script", "style", "meta", "link"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        clean_text = "\n".join(lines)

        images = []
        for img in soup.find_all("img"):
            src = img.get("data-src") or img.get("src", "")
            if src and src.startswith("http"):
                images.append(src)

        return {"text": clean_text[:15000], "images": images[:5]}
    except Exception as e:
        logger.error(f"HTML parse error: {e}")
        return {"text": html[:3000], "images": []}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python fetch.py <article_url>")
        sys.exit(1)
    result = get_article_content(sys.argv[1])
    print(result["text"])
