#!/usr/bin/env python3
"""Build 2026-07-12-chatgpt-prompting-guide.html from the khairallah reference skeleton."""
import re
from pathlib import Path

BASE = Path("/Users/a1-6/My_channel/papers/papers_html")
REF = BASE / "2026-06-08-30-system-prompts-khairallah.html"
OUT = BASE / "2026-07-12-chatgpt-prompting-guide.html"

ref = REF.read_text()

# ============================================================================
# 13 prompt cards (EN = OpenAI original, CN = Zhu Youyi voice translation)
# ============================================================================

CARDS = [
    {
        "num": "01",
        "en_name": "Understand a Topic",
        "cn_name": "解释一个概念",
        "section": "Chat · 概念理解",
        "en": (
            "Explain how compound interest works for someone who has never invested. "
            "Use one concrete example and define any financial terms you introduce."
        ),
        "cn": (
            "用初学者能秒懂的话讲清楚「复利」是怎么回事。"
            "举一个具体的例子（房贷或者定投都行），所有金融术语都用大白话再解释一遍。"
        ),
    },
    {
        "num": "02",
        "en_name": "Draft and Refine Writing",
        "cn_name": "起草并打磨一段文字",
        "section": "Chat · 写作起草",
        "en": (
            "Draft a friendly email declining this invitation because I will be traveling. "
            "Keep it under 120 words and leave the door open for a future event."
        ),
        "cn": (
            "帮我写一封礼貌的拒绝邮件——因为那段时间我要出差，婉拒这次的邀请。"
            "全文控制在 120 字以内，语气要友好，给对方留个台阶，下次活动还可以再约。"
        ),
    },
    {
        "num": "03",
        "en_name": "Compare Options",
        "cn_name": "对比几个选项",
        "section": "Chat · 选项对比",
        "en": (
            "Compare these two phone plans for one person who travels internationally twice a year. "
            "Show the important differences in a table, then recommend one and explain the tradeoff."
        ),
        "cn": (
            "帮我对比这两款手机套餐——我每年出国两次。"
            "把核心差异整理成一张表格，然后给我一个推荐，再说一下为什么这个推荐不是完美的（有什么取舍）。"
        ),
    },
    {
        "num": "04",
        "en_name": "Make a Practical Plan",
        "cn_name": "做一份落地方案",
        "section": "Chat · 落地方案",
        "en": (
            "Plan five weekday dinners that take less than 30 minutes. "
            "Avoid peanuts, reuse ingredients across meals, and finish with one consolidated shopping list."
        ),
        "cn": (
            "帮我列 5 天的工作日晚餐方案，每道菜 30 分钟以内做完。"
            "不要花生；同一种食材尽量在多道菜里复用，别浪费；最后给我一张合并的购物清单。"
        ),
    },
    {
        "num": "05",
        "en_name": "Turn Source Material into Finished Files",
        "cn_name": "把素材变成成品文件",
        "section": "Work · 成品交付",
        "en": (
            "Use the attached quarterly reports to create a leadership brief and a six-slide presentation. "
            "The audience is the executive team. "
            "Lead with the three decisions they need to make, distinguish reported facts from your analysis, "
            "cite each number to its source file, and check that the brief and slides agree before you finish."
        ),
        "cn": (
            "用我附上的三份季报，做一份给董事会看的简报 + 一份 6 页 PPT。"
            "受众是高管团队。开头先讲他们必须拍板的三个决定；区分开「报告里写的事实」和「你的分析」；"
            "每个数字都标出来源文件；做完之后自己核对一遍，简报和 PPT 里的数字要对得上。"
        ),
    },
    {
        "num": "06",
        "en_name": "Research a Decision",
        "cn_name": "调研一个决策",
        "section": "Work · 决策调研",
        "en": (
            "Research three customer-support platforms for a 50-person company. "
            "Compare pricing, security, integrations, and migration effort using current sources. "
            "Deliver a recommendation memo with links, assumptions, "
            "and the questions we should answer before signing a contract."
        ),
        "cn": (
            "帮我们调研 3 家客服平台，公司规模 50 人。"
            "对比价格、安全性、第三方集成、迁移工作量——资料用最新的。"
            "最后交付一份推荐 memo，里面要附链接、关键假设，以及签合同之前我们必须先回答的几个问题。"
        ),
    },
    {
        "num": "07",
        "en_name": "Coordinate a Launch",
        "cn_name": "协调一次发布",
        "section": "Work · 发布协调",
        "en": (
            "Create a launch plan for the attached product brief. "
            "Include the timeline, owners, dependencies, risks, announcement draft, customer FAQ, "
            "and a checklist for launch day. "
            "Flag any missing decisions before producing the final files."
        ),
        "cn": (
            "基于我附的产品 brief，给我出一份上线计划。"
            "要包含：时间表、责任人、依赖关系、风险点、上线公告草稿、用户 FAQ、上线日 checklist。"
            "如果发现还有关键决定没做，先标出来再生成最终文件。"
        ),
    },
    {
        "num": "08",
        "en_name": "One-Page Project Status Update",
        "cn_name": "一页纸项目状态",
        "section": "Work · 综合示例",
        "en": (
            "Prepare a one-page project status update for Monday's leadership meeting. "
            "Use the latest project plan in Drive and relevant decisions and updates from the project's Slack channel. "
            "Lead with the decisions leadership needs to make and the next steps. "
            "Summarize progress, risks, owners, and due dates. "
            "Keep approved dates and budget figures unchanged. "
            "Flag any conflicting or missing information, and don't send or publish anything. "
            "Before you finish, check that every next step has an owner and due date."
        ),
        "cn": (
            "给我准备一份一页纸的项目状态更新，周一高管会上要用。"
            "用 Drive 里最新的项目计划 + Slack 频道里相关的决定和进展。"
            "开头先讲领导层需要拍板的决定 + 下一步动作；"
            "后面总结进度、风险点、责任人、截止日期。"
            "已经审批过的日期和预算数字不要改。"
            "如果信息冲突或缺失，直接标出来；"
            "这份只是草稿，不要发也不要发布。"
            "做完之前自己检查：每一条「下一步」都要有责任人和截止日期。"
        ),
    },
    {
        "num": "09",
        "en_name": "Explain a Codebase",
        "cn_name": "解释一段代码",
        "section": "Codex · 代码理解",
        "en": (
            "Explain how the request flows through the selected code. "
            "Include:\n"
            "- a short summary of the responsibilities of each module involved\n"
            "- what data is validated and where\n"
            "- one or two \"gotchas\" to watch for when changing this"
        ),
        "cn": (
            "帮我解释一下这段代码里一个请求是怎么跑起来的。\n"
            "需要包含：\n"
            "- 每个模块分别负责什么（简短总结）\n"
            "- 数据在哪些地方被校验\n"
            "- 改这段代码时要注意的 1-2 个坑"
        ),
    },
    {
        "num": "10",
        "en_name": "Fix a Bug (CLI workflow)",
        "cn_name": "修一个 bug",
        "section": "Codex · bug 修复",
        "en": (
            "Bug: Clicking \"Save\" on the settings screen sometimes shows \"Saved\" "
            "but doesn't persist the change.\n\n"
            "Repro:\n"
            "1) Start the app: npm run dev\n"
            "2) Go to /settings\n"
            "3) Toggle \"Enable alerts\"\n"
            "4) Click Save\n"
            "5) Refresh the page: the toggle resets\n\n"
            "Constraints:\n"
            "- Do not change the API shape.\n"
            "- Keep the fix minimal and add a regression test if feasible.\n\n"
            "Start by reproducing the bug locally, then propose a patch and run checks."
        ),
        "cn": (
            "Bug：设置页点「保存」，有时候提示「已保存」但其实改动没生效。\n\n"
            "复现步骤：\n"
            "1) 启动应用：npm run dev\n"
            "2) 进入 /settings\n"
            "3) 打开「Enable alerts」开关\n"
            "4) 点 Save\n"
            "5) 刷新页面，开关又回到关闭状态\n\n"
            "约束：\n"
            "- 不要改 API 的字段结构。\n"
            "- 改动尽量小，能加回归测试就加。\n\n"
            "先在本地复现一遍 bug，然后给我打个 patch，再跑一下相关检查。"
        ),
    },
    {
        "num": "11",
        "en_name": "Write a Test",
        "cn_name": "写一个测试",
        "section": "Codex · 测试编写",
        "en": (
            "Write a unit test for this function. Follow conventions used in other tests."
        ),
        "cn": (
            "给这个函数写一个单测。命名风格、目录结构都按仓库里已有的测试来。"
        ),
    },
    {
        "num": "12",
        "en_name": "Prototype from a Screenshot",
        "cn_name": "看截图起原型",
        "section": "Codex · 原型搭建",
        "en": (
            "Create a new dashboard based on this image.\n\n"
            "Constraints:\n"
            "- Use react, vite, and tailwind. Write the code in typescript.\n"
            "- Match spacing, typography, and layout as closely as possible.\n\n"
            "Outputs:\n"
            "- A new route/page that renders the UI\n"
            "- Any small components needed\n"
            "- README.md with instructions to run it locally"
        ),
        "cn": (
            "根据我附的截图，做一个新的 dashboard 页面。\n\n"
            "约束：\n"
            "- 用 react + vite + tailwind，代码用 TypeScript 写。\n"
            "- 间距、字体、布局尽量贴近原图。\n\n"
            "交付物：\n"
            "- 一个新的 route/page 渲染这个 UI\n"
            "- 拆出来需要的小组件\n"
            "- 一份 README.md，写清本地怎么跑起来"
        ),
    },
    {
        "num": "13",
        "en_name": "Iterate on UI with Live Updates",
        "cn_name": "边改边看的 UI 迭代",
        "section": "Codex · UI 迭代",
        "en": (
            "Propose 2-3 styling improvements for the landing page."
        ),
        "cn": (
            "给我 2-3 个 landing page 样式优化的方向，挑你觉得最能提升质感的说。"
        ),
    },
]


