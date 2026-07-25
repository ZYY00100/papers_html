# STORYBOARD

**Format:** 1920×1080 landscape
**Audio:** Chinese TTS narration (MiniMax `moss_audio_ce44fc67`) + Lo-Fi BGM (`bgm-lofi.wav`) + soft SFX (chimes / ticks / page-turns)
**Style basis:** `DESIGN.md` — light editorial, white cards on `#F5F5F7` canvas, Cormorant + Noto Serif SC + Rajdhani, gold numeral system.

---

## Global Direction

- **Canvas:** `#F5F5F7` with the 80px grid overlay (repeating-linear-gradient at 0.024 opacity).
- **Type rules:** Display = Cormorant Garamond; body CN = Noto Serif SC; labels = Rajdhani uppercase.
- **Color rules:** Use gold `#C9A962` only on numbered prefixes (01–13); red `#C8161D` only on `Unknown Unknowns` highlight + active states.
- **Motion language:** Slow, restrained, fade-and-rise. No flashy reveals. Each beat begins with ~0.3s of stillness before content enters.
- **Frame discipline:** 1920×1080 single canvas, content column centered. Generous side margins (120–160px).

---

## Underscore / Music Direction

Lo-Fi ambient pad with sparse piano notes. No percussion. Sits underneath VO without competing. Slight swell during the 4 Unknowns reveal (Beat 3), thins to single sustained pad during the 8 technique beats, resolves on a clean chord at the closing beat.

---

## Asset Audit

| Asset | Type | Assign to Beat | Role |
|---|---|---|---|
| `capture/assets/cover.jpg` | cover diagram (Hero, 2400×960) | Beat 1 (Hook) | Establishes the article visually on entry |
| `capture/assets/x-01.jpg` | inline diagram (1000×720, map vs territory) | Beat 2 (Map vs Territory) | Visual proof of the central metaphor |
| `capture/assets/x-02.jpg` | inline diagram (2000×1120, 4 unknowns) | Beat 3 (4 Unknowns) | Visual reference of Rumsfeld matrix |
| `capture/assets/x-03.jpg` | inline diagram (1000×560, instructing claude) | Beat 4 (Help Claude) | Visual reference of the balance |
| `capture/assets/x-04.jpg` | long-form diagram (2000×2480, 8 techniques) | Beat 5 (Pre-Impl cover) | Visual proof of 5 tools |
| `capture/assets/x-05.jpg` | inline diagram (1000×460, pitches & quizzes) | Beat 12 (Pitch+Quiz) | Visual reference for post-impl |
| `audio/bgm-lofi.wav` | Lo-Fi underscore | All beats | Background atmosphere |
| `audio/sfx/beep.wav` | soft tonal chime | Multiple beats | Card entry accent |
| `audio/sfx/keystroke.wav` | soft digital tick | Multiple beats | Number/timeline tick |
| `audio/sfx/transition.wav` | soft whoosh | Beat transitions | Scene change texture |

**Utilization:** 6/6 captured assets used (100%). All 6 article inline/cover diagrams appear, matching the source article's imagery density.

---

## Rhythm Plan

```
Beat 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13
 hold  hold  PEAK  hold  hold  hold hold hold hold hold  hold  hold  resolve
 (slow)(slow)(dense)(quiet)(quiet)(clean)(clean)(clean)(clean)(clean)(clean)(clean)(still)
```

The video peaks at Beat 3 (the 4 Unknowns reveal — visually the most information-dense moment). Beats 6–12 are deliberate holds, each framing one technique with consistent pacing. Beat 1 is a slow build; Beat 13 is a quiet close.

---

## Per-Beat Direction

### BEAT 1 — HOOK (0:00–0:14)

**On-screen text:** "Claude Fable 的工程师 Thariq 写了一篇方法论：地图不是疆域。'未知'决定 Claude 的工作质量。"

**Concept:** The viewer opens a magazine to its title page. Calm, patient. We're establishing a single idea — *what does this article claim?* — and letting it breathe. The cover image slides into the lower half as the definition lands above.

