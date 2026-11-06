# 项目上下文

### 版本技术栈

- **Framework**: Next.js 16 (App Router)
- **Core**: React 19
- **Language**: TypeScript 5
- **UI 组件**: shadcn/ui (基于 Radix UI)
- **Styling**: Tailwind CSS 4

## 目录结构

```
├── public/                 # 静态资源
├── scripts/                # 构建与启动脚本
│   ├── build.sh            # 构建脚本
│   ├── dev.sh              # 开发环境启动脚本
│   ├── prepare.sh          # 预处理脚本
│   └── start.sh            # 生产环境启动脚本
├── src/
│   ├── app/                # 页面路由与布局
│   ├── components/ui/      # Shadcn UI 组件库
│   ├── hooks/              # 自定义 Hooks
│   ├── lib/                # 工具库
│   │   └── utils.ts        # 通用工具函数 (cn)
│   └── server.ts           # 自定义服务端入口
├── next.config.ts          # Next.js 配置
├── package.json            # 项目依赖管理
└── tsconfig.json           # TypeScript 配置
```

- 项目文件（如 app 目录、pages 目录、components 等）默认初始化到 `src/` 目录下。

## 包管理规范

**仅允许使用 pnpm** 作为包管理器，**严禁使用 npm 或 yarn**。
**常用命令**：
- 安装依赖：`pnpm add <package>`
- 安装开发依赖：`pnpm add -D <package>`
- 安装所有依赖：`pnpm install`
- 移除依赖：`pnpm remove <package>`

## 开发规范

### 编码规范

- 默认按 TypeScript `strict` 心智写代码；优先复用当前作用域已声明的变量、函数、类型和导入，禁止引用未声明标识符或拼错变量名。
- 禁止隐式 `any` 和 `as any`；函数参数、返回值、解构项、事件对象、`catch` 错误在使用前应有明确类型或先完成类型收窄，并清理未使用的变量和导入。

### next.config 配置规范

- 配置的路径不要写死绝对路径，必须使用 path.resolve(__dirname, ...)、import.meta.dirname 或 process.cwd() 动态拼接。

### Hydration 问题防范

1. 严禁在 JSX 渲染逻辑中直接使用 typeof window、Date.now()、Math.random() 等动态数据。**必须使用 'use client' 并配合 useEffect + useState 确保动态内容仅在客户端挂载后渲染**；同时严禁非法 HTML 嵌套（如 <p> 嵌套 <div>）。
2. **禁止使用 head 标签**，优先使用 metadata，详见文档：https://nextjs.org/docs/app/api-reference/functions/generate-metadata
   1. 三方 CSS、字体等资源可在 `globals.css` 中顶部通过 `@import` 引入或使用 next/font
   2. preload, preconnect, dns-prefetch 通过 ReactDOM 的 preload、preconnect、dns-prefetch 方法引入
   3. json-ld 可阅读 https://nextjs.org/docs/app/guides/json-ld

## UI 设计与组件规范 (UI & Styling Standards)

- 模板默认预装核心组件库 `shadcn/ui`，位于`src/components/ui/`目录下
- Next.js 项目**必须默认**采用 shadcn/ui 组件、风格和规范，**除非用户指定用其他的组件和规范。**

---

## 数益坊 · K12 数学学习网站（本项目）

### 项目概述
面向 K12 中小学的数学学习网站。内容按「学段 → 年级 → 课时」组织，每个课时含知识点精讲（概念/公式/例题）+ 随堂交互练习（选择题，即时判分），实现「学 — 练 — 测」闭环。

### 关键入口 / 路由
- `/` 首页：hero、三学段入口卡、三步学习法、精选课时
- `/stage/[stage]` 学段页：小学/初中/高中，按年级聚合该学段课时
- `/lesson/[id]` 课时页：知识讲解 + 交互练习
- 学段 id：`xiaoxue` / `chuzhong` / `gaozhong`

### 数据与组件
- **课程内容集中在 `src/lib/data.ts`**：`stages`（学段）、`lessons`（课时）及其 `questions`（练习题）。新增课时/题目只需改此文件，无需改路由。
  - `QuizQuestion`：`prompt`/`options`/`answer`(正确项索引从0)/`explanation`
  - `KnowledgeBlock.kind`：`concept|formula|example`（决定讲解标签配色）
  - `LessonCard` 自动按 `lesson.grade` 分类展示。
- 业务组件：`src/components/lesson-card.tsx`（课时卡）、`src/components/quiz.tsx`（**'use client'** 交互练习，本地 state）、`src/components/layout/*`（页头/页脚）。

### 设计与主题
- 设计方向记于 `DESIGN.md`：意象「黑板 × 演算纸」，配色已写入 `src/app/globals.css` 的 `:root` 变量（纸面米白底、黑板墨绿主色、粉笔黄 accent）。
- 后续加学段/页面时须保持该视觉语言与信息架构一致。

### 运行时注意
- 无外部 API，纯静态内容，无 `app/api` 路由；交付验收以 `pnpm lint --quiet` + `pnpm ts-check` + 页面冒烟为准（经 `test_run`）。
- 页脚 `© year` 使用服务端组件渲染一次，属静态范围，无 hydration 风险。
