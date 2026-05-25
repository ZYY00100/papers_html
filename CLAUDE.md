# 朱有以 · AI 自媒体项目规范

---

## 一、项目概述

### 仓库结构

```
papers_html/                    ← 唯一 git 仓库
├── index.html                  ← 文章列表首页
├── 2026-05-25-ai-20-concepts.html
├── 2026-05-23-claude-cowork-templates.html
├── 2026-05-22-claude-guide.html
├── 2026-05-22-ai-platforms-guide.html
├── *.md                        ← md 源稿（备份/草稿）
├── create-docx.js              ← docx 生成脚本
└── CLAUDE.md                   ← 本规范文档
```

### 部署原理

推送到 `https://github.com/ZYY00100/papers_html.git` 的 main 分支后，GitHub Pages 自动部署。

访问地址：https://ZYY00100.github.io/papers_html/

---

## 二、内容来源与发布流程

### 两种内容来源

**A. 有 md 文件**
1. 读取 md 内容
2. 按已有 HTML 的样式模板生成 HTML
3. 更新 `index.html` 加入文章卡片
4. `papers_html/` 内 git add → commit → push

**B. 直接给内容或方向**
1. 你直接给内容 / 主题方向
2. 我生成 HTML（直接带样式，不需要先写 md）
3. 更新 `index.html` 加入文章卡片
4. `papers_html/` 内 git add → commit → push

### 标准发布流程（每次发新文章）

1. **生成 HTML** — 文件名格式：`YYYY-MM-DD-<主题>.html`
2. **更新 index.html** — 在 `.article-list` 里加一个 `.article-card`，在悬浮导航里加一个 `.nav-article`
3. **推送部署**
   ```bash
   git add .
   git commit -m "Add/Update <文章标题>"
   git push
   ```
4. 等待 GitHub Pages 自动构建

---

## 三、写作规范

### 触发条件

每次收到写文章或修改网页的需求时，按本规范执行。

### 第一步：需求确认

**生成或修改文章/网页之前，必须先向我询问许可。**

沟通顺序如下，每次只问一个问题：

1. **受众**：文章给谁看？（例：普通职场人、程序员、自媒体读者）
2. **核心看点**：这篇文想传达什么？（一个功能、一个概念、一个方法论）
3. **风格偏向**：偏科普/偏教程/偏案例/偏资讯？
4. **读者行动**：读完后希望读者做什么？（下载试用、实际操作、分享转发）

> 原则：结论先行，再给理由。不要铺垫、不要夸、不要"当然可以"。

确保需求沟通到位并达成一致后，再进入下一步。

### 设计方案

方案包含：

- **标题**（待确认）
- **篇幅**
- **结构**（章节安排，每章一句话说明目的）
- **亮点说明**（这篇文的独特角度）

结构方案给出 2-3 个供选择，附建议。最终方案由用户确认。

### 素材理解

动笔前必须吃透素材：

- 提炼核心概念
- 梳理功能点
- 确认关键细节（时间、来源、版本等）

用"我理解的是……，对吗？"的方式向用户确认。

### 起草

写作要求：

- **聚焦**：主要内容始终围绕核心主题，不要发散
- **通俗**：用词不官方，口语化，有活人感，真诚
- **结构清晰**：分章节，一章一个核心
- **场景驱动**：概念用具体场景带出来，不要干讲

### 用户审核

初稿完成后等待用户反馈，根据意见修改。可多轮。

### 交付

最终交付 `.md` 格式文件（主要版本），如需要可生成 `.docx`。

### 输出格式约定

- 文件名：`YYYY-MM-DD-<主题>-intro.md`
- 中文正文，代码/命令/变量名用英文
- 标题层级用 H1/H2/H3，不要乱用
- 列表用正式列表格式（`-` 或 `1.`），不要用 emoji 作为 bullet

---

## 四、网页样式规范

### 顶部 Header

所有文章页面（除 index.html）顶部需要包含：

```html
<header class="site-header">
  <div class="container">
    <a href="index.html" class="site-name">为 <span class="ai-glow">AI</span> 发电</a>
    <a href="index.html" class="back-link">← 返回文章列表</a>
  </div>
</header>
```

- `.site-header`：固定顶部，背景色，底部边框线
- `.ai-glow`：`color: #C8161D` + 红色发光效果

### 悬浮导航

**所有页面都需要**，右下角圆形按钮 + 展开面板：

```html
<button class="floating-nav-toggle" id="navToggle">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M4 6h16M4 12h16M4 18h16"/>
  </svg>
</button>

<nav class="floating-nav-panel" id="navPanel">
  <div class="nav-panel-header">目录导航</div>
  <div class="nav-panel-content">
    <!-- 链接列表 -->
  </div>
</nav>
```

对应 JS：
- 点击按钮切换面板显示/隐藏
- 点击外部关闭面板
- 点击链接后关闭面板

**index.html 悬浮导航显示文章列表**（标题 + 日期 + 简介），其他页面显示章节导航。

### 布局收紧原则

- 标题与正文之间**不留竖线装饰**
- 卡片左侧**不留竖线装饰**（`.card::before { display: none; }`）
- Hero 区域 padding：60-80px（不要超过 80px）
- 卡片内边距：28-32px
- 卡片间距：24-28px