**Mood direction:** The first page of an Apple developer essay. Editorial restraint. White space dominates.

**Animation choreography:**
- Gold numeral `01` Rajdhani fades in upper-left, 0.15–0.55s, opacity 0→1, y:-8→0
- Small Rajdhani kicker `CLAUDE FABLE · METHODOLOGY` letter-spacing 2.2px, fades 0.55–0.95s
- Main display title `地图不是疆域` — Cormorant Garamond 72px + Noto Serif SC 64px, types on, 0.8–2.6s, stagger 0.05s per char, y: 16→0 + opacity 0→1
- Subtitle `Claude 工程师 Thariq 的方法论：未知决定工作质量` Noto Serif SC 26px, fades 2.6–3.6s
- Cover image `cover.jpg` slides up from bottom, 3.5–5.5s, y: 80→0, opacity 0→1, soft shadow
- Image caption `原文配图 · A FIELD GUIDE TO FABLE · 2026/07/03` Rajdhani 12px, fades 5.5–6.5s
- Hold 6.5–14s — stillness, ambient pad swells gently

**Transition OUT:** Velocity-matched upward — exit `y:0→-100, blur:0→24px, 0.4s power2.in`

**Depth layers:**
- BG: `#F5F5F7` canvas + 80px grid overlay
- MG: numeral, kicker, title block (top half)
- FG: cover image + caption (lower 40%)

**SFX:** Single low pad chord on entry. Subtle "page turn" texture at 3.5s when image slides up.

**Assets:** `capture/assets/cover.jpg`

---

### BEAT 2 — MAP vs TERRITORY (0:14–0:28)

**On-screen text:** "地图 = 你给 Claude 的 prompt、skill、context。疆域 = 代码库、真实世界。两者的差距，就是 unknowns。"

**Concept:** Side-by-side dual-card composition. Left card: "地图" (the map) with examples. Right card: "疆域" (the territory) with examples. Center dashed line + label "Unknowns" between them. Visualizes the central metaphor with geometric clarity.

**Mood direction:** Architectural. Two columns of understanding, with the gap in the middle.

**Animation choreography:**
- Gold numeral `02` Rajdhani fades 0.0–0.4s
- H2 `The map is not the territory` Cormorant 44px + CN `地图不是疆域` Noto Serif SC 28px, fade + slide up 0.3–1.4s
- Left card (Map) — 1.6s: x: -80→0, opacity 0→1, 0.6s power3.out
  - Card title: `地图` (large)
  - Subtitle: `你给 Claude 的东西`
  - List: `prompt` / `skill` / `context` (Rajdhani uppercase, stacked)
- Right card (Territory) — 1.8s: x: +80→0, opacity 0→1, 0.6s power3.out
  - Card title: `疆域`
  - Subtitle: `真实世界`
  - List: `代码库` / `约束` / `真实场景`
- Center dashed line + "Unknowns" label — 2.4s: opacity 0→1, scale 0.9→1
- Image `x-01.jpg` (small inset) appears bottom-left, 3.0s: opacity 0→1
- Hold 3.5–14s — stillness

**Transition OUT:** Blur-through — exit `blur:0→16px, opacity:1→0, 0.4s power2.in`

**Depth layers:**
- BG: canvas
- MG: title block (top center)
- FG: 2 cards (left + right) + center label + small inline image

**SFX:** Two soft chimes (one per card entry). Subtle tick when "Unknowns" label appears.

**Assets:** `capture/assets/x-01.jpg` (small reference inset)

---

### BEAT 3 — 4 UNKNOWNS / RUMSFELD (0:28–0:46) — KEY VISUAL

**On-screen text:** "Unknowns 分四类。" (then individually) "Known Knowns / Known Unknowns / Unknown Knowns / Unknown Unknowns"

**Concept:** The most information-dense beat. The Rumsfeld 2×2 matrix as a 4-card grid + center red dot. The "Unknown Unknowns" card (bottom-right) gets a red border highlight — it's the focus of the entire article. The 4 cards appear in stagger; then the red dot; then the red border on UU.

