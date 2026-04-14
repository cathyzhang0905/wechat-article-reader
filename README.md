# wechat-article-reader

A [Claude Code](https://claude.ai/code) skill that lets Claude read and search WeChat public account articles on your behalf.

一个 [Claude Code](https://claude.ai/code) skill，让 Claude 帮你阅读、搜索和总结微信公众号文章。

---

## How It Works / 工作原理

When you paste a WeChat article URL into Claude, Claude normally can't fetch it —
WeChat blocks requests from Anthropic's servers. This skill runs the fetch **locally on
your machine**, so WeChat sees a normal browser-like request and returns the content.

你直接把微信文章链接发给 Claude，Claude 是抓不到内容的——微信会屏蔽来自 Anthropic
服务器的请求。这个 skill 让抓取请求**在你本地机器上执行**，微信以为是普通用户在浏览器里
打开文章，就会正常返回内容。

**No token or login required. / 不需要 token，不需要登录微信后台。**

Only works with public share URLs (`mp.weixin.qq.com/s/...`).
仅支持公开分享链接（`mp.weixin.qq.com/s/...`），不支持仅关注者可见的文章。

---

## Requirements / 环境要求

- [Claude Code](https://claude.ai/code) CLI installed
- Python 3.9+

---

## Installation / 安装

```bash
# 1. Clone into your Claude skills directory
#    把仓库 clone 到 Claude skills 目录
git clone https://github.com/cathyzhang0905/wechat-article-reader \
  ~/.claude/skills/wechat-article-reader

# 2. Run setup (creates a virtualenv and installs dependencies)
#    运行安装脚本（创建虚拟环境并安装依赖）
cd ~/.claude/skills/wechat-article-reader
chmod +x setup.sh && ./setup.sh
```

That's it. / 安装完成。

---

## Usage / 使用方法

### Mode 1: Read a given URL / 读取指定文章

Paste a WeChat article URL and ask Claude to read or summarize it.

把微信文章链接发给 Claude，让它帮你阅读或总结。

> 帮我读一下这篇文章：https://mp.weixin.qq.com/s/xxxxxxxx

### Mode 2: Search WeChat articles / 搜索公众号文章

Ask Claude to search for WeChat articles on a topic. Claude will search
`site:mp.weixin.qq.com`, pick the most relevant results, fetch them, and
synthesize the content into a response.

让 Claude 搜索某个话题的微信公众号文章。Claude 会自动搜索、挑选相关链接、
读取正文并综合成回答。

> 帮我搜一下微信上关于 Claude Code 最佳实践的文章

> 看看微信公众号上有没有关于 XX 的内容

The skill triggers when you explicitly mention WeChat / 公众号 in your request.
说到"微信"、"公众号"时 skill 会自动触发，普通搜索不会误触发。

---

## Caching / 缓存

Fetched articles are cached in `article_cache.json`. Re-fetching the same URL is instant.

抓取过的文章会缓存到 `article_cache.json`，重复请求同一链接无需再次网络请求。

---

## License

MIT