def card_html(c):
    en = c["en"].replace("\n", "\n      ")
    cn = c["cn"].replace("\n", "\n      ")
    return f'''      <!-- {c["num"]} {c["en_name"]} -->
      <div class="prompt-card" data-card id="prompt-{c["num"]}">
        <div class="prompt-card-head">
          <span class="prompt-card-tag">
            <span class="prompt-num">{c["num"]}</span>
            <span class="prompt-name-stack">
              <span class="prompt-name-en">{c["en_name"]}</span>
              <span class="prompt-name-cn">{c["cn_name"]}</span>
            </span>
          </span>
          <div class="prompt-card-actions">
            <div class="lang-toggle">
              <button class="lang-btn active" data-lang="en">EN</button>
              <button class="lang-btn" data-lang="cn">中文</button>
            </div>
            <button class="copy-btn" data-copy-btn>Copy</button>
          </div>
        </div>
        <div class="prompt-card-body" data-lang="en">{
        en}</div>
        <div class="prompt-card-body" data-lang="cn" hidden>{
        cn}</div>
      </div>'''


# ============================================================================
# New MAIN content (replaces hero + intro + all 30-prompt sections)
# ============================================================================

NEW_MAIN = f'''    <!-- HERO -->
    <section class="article-hero">
      <div class="article-category">AI PROMPT · OFFICIAL GUIDE</div>
      <h1 class="article-title">OpenAI 官方 Prompting 指南</h1>
      <p class="article-subtitle">四要素框架 + 13 个复制即用 prompt</p>
      <div class="article-byline">
        <span class="byline-author">朱有以</span>
        <span>·</span>
        <span class="byline-source">原文 learn.chatgpt.com/docs/prompting</span>
        <span>·</span>
        <span>2026/07/12</span>
      </div>
      <p class="article-desc">OpenAI 这次没讲 prompt 技巧，讲的是「怎么管理 prompt 的边界」——Goal + Context + Output + Boundaries 四要素框架，ChatGPT / Work / Codex 三个产品通用。原文 13 个例子全部做成双语卡片（中英切换 + 一键复制），按场景穿插在正文里。</p>
      <div class="hero-cover">
        <img src="./images/2026-07-12-chatgpt-prompting-guide/cover.svg" alt="OpenAI Prompting Guide 四要素框架封面" />
      </div>
    </section>

    <!-- TOC -->
    <section class="toc-mini">
      <div class="toc-mini-title">本文目录</div>
      <div class="toc-mini-links">
        <a href="#sec-intro">引子</a>
        <a href="#sec-framework">四要素框架</a>
        <a href="#sec-action">让结果能用</a>
        <a href="#sec-followup">进阶：多轮对话</a>
        <a href="#sec-products">跨产品落地</a>
        <a href="#sec-takeaway">我的解读</a>
      </div>
    </section>

    <!-- INTRO -->
    <section class="article-intro" id="sec-intro">
      <p class="intro-lead">2026 年，OpenAI 自己出了一份 <strong>Prompting 官方指南</strong>。</p>
      <p class="intro-lead">但这次，OpenAI 没讲 prompt 技巧——它讲的是<strong>四要素框架</strong>。</p>
      <p class="intro-statement">读完之后你会发现：所谓"好的 prompt"，本质上就是把这四件事说清楚——Goal、Context、Output、Boundaries。剩下的 follow-up、迭代、跨产品（Chat/Work/Codex）落地，都是这个框架的延伸。</p>
      <p class="intro-statement">下面我把这份指南翻译、拆解、再加上我自己的解读。13 个官方示例全部做成双语卡片——EN 是 OpenAI 原文，CN 是按中文工作场景重写的中文意译（不直译，去机翻味），两者都能直接复制粘贴。</p>

      <figure class="inline-figure voice-dict-figure">
        <div class="voice-dict-pair">
          <img src="./images/2026-07-12-chatgpt-prompting-guide/voice-dictation-light.webp" alt="ChatGPT 桌面端语音输入指示器 - 浅色主题" />
          <img src="./images/2026-07-12-chatgpt-prompting-guide/voice-dictation-dark.webp" alt="ChatGPT 桌面端语音输入指示器 - 深色主题" />
        </div>
        <figcaption>OpenAI 也在推动更自然的输入方式——桌面端 Ctrl+M 可以语音输入，写 prompt 不一定要打字。</figcaption>
      </figure>
    </section>

    <!-- PULL QUOTE -->
    <section class="pull-quote">
      <div class="pull-quote-text">好的 prompt = <span class="arrow">→</span> 四件事说清楚</div>
      <div class="pull-quote-caption">Goal · Context · Output · Boundaries — OpenAI 官方框架</div>
    </section>

    <!-- SECTION 1: 四要素框架 -->
    <section class="section" id="sec-framework">
      <div class="section-head">
        <div class="section-num">01</div>
        <div class="section-title-group">
          <div class="section-kicker">THE FOUR ELEMENTS</div>
          <h2 class="section-title">四要素框架</h2>
          <div class="section-range">GOAL · CONTEXT · OUTPUT · BOUNDARIES</div>
        </div>
      </div>
      <p class="prompt-cards-intro">OpenAI 把所有好 prompt 的共性压成了这四个要素。不用每个 prompt 都填满，挑有用的说就行。</p>

      <div class="framework-grid">
        <div class="framework-card">
          <div class="framework-num">01</div>
          <div class="framework-en">Goal</div>
          <div class="framework-cn">目标</div>
          <div class="framework-desc">你要 ChatGPT 做什么？</div>
        </div>
        <div class="framework-card">
          <div class="framework-num">02</div>
          <div class="framework-en">Context</div>
          <div class="framework-cn">上下文</div>
          <div class="framework-desc">哪些信息/资料会影响结果？</div>
        </div>
        <div class="framework-card">
          <div class="framework-num">03</div>
          <div class="framework-en">Output</div>
          <div class="framework-cn">输出</div>
          <div class="framework-desc">要什么格式、长度、详细程度？</div>
        </div>
        <div class="framework-card">
          <div class="framework-num">04</div>
          <div class="framework-en">Boundaries</div>
          <div class="framework-cn">边界</div>
          <div class="framework-desc">哪些不能动？要不要先确认？</div>
        </div>
      </div>

      <h3 class="section-h3">一句话：先说 Goal，再补 Context，再讲 Output，最后用 Boundaries 兜底</h3>
      <p class="prose">OpenAI 的原话：</p>
      <blockquote class="openai-quote">
        A short prompt is often enough. For larger or more important tasks, include the parts that matter:
        <strong>Goal</strong> — What should ChatGPT do? <strong>Context</strong> — What information or sources will help?
        <strong>Output</strong> — What format, length, or level of detail do you need?
        <strong>Boundaries</strong> — What must stay unchanged? What should ChatGPT avoid or check with you before it acts?
      </blockquote>
      <p class="prose">中文直译：短的 prompt 经常就够了。但任务大或重要时，把下面四块填上——目标、上下文、输出、边界。</p>

      <h3 class="section-h3">第一个例子：用"Goal + Output"讲清楚一个概念</h3>
      <p class="prose">这是个 Chat 场景下"解释一个概念"的 prompt。你会发现：哪怕只写了 Goal 和 Output，效果就比"跟我讲讲复利"好得多。</p>

{card_html(CARDS[0])}

      <p class="prose">看 EN 原文——只有两句话：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Explain how compound interest works</li>
        <li><strong>Output</strong>：for someone who has never invested · Use one concrete example · define any financial terms</li>
      </ul>
      <p class="prose">没有 Context（不需要文件、不需要联网），没有 Boundaries（不涉及敏感操作）。但 Goal + Output 写清楚后，结果已经好过 90% 的"跟我讲讲 X"了。</p>
    </section>

    <!-- SECTION 2: 让结果"能用" -->
    <section class="section" id="sec-action">
      <div class="section-head">
        <div class="section-num">02</div>
        <div class="section-title-group">
          <div class="section-kicker">MAKE IT USEFUL</div>
          <h2 class="section-title">让结果"能用"</h2>
          <div class="section-range">DESCRIBE RESULT · ADD CONTEXT · SET BOUNDARIES</div>
        </div>
      </div>
      <p class="prompt-cards-intro">四要素框架拆开看，每个要素都有具体的写法。下面是三个实战：起草一段文字、对比选项、设置边界。</p>

      <h3 class="section-h3">2.1 先讲结果，再讲步骤</h3>
      <p class="prose">OpenAI 反复强调的一点：<strong>从结果开始，而不是从步骤开始</strong>。告诉 ChatGPT 你要什么（Goal + Output），把过程留给它自己找。</p>

{card_html(CARDS[1])}

      <p class="prose">EN 原文结构：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Draft a friendly email declining this invitation</li>
        <li><strong>Context</strong>：because I will be traveling（一个原因就够）</li>
        <li><strong>Output</strong>：under 120 words · leave the door open for a future event</li>
      </ul>
      <p class="prose">没有列步骤（不要写"第一步问候，第二步解释，第三步结尾"），只讲结果。ChatGPT 会自己找最合适的表达方式。</p>

      <h3 class="section-h3">2.2 对比 + 表格 + 推荐——把"判断"也写在 prompt 里</h3>
      <p class="prose">要 ChatGPT 帮你做决定，不要只问"哪个好"。把判断标准也写进去——格式、权衡、推荐动作。</p>

{card_html(CARDS[2])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Compare these two phone plans</li>
        <li><strong>Context</strong>：for one person who travels internationally twice a year</li>
        <li><strong>Output</strong>：Show the important differences in a table · recommend one · explain the tradeoff</li>
      </ul>
      <p class="prose">注意 Output 的写法——不是"给我一份对比"，而是"表格 + 推荐 + 解释权衡"。你想要的"判断动作"都明示了。</p>

      <h3 class="section-h3">2.3 Boundaries——最重要的、也最容易被忽略的一块</h3>
      <p class="prose">OpenAI 对 Boundaries 的定义：<strong>边界是那几条让 ChatGPT 别做出格动作的指令</strong>。需要的时候才加，不是什么时候都要写。</p>
      <p class="prose">原文给的四个典型 Boundary：</p>
      <ul class="prose-list">
        <li>Keep the approved dates and budget figures unchanged.（日期和预算不要改）</li>
        <li>Use only the supplied sources. Flag missing information instead of guessing.（只用提供的资料，缺了标出来，不要瞎猜）</li>
        <li>Keep recommendations within the stated budget.（推荐要在预算范围内）</li>
        <li>Prepare the message as a draft. Don't send it.（先做草稿，别发）</li>
      </ul>
      <p class="prose">原则：<strong>只写那 1-2 个真重要的边界</strong>。你不需要控制 ChatGPT 的每一步。</p>
    </section>

    <!-- SECTION 3: 进阶 -->
    <section class="section" id="sec-followup">
      <div class="section-head">
        <div class="section-num">03</div>
        <div class="section-title-group">
          <div class="section-kicker">FOLLOW-UP & STEERING</div>
          <h2 class="section-title">进阶：多轮对话</h2>
          <div class="section-range">FOLLOW-UP · STEER · QUEUE</div>
        </div>
      </div>
      <p class="prompt-cards-intro">第一条 prompt 不用完美。先发，再根据结果改——这是 OpenAI 反复强调的迭代思路。</p>

      <h3 class="section-h3">3.1 你的第一条 prompt 不用完美</h3>
      <p class="prose">原文原话：</p>
      <blockquote class="openai-quote">
        Your first prompt doesn't need to be perfect. Review the result, then ask for the specific change you want.
      </blockquote>
      <p class="prose">中文：你第一条 prompt 不用写得完美。先发，看结果，再追问具体的修改。</p>
      <p class="prose">一个"补一句"的范例：</p>

      <div class="quote-block">
        <div class="quote-en">"Make the opening more direct, keep the evidence, and move the recommendation above the background section."</div>
        <div class="quote-cn">「开头再直接一点，证据保留，把推荐结论挪到背景介绍前面。」</div>
      </div>

      <p class="prose">可以加缺失的资料、纠正方向、要别的选项、调整详细程度——都不需要重头来过。</p>

      <h3 class="section-h3">3.2 Steering 和 Queuing——Codex 时代的两个新动作</h3>
      <p class="prose">当 Codex 已经在跑时，你可以再发一条消息，不用等当前任务跑完：</p>
      <ul class="prose-list">
        <li><strong>Steer（介入）</strong>：把消息塞进当前这轮。用来改方向、补漏、提供新信息。</li>
        <li><strong>Queue（排队）</strong>：把消息存到下一轮。用来做"等这个跑完再做"的跟进。</li>
      </ul>
      <p class="prose">桌面端默认行为在 <code>Settings > General > Follow-up behavior</code> 里改。Codex CLI 里：<code>Enter</code> 介入当前轮，<code>Tab</code> 排队到下一轮。</p>

      <h3 class="section-h3">3.3 一个多约束的"实战 prompt"</h3>
      <p class="prose">下面这个例子同时塞了四要素——Goal、Context、Output、Boundaries 全都到位了。注意它是怎么处理多轮迭代的暗示："做完之前自己检查"。</p>

{card_html(CARDS[3])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Plan five weekday dinners</li>
        <li><strong>Context</strong>：less than 30 minutes（隐含的时间约束）</li>
        <li><strong>Output</strong>：5 道菜 + 食材步骤 + 一张合并购物清单</li>
        <li><strong>Boundaries</strong>：Avoid peanuts（唯一明确写出的边界）</li>
      </ul>
      <p class="prose">"reuse ingredients across meals" 是 Output 里隐含的优化目标——它没有写成 Boundary（"必须重用"），而是作为 Output 的偏好，让 ChatGPT 自由发挥。</p>
    </section>

    <!-- SECTION 4: 跨产品落地 -->
    <section class="section" id="sec-products">
      <div class="section-head">
        <div class="section-num">04</div>
        <div class="section-title-group">
          <div class="section-kicker">CHAT · WORK · CODEX</div>
          <h2 class="section-title">跨产品落地</h2>
          <div class="section-range">PROMPT 05 – 13</div>
        </div>
      </div>
      <p class="prompt-cards-intro">同一套四要素框架，在 Chat、Work、Codex 三个产品上的不同写法。下面 9 个例子按场景分组。</p>

      <h3 class="section-h3">4.1 Chat——轻量问答场景</h3>
      <p class="prose">已经在前面看到 4 个 Chat 场景了：解释概念、起草文字、对比选项、做计划。它们都不需要文件、不需要工具，Goal + Output 写清楚就够。</p>

      <h3 class="section-h3">4.2 Work——多源、多步骤、要交成品</h3>
      <p class="prose">Work 适合时间长的、需要多种来源或工具、要按顺序执行的任务——比如把三份季报提炼成董事会一页纸。</p>

      <h4 class="section-h4">5. 把素材变成成品文件</h4>

{card_html(CARDS[4])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：create a leadership brief and a six-slide presentation</li>
        <li><strong>Context</strong>：Use the attached quarterly reports · audience is the executive team</li>
        <li><strong>Output</strong>：lead with three decisions · distinguish facts from analysis · cite numbers to source files · check that brief and slides agree</li>
        <li><strong>Boundaries</strong>：（隐含）不能瞎编数字；要做完自己核对</li>
      </ul>

      <h4 class="section-h4">6. 调研一个决策</h4>

{card_html(CARDS[5])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Research three customer-support platforms</li>
        <li><strong>Context</strong>：for a 50-person company · using current sources</li>
        <li><strong>Output</strong>：Compare pricing · security · integrations · migration effort · recommendation memo with links and assumptions</li>
        <li><strong>Boundaries</strong>：use current sources（隐含的"不要用过期资料"）</li>
      </ul>

      <h4 class="section-h4">7. 协调一次发布</h4>

{card_html(CARDS[6])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Create a launch plan</li>
        <li><strong>Context</strong>：attached product brief</li>
        <li><strong>Output</strong>：timeline · owners · dependencies · risks · announcement draft · customer FAQ · checklist for launch day</li>
        <li><strong>Boundaries</strong>：Flag any missing decisions before producing the final files</li>
      </ul>

      <h4 class="section-h4">8. 综合示例：一页纸项目状态</h4>
      <p class="prose">这是官方给的"四要素齐全"的范例——Goal + Context + Output + Boundaries 全部明示，是整份指南最有代表性的一张卡片。</p>

{card_html(CARDS[7])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Prepare a one-page project status update for Monday's leadership meeting</li>
        <li><strong>Context</strong>：Use the latest project plan in Drive · relevant decisions and updates from the project's Slack channel</li>
        <li><strong>Output</strong>：Lead with the decisions · next steps · summarize progress · risks · owners · due dates</li>
        <li><strong>Boundaries</strong>：Keep approved dates and budget figures unchanged · don't send or publish anything</li>
        <li><strong>Final check</strong>：Before you finish, check that every next step has an owner and due date</li>
      </ul>
      <p class="prose">最后一句 "Before you finish, check that..." 是 OpenAI 反复用的句式——把"自检动作"写进 prompt 里，让 ChatGPT 在交活之前自己跑一遍检查。</p>

      <h3 class="section-h3">4.3 Codex——开发者工作流</h3>
      <p class="prose">Codex 的 prompt 比 Chat/Work 复杂一些：它要涉及文件路径、CLI 命令、IDE 选区、复现步骤。下面 5 个例子是开发者最常用的场景。</p>
      <p class="prose">Codex 的 IDE 插件会自动把当前打开的文件作为上下文；CLI 里则需要用 <code>@path</code> 或者 <code>/mention</code> 显式附加文件。</p>

      <h4 class="section-h4">9. 解释一段代码（IDE）</h4>

{card_html(CARDS[8])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Explain how the request flows through the selected code</li>
        <li><strong>Context</strong>：（IDE 自动带入）选中的代码 + 当前打开的文件</li>
        <li><strong>Output</strong>：responsibilities of each module · what data is validated and where · 1-2 "gotchas"</li>
      </ul>

      <h4 class="section-h4">10. 修一个 bug（CLI）</h4>
      <p class="prose">这是个典型的"bug 报告模板"——复现步骤 + 约束 + 期望动作 全部写清楚。</p>

{card_html(CARDS[9])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Fix the bug causing "Saved" to show without persisting changes</li>
        <li><strong>Context</strong>：完整复现步骤（npm run dev → /settings → toggle → Save → refresh）</li>
        <li><strong>Output</strong>：Find the bug · propose a fix · tell me how to verify it</li>
        <li><strong>Boundaries</strong>：Do not change the API shape · Keep the fix minimal · add a regression test if feasible</li>
        <li><strong>Final check</strong>：Start by reproducing the bug locally, then propose a patch and run checks</li>
      </ul>

      <h4 class="section-h4">11. 写一个测试（IDE）</h4>
      <p class="prose">最短的一张 Codex 卡片——但已经够用。IDE 自动带入选中的函数，Output 写明"按仓库已有约定"。</p>

{card_html(CARDS[10])}

      <h4 class="section-h4">12. 看截图起原型（CLI）</h4>
      <p class="prose">Codex CLI 支持直接拖图片进终端作为输入。这个例子把"视觉要求"和"实现约束"分开写——图片管视觉，文字管技术栈。</p>

{card_html(CARDS[11])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Create a new dashboard based on this image</li>
        <li><strong>Context</strong>：（图片提供视觉）</li>
        <li><strong>Output</strong>：Match spacing · typography · layout as closely as possible · new route · small components · README.md with run instructions</li>
        <li><strong>Boundaries</strong>：Use react · vite · tailwind · TypeScript</li>
      </ul>
      <p class="prose">图片无法表达的状态（hover、校验、键盘交互），要靠文字补——这是 OpenAI 反复强调的"视觉 ≠ 全部需求"。</p>

      <h4 class="section-h4">13. 边改边看的 UI 迭代（CLI）</h4>
      <p class="prose">Codex 的特点是能跑 dev server 然后给你实时改。每轮迭代聚焦一个小改动，不要堆需求。</p>

{card_html(CARDS[12])}

      <p class="prose">EN 原文拆解：</p>
      <ul class="prose-list">
        <li><strong>Goal</strong>：Propose 2-3 styling improvements for the landing page</li>
        <li><strong>Context</strong>：（CLI 自动看到代码）</li>
        <li><strong>Output</strong>：3 个可选方向，让用户挑</li>
      </ul>
      <p class="prose">接下来的迭代都是"小步快跑"——选一个方向 → 缩小范围 → 改 → 看效果 → 再缩小。原文给了一个完整迭代节奏：</p>
      <ol class="prose-list">
        <li>选方向（Go with option 2）</li>
        <li>缩小范围（only the header · make typography more editorial · increase whitespace · looks good on mobile）</li>
        <li>下一轮（reduce visual noise · keep layout · simplify colors · remove redundant borders）</li>
        <li>循环</li>
      </ol>
    </section>

    <!-- SECTION 5: 我的解读 -->
    <section class="section" id="sec-takeaway">
      <div class="section-head">
        <div class="section-num">05</div>
        <div class="section-title-group">
          <div class="section-kicker">MY TAKE</div>
          <h2 class="section-title">我的解读</h2>
          <div class="section-range">WHAT THIS GUIDE IS REALLY SAYING</div>
        </div>
      </div>

      <h3 class="section-h3">5.1 OpenAI 在引导你"管理 prompt 的边界"，而不是"写好 prompt 的技巧"</h3>
      <p class="prose">这是这份指南最反直觉的一点。</p>
      <p class="prose">如果你期待的是"10 个 prompt 技巧"、"高级 prompt 写法"、"few-shot 教程"——你会失望。OpenAI 这次完全没有讲这些。</p>
      <p class="prose">它讲的是：<strong>不要试图控制 ChatGPT 的每一步</strong>。只要把四件事说清楚（Goal + Context + Output + Boundaries），剩下的过程让它自己决定。</p>
      <p class="prose">这是一个范式转换——从"我写 prompt 技巧"到"我和 AI 协作时怎么定边界"。</p>

      <h3 class="section-h3">5.2 四要素里，Boundaries 是真正的护城河</h3>
      <p class="prose">很多人写 prompt 都堆在 Goal 和 Output 上——"给我写一篇文章，要 1000 字，要三个小标题"。但 Boundaries 才是让 AI 输出变得可用的关键。</p>
      <p class="prose">OpenAI 给的四个典型 Boundary 都很朴素：</p>
      <ul class="prose-list">
        <li>日期和预算不要改</li>
        <li>只用提供的资料，缺了标出来</li>
        <li>推荐要在预算范围内</li>
        <li>先做草稿，别发</li>
      </ul>
      <p class="prose">它们看起来都是"废话"，但每一个都是上一次"AI 帮倒忙"换来的教训。<strong>Boundaries 不是 prompt 技巧，是事故复盘</strong>。</p>

      <h3 class="section-h3">5.3 "做完之前自己检查"——这句要抄下来</h3>
      <p class="prose">整份指南里出现频率最高的一个句式是：</p>
      <blockquote class="openai-quote">
        Before you finish, check that every [thing] has [property].
      </blockquote>
      <p class="prose">翻译："做完之前自己检查一遍，每个 [东西] 都要有 [属性]。"</p>
      <p class="prose">在 prompt 末尾加一句自检指令——比"写好一点"、"仔细一点"管用一百倍。因为它把"仔细"这个抽象词变成了具体的检查清单。</p>
      <p class="prose">下次写 prompt 的时候，最后一句加上："Before you finish, check that..." 试试。</p>

      <h3 class="section-h3">5.4 对中文用户的额外提醒</h3>
      <p class="prose">官方例子里有几个英文习惯，放到中文场景里要替换掉：</p>
      <ul class="prose-list">
        <li><code>lead with X</code> → "开头先讲 X"、"把 X 放最前面"</li>
        <li><code>flag</code> → "标出来"、"提示一下"、"提醒一句"</li>
        <li><code>cite X to Y</code> → "标注 X 出处为 Y"</li>
        <li><code>before you finish, check that...</code> → "做完之前检查一遍..."</li>
      </ul>
      <p class="prose">直接用中文 prompt 也行，但把英文短语当模板套用更稳——英文社区已经把句式打磨过了。</p>

      <h3 class="section-h3">5.5 一句话带走</h3>
      <div class="takeaway-box">
        <p class="takeaway-text">好的 prompt = Goal + Context + Output + Boundaries 四件事说清楚。<br/>剩下交给 AI 自己找路径。</p>
        <p class="takeaway-en">A good prompt is just four things said clearly. Leave the rest to the model.</p>
      </div>

      <p class="prose">上面 13 张卡片覆盖了 Chat / Work / Codex 三种典型场景。建议先挑 3 张你日常会用到的场景复制下来——比如"起草邮件"、"做计划"、"修 bug"——存到你的 prompt 模板库。一个月后回来补剩下的。</p>
    </section>'''