**Mood direction:** Analytical. The framework is laid bare.

**Animation choreography:**
- Gold numeral `03` Rajdhani fades 0.0–0.4s
- H2 `Knowing your unknowns` Cormorant 44px + CN `把未知分成四类` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- 4 cards stagger in (left-to-right, top-to-bottom), 1.6s starting:
  - Card 1 (top-left, KK): `Known Knowns` + `已在 prompt 里说清楚` (Cn)
  - Card 2 (top-right, KU): `Known Unknowns` + `知道没想清楚`
  - Card 3 (bottom-left, UK): `Unknown Knowns` + `太显然没写下来`
  - Card 4 (bottom-right, UU): `Unknown Unknowns` + `根本没想到的`
- Each card: scale 0.92→1, opacity 0→1, 0.5s power2.out, stagger 0.18s
- Center red dot `#C8161D` (small, 12px) appears 2.6s, scale 0→1, 0.4s back.out
- **Highlight ring on Card 4 (UU)**: red border `#C8161D` 3px, scales from 0.95 to 1.02 to 1, 3.2s, 0.6s
- Caption at bottom: `Rumsfeld 矩阵 · 越往右下越危险` Rajdhani 12px muted, fades 4.0s
- Hold 4.5–18s — stillness, music swells

**Transition OUT:** Velocity-matched rightward — exit `x:0→+150, blur:0→20px, 0.45s power2.in`

**Depth layers:**
- BG: canvas
- MG: title block (top center)
- FG: 2×2 card grid + center red dot + red border highlight on UU

**SFX:** 4 soft chimes (one per card). One subtle "tick" on the red dot. A soft "ping" on the red border highlight.

**Assets:** `capture/assets/x-02.jpg` (optional small inset, can be skipped for cleanliness)

---

### BEAT 4 — HELP CLAUDE (0:46–0:56)

**On-screen text:** "指令是个微妙平衡。指令太具体，Claude 不会变通；太模糊，Claude 套用行业惯例。"

**Concept:** A chapter transition card. The viewer's eyes transition from the analytical Rumsfeld matrix to a soft, almost philosophical statement. Visual: single centered text block, with the article's "balance scale" image as a soft background reference.

**Mood direction:** Quiet, almost philosophical. A pause to set up the practical tools that follow.

**Animation choreography:**
- Gold numeral `04` Rajdhani fades 0.0–0.4s
- H2 `Help Claude help you` Cormorant 44px + CN `让 Claude 帮你发现 unknowns` Noto Serif SC 28px, fade + slide up 0.3–1.4s
- Two contrast lines fade in below:
  - `太具体 ⟶ 不会变通` (left, in red, 1.6s)
  - `太模糊 ⟶ 套用惯例` (right, in red, 1.6s, +0.15s delay)
- Center dot `·` (large) between them, 2.0s: scale 0→1
- Subtitle: `Claude 能更快发现 unknowns — 搜代码、搜网络、迭代` Noto Serif SC 22px, fades 2.6s
- Hold 3.5–10s — stillness

**Transition OUT:** Velocity-matched downward — exit `y:0→+100, blur:0→20px, 0.4s power2.in`

**Depth layers:**
- BG: canvas
- MG: title block (top)
- FG: two contrast lines + center dot + subtitle

**SFX:** Single low pad chord. Subtle beep on each contrast line.

**Assets:** None (typography only)

---

### BEAT 5 — PRE-IMPL 章扉 (0:56–1:04)

**On-screen text:** "实施前有 5 个工具。" (with 5 chip labels below)

**Concept:** Chapter title card for the practical section. Big title + 5 chip labels previewing the techniques. Like opening the index page of a chapter.

**Mood direction:** Crisp, organized. A table of contents.

