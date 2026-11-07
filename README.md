# 数益坊 · K12 数学动画课

用**带中文配音的动画**把公式和定理讲明白，而不是让人背下来。每节课都是同一套结构：

> 生活例子 → 动画看懂 → 文字精讲 → 易错提醒 → 随堂练习

站点是**纯静态 HTML**：没有服务端、没有前端框架、没有构建运行时。双击 `index.html` 就能看，也可以整包扔到任意静态托管上。

当前内容：28 节课时、28 支 1080p 配音视频、112 道随堂练习、5 个互动实验室。

| 学段 | 课时 | 视频 |
| --- | --- | --- |
| 小学 | 凑十法 / 认识图形 / 认识钟表 / 分类与整理 / 连加连减与混合运算 / 乘法的意义 / 除法的意义 / 角的认识 / 条形统计图 / 测量与时分秒 / 多位数乘一位数 / 除数是一位数的除法 / 长方形和正方形的面积 / 分数的初步认识 / 小数的初步认识 / 平移旋转与轴对称 / 大数的认识与万以内加减法 / 线与角（平行与垂直） / 运算律 / 小数乘法 / 平行四边形和梯形 / 用字母表示数 / 生活中的负数 / 三角形的面积 | 81.1s / 84.9s / 97.5s / 61.6s / 98.0s / 68.8s / 58.1s / 89.5s / 79.4s / 95.4s / 96.3s / 94.2s / 110.2s / 104.4s / 95.9s / 92.5s / 104.4s / 115.7s / 127.3s / 102.3s / 120.9s / 121.7s / 118.8s / 53.6s |
| 初中 | 一元一次方程 / 完全平方公式 / 勾股定理 | 63.5s / 59.1s / 85.9s |
| 高中 | 等差数列求和 | 58.4s |

## 覆盖现状

**这 28 节是精品单课，不是完整课程。** 按北师大版教材（小学、初中）与人教 A 版（高中）拆到「能独立成课的核心考点」，小初高合计 **137 个**，目前：

| 学段 | 考点数 | 已完整讲解 | 覆盖率 |
| --- | ---: | ---: | ---: |
| 小学 | 49 | 17（另 3 个部分覆盖） | 34.7% |
| 初中 | 50 | 2（另 2 个部分覆盖） | 4.0% |
| 高中 | 38 | 1 | 2.6% |
| **合计** | **137** | **20** | **14.6%** |

完整的考点矩阵、中考 / 广东新高考 I 卷高频清单、四条学习依赖链和分批生产计划见 **[`docs/coverage.md`](docs/coverage.md)**。加新课前先查这张表，确认前置是否已讲。

## 目录结构

```
docs/coverage.md            K12 覆盖矩阵（考点、优先级、依赖链、分批计划）
index.html                 首页
lessons.html               全部课时（按学段筛选）
labs.html                  互动实验室入口
lesson-*.html              28 个课时页（由脚本生成，不要手改）
assets/
  css/site.css             全站样式（黑板 × 演算纸主题）
  js/site.js               入场动效、目录高亮、章节跳转、答题判分、筛选
  videos/*.mp4             成片
  videos/posters/*.jpg     视频封面（卡片与播放器 poster）
  videos/chapters.json     每节课的章节起始时间（秒）
labs/*.html                5 个互动实验（独立静态页，已统一配色）
site/
  lessons.py               全部课时文案与题目（唯一内容源）
  build.py                 静态页生成器
  check.py                 链接 / 页面 / 答案自检
  extract_chapters.py     从成片检测章节时间
  theme_labs.py            把 labs 副本换成主站配色（幂等）
video_build/               7 节新课的 Manim 分镜 + 配音 + 渲染脚本
pythagoras_lesson.py       勾股定理视频源
narration.py               勾股定理配音脚本
audio_segments/            勾股定理分段配音与时长
```

## 本地预览

```powershell
# 方式一：直接双击 index.html（file:// 协议，视频可正常跳章节）

# 方式二：起一个静态服务
python -m http.server 8899
# 打开 http://127.0.0.1:8899/
```

> 注意：Python 自带的 `http.server` 不支持 `Range` 请求，浏览器里拖动视频进度条会回到 0 秒。`file://` 或支持 Range 的静态托管（Nginx、Vercel、OSS 等）没有这个问题。

## 改内容 / 加课时

