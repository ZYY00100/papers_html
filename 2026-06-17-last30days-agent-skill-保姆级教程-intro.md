# last30days：AI 帮你做全球热点知识追更的 43k stars 开源 skill 保姆级教程

> 从安装、第一次跑通，到 5 个真实场景配方 + v3 杀手级功能

---

## 一、这个 skill 解决什么问题

你想认真学一个东西——可能是 Nano Banana Pro 的 prompt 技巧，可能是 Polymarket 的赔率机制，可能是一个你完全不熟悉的开源项目——但打开浏览器就懵了。

教程、博客、推文、Reddit 长贴、YouTube 长视频、GitHub Issues、Hacker News 讨论……全都在说这个东西，但**散落在十几个平台、各说各的、互相矛盾**。你不可能一个一个平台去搜，更不可能花一整天去刷。

传统做法是：先 Google 一下，被 SEO 农场的过时文章骗一轮；再上 Reddit 找真实讨论，被淹没在不相关帖子里；最后 YouTube 找个最热门的视频，看完发现他说的是去年的事。

**"系统性了解一个东西最近 30 天的真实情况"——这件事，过去只能靠人肉。** 学得快的人要 2-3 小时，普通人根本不会去做。

last30days（GitHub：mvanhorn/last30days-skill）就是为这件事而生的：让你的 AI agent 并行去十几个平台（Reddit、X、YouTube、Hacker News、Polymarket、GitHub、TikTok、Bluesky……）搜过去 30 天的内容，按真实互动量（点赞、upvote、Polymarket 真金白银押注的赔率）排序，最后合成一份带引用的简报给你。

43,684 stars、3,593 forks、上过 GitHub Trending #1，作者 Matt Van Horn（mvanhorn）还在保持高强度迭代。**这可能是当下最被低估的"学习外挂"**——一个让 AI 替你读 30 天社交媒体、帮你研究一个话题的工具。

而且关键是：**不配任何 key 也能跑**——Reddit、Hacker News、Polymarket、GitHub 这四个数据源是开箱即用的。

这篇文章就把这个工具从 0 到 1 拆给你看，包括安装、跑通、加数据源、5 个真实学习/研究场景、v3 杀手级功能、踩坑速查。看完你应该能 15 分钟内自己跑起来第一次。

---

## 二、动手前需要搞懂的 3 个概念

虽然一上来就跑也行，但理解这 3 个词能帮你以后看官方文档不迷路。

**Agent Skills**：一种开放格式，把"AI agent 怎么干某件事"打包成 `SKILL.md` + 一组脚本，让任何支持这个格式的 AI 工具（Claude Code、Codex、Cursor、GitHub Copilot、Gemini CLI 等 50+ 个）都能用。last30days 就是其中一个 skill。

**Skill / Engine / Harness**：这是 last30days 仓库自己用的术语，记住就行——

| 词 | 含义 |
|---|---|
| **Skill** | 一个打包好的能力包，由 `SKILL.md`（给 AI 看的指令合同）+ `scripts/`（实际干活的代码）组成 |
| **Engine** | Skill 里那个真正干活的 Python 脚本（`scripts/last30days.py`），AI 调用它执行查询 |
| **Harness** | 装在哪个 AI 工具里跑。Claude Code 是最常见的 harness，但同一个 skill 在 Codex、Cursor 里也是同一份逻辑 |

**Keyless path vs Keyed path**：这个最重要。

- **Keyless path（零配置）**：用公开数据（Reddit 的公共 JSON、HN 的免费 API、Polymarket 的赔率、GitHub 的 star/API）以及本地 CLI（`gh`、`yt-dlp`），不需要你注册任何 API key。
- **Keyed path（要配 key）**：想搜 X、TikTok、Instagram、Threads、Pinterest 这种封闭平台，需要 API key 或浏览器 cookie。

**结论：先跑 Keyless path，95% 的场景够用了。** 等你真觉得"还想要 X / TikTok 的数据"，再来配 key。

---

## 三、三种安装方式（选你用的那一种）

打开终端（macOS 是 Terminal，Windows 是 PowerShell）。

