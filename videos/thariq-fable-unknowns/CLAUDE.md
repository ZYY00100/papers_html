# thariq-fable-unknowns · 项目规范

## 项目目标

3 分钟中文解读视频，主题：Anthropic Claude Code 工程师 Thariq Shihipar 的文章《A Field Guide to Fable: Finding Your Unknowns》。

发布渠道：B 站 / 视频号 / YouTube。

## 视觉规范

完全沿用 `claude-loops-intro` 的 Apple editorial 设计语言，详见 `DESIGN.md`。

关键 token：
- Canvas: `#F5F5F7` + 80px grid 0.024 透明度
- Card: `#FFFFFF`
- Primary text: `#1D1D1F`
- Secondary text: `#4A4A4F`
- Muted: `#8A8A8E`
- Accent red: `#C8161D`（红边高亮 / 链接）
- Accent gold: `#C9A962`（数字序号）
- Code bg: `#0E0E10`（prompt-card）

字体（5 字体系统，Google Fonts CDN）：
- Cormorant Garamond（英文 display）
- Noto Serif SC（中文正文）
- Inter（sans body）
- JetBrains Mono（code / prompt）
- Rajdhani（标签 / 序号，letter-spacing 2.2px）

## 时长

精确 180s（3:00），允许 ±5s 缓冲。

## 音频

- TTS：MiniMax `moss_audio_ce44fc67` 男声
- BGM：`audio/bgm-lofi.wav`（软链至 `01_Foundation/hyperframes/audio/bgm-lofi.wav`）
- SFX：复用 `01_Foundation/hyperframes/audio/sfx/{beep,keystroke,transition}.wav`

## 13-Beat 节奏

| # | Beat | 时长 | 视觉重心 |
|---|---|---|---|
| 01 | HOOK | 14s | 标题 + 封面图 |
| 02 | MAP vs TERRITORY | 14s | 隐喻展开 |
| 03 | 4 UNKNOWNS | 18s | Rumsfeld 2×2 |
| 04 | HELP CLAUDE | 10s | 章节扉页 |
| 05 | PRE-IMPL 章扉 | 8s | 5 工具分页 |
| 06 | Blind Spot | 14s | prompt-card |
| 07 | Brainstorm | 14s | prompt-card |
| 08 | Interview | 12s | prompt-card |
| 09 | References | 14s | prompt-card |
| 10 | Impl Plan | 14s | prompt-card |
| 11 | Impl Notes | 12s | prompt-card |
| 12 | Pitch+Quiz | 14s | 双 prompt-card |
| 13 | FABLE+CTA | 22s | 4 步 timeline |

## 资产

| 类别 | 路径 |
|---|---|
| 6 张原图 | `capture/assets/{cover,x-01..x-05}.jpg` |
| BGM | `audio/bgm-lofi.wav`（软链） |
| SFX | `audio/sfx/{beep,keystroke,transition}.wav`（软链） |
| 旁白 | `audio/narration.wav`（TTS 生成） |
| 字幕 | `transcript.json` |

## 命令

```bash
# Lint
npx hyperframes lint

# 验证
npx hyperframes validate

# 检视
npx hyperframes inspect

# 预览
npx hyperframes preview

# 渲染
npx hyperframes render --output renders/thariq-fable-unknowns.mp4
```

## 注意事项

- 13 个 beat 用 sub-composition 模式（`data-composition-src`），不在主 index.html 里写长 timeline
- 入口动画统一用 `tl.fromTo()`，offset 0.1-0.3s
- **不要写 exit tween** — 由 framework transition 处理
- prompt-card 视觉一致性：所有工具 beat 用同一 dark `#0E0E10` 卡 + 16-18px JetBrains Mono + 8px radius
- 红边高亮只在 Rumsfeld 矩阵的 "Unknown Unknowns" 用
