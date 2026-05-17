const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, LevelFormat } = require('docx');
const fs = require('fs');

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 24 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 48, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 0, after: 240 }, alignment: AlignmentType.LEFT } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, color: "333333", font: "Arial" },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
      { id: "BodyText", name: "Body Text", basedOn: "Normal",
        run: { size: 24, color: "333333", font: "Arial" },
        paragraph: { spacing: { after: 160, line: 360 } } }
    ]
  },
  numbering: {
    config: [
      { reference: "bullet-list",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "bullet-list-2",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
    ]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [
      new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Claude Code 的 Agent View 功能：让多个 AI 同时帮你打工')] }),

      new Paragraph({ style: "BodyText", children: [new TextRun('今天刷 X 的时候，看到 Claude 官方发了一条新功能推送——Agent View，配了一个界面截图，看完第一反应是"这不就是多任务管理吗"。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('但点进去官方文档读了几分钟，发现不是我想的那样。这个功能解决的不只是"同时开几个窗口"的问题，而是重新定义了一个人和 AI 的协作方式。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('这篇文章就是我读完官方文档后的整理，想写给和我一样对 AI 工具感兴趣、但不想被技术细节绕进去的人。')] }),

      new Paragraph({ children: [new TextRun('---')] }),

      new Paragraph({ style: "BodyText", children: [new TextRun('你有没有过这种感觉——手上的活堆成山，改代码、写文档、看 PR，每一个都急，但 AI 只能一个一个来，排队排到崩溃。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('上周 Claude Code 更新了一个功能，叫 Agent View，解决的就是这个问题。它能让你同时调度多个 AI 干活，每个各干各的，互不干扰。你只需要坐在监工的位置上，盯着就行。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('多 agent 协作：不是 AI 变强了，而是多了几个帮手')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('在说 Agent View 之前，得先理解它背后的概念——多 agent 协作。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('你以前用 AI，可能是一个问题抛出去，AI 回复了，你再问下一个。它再强，也是一次只能干一件事。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('多 agent 协作的意思是：你同时派出去好几个 AI，各自从不同的方向帮你干活。')] }),

      new Paragraph({ style: "BodyText", children: [new TextRun('举一个具体的场景——')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('你今天要同时做三件事：')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('修一个 bug')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('写一份设计文档')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('回复 Code Review 意见')] }),
      new Paragraph({ style: "BodyText", spacing: { before: 160 }, children: [new TextRun('以前你只能排优先级，AI 干完一件你再喂下一件。现在你可以同时开三个 session，一个修 bug、一个写文档、一个看 PR，三个 AI 同步在线，各干各的。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('这就像你同时雇了三个实习生，每个人独立负责一摊。你是老板，分配任务、看进展、在关键节点把关。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('不是 AI 变聪明了，是干活的 AI 变多了。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('Agent View 是什么')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('那怎么同时管这么多 AI？')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('Claude Code 给了一个专门的界面，叫 Agent View。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('你只需要在终端里运行：')] }),

      new Paragraph({ spacing: { before: 120, after: 120 }, children: [new TextRun({ text: 'claude agents', bold: true, font: "Courier New", size: 24 })] }),

      new Paragraph({ style: "BodyText", children: [new TextRun('就会看到这样一个界面——')] }),
      new Paragraph({ spacing: { before: 120, after: 120 }, children: [new TextRun({ text: '（这里会展示 Agent View 的截图）', color: "888888", italics: true })] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('这张表里，每一行就是一个正在跑的任务。你一眼就能看到：')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('哪个在干活（Working）')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('哪个卡住了，需要你回复（Needs Input）')] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 }, children: [new TextRun('哪个已经完成了（Completed）')] }),
      new Paragraph({ style: "BodyText", spacing: { before: 160 }, children: [new TextRun('不用再去翻一个个聊天记录，直接在这里一览无余。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('怎么用')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('打开界面')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('在终端输入 claude agents，回车，界面就出来了。最底部有一个输入框。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('分发任务')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('在底部输入你想让 AI 干的事，回车，它就启动一个新的独立 session 开始跑。你可以同时输入多个任务，每个都是独立并行跑起来的。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('查看进展')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('你想知道某个任务在做什么？选中那一行，按空格，会弹出一个 peek 面板，显示它最近在做什么、输出了什么。不用离开 Agent View，不用打断其他任务。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('回复和操作')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('在 peek 面板里，你可以直接打字回复它。比如它问你要一个决策，你直接在面板里回答，回车发送，整个过程不用离开这个界面。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('深入操作')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('如果你觉得某个任务需要更深度地介入，选中那行，按回车或者右箭头，就"钻进"了那个 session，像正常使用 Claude Code 一样去操作。操作完，按左箭头回到 Agent View。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('整理界面')] }),
      new Paragraph({ numbering: { reference: "bullet-list-2", level: 0 }, children: [new TextRun('按 Ctrl+T 把某个任务钉到顶部，方便关注')] }),
      new Paragraph({ numbering: { reference: "bullet-list-2", level: 0 }, children: [new TextRun('按 Ctrl+S 在"按状态分组"和"按目录分组"之间切换')] }),
      new Paragraph({ numbering: { reference: "bullet-list-2", level: 0 }, children: [new TextRun('按 Ctrl+R 给任务改名，方便识别')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('几个说明')] }),

      new Paragraph({ style: "BodyText", children: [new TextRun({ text: '关于隔离：', bold: true }), new TextRun('每个 session 都在独立的 worktree 里运行，不会互相干扰文件编辑。你改代码的时候不会影响到另一个 session 在写的文档。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun({ text: '关于状态：', bold: true }), new TextRun('session 有六种状态——Working（运行中）、Needs Input（等你回复）、Idle（闲置）、Completed（完成）、Failed（出错）、Stopped（手动停止）。如果某个任务没响应了，看看状态栏。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun({ text: '关于持续运行：', bold: true }), new TextRun('只要你的电脑不关机睡眠，这些 background session 会一直跑。你关掉 Agent View 也没事，下次打开 claude agents，它们还会在那里等你。')] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('为什么这个更新值得关注')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('Agent View 不只是一个"多任务管理界面"。它代表了一种工作思路的变化：从"问 AI 一个问题"到"调配一群 AI"。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('以前你是单兵作战，AI 是你的辅助工具。现在你可以把 AI 当成团队来用，每个人各司其职，你做资源调配和决策把关。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('这种工作流特别适合需要并行处理、周期较长的任务——技术调研、代码审查、文档撰写、内容创作，都可以用这种方式来加速。')] }),
      new Paragraph({ style: "BodyText", children: [new TextRun('如果你的电脑上跑着 Claude Code，现在就可以试试 claude agents 这个命令，打开看看。也许你会发现，原来一个人也能同时推进好多事情。')] }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/Users/a1-6/My_channel/papers/agent-view-intro.docx", buffer);
  console.log("Done");
});