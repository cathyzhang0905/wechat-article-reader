# wechat-article-reader

A [Claude Code](https://claude.ai/code) skill that gives Claude the ability to **read** and **search** WeChat public account articles — no token, no login required.

一个 [Claude Code](https://claude.ai/code) skill，让 Claude 具备**阅读**和**搜索**微信公众号文章的能力——无需 token，无需登录。

---

## Capabilities / 核心能力

| | English | 中文 |
|---|---|---|
| 📖 **Read** | Fetch and parse any public WeChat article from a URL | 抓取并解析任意公开微信文章 |
| 🔍 **Search** | Search WeChat articles by topic, then read the top results | 按话题搜索公众号文章并读取正文 |
| ⚡ **Cache** | Repeat fetches are instant — results cached locally | 重复抓取秒返回，结果本地缓存 |

---

## How It Works / 工作原理

When you paste a WeChat article URL into Claude, Claude normally can't fetch it —
WeChat blocks requests from Anthropic's servers. This skill runs the fetch **locally on
your machine**, so WeChat sees a normal browser-like request and returns the content.

你直接把微信文章链接发给 Claude，Claude 是抓不到内容的——微信会屏蔽来自 Anthropic
服务器的请求。这个 skill 让抓取请求**在你本地机器上执行**，微信以为是普通用户在浏览器里
打开文章，正常返回内容。

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

### 📖 Read / 阅读

Paste any WeChat article URL — Claude will fetch, parse, and summarize it.

粘贴任意微信文章链接，Claude 自动抓取、解析、总结。

```
帮我读一下这篇文章：https://mp.weixin.qq.com/s/xxxxxxxx
```

```
总结一下这篇文章的核心观点：https://mp.weixin.qq.com/s/xxxxxxxx
```

### 🔍 Search / 搜索

Ask Claude to find WeChat articles on any topic. Claude will search, pick the most
relevant results, read each one, and synthesize a response.

让 Claude 搜索某个话题的公众号文章。Claude 会自动搜索、挑选、读取，并综合成回答。

```
帮我搜一下微信上关于 Claude Code 最佳实践的文章
```

```
看看微信公众号上有没有关于 XX 的内容
```

> **Trigger / 触发条件**：The skill activates when you explicitly mention WeChat or 公众号.
> 显式提到"微信"或"公众号"时触发，普通搜索不会误触发。

---

## License

MIT