# ============================================================================
# Floating nav (replaces the 30-prompt khairallah nav)
# ============================================================================

NAV_ITEMS = []
for c in CARDS:
    NAV_ITEMS.append(f'''      <a href="#prompt-{c["num"]}" class="nav-item">
        <span class="nav-item-num">{c["num"]}</span>
        <span class="nav-item-stack">
          <span class="nav-item-en">{c["en_name"]}</span>
          <span class="nav-item-cn">{c["cn_name"]}</span>
        </span>
      </a>''')
NAV_HTML = "\n".join(NAV_ITEMS)

NEW_NAV = f'''  <nav class="floating-nav-panel" id="navPanel">
    <div class="nav-panel-header">本文 13 个 Prompt</div>
    <div class="nav-panel-content">
      <div class="nav-category">CHAT · 4 张</div>
{NAV_ITEMS[0]}
{NAV_ITEMS[1]}
{NAV_ITEMS[2]}
{NAV_ITEMS[3]}
      <div class="nav-category">WORK · 4 张</div>
{NAV_ITEMS[4]}
{NAV_ITEMS[5]}
{NAV_ITEMS[6]}
{NAV_ITEMS[7]}
      <div class="nav-category">CODEX · 5 张</div>
{NAV_ITEMS[8]}
{NAV_ITEMS[9]}
{NAV_ITEMS[10]}
{NAV_ITEMS[11]}
{NAV_ITEMS[12]}
    </div>
  </nav>'''

