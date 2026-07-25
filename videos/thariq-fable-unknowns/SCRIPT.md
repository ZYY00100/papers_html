# SCRIPT

**Duration target:** 180 seconds (3:00)
**Word count:** ~450 Chinese characters (≈2.5 chars/sec natural pace)
**Tone:** Chinese, calm, editorial — closer to reading aloud than advertising
**Structure:** Hook → Map vs Territory → 4 Unknowns → Help Claude → 5 Pre-Impl Tools → During → Post → Case Study + CTA

---

## 脚本

> [Beat 01 — HOOK · 0:00–0:14]
> Claude Fable 的工程师 Thariq 写了一篇方法论：地图不是疆域。"未知"决定 Claude 的工作质量。
>
> [Beat 02 — MAP vs TERRITORY · 0:14–0:28]
> 地图，是你给 Claude 的 prompt、skill、context。疆域，是代码库、真实世界、和它的实际约束。两者的差距，就是 unknowns。
>
> [Beat 03 — 4 UNKNOWNS · 0:28–0:46]
> Unknowns 分四类。Known Knowns — prompt 里说清楚的。Known Unknowns — 知道没想清楚的。Unknown Knowns — 太显然没写下来的。Unknown Unknowns — 根本没想到的。
>
> [Beat 04 — HELP CLAUDE · 0:46–0:56]
> 指令是个微妙平衡。指令太具体，Claude 不会变通；太模糊，Claude 套用行业惯例。让 Claude 帮你，更快发现 unknowns。
>
> [Beat 05 — PRE-IMPL 章扉 · 0:56–1:04]
> 实施前有 5 个工具。让你在写第一行代码前，先把 unknowns 摊开。
>
> [Beat 06 — BLIND SPOT · 1:04–1:18]
> 工具一：Blind Spot Pass。直接说"帮我做一次 blindspot pass"，让 Claude 帮你找 unknown unknowns。
>
> [Beat 07 — BRAINSTORM · 1:18–1:32]
> 工具二：脑暴和原型。让 Claude 给你 4 个截然不同的方向，而不是一个确定的方案。让你看到才知道想要什么。
>
> [Beat 08 — INTERVIEW · 1:32–1:44]
> 工具三：让 Claude 反过来采访你。一次一个问题，专挑那些能改变架构的。
>
> [Beat 09 — REFERENCES · 1:44–1:58]
> 工具四：References。说不清想要什么？最有效的 reference 是源代码。指给 Claude 一个目录，告诉它看什么。
>
> [Beat 10 — IMPL PLAN · 1:58–2:12]
> 工具五：Implementation Plan。让 Claude 写一份实施计划，让你 review。数据模型、type 接口、UX 流程排前面。
>
> [Beat 11 — IMPL NOTES · 2:12–2:24]
> 实施中，让 Claude 维护一份 implementation-notes.md。记下它做的决定，下次复盘。
>
> [Beat 12 — PITCH + QUIZ · 2:24–2:38]
> 实施完，做两件事。Pitches：打包 demo、spec、笔记，丢 Slack 拿 buy-in。Quizzes：让 Claude 出题考你，必须满分才 merge。
>
> [Beat 13 — FABLE + CTA · 2:38–3:00]
> Fable 启动视频，完全由 Claude Code 剪辑。Thariq 不知道 color grading，就让 Claude 先教他，再动手。模型越强，clarify unknowns 的能力就越是瓶颈。所以让你的下一个项目，从找 unknowns 开始。

---

## TTS Pronunciation Notes

- `Thariq` — 念「塔里克」（Tha-rik），不要念「萨里克」
- `Claude` — 念「Kluud」（按英文发音），不要念「克劳德」
- `Fable` — 念「Fey-bull」
- `prompt` — 念「prompt」（保留英文）
- `skill` — 念「skill」（保留英文）
- `context` — 念「con-text」
- `evaluator` — 念「evaluator」（保留英文）或「评测器」
- `auto mode` — 保留英文
- `dynamic workflows` — 保留英文
- `Unknowns` — 念「unknowns」（保留英文）
- `Known Knowns` / `Known Unknowns` / `Unknown Knowns` / `Unknown Unknowns` — 全部保留英文
- `Buy-in` — 念「buy-in」
- `merge` — 念「merge」（保留英文）
- `Remotion` — 念「Remo-tion」
- `ffmpeg` — 念「ff-mpeg」
- `Whisper` — 念「Whis-per」
- `/` — 念「斜杠」
- `map ≠ territory` — 念「map 不等于 territory」
- 数字 01-13 不在脚本里念出来，画面用金色 Rajdhani 序号呈现

---

## Beat Map

| # | Beat (zh) | Chars | Sec | Section |
|---|---|---|---|---|
| 1 | Hook（核心命题） | ~35 | 14s | 开场 |
| 2 | Map vs Territory | ~35 | 14s | 隐喻展开 |
| 3 | 4 Unknowns 框架 | ~45 | 18s | 核心分析 |
| 4 | Help Claude | ~25 | 10s | 过渡 |
| 5 | Pre-Impl 章扉 | ~20 | 8s | 过渡 |
| 6 | Blind Spot | ~35 | 14s | 工具 1 |
| 7 | Brainstorm | ~35 | 14s | 工具 2 |
| 8 | Interview | ~30 | 12s | 工具 3 |
| 9 | References | ~35 | 14s | 工具 4 |
| 10 | Impl Plan | ~35 | 14s | 工具 5 |
| 11 | Impl Notes | ~30 | 12s | 实施中 |
| 12 | Pitch + Quiz | ~35 | 14s | 实施后 |
| 13 | Fable + CTA | ~55 | 22s | 案例 + 收束 |
| **Total** | | **~450** | **180s** | |

---

## Notes for Step 4

- Beat 1 (Hook) 视觉：用静态排版 + 慢速 reveal，氛围是「打开一篇文章」。封面图占下半部分。
- Beat 3 (4 Unknowns) 视觉：Rumsfeld 2×2 矩阵是**全片最关键的一帧**，需要 18s 让它清晰呈现。Unknown Unknowns 卡片用红边高亮。
- Beat 6-12 (8 个工具) 视觉：每节一张节奏一致的 prompt-card 入场。统一暗色 `#0E0E10` + JetBrains Mono 18px + 8px radius。
- Beat 13 (Fable) 视觉：4 步 timeline 竖向排列，最后放大金句「让你的下一个项目，从找 unknowns 开始」。
- 不需要 flash 转场，editorial 调性靠呼吸和留白。背景音乐 Lo-Fi，浅响度，不抢旁白。