所有文案、公式、题目都在 `site/lessons.py` 的 `LESSONS` 列表里。改完后重新生成页面：

```powershell
python site\build.py     # 输出 index.html、lessons.html、labs.html、lesson-*.html
python site\check.py     # 链接、题目数、章节数、视频与封面是否齐全
```

新增一节课的最小步骤：

1. 在 `site/lessons.py` 里 `LESSONS.append({...})`，字段照抄现有课时；
2. 把视频放到 `assets/videos/<id>.mp4`，封面放到 `assets/videos/posters/<id>.jpg`；
3. 运行 `python site\extract_chapters.py` 生成 `chapters.json`；
4. 运行 `python site\build.py`。

`build.py` 会自动处理：首页与目录卡片、上一节/下一节翻页、章节按钮时间、答题判分数据、视频封面。

## 视频流水线

动画用 [Manim Community](https://www.manim.community/) 0.22.1 渲染，配音用 [edge-tts](https://github.com/rany2/edge-tts)（`zh-CN-YunxiNeural`，`rate=-8%`），逐段生成后按真实时长对齐画面。

```powershell
# 单节重渲染（必须显式关缓存）
cd video_build
manim -qh --fps 30 --disable_caching scene_chufa.py ChufaScene
# 成功后把 media\videos\scene_chufa\1080p30\ChufaScene.mp4 复制到 ..\assets\videos\chufa-yiyi.mp4

# 6 节新课批量
powershell -ExecutionPolicy Bypass -File video_build\render_all.ps1
```

### 两个必须记住的坑

1. **重渲染一定要加 `--disable_caching`。** Manim 的缓存片段会复用旧的音频拼接结果，曾导致除法的前 19 秒完全没有声音。
2. **字幕用 `Text(font="Microsoft YaHei")`，不要用 `MathTex`。** 运行环境没有 TeX，用 LaTeX 会直接失败。

### 章节时间怎么来的

`site/extract_chapters.py` 用 ffmpeg 的 `silencedetect` 找出成片里 1.5 秒以上的段间静音，静音结束点即下一章起点。如果成片音画贴合到没有明显静音缝（勾股定理就是这样），自动回退为「配音各段时长累加」。

```powershell
python site\extract_chapters.py
```

没有匹配到、且配音时长也没有时，页面会退化成带序号的章节列表（仍可读，只是不能跳转）。

## 互动实验室

5 个实验（数轴加法、竖式加法、面积拼图、乘法点阵、勾股定理拼图）都是独立的单文件 HTML，`labs/` 下是用于站点展示的副本，原始文件保留在 `src/`。

副本的配色由脚本统一成主站的黑板色（幂等，重复执行不会叠加）：

```powershell
python site\theme_labs.py
```

如果修改了 `src/` 里的实验，需要重新复制到 `labs/` 再跑一次 `theme_labs.py`。

## 设计规范

配色与排版约定见 `DESIGN.md`，核心是「黑板 × 演算纸」：

- 纸面底色 `#f7f4ec`，正文墨色深绿黑
- 黑板 `#163a35`，粉笔白 `#f4efe2`，粉笔黄 `#f2c14e`
- 标题用衬线字体，公式用等宽字体，正文用系统无衬线
- 移动端断点 900px / 640px，375px 宽下无横向滚动

## 浏览器行为说明

- **入场动效**：`.reveal` 元素默认可见，只有在 `html` 带 `js-reveal` 类（脚本正常执行）时才隐藏并逐步显现；另有 1.6 秒兜底，避免脚本异常或截图工具导致内容空白。
- **答题**：选项点击后立即锁定、标出正确项并显示解析；顶部进度条与得分同步更新，「再做一次」可整组重置。
- **章节跳转**：点击章节按钮直接 `currentTime = t`，播放中会自动高亮当前章节。
- 全站无第三方请求、无统计脚本，可离线使用。

## 遗留文件说明

仓库里还留着项目早期的 Next.js 脚手架（`src/app/`、`package.json`、`next.config.ts`、`scripts/` 等）和实验室原始页面（`src/*/*.html`）。**静态站点完全不依赖它们**，保留只是为了存档与回溯；`legacy/` 里放的是勾股定理的早期导出成片。

如果要彻底瘦身，可以删除上述 Next.js 相关文件，只保留根目录 HTML、`assets/`、`labs/`、`site/`、`video_build/`。