# ============================================================================
# Patch the reference file
# ============================================================================

# 1. Replace <title>
new_html = re.sub(
    r"<title>.*?</title>",
    "<title>OpenAI 官方 Prompting 指南：四要素框架 + 13 个复制即用 prompt · 朱有以</title>",
    ref,
    count=1,
)

# 2. Replace main content (between <main class="container"> and </main>)
m = re.search(r'<main class="container">.*?</main>', new_html, flags=re.DOTALL)
if not m:
    raise SystemExit("Could not find <main> in reference")
new_html = new_html[:m.start()] + f'<main class="container">\n\n{NEW_MAIN}\n\n  </main>' + new_html[m.end():]

# 3. Replace floating nav content
m = re.search(r'<nav class="floating-nav-panel" id="navPanel">.*?</nav>', new_html, flags=re.DOTALL)
if not m:
    raise SystemExit("Could not find <nav class=\"floating-nav-panel\">")
new_html = new_html[:m.start()] + NEW_NAV + new_html[m.end():]

# 4. Add new styles (TOC + framework grid + voice-dict-pair + quote-block + takeaway-box + inline-figure)
# These are inserted into <style> just before </style>
EXTRA_CSS = '''
    /* ===== Article-specific additions ===== */
    .toc-mini {
      max-width: 680px;
      margin: 32px auto 0;
      padding: 18px 22px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
    }
    .toc-mini-title {
      font-family: 'Rajdhani', sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.25em;
      color: var(--accent-gold);
      margin-bottom: 10px;
    }
    .toc-mini-links {
      display: flex;
      flex-wrap: wrap;
      gap: 8px 14px;
      font-size: 14px;
    }
    .toc-mini-links a {
      color: var(--text-secondary);
      text-decoration: none;
      padding: 4px 10px;
      border: 1px solid var(--border-subtle);
      border-radius: 4px;
      transition: all 0.2s ease;
    }
    .toc-mini-links a:hover {
      color: var(--text-primary);
      border-color: var(--accent-gold);
      background: rgba(201, 169, 98, 0.06);
    }
    .hero-cover {
      max-width: 560px;
      margin: 32px auto 0;
    }
    .hero-cover img {
      width: 100%;
      height: auto;
      display: block;
      border-radius: 6px;
      box-shadow: var(--shadow-hover);
    }
    .framework-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin: 24px 0 8px;
    }
    @media (max-width: 600px) {
      .framework-grid { grid-template-columns: 1fr; }
    }
    .framework-card {
      padding: 22px 22px 20px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      transition: box-shadow 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  border-color 0.3s ease;
    }
    .framework-card:hover {
      transform: scale(1.006);
      box-shadow: var(--shadow-hover);
      border-color: rgba(201, 169, 98, 0.4);
    }
    .framework-num {
      font-family: 'Rajdhani', sans-serif;
      font-size: 12px;
      letter-spacing: 0.2em;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }
    .framework-en {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.1;
    }
    .framework-cn {
      font-family: 'Noto Serif SC', serif;
      font-size: 14px;
      color: var(--text-secondary);
      margin-top: 2px;
    }
    .framework-desc {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 12px;
      line-height: 1.6;
    }
    .openai-quote {
      margin: 20px 0;
      padding: 18px 22px;
      background: var(--bg-card);
      border-left: 3px solid var(--accent-gold);
      font-size: 15px;
      color: var(--text-primary);
      line-height: 1.85;
    }
    .openai-quote strong {
      color: var(--accent-gold-dim);
    }
    .quote-block {
      margin: 18px 0;
      padding: 18px 22px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
    }
    .quote-en {
      font-family: 'Cormorant Garamond', serif;
      font-size: 16px;
      color: var(--text-primary);
      font-style: italic;
    }
    .quote-cn {
      font-size: 14px;
      color: var(--text-secondary);
      margin-top: 8px;
    }
    .inline-figure {
      margin: 32px 0;
      text-align: center;
    }
    .voice-dict-pair {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    @media (max-width: 600px) {
      .voice-dict-pair { grid-template-columns: 1fr; }
    }
    .voice-dict-pair img {
      width: 100%;
      height: auto;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
    }
    .inline-figure figcaption {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 10px;
    }
    .section-h3 {
      font-family: 'Noto Serif SC', serif;
      font-size: 19px;
      font-weight: 600;
      color: var(--text-primary);
      margin: 32px 0 12px;
      letter-spacing: 0.02em;
    }
    .section-h4 {
      font-family: 'Rajdhani', sans-serif;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.2em;
      color: var(--accent-gold);
      margin: 28px 0 10px;
      text-transform: uppercase;
    }
    .prose {
      font-family: 'Noto Serif SC', serif;
      font-size: 16px;
      line-height: 1.9;
      color: var(--text-primary);
      margin: 12px 0;
    }
    .prose code {
      font-family: 'Courier New', monospace;
      font-size: 14px;
      padding: 2px 6px;
      background: var(--bg-code);
      color: #f5f5f7;
      border-radius: 3px;
    }
    .prose-list {
      font-family: 'Noto Serif SC', serif;
      font-size: 15px;
      line-height: 1.9;
      color: var(--text-primary);
      margin: 12px 0 12px 22px;
      padding-left: 8px;
    }
    .prose-list li { margin: 6px 0; }
    .prose-list strong {
      color: var(--accent-gold-dim);
      font-weight: 600;
    }
    .takeaway-box {
      margin: 28px 0;
      padding: 32px 28px;
      background: var(--bg-code);
      border-radius: 8px;
      text-align: center;
    }
    .takeaway-text {
      font-family: 'Noto Serif SC', serif;
      font-size: 20px;
      font-weight: 500;
      color: #f5f5f7;
      line-height: 1.6;
      letter-spacing: 0.02em;
    }
    .takeaway-en {
      font-family: 'Cormorant Garamond', serif;
      font-size: 16px;
      color: var(--accent-gold);
      font-style: italic;
      margin-top: 12px;
    }
'''
new_html = new_html.replace("  </style>", EXTRA_CSS + "  </style>", 1)

OUT.write_text(new_html)
print(f"Wrote {OUT}  ({len(new_html):,} chars)")
print(f"Prompt cards: {new_html.count('data-card')}")
print(f"Prompt bodies (EN+CN expected = 26): {new_html.count('prompt-card-body')}")