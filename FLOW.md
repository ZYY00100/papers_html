# 项目流程

## 仓库结构

| 文件 | 作用 |
|------|------|
| `*.html` | 部署的网页 |
| `index.html` | 文章列表首页 |
| `*.md` | md 源稿（备份/草稿） |
| `create-docx.js` | docx 生成脚本 |
| `FLOW.md` | 本流程文档 |

```
papers_html/                    ← 唯一 git 仓库
├── index.html                  ← 文章列表首页
├── 2026-05-22-claude-guide.html
├── 2026-05-22-ai-platforms-guide.html
├── agent-view-intro.html
├── agent-view-intro.md         ← md 源稿
├── 2026-05-22-claude使用指南-完整版.md
├── create-docx.js
└── FLOW.md
```

**部署原理**：推送到 `https://github.com/ZYY00100/papers_html.git` 的 main 分支后，GitHub Pages 自动部署。

---

## 两种内容来源

### A. 有 md 文件
1. 读取 md 内容
2. 按已有 HTML 的样式模板生成 HTML
3. 更新 `index.html` 加入文章卡片
4. `papers_html/` 内 git add → commit → push

### B. 直接给内容或方向
1. 你直接给内容 / 主题方向
2. 我生成 HTML（直接带样式，不需要先写 md）
3. 更新 `index.html` 加入文章卡片
4. `papers_html/` 内 git add → commit → push

---

## 标准流程（每次发新文章）

1. **生成 HTML** — 文件名格式：`YYYY-MM-DD-<主题>.html`，放在 `papers_html/` 内
2. **更新 index.html** — 在 `.article-list` 里加一个 `.article-card` 链接新 HTML
3. **推送部署** — 在 `papers_html/` 内：
   ```bash
   git add .
   git commit -m "Add/Update <文章标题>"
   git push
   ```
4. 等待 GitHub Pages 自动构建，访问 `https://ZYY00100.github.io/papers_html/` 查看

---

## 样式模板

HTML 使用统一样式（见现有文件），包含：
- 浅灰网格背景 + 淡金色强调色
- Cormorant Garamond + Noto Serif SC + Inter 字体组合
- 卡片式文章列表，进入动画
- 移动端适配