### 方式 A：Claude Code 用户（推荐）

如果你用 Claude Code，直接在 Claude Code 里说：

```
/plugin marketplace add mvanhorn/last30days-skill
```

回车，Claude Code 自己会跑。然后再说：

```
/plugin install last30days
```

完事。装完会自动更新，以后作者发新版本你也不用管。

### 方式 B：Cursor / Codex / Copilot / Gemini CLI 等其他 50+ 工具

打开终端（注意不是工具里，是系统的终端）：

```bash
npx skills add mvanhorn/last30days-skill -g
```

`-g` 表示装在用户级别（所有项目都能用）。如果你只想在当前项目用，去掉 `-g`。

这个命令会通过 [Agent Skills](https://agentskills.io/) 生态的注册表自动识别你装的是哪个 harness 并放到对的位置。

### 方式 C：手动装（不推荐但能用）

去 GitHub 仓库的 [skills/last30days/](https://github.com/mvanhorn/last30days-skill/tree/main/skills/last30days) 目录，把整个 `SKILL.md` + `scripts/` 复制到你 AI 工具的 skill 目录里。

不同 harness 的目录不一样：
- Claude Code：`~/.claude/skills/last30days/`
- Codex：`~/.codex/skills/last30days/`
- Cursor：`~/.cursor/skills/last30days/`

不推荐是因为手动装的不会自动更新，作者一改你就过时了。

---

## 四、第一次跑：零配置 demo

装完之后，**不需要任何额外配置**就能跑。

打开你的 AI 工具（下面以 Claude Code 为例，其他工具类似），输入：

```
/last30days OpenAI
```

回车。等几十秒到几分钟（取决于你 AI 的速度），你会看到一份结构化的简报。

第一次跑会默认启用 4 个零配置数据源：
- **Reddit**（公开 JSON，不要 key）
- **Hacker News**（免费 API）
- **Polymarket**（公开赔率）
- **GitHub**（用你 `gh` CLI 已有的认证）

如果你的电脑装了 `yt-dlp`（YouTube 下载工具），YouTube 也会自动开。如果没有，去 `brew install yt-dlp`（mac）或 `pip install yt-dlp` 装一下就有了。

**跑通了吗？** 看到一份带 badge、引用、Best Takes 段落的简报就说明成功了。

如果出错了，别急——跳到第十章的踩坑速查。

---

## 五、输出长什么样：5 个部分一次看懂

假设你跑 `/last30days OpenAI`，拿到的输出大致是这么组织的：

### 1. 顶部 badge

```
🌐 last30days v3.3.2 · synced 2026-06-17
```

这是 v3 强制要求的开头，相当于"这确实是 last30days 跑出来的、不是 AI 自己编的"——也是一个安全锚，防止 AI 把 `/last30days` 当成普通关键词瞎发挥。

### 2. 主题元信息

研究的是 OpenAI 这个**实体**（entity），关联的 subreddit、@handle、相关产品会自动被识别出来。这背后是 v3 新加的"intelligent search"功能——引擎会先把"OpenAI"这个词解析成"对应哪些人/产品/社区"，再去搜，不是简单丢关键词。

### 3. 核心 synthesis

一份段落形式的总结，每个观点后面带 `r/ClaudeCode 569 upvotes` 这样的引用标签——直接告诉你这条信息来自哪个平台、多少真实互动。

### 4. Best Takes

单独一个段落，专门放"最有梗、最容易传播"的金句。比如某个 CEO 的反向发言、某个 Reddit 顶到 1.5k 赞的神评论。这是 v3 加的第二个 judge 评分（一个看相关、一个看好玩）筛出来的。

### 5. 底部 footer

```
✅ All agents reported back!
├── ✓ Reddit (12 items)
├── ✓ Hacker News (5 items)
├── ✓ Polymarket (2 items)
└── ✓ GitHub (3 items)
📎 Raw results saved to ~/Documents/Last30Days/openai-raw.md
```

这个 ASCII 树告诉你哪些数据源返回成功、拿回多少条、以及原始结果存在哪里（默认在 `~/Documents/Last30Days/`，Windows 在 `我的文档\Last30Days\`）。

---

## 六、想搜更多平台：按优先级配 key

零配置够用一段时间后，你会开始想"我还想看 X 上怎么说、想看 YouTube 视频的字幕、想看 TikTok 创作者的反应"。这时候就要配 key 了。

**先说推荐顺序**——别一上来把 8 个 key 全配了，先配你 80% 时间想要的那 1-2 个：

| Key | 解锁什么 | 推荐度 | 备注 |
|---|---|---|---|
| `SCRAPECREATORS_API_KEY` | TikTok + Instagram + Threads + Pinterest | ⭐⭐⭐⭐⭐ | 一次性开 4 个平台，10K 免费调用 |
| Bluesky 的 `BSKY_HANDLE` + `BSKY_APP_PASSWORD` | Bluesky | ⭐⭐⭐⭐ | 免费，去 bsky.app/settings/app-passwords 申请 19 位 app password |
| X 的 `AUTH_TOKEN` + `CT0`（浏览器 cookie） | X / Twitter | ⭐⭐⭐⭐ | 免费但不优雅——导出浏览器 cookie，技术门槛有 |
| `BRAVE_API_KEY` | Web search 后端 | ⭐⭐⭐ | 有免费额度，配了能让"补充搜索"质量更好 |
| `OPENAI_API_KEY` 或 `GEMINI_API_KEY` | 推理 provider | ⭐⭐⭐ | Claude Code / Codex 用户其实不需要，主模型自己就是推理器 |
| `XAI_API_KEY` / xAI 直接调 X | X | ⭐⭐ | 付费，X 一次查询成本不低 |

**配在哪里？** 在你的 home 目录建 `~/.config/last30days/.env` 文件：

```bash
# 第一次配 key
mkdir -p ~/.config/last30days
touch ~/.config/last30days/.env
chmod 600 ~/.config/last30days/.env

# 用任意编辑器打开，把 key 填进去
open ~/.config/last30days/.env
```

文件内容示例（占位符，**换成你自己的 key**）：

```bash
# 一次性开 TikTok/IG/Threads/Pinterest
SCRAPECREATORS_API_KEY=你的 key

# Bluesky
BSKY_HANDLE=你的handle.bsky.social
BSKY_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx

# 推理 provider（Claude Code 用户可以不配）
# GOOGLE_API_KEY=你的 Gemini key
```

**为什么要 `chmod 600`？** 装的时候脚本会检查文件权限，如果不是 600 每次跑都会在 stderr 警告你——这些 key 直接关系到你付费平台的账号。

**配完怎么验证？** 在项目目录跑：

```bash
python3 skills/last30days/scripts/last30days.py --diagnose
```

（如果你的 skill 不是装在项目目录，把路径换成 `npx skills` 装的位置，或者直接 `/last30days 任何关键词` 跑一次看 footer 里哪些源激活了。）

它会按数据源告诉你：哪些 key 识别到了、哪些 CLI 工具检测到了、哪些后端可达——**不动你的数据**，纯粹诊断。

---

## 七、5 个真实场景配方（这部分建议收藏）

这部分是这个 skill 最值钱的玩法。直接给"输入 → 输出"对比，你照着抄就行。

### 场景 1：研究一个公司 / 项目在押注什么

**输入**：

```
/last30days Anthropic --hiring-signals
```

**会拿到什么**：过去 30 天 Reddit/X/HN/招聘页上关于 Anthropic 的所有讨论，以及一个 hiring signals 段落——他们最近在招什么岗位（招企业安全 = 可能在加安全层；招基础设施 = 在扩规模；招 customer success = 在做 to-B 转型）。这不是预测 roadmap，是从招聘行为反推出来的"他们在押注什么"。

比看 LinkedIn 真实 100 倍——你拿到的不是官方通稿，是社区在讨论什么、员工在推特吐槽什么、用户在实际使用中遇到什么问题。

### 场景 2：做 AI 自媒体，找选题

**输入**：

```
/last30days Claude Code --days=14
```

**会拿到什么**：过去两周关于 Claude Code 的高赞 Reddit 讨论、爆款 X 推文、HN 争议、YouTube 深度评测、Polymarket 相关押注（如果有的话）。扫一眼 Best Takes 段落，分分钟抓到 3-5 个值得写的话题。

进阶版：加 `--competitors`，让引擎自动发现 2 个对标产品（Anthropic Code / Cursor / Copilot）跑三方对比。

### 场景 3：追热点

某新闻爆出 30 分钟后：

```
/last30days <事件名或人物名>
```

**会拿到什么**：全网第一波反应，附原始链接和互动量。比刷 Twitter trending 强在：你不会错过 Reddit 那边的高赞长贴、HN 的技术分析、YouTube 第一时间出的解读视频。

### 场景 4：买之前做尽调（不是金融那种，是消费决策）

**输入**：

```
/last30days Universal Epic Universe wait times
```

**会拿到什么**：Reddit r/UniversalStudios 里大家最近的真实体验、YouTube 攻略视频的核心观点、TikTok 上吐槽哪个项目排队 148 分钟的爆款——**比官网的"建议游玩时长 4 小时"真实 100 倍**。

### 场景 5：学一个新概念 / 新工具

**输入**：

```
/last30days Nano Banana Pro prompting
```

**会拿到什么**：Reddit / X / YouTube / 博客上所有关于这个 prompt 技巧的高质量讨论，**末尾会自动帮你写一个 production-ready prompt**（用了社区验证过的格式）。等于一次性把"教程 + 配方"全拿了。

---

## 八、v3 杀手级功能：6 个新东西值得专门用

2026 年上半年发布的 v3 不只是 bug 修复，加了 6 个新手也能立刻用上的功能。

### 1. HTML 简报（直接发 Slack / 邮件 / Notion）

```bash
/last30days OpenClaw --emit=html
```

或者直接用中文说：

```
/last30days OpenClaw，给我一份能直接发 Slack 的 HTML 简报
```

**会拿到什么**：一个自包含的、深色模式、可打印的 HTML 文件，存到 `~/Documents/Last30Days/openclaw-brief.html`。无 JS、纯内联 CSS，离线能开，**双击就能在浏览器看**，直接拖进 Slack / Notion / 邮件都行。

### 2. ELI5 模式（"说人话"）

跑完任何研究后，再说：

```
eli5 on
```

**会拿到什么**：同一份数据，但用大白话重写。原文可能是"Arizona's identity is paint scoring (50%+ shooting, 9th nationally)"，ELI5 之后变成"Arizona 赢球靠身体硬"。

数据没变、引用没变、来源没变——就是把术语剥掉。

### 3. Best Takes（最有梗的金句）

v3 加了第二个 judge：一个看相关度，一个看好不好笑 / 病毒潜力。每份简报末尾会单独有一段"最有梗的 5 条"，适合做封面图、适合直接发推。

### 4. Cross-source 合并

同一个新闻如果同时在 Reddit、X、YouTube 出现，v3 会合并成一个 cluster，不会列三遍。

### 5. GitHub Person Mode

查一个人的时候，引擎会从"搜名字"切到"扫他的 commit"：

```
/last30days Peter Steinberger --github-user=steipete
```

**会拿到什么**：过去 30 天他 merge 了多少 PR（85% merge rate = 高产高质）、在哪些 repo、release notes 里发了什么。配合 X / Reddit 数据，就能拼出一个完整的人。

### 6. 单次三方对比（不用手动跑三次）

```
/last30days OpenClaw vs Hermes vs Paperclip
```

**v2 跑这种对比要 12+ 分钟（3 次串行），v3 3 分钟搞定**（一次调用，entity 感知子查询并行）。

---

## 九、进阶：把"临时查询"变成"日常雷达"

到这一步你已经会用 last30days 回答"过去 30 天 X 怎么样"。但如果某个话题你想**每天/每周自动盯着**呢？

需要 3 个组件配合：

### 1. `--store`：把结果存进 SQLite

```bash
/last30days "AI agent framework" --store
```

加了 `--store`，引擎会同时把每条 finding 写进本地 SQLite（默认 `~/.local/share/last30days/research.db`）。URL 唯一约束——同一个链接再出现就更新，不重复入库。

**省去每次都加 flag 的笨办法**：在 `.env` 里加一行：

```bash
LAST30DAYS_STORE=1
```

之后所有运行都自动存。

### 2. `watchlist.py`：登记要长期监控的话题

```bash
python3 skills/last30days/scripts/watchlist.py add "British Airways Middle East" --weekly
```

登记完之后它本身不跑——**你需要外接一个调度器**（cron / Task Scheduler / GitHub Actions）定时去触发它。

或者手动触发：

```bash
python3 skills/last30days/scripts/watchlist.py run-all
```

**推送**：可以配 Slack incoming webhook，只有"有新 finding"时才推，不会刷屏。

### 3. `briefing.py`：每天/每周给你一份汇总

```bash
python3 skills/last30days/scripts/briefing.py generate
# 周报
python3 skills/last30days/scripts/briefing.py generate --weekly
```

它读 SQLite 库、生成结构化数据，让 AI 合成一份日报/周报。**配合 watchlist = 一个永远在线的"AI 舆情值班员"。**

---

## 十、踩坑速查（出错先翻这一章）

| 现象 | 最常见原因 | 怎么查 |
|---|---|---|
| 跑出来内容很少 | 没数据 / 数据源被 key 锁了 | 跑 `--diagnose` 看 footer 里 `✗` 的源 |
| 配了 key 还是不生效 | `.env` 路径不对或权限不是 600 | 看 stderr 警告；`ls -la ~/.config/last30days/.env` |
| X 一直不出结果 | X 是封闭平台，cookie 过期了 | 重新导出 `AUTH_TOKEN` + `CT0`；或改用 `XAI_API_KEY` |
| 跑一次要 10+ 分钟 | 网络慢或触发了 `--deep-research` 标志 | 不要随便加 `--deep-research`（每次 $0.9） |
| 装完 Claude Code 不认 | marketplace 没 add 或缓存过时 | 重新跑 `/plugin marketplace add` + `/plugin install` |
| Python 报错 | Python < 3.12 | 装 Python 3.12+：`brew install python@3.12` |
| 怎么知道 key 起没起作用 | — | 跑 `/last30days` 任何关键词，看 footer 的 `✓` / `✗` 列表 |

**最常用的自救命令**（记这一个就够）：

```bash
python3 skills/last30days/scripts/last30days.py --diagnose
```

它**不跑实际搜索**，只做健康检查：哪些 key 检测到了、哪些 CLI 装好了、哪些数据源能连通。

---

## 十一、5 分钟起步清单

如果只做一件事：

1. **现在就装上 skill**（第三节三种方式选一种，复制命令粘贴回车）
2. **跑一次零配置 demo**：`/last30days OpenAI`（或任何你最近感兴趣的话题）
3. **扫一眼输出**：重点看 Best Takes 段落和 footer 的 `✓` 列表
4. **试一个真实场景**：见客户 → `/last30days 客户名 --hiring-signals`；做选题 → `/last30days 你关注的领域 --days=14`
5. **真觉得好用了再来配 key**：先 `SCRAPECREATORS_API_KEY`（一次性开 4 个平台），再 Bluesky

这五步全做完，**15 分钟**。

---

## 参考资料

- 仓库：<https://github.com/mvanhorn/last30days-skill>
- Agent Skills 生态：<https://agentskills.io/>
- 概念定义（Skill / Engine / Harness）：<https://github.com/mvanhorn/last30days-skill/blob/main/CONCEPTS.md>
- 配置参考：<https://github.com/mvanhorn/last30days-skill/blob/main/CONFIGURATION.md>
- v3 changelog：<https://github.com/mvanhorn/last30days-skill/blob/main/CHANGELOG.md>

---

> 觉得有用的话，**点个收藏**，下次追热点、做选题之前翻出来照着抄。
> 有其他想看的内容 / 玩法，欢迎留言告诉我，下一篇可能就写它。
