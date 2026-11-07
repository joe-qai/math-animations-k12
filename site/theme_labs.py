# -*- coding: utf-8 -*-
"""把复制到 labs/ 的互动演示统一成主站的黑板配色。

只改 labs/ 下的副本，src/ 里的原始文件保持不动。
重复执行安全（有 marker 判断）。
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABS = ROOT / "labs"
MARKER = "<!-- chalk-theme -->"

REPLACEMENTS = [
    ("#6c5ce7", "#f2c14e"),
    ("#00cec9", "#8fd9a8"),
    ("#fd79a8", "#82c8e8"),
    ("#0f1117", "#12302c"),
    ("#1a1d27", "#1b443e"),
    ("#e8e8f0", "#f4efe2"),
    ("#6b7280", "#a9bdb6"),
    ("#00b894", "#8fd9a8"),
    ("#fdcb6e", "#f7d98a"),
    ("rgba(108,92,231", "rgba(242,193,78"),
    ("rgba(0,206,201", "rgba(143,217,168"),
    ("rgba(253,121,168", "rgba(130,200,232"),
]

STYLE = MARKER + """
<style>
  /* 与主站统一：黑板 × 粉笔 */
  :root {
    --bg: #12302c;
    --card: #1b443e;
    --accent: #f2c14e;
    --accent2: #8fd9a8;
    --text: #f4efe2;
    --muted: #a9bdb6;
    --warm: #e8813a;
    --success: #8fd9a8;
    --warn: #f7d98a;
    --a-color: #f2c14e;
    --b-color: #8fd9a8;
    --c-color: #82c8e8;
  }
  body {
    font-family: 'PingFang SC', 'Microsoft YaHei', ui-sans-serif, system-ui, sans-serif;
    background-image:
      radial-gradient(ellipse at 12% 0%, rgba(244, 239, 226, 0.06), transparent 55%),
      radial-gradient(ellipse at 92% 100%, rgba(242, 193, 78, 0.06), transparent 52%);
    background-attachment: fixed;
  }
  a.back { letter-spacing: 0.02em; }
  a.back:hover { color: var(--accent); }
  h1 { letter-spacing: 0.02em; }
</style>
"""

CANVAS_STYLE = """<style>
  /* 画布按设计尺寸显示，避免 2x 像素比把 CSS 尺寸撑成两倍；
     小屏放不下时在卡片内横向滚动，不撑宽整页 */
  .canvas-scroll {
    max-width: 100%;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    border-radius: 12px;
  }
  __EXTRA__
  .canvas-scroll canvas { max-width: none; }
</style>
"""

FIXED_CSS = {
    "area.html": "#canvas { width: 600px; height: 400px; }",
    "pythagoras.html": "#canvas { width: 600px; height: 500px; }",
    "multiplication.html": "#spiralCanvas { width: 600px; height: 600px; }",
}

EXTRA_MARKER = "<!-- labs-extra -->"
EXTRA_STYLE = EXTRA_MARKER + """<link rel="icon" href="data:,">
<style>
  /* 控件在窄屏自动换行，避免右侧按钮被卡片裁掉 */
  .controls { flex-wrap: wrap; }
</style>
"""


def wrap_canvas(text: str, extra_css: str = "") -> str:
    """先插入样式（会改变长度），再定位 canvas，避免下标错位。"""
    if EXTRA_MARKER not in text:
        text = text.replace("</head>", EXTRA_STYLE + "</head>", 1)
    if "<canvas" not in text:
        return text
    if "canvas-scroll" not in text:
        style = CANVAS_STYLE.replace("__EXTRA__", extra_css)
        text = text.replace("</head>", style + "</head>", 1)
    start = text.find("<canvas")
    close = text.find("</canvas>", start)
    if close == -1:
        return text
    close += len("</canvas>")
    if text.rfind('<div class="canvas-scroll">', 0, start) > text.rfind("</div>", 0, start):
        return text
    return (
        text[:start]
        + '<div class="canvas-scroll">'
        + text[start:close]
        + "</div>"
        + text[close:]
    )


def main() -> None:
    for path in sorted(LABS.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        extra = FIXED_CSS.get(path.name, "")
        if MARKER in text:
            text = wrap_canvas(text, extra)
            path.write_text(text, encoding="utf-8")
            print(f"[SKIP-STYLE] {path.name}")
            continue
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        text = text.replace("</head>", STYLE + "</head>", 1)
        text = wrap_canvas(text, extra)
        path.write_text(text, encoding="utf-8")
        print(f"[OK] {path.name}")


if __name__ == "__main__":
    main()