**Animation choreography:**
- Gold numeral `05` Rajdhani fades 0.0–0.4s
- Section kicker `PRE-IMPLEMENTATION · 5 TOOLS` Rajdhani 12px, fade 0.4–0.8s
- H2 `5 工具 · 实施前` Cormorant 56px + Noto Serif SC 48px, fade + slide up 0.6–1.8s
- 5 chip labels in horizontal row, stagger 0.15s, starting 2.0s:
  - `01 BLIND SPOT`
  - `02 BRAINSTORM`
  - `03 INTERVIEW`
  - `04 REFERENCES`
  - `05 IMPL PLAN`
- Each chip: opacity 0→1, y: 12→0, 0.4s power2.out
- Chips have subtle border + soft bg
- Hold 3.5–8s — stillness

**Transition OUT:** Velocity-matched upward — exit `y:0→-100, blur:0→24px, 0.35s power2.in`

**Depth layers:**
- BG: canvas
- MG: title block (top)
- FG: 5 chip row (centered)

**SFX:** 5 soft chimes (one per chip). Pad underneath.

**Assets:** None (typography only)

---

### BEAT 6 — BLIND SPOT PASS (1:04–1:18)

**On-screen text:** "工具一：Blind Spot Pass。直接说'帮我做一次 blindspot pass'，让 Claude 帮你找 unknown unknowns。"

**Concept:** First tool deep-dive. Standard "left text + right prompt-card" composition. The prompt-card is the dark `#0E0E10` block with the example prompt quoted from the article.

**Mood direction:** Technical, focused. The dark code card creates visual contrast on the light canvas.

**Animation choreography:**
- Gold numeral `06 / BLIND SPOT PASS` Rajdhani fades 0.0–0.4s
- H2 `Blind Spot Pass` Cormorant 44px + CN `工具一：盲点扫描` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Left text: explanation fades 1.4s
  - `给 Claude 你的身份背景和知识水平` (line 1)
  - `直接说 "blindspot pass"` (line 2, Rajdhani monospace)
  - `让它找出你的 unknown unknowns` (line 3)
- Right prompt-card slides in 1.8s: x: +120→0, opacity 0→1, 0.6s power3.out
  - Dark `#0E0E10` background
  - JetBrains Mono 16px white text:
    - `"I'm working on adding a new auth provider but I know nothing about the auth modules. Can you do a blindspot pass..."`
  - 8px radius, soft shadow
- Caption bottom: `原文 prompt 例 1` Rajdhani 11px muted, fades 3.0s
- Hold 4.0–14s — stillness

**Transition OUT:** Blur-through — exit `blur:0→16px, opacity:1→0, 0.4s power2.in`

**Depth layers:**
- BG: canvas
- MG: title + explanation (left)
- FG: prompt-card (right)

**SFX:** Single soft chime at prompt-card entry. Subtle keystroke tick on text reveal.

**Assets:** None (typography + dark prompt-card only)

---

### BEAT 7 — BRAINSTORM + PROTOTYPE (1:18–1:32)

**On-screen text:** "工具二：脑暴和原型。让 Claude 给你 4 个截然不同的方向，而不是一个确定的方案。"

**Concept:** Same composition as Beat 6. The prompt-card shows the article's "4 wildly different design directions" example.

**Mood direction:** Creative, energetic (relative to the previous beat). The "4 directions" idea is conveyed via 4 sub-cards inside the prompt-card.

**Animation choreography:**
- Gold numeral `07 / BRAINSTORM` Rajdhani fades 0.0–0.4s
- H2 `Brainstorm & Prototype` Cormorant 44px + CN `工具二：脑暴和原型` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Left text: 1.4s
  - `让 Claude 给你多个方向` (line 1)
  - `让你"看到才知道"想要什么` (line 2, italic)
  - `早期 verbalize unknown knowns 成本最低` (line 3)
- Right prompt-card slides in 1.8s: x: +120→0
  - Inside the dark card: 4 small sub-cards in a 2×2 grid showing the 4 design directions concept
  - Each sub-card: thin border `#E8E8EA` (20% opacity)
  - JetBrains Mono 14px: `direction 1 / 2 / 3 / 4`
