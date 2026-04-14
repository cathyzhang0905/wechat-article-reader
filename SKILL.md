---
name: wechat-article-reader
description: Use when (1) the user shares a WeChat article URL (mp.weixin.qq.com), or (2) the user explicitly asks to look at WeChat public accounts or find WeChat articles on a topic (e.g. "看看微信上有没有", "搜一下公众号", "微信上的相关文章").
---

# WeChat Article Reader

## Overview

Fetch WeChat article content by running a local Python script on the user's machine.
This works without authentication for public articles — the request comes from the user's
own IP with browser-like headers, so WeChat treats it as a normal browser visit.

## Mode 1: Read a Given URL

When the user shares a WeChat article link:

```bash
~/.claude/skills/wechat-article-reader/.venv/bin/python \
  ~/.claude/skills/wechat-article-reader/fetch.py \
  "ARTICLE_URL_HERE"
```

Replace `ARTICLE_URL_HERE` with the actual URL from the user's message.

## Mode 2: Search + Read (for Research Tasks)

When the user wants to find WeChat articles on a topic:

1. **Search** using WebSearch with `site:mp.weixin.qq.com`:
   ```
   关键词 site:mp.weixin.qq.com
   ```
2. **Pick** 2–3 most relevant `mp.weixin.qq.com` links from results
3. **Fetch** each one using the command above
4. **Synthesize** content into the response

Use this mode proactively when doing Chinese-language research — WeChat public accounts
are a major source of practitioner knowledge that general web search often misses.

## Notes

- Results are cached in `article_cache.json` — repeat fetches of the same URL are instant
- Text is truncated to 8000 characters; images are extracted but rarely needed
- Only works with **public share URLs** (`mp.weixin.qq.com/s/...`) — not follower-only articles
- If fetch fails or returns empty text, ask the user to paste the content manually
- Never print the contents of any `.env` or auth files

## Why This Works (vs. Pasting the URL Directly to Claude)

When Claude fetches a URL via WebFetch, the request comes from Anthropic's servers —
WeChat blocks these as bots. This skill runs the fetch on the **user's local machine**,
so WeChat sees a normal browser-like request from a regular IP address.