- Caption: `原文 prompt 例 2` Rajdhani 11px muted, fades 3.0s
- Hold 4.0–14s

**Transition OUT:** Velocity-matched leftward — exit `x:0→-150, blur:0→20px, 0.35s power2.in`

**Depth layers:**
- BG: canvas
- MG: title + explanation (left)
- FG: prompt-card with 4 sub-cards (right)

**SFX:** Single soft chime + 4 quick ticks (one per sub-card entry).

**Assets:** None

---

### BEAT 8 — INTERVIEW (1:32–1:44)

**On-screen text:** "工具三：让 Claude 反过来采访你。一次一个问题，专挑那些能改变架构的。"

**Concept:** Tighter beat (12s) — single question visualization. The "1 question at a time" idea is shown via a single large "Q1" letter and the prompt text.

**Mood direction:** Intimate, conversational. The viewer feels a question being asked.

**Animation choreography:**
- Gold numeral `08 / INTERVIEW` Rajdhani fades 0.0–0.4s
- H2 `Interviews` Cormorant 44px + CN `工具三：让 Claude 反问` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Large decorative `Q1` Cormorant 200px (very light `#E5E5E8`) center-left, fades 1.4s: scale 0.9→1, opacity 0→0.6
- Right prompt-card slides in 1.6s: x: +100→0
  - Dark card with JetBrains Mono:
    - `"Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture."`
- Caption: `原文 prompt 例 3` Rajdhani 11px, fades 2.8s
- Hold 3.5–12s

**Transition OUT:** Blur-through

**Depth layers:**
- BG: canvas
- MG: title + decorative Q1
- FG: prompt-card

**SFX:** Single soft chime + subtle "ping" on the Q1.

**Assets:** None

---

### BEAT 9 — REFERENCES (1:44–1:58)

**On-screen text:** "工具四：References。说不清想要什么？最有效的 reference 是源代码。"

**Concept:** Same composition pattern. The "源代码" (source code) concept is highlighted with a small "📁 → Claude" diagram or a folder icon visual.

**Mood direction:** Practical, matter-of-fact. References are how pros communicate.

**Animation choreography:**
- Gold numeral `09 / REFERENCES` Rajdhani fades 0.0–0.4s
- H2 `References` Cormorant 44px + CN `工具四：参考物` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Left text: 1.4s
  - `说不清时，最好的答案是 reference` (line 1)
  - `图、文档、组件 — 都可以` (line 2)
  - `但最有效的，是源代码` (line 3, **bold**)
- Right prompt-card slides in 1.8s
  - Dark card with JetBrains Mono:
    - `"This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client."`
- Small badge `源代码` Rajdhani 11px red `#C8161D`, top-right of card, fades 2.8s
- Caption: `原文 prompt 例 4 · 跨语言读源码` Rajdhani 11px, fades 3.0s
- Hold 4.0–14s

**Transition OUT:** Velocity-matched upward

**Depth layers:**
- BG: canvas
- MG: title + explanation
- FG: prompt-card + "源代码" badge

**SFX:** Single soft chime + keystroke ticks on the bold "源代码" line.

**Assets:** None

---

### BEAT 10 — IMPLEMENTATION PLANS (1:58–2:12)

**On-screen text:** "工具五：Implementation Plan。让 Claude 写一份实施计划，让你 review。"

**Concept:** Same composition. The "重点先 review" concept is shown via a hierarchical list in the prompt-card.

**Mood direction:** Methodical, organized. The viewer is being shown the planning ritual.

**Animation choreography:**
- Gold numeral `10 / IMPL PLAN` Rajdhani fades 0.0–0.4s
- H2 `Implementation Plans` Cormorant 44px + CN `工具五：实施计划` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Left text: 1.4s
  - `让 Claude 写实施计划` (line 1)
  - `你 review 最重要的部分` (line 2)
  - `机械重构放手让它做` (line 3)
- Right prompt-card slides in 1.8s
  - Dark card with JetBrains Mono:
    - `"Write an implementation plan in HTML, but lead with the decisions I'm most likely to tweak with: data model changes, new type interfaces, and anything user-facing..."`
- Below prompt-card: small priority labels `数据模型 / type 接口 / UX 流程` in 3 micro chips, stagger 0.1s starting 2.6s
- Caption: `原文 prompt 例 5` Rajdhani 11px, fades 3.0s
- Hold 4.0–14s

**Transition OUT:** Blur-through

**Depth layers:**
- BG: canvas
- MG: title + explanation
- FG: prompt-card + 3 priority chips

**SFX:** Single soft chime + 3 quick ticks (one per priority chip).

**Assets:** None

---

### BEAT 11 — IMPL NOTES (2:12–2:24)

**On-screen text:** "实施中，让 Claude 维护一份 implementation-notes.md。记下它做的决定，下次复盘。"

**Concept:** Same composition. The "deviations log" concept is shown via a small file-tree visualization inside the prompt-card.

**Mood direction:** Mid-process, focused. The viewer is watching work happen.

**Animation choreography:**
- Gold numeral `11 / DURING` Rajdhani fades 0.0–0.4s
- H2 `Implementation notes` Cormorant 44px + CN `实施中：记下决定` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Left text: 1.4s
  - `新开 session，传入 spec + prototype` (line 1)
  - `但永远会有 unknown unknowns 浮出` (line 2)
  - `让 Claude 维护一份 notes.md` (line 3)
- Right prompt-card slides in 1.8s
  - Dark card with JetBrains Mono:
    - `"Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going."`
- Small label `Deviations` red `#C8161D` on right side of card
- Caption: `原文 prompt · DURING` Rajdhani 11px, fades 2.8s
- Hold 3.5–12s

**Transition OUT:** Velocity-matched rightward

**Depth layers:**
- BG: canvas
- MG: title + explanation
- FG: prompt-card + Deviations label

**SFX:** Single soft chime.

**Assets:** None

---

### BEAT 12 — PITCH + QUIZ (2:24–2:38)

**On-screen text:** "实施完，做两件事。Pitches：打包 demo、spec、笔记，丢 Slack 拿 buy-in。Quizzes：让 Claude 出题考你，必须满分才 merge。"

**Concept:** Two-card horizontal layout. Two cards side-by-side, each with one technique. Pitches on the left, Quizzes on the right. Mirrors the article's two-paragraph structure.

**Mood direction:** Final step before shipping. Two parallel rituals.

**Animation choreography:**
- Gold numeral `12 / POST-IMPL` Rajdhani fades 0.0–0.4s
- H2 `Pitches & Quizzes` Cormorant 44px + CN `实施后：推介 + 自测` Noto Serif SC 26px, fade + slide up 0.3–1.4s
- Two cards side-by-side, 1.8s + 2.0s stagger:
  - Left card (Pitches): dark `#0E0E10`, Rajdhani label `01 PITCHES`, JetBrains Mono 14px text:
    - `"Package the prototype, the spec, and the implementation notes into a single doc I can drop in Slack to get buy-in. Lead with the demo GIF."`
  - Right card (Quizzes): dark `#0E0E10`, Rajdhani label `02 QUIZZES`, JetBrains Mono 14px text:
    - `"I want to make sure I understand everything that's happened in this change. Give me a HTML report on the changes... and a quiz at the bottom on the changes that I must pass."`
- Both cards: y: 30→0, opacity 0→1, 0.6s power3.out
- Caption bottom: `原文 prompt · POST-IMPL · 两件事` Rajdhani 11px, fades 3.0s
- Hold 4.0–14s

**Transition OUT:** Velocity-matched downward

**Depth layers:**
- BG: canvas
- MG: title (top)
- FG: 2 dark cards (horizontal pair, centered)

**SFX:** 2 soft chimes (one per card).

**Assets:** None (or optional `x-05.jpg` as small reference, can be skipped)

---

### BEAT 13 — FABLE LAUNCH + CTA (2:38–3:00)

**On-screen text:** "Fable 启动视频完全由 Claude Code 剪辑。Thariq 不知道 color grading，就让 Claude 先教他，再动手。模型越强，clarify unknowns 的能力就越是瓶颈。所以让你的下一个项目，从找 unknowns 开始。"

**Concept:** The closing act. A 4-step vertical timeline showing how Thariq applied the framework to launch Fable's video. The 4 steps reveal in sequence, then the closing gold sentence takes the whole frame.

**Mood direction:** Resolves with quiet authority. The framework has been demonstrated; the viewer should feel equipped.

**Animation choreography:**
- Gold numeral `13 / CASE STUDY` Rajdhani fades 0.0–0.4s
- H2 `How this comes together` Cormorant 44px + CN `实战：Fable 启动视频` Noto Serif SC 28px, fade + slide up 0.3–1.4s
- 4 timeline steps, vertical, stagger 0.4s starting 1.8s:
  - Step 1: `Whisper 转录讲解` + small dot indicator
  - Step 2: `Remotion prototype` + small dot
  - Step 3: `ffmpeg 剪 ums` + small dot
  - Step 4: `Color grading 教学` + small dot (highlighted with red border)
- Each step: x: -40→0, opacity 0→1, 0.5s power2.out
- A connecting vertical line on the left side, 1.4s: scaleY 0→1
- Hold 3.5–12s — narrative voiceover runs
- Final gold sentence: `所以让你的下一个项目，从找 unknowns 开始` Cormorant 48px, fades 12s: scale 0.95→1, opacity 0→1
- 4 timeline steps fade out 12s: opacity 1→0, 0.6s (final scene exception — allowed to fade elements)
- Hold gold sentence 14–22s
- Fade to canvas 22s

**Transition OUT:** Fade to canvas — opacity → 1.0, no motion (final scene)

**Depth layers:**
- BG: canvas
- MG: title block (top)
- FG: 4-step vertical timeline (left half) + closing gold sentence (centered, full width)

**SFX:** 4 soft ticks (one per step). Soft pad resolves on chord at the closing sentence.

**Assets:** None (typography only)

---

## Production Architecture

```
thariq-fable-unknowns/
├── index.html                    root — orchestration + TTS + BGM + beat clips
├── DESIGN.md                     brand reference
├── SCRIPT.md                     narration text (this file's source)
├── STORYBOARD.md                 THIS FILE — creative north star
├── transcript.json               word-level timestamps (from Stage 5)
├── narration.wav                 TTS audio (from Stage 5)
├── CLAUDE.md                     project conventions
├── capture/
│   └── assets/                   6 original article images
├── audio/                        symlinks to 01_Foundation BGM + SFX
└── compositions/
    ├── _partials/
    │   ├── prompt-card.html      (8 tools reuse)
    │   └── section-header.html   (chapter title reuse)
    ├── beat-01-hook.html
    ├── beat-02-map-vs-territory.html
    ├── beat-03-rumsfeld.html              ← key visual
    ├── beat-04-help-claude.html
    ├── beat-05-pre-impl.html
    ├── beat-06-blind-spot.html
    ├── beat-07-brainstorm.html
    ├── beat-08-interview.html
    ├── beat-09-references.html
    ├── beat-10-impl-plan.html
    ├── beat-11-impl-notes.html
    ├── beat-12-pitch-quiz.html
    └── beat-13-fable-cta.html
```

---

## Self-Review Checklist (run after building each composition)

- [ ] No overlapping text elements
- [ ] No asset placed outside safe zones
- [ ] Animation matches verb in storyboard
- [ ] Gold `#C9A962` only on numerals
- [ ] Red `#C8161D` only on `Unknown Unknowns` highlight + `Deviations` label + `源代码` badge
- [ ] No new fonts introduced
- [ ] Background is `#F5F5F7` with grid overlay
- [ ] Voiceover ends before transition starts
- [ ] Total duration = 180s
