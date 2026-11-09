# -*- coding: utf-8 -*-
"""把 site/lessons.py 的内容渲染成纯静态 HTML 页面。

用法：python site/build.py
产物：index.html、lessons.html、labs.html、lesson-*.html（全部是静态文件）
"""

from __future__ import annotations

import html
import subprocess
from pathlib import Path

from lessons import LESSONS

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "assets" / "videos"

STAGES = [
    {
        "id": "xiaoxue",
        "name": "小学数学",
        "en": "PRIMARY",
        "color": "#c98d22",
        "tagline": "先把数感和图形直觉长出来。乘法不是口诀，除法不是命令，面积公式也不是天上掉下来的。",
        "grades": ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级", "小升初"],
    },
    {
        "id": "chuzhong",
        "name": "初中数学",
        "en": "JUNIOR",
        "color": "#3f7cbe",
        "tagline": "从算术走向代数。天平、面积图、方格纸，都是把抽象式子变回看得见的东西。",
        "grades": ["七年级", "八年级", "九年级", "中考专题"],
    },
    {
        "id": "gaozhong",
        "name": "高中数学",
        "en": "SENIOR",
        "color": "#2f8877",
        "tagline": "公式开始变长，但证明仍然可以很直观：把数列摆成阶梯，倒过来，就看见公式。",
        "grades": ["初升高衔接", "高一"],
    },
]

STAGE_BY_ID = {s["id"]: s for s in STAGES}

THUMB = {
    "coushifa": "9 + 4 = 13",
    "tuiwei-jianfa": "13 − 9 = 4",
    "bai-yinei-jiajian": "36 + 27 = 63",
    "liangwei-cheng-liangwei": "23 × 14 = 322",
    "chufa-liangwei": "84 ÷ 21 = 4",
    "jieti-celue": "鸡 3 只，兔 5 只",
    "sanjiaoxing-neijiaohe": "内角和 180°",
    "changfangti-zhankaitu": "6 面 12 棱 8 顶点",
    "biaomianji": "三组面相加再乘 2",
    "zhexian-tongjitu": "点看数量，线看变化",
    "gujisuan": "看成整十整百",
    "tansuo-guilv": "因数乘几，积乘几",
    "weizhi-shunxu": "说位置要带参照",
    "renminbi-renshi": "1 元 = 10 角",
    "dapei-tuili": "搭配用乘法",
    "shuju-diaocha": "先收集，再整理",
    "queding-weizhi": "数对先列后行",
    "zhijiao-sanjiaoxing": "30° 对边 = 斜边一半",
    "fangcha": "方差越小越稳定",
    "kexue-jishufa": "一位整数乘十的幂",
    "daishushi-qiuzhi": "先代入，再计算",
    "weisi": "坐标同乘一个比",
    "tixing-tuxing": "中位线 × 高",
    "renshi-tuxing": "□ △ ○",
    "renshi-zhongbiao": "3:00 / 3:30",
    "fenlei-zhengli": "4 + 3 + 2 = 9",
    "lianjia-lianjian": "45 - 20 + 12 = 37",
    "jiao-renshi": "锐角 ＜ 直角 ＜ 钝角",
    "tiaoxing-tongji": "直条越高，数量越多",
    "celiang-shifenmiao": "1 米 = 100 厘米",
    "duowei-cheng-yiwei": "满几十，向前一位进几",
    "chufa-yiwei": "余数一定要比除数小",
    "changfangxing-mianji": "面积 = 长 × 宽",
    "fenshu-chubu": "必须平均分",
    "xiaoshu-chubu": "加减先对齐小数点",
    "pingyi-xuanzhuan": "平移是直着走",
    "dashu-jianfa": "数位对齐，满十进一",
    "xian-yujiao": "平行不相交",
    "yun-suanlv": "先凑整，再计算",
    "xiaoshu-cheng": "先按整数乘",
    "pingxing-sibianxing": "两组对边平行",
    "zimu-biaoshi": "a² 就是 a×a",
    "fushu-chubu": "0 是分界线",
    "kenengxing": "谁多谁可能性大",
    "xiaoshu-chu": "除数变成整数",
    "yinshu-beishu": "因数成对找",
    "fenshu-xingzhi": "同乘同除，大小不变",
    "fenshu-jiajian": "分母不变，分子加减",
    "fenshu-chengchu": "除以一个数，乘倒数",
    "jianyi-fangcheng": "两边同变，等式不变",
    "pingxing-mianji": "底乘高，求面积",
    "tixing-mianji": "两底和乘高除二",
    "changfangti-tiji": "长乘宽乘高",
    "yuan-zhouchang": "周长 = π 乘直径",
    "yuan-mianji": "面积 = π r 平方",
    "baifenshu": "百分之几，分母一百",
    "bi": "前后项同乘同除",
    "zhengfan-bili": "商一定正，积一定反",
    "shanxing-tongjitu": "圆心角 = 360°×百分比",
    "pingjun-shu": "平均数 = 总数÷份数",
    "fenshu-hunhe": "先乘除，后加减",
    "bili-yingyong": "总量 ÷ 总份数",
    "baifenshu-yingyong": "原价 × 折扣",
    "fangcheng-yingyong": "设 列 解 验",
    "yuan-zonghe": "整体减空白",
    "chengfa-yiyi": "3 × 4 = 12",
    "chufa-yiyi": "12 ÷ 4 = 3",
    "sanjiaoxing-mianji": "底 × 高 ÷ 2",
    "youli-shu": "|-3| = 3",
    "youli-yunsuan": "(-3) + 5 = 2",
    "daishu-shi": "3x + 5x = 8x",
    "jiben-tuxing": "1° = 60′",
    "shuju-shouji": "频率 × 360°",
    "mi-yunsuan": "aᵐ · aⁿ = aᵐ⁺ⁿ",
    "zhengshi-chengfa": "3x² · 2x³ = 6x⁵",
    "pingfang-cha": "(a+b)(a−b) = a² − b²",
    "xiangjiao-pingxing": "同位角相等 → 平行",
    "sanjiaoxing": "内角和 = 180°",
    "pingjunshu": "平均数 = 总和÷个数",
    "shishu": "√(a²) = |a|",
    "yinshi": "a²−b²=(a+b)(a−b)",
    "fenshi": "A/B = (A·C)/(B·C)",
    "fenshi-fangcheng": "公分母为零 → 增根",
    "quandeng": "SSS · SAS · ASA · AAS · HL",
    "gougu-nidingli": "5² + 12² = 13²",
    "duicheng-dengyao": "对折 → 两边重合",
    "hanshu-yici": "y = kx + b",
    "pinlv-gailv": "频率稳 → 概率定",
    "erci-genshi": "√(a²) = |a|",
    "eryuan-yici": "二元变一元，消元",
    "yiyuan-budengshi": "负数乘除要变号",
    "fanbili-hanshu": "k 定象限",
    "pingxing-xingzhi": "对角线互相平分",
    "teshu-pingxing-sibianxing": "矩形看角，菱形看边",
    "xiangsi-sanjiaoxing": "两角相等即相似",
    "shitu-touying": "长对正 高平齐 宽相等",
    "yiyuan-erci-fangcheng": "先化一般式再解",
    "erci-fangcheng-yingyong": "列等量关系再检验",
    "erci-hanshu": "先看开口再找顶点",
    "yuan-jiben-xingzhi": "垂径定理，圆周角",
    "zhixian-yuan-weizhi": "比 d 和 r，连半径",
    "yuan-zhong-jisuan": "弧长面积，看圆心角",
    "lieju-fa-gailv": "写全结果再数个数",
    "ruijiao-sanjiao-hanshu": "定角，认边，写比值",
    "jie-zhijiao-sanjiaoxing": "画图标边，选式求解",
    "fangcheng-budengshi-yingyong": "找关系，再设未知数",
    "hanshu-fangcheng-tuxiang": "交点即解，上下即大小",
    "chigui-zuotu": "留痕迹，写结论",
    "tongjitu-xuanze": "先看目的再选图",
    "zhongkao-shu-yu-shi": "先定符号，再动笔",
    "zhongkao-fangcheng-budengshi": "解完先验，再写答案",
    "zhongkao-hanshu-yingyong": "先看范围，再求最值",
    "zhongkao-sanjiaoxing-sibianxing": "△ABC ≌ △DEF",
    "zhongkao-yuan-sanjiao-hanshu": "ℓ = nπr / 180",
    "zhongkao-tongji-gailv": "P = m / n",
    "zhongkao-yazhou-jieti": "先拿稳的，再冲难的",
    "h0-yinshi-fenjie": "提公因式，十字相乘",
    "yiyuan-yici-fangcheng": "2x + 3 = 11",
    "wanquan-pingfang": "(a+b)²",
    "dengcha-shulie": "首项 + 末项",
    "gougu-dingli": "a² + b² = c²",
    "jihe-yunsuan": "∩ 共同 ∪ 全部",
    "chongyao-tiaojian": "小范围推大范围",
    "liangci-mingti": "全称 ↔ 存在",
    "budengshi-xingzhi": "乘负要变号",
    "jiben-budengshi": "a + b ≥ 2√ab",
    "hanshu-gainian": "y = f(x)",
    "hanshu-xingzhi": "奇原点，偶 y 轴",
    "mihanshu": "y = xᵅ",
    "hanshu-lingdian": "f(x) = 0",
    "hanshu-moxing": "先建模，再求解",
    "zhishu-hanshu": "同底相乘，指数相加",
    "duishu-hanshu": "对数就是问指数",
    "sanjiao-dingyi": "一全正，二正弦",
    "sanjiao-tuxiang": "五点作图，周期 2π",
    "sanjiao-hengbian": "余弦相反，正弦相同",
    "xiangliang-yunsuan": "首尾相接，指向终点",
    "xiangliang-shuliangji": "数量积 = 模乘余弦",
    "jie-sanjiaoxing": "边比对边，角用余弦",
    "fushu": "实部虚部，i² = −1",
    "liti-chubu": "线面平行，线线平行",
    "kongjian-xiangliang": "法向量定线面角",
    "zhixian-fangcheng": "点斜式定直线",
    "yuan-fangcheng": "圆心定位置，半径定大小",
    "sanshitu": "长对正，高平齐",
    "tuoyuan": "到两定点距离和为 2a",
    "shuangquxian": "到两定点距离差为 2a",
    "paowuxian": "到焦点与准线等距",
    "zhixian-yuanzhuiquxian": "联立、韦达、判别式",
    "zhuiquxian-zonghe": "设点联立，韦达代入",
    "shulie-gainian": "通项看 aₙ，和看 Sₙ",
    "dengbi-shulie": "后项比前项等于 q",
    "shulie-qiuhe": "错位相减，裂项相消",
    "daoshu-gainian": "导数就是瞬时变化率",
    "daoshu-yingyong": "导数定单调与极值",
    "jishu-yuanli": "分类相加，分步相乘",
    "pailie-zuhe": "有序排列，无序组合",
    "erxiangshi": "二项展开看通项",
    "suiji-shijian-gailv": "互斥相加，独立相乘",
    "suiji-bianliang": "分布列概率和为一",
    "chouyang-guji": "样本估计总体",
    "huigui-duli": "回归看相关，检验看 χ²",
}

LABS = [
    {
        "no": "LAB 01",
        "title": "数轴上的加法",
        "desc": "在数轴上跳格子：加几就向右跳几格，负数就向左跳。进位与退位，都变成脚步。",
        "href": "labs/number-line.html",
        "for": "小学 · 加法",
    },
    {
        "no": "LAB 02",
        "title": "竖式加法",
        "desc": "一位一位对齐，满十进一。把竖式的每一步拆开看，进位不再靠死记。",
        "href": "labs/vertical.html",
        "for": "小学 · 加法",
    },
    {
        "no": "LAB 03",
        "title": "面积拼图",
        "desc": "拖一拖、剪一剪：平行四边形、三角形、梯形的面积公式，都能拼出来。",
        "href": "labs/area.html",
        "for": "小学 · 面积",
    },
    {
        "no": "LAB 04",
        "title": "乘法点阵",
        "desc": "点阵转个方向，行列互换、总数不变。交换律不是规定，是数出来的。",
        "href": "labs/multiplication.html",
        "for": "小学 · 乘法",
    },
    {
        "no": "LAB 05",
        "title": "勾股定理拼图",
        "desc": "调节两条直角边，把两个小正方形里的小方格，一格一格搬进斜边的大正方形。",
        "href": "labs/pythagoras.html",
        "for": "初中 · 勾股定理",
    },
]

DIFFICULTY = {1: "基础", 2: "进阶", 3: "挑战"}


# ---------------------------------------------------------------- 工具函数

def esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def video_seconds(lesson_id: str) -> int:
    path = VIDEO_DIR / f"{lesson_id}.mp4"
    if not path.exists():
        return 0
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    try:
        return int(round(float(out.stdout.strip())))
    except ValueError:
        return 0


def mmss(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


def head(title: str, description: str, prefix: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#163a35">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='6' fill='%23163a35'/%3E%3Ctext x='32' y='45' font-size='38' text-anchor='middle' fill='%23f2c14e' font-family='serif'%3E%E6%95%B0%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{prefix}assets/css/site.css">
<script>document.documentElement.classList.add('js-reveal');</script>
</head>
<body>"""


def header(prefix: str = "", current: str = "") -> str:
    def cur(key: str) -> str:
        return ' aria-current="page"' if current == key else ""

    return f"""
<a class="skip" href="#main">跳到主要内容</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{prefix}index.html">
      <span class="brand-mark">数</span>
      <span>数益坊<small>K12 数学 · 动画课</small></span>
    </a>
    <nav class="nav-links" aria-label="主导航">
      <a href="{prefix}index.html"{cur('home')}>首页</a>
      <a href="{prefix}lessons.html"{cur('lessons')}>全部课时</a>
      <a href="{prefix}labs.html"{cur('labs')}>互动实验室</a>
    </nav>
    <div class="nav-side">
      <span class="pill">{len(LESSONS)} 节课时</span>
      <span>北师大版</span>
    </div>
  </div>
</header>"""


def footer(prefix: str = "") -> str:
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{prefix}index.html">
          <span class="brand-mark">数</span>
          <span>数益坊<small>K12 数学 · 动画课</small></span>
        </a>
        <p>每节课四件事：生活例子、动画看懂、文字精讲、练习巩固。公式先被看见，再被记住。</p>
      </div>
      <div>
        <h4>课程</h4>
        <ul>
          <li><a href="{prefix}lessons.html#xiaoxue">小学数学</a></li>
          <li><a href="{prefix}lessons.html#chuzhong">初中数学</a></li>
          <li><a href="{prefix}lessons.html#gaozhong">高中数学</a></li>
          <li><a href="{prefix}labs.html">互动实验室</a></li>
        </ul>
      </div>
      <div>
        <h4>关于</h4>
        <ul>
          <li><a href="{prefix}index.html#how">学习方法</a></li>
          <li><a href="{prefix}lesson-gougu.html">示范课时 · 勾股定理</a></li>
          <li>纯静态站点，无账号与追踪</li>
          <li>动画 Manim · 配音 edge-tts</li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>© 数益坊 · 北师大版</span>
      <span>Static HTML · No runtime</span>
    </div>
  </div>
</footer>
<script src="{prefix}assets/js/site.js"></script>
</body>
</html>
"""


def lesson_card(lesson: dict, prefix: str = "") -> str:
    stage = STAGE_BY_ID[lesson["stage"]]
    seconds = video_seconds(lesson["id"])
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in lesson["tags"][:3])
    search_text = " ".join(
        [
            lesson["title"],
            lesson.get("subtitle", ""),
            stage["name"],
            lesson["grade"],
            " ".join(lesson["tags"]),
            lesson["keyformula"],
            " ".join(k["title"] for k in lesson["knowledge"]),
        ]
    ).lower()
    poster = VIDEO_DIR / "posters" / f"{lesson['id']}.jpg"
    if poster.exists():
        thumb = (
            f'<img src="assets/videos/covers/{lesson["id"]}.jpg" alt="" decoding="async">'
            '<span class="thumb-shade"></span>'
        )
    else:
        thumb = f'<span class="thumb-fallback formula">{esc(THUMB[lesson["id"]])}</span>'
    if seconds:
        badge = f'<span class="play-badge"><i></i>{mmss(seconds)}</span>'
    else:
        badge = '<span class="play-badge text-only">图文精讲</span>'
    # 超过 11 个字的标题在窄卡片上会放不下，单独加类名按卡片宽度缩放字号
    title_cls = ' class="long"' if len(lesson["title"]) >= 12 else ""
    return f"""
<article class="lesson-card reveal" data-search="{html.escape(search_text, quote=True)}">
  <a class="lesson-hit" href="{prefix}{lesson['file']}" aria-label="{esc(lesson['title'])} · {esc(stage['name'])}{esc(lesson['grade'])}"></a>
  <div class="lesson-thumb" aria-hidden="true">
    {thumb}
    <span class="stage-badge">{esc(stage['name'])} · {esc(lesson['grade'])}</span>
    {badge}
  </div>
  <div class="lesson-body">
    <div class="meta-line"><span>{esc(stage['name'])}</span><span>/</span><span>{esc(lesson['grade'])}</span><span>/</span><span>约 {lesson['minutes']} 分钟</span></div>
    <h3{title_cls}>{esc(lesson['title'])}</h3>
    <div class="tags">{tags}</div>
  </div>
</article>"""


def quiz(lesson: dict) -> str:
    items = []
    for i, q in enumerate(lesson["questions"]):
        opts = []
        for j, opt in enumerate(q["options"]):
            key = "ABCD"[j]
            opts.append(
                f'<button class="option" type="button" data-i="{j}">'
                f'<span class="key">{key}</span><span>{esc(opt)}</span></button>'
            )
        items.append(
            f"""
  <article class="q" data-answer="{q['answer']}">
    <div class="q-head"><span class="q-index">{i + 1:02d}</span><p class="q-prompt">{esc(q['prompt'])}</p></div>
    <div class="options">{''.join(opts)}</div>
    <div class="feedback" role="status" data-explain="{html.escape(q['explanation'], quote=True)}"></div>
  </article>"""
        )

    return f"""
<section class="quiz" data-quiz>
  <div class="quiz-top">
    <span class="progress-text" data-progress>已完成 0 / {len(lesson['questions'])}</span>
    <div class="quiz-bar"><span data-bar></span></div>
    <span class="quiz-score" data-score>得分 0</span>
  </div>{''.join(items)}
  <div class="quiz-result" data-result>
    <div>
      <div class="score-big" data-result-score>0 / {len(lesson['questions'])}</div>
      <p data-result-text></p>
    </div>
    <button class="btn" type="button" data-reset>再做一次</button>
  </div>
</section>"""


def knowledge_blocks(lesson: dict) -> str:
    out = []
    for block in lesson["knowledge"]:
        kind = block["kind"]
        label = {"concept": "概念", "formula": "公式", "example": "例题"}[kind]
        cls = "know formula-block" if kind == "formula" else "know"
        body = "".join(f"<p>{esc(p)}</p>" for p in block["body"])
        formula = f'<p class="formula-big">{esc(block["formula"])}</p>' if block.get("formula") else ""
        out.append(
            f"""
<article class="{cls}">
  <div class="know-head"><span class="kind {kind}">{label}</span><h3>{esc(block['title'])}</h3></div>
  {body}{formula}
</article>"""
        )
    return "".join(out)


def lab_link(lesson: dict) -> str | None:
    mapping = {
        "chengfa-yiyi": ("labs/multiplication.html", "乘法点阵实验室", "把点阵转 90 度，亲眼确认 3 × 4 = 4 × 3。"),
        "sanjiaoxing-mianji": ("labs/area.html", "面积拼图实验室", "拖动图形，把两个三角形拼成平行四边形。"),
        "gougu-dingli": ("labs/pythagoras.html", "勾股定理拼图", "调节直角边长度，看小方格如何搬进斜边正方形。"),
    }
    return mapping.get(lesson["id"])


def build_home() -> str:
    video_count = sum(1 for l in LESSONS if (VIDEO_DIR / f"{l['id']}.mp4").exists())
    question_count = sum(len(l["questions"]) for l in LESSONS)
    stage_cards = []
    for stage in STAGES:
        stage_lessons = [l for l in LESSONS if l["stage"] == stage["id"]]
        grade_count = len({l["grade"] for l in stage_lessons})
        stage_cards.append(
            f"""
<article class="stage-card reveal" style="--stage-color:{stage['color']}">
  <div class="stage-top">
    <h3>{esc(stage['name'])}</h3>
    <span class="stage-en">{stage['en']}</span>
  </div>
  <p class="stage-desc">{esc(stage['tagline'])}</p>
  <p class="stage-meta">{grade_count} 个年级 · {len(stage_lessons)} 节课</p>
  <a class="stage-more" href="lessons.html#{stage['id']}">进入{esc(stage['name'][:2])}课时</a>
</article>"""
        )

    featured_ids = [
        "coushifa", "changfangxing-mianji", "yuan-mianji",
        "youli-shu", "gougu-dingli", "erci-hanshu",
        "jihe-yunsuan", "dengcha-shulie", "daoshu-gainian",
    ]
    by_id = {l["id"]: l for l in LESSONS}
    featured = "".join(lesson_card(by_id[i]) for i in featured_ids if i in by_id)

    hero_figure = """
<figure class="hero-figure">
  <svg viewBox="0 -40 620 580" role="img" aria-label="直角三角形三条边上各有一个正方形，两条直角边上的正方形面积之和等于斜边上的正方形面积">
    <g class="chalk-line" stroke="#f4efe2" stroke-width="2.6">
      <rect x="225" y="350" width="150" height="150" fill="#f2c14e" fill-opacity="0.16"/>
      <rect x="25" y="150" width="200" height="200" fill="#82c8e8" fill-opacity="0.16"/>
      <path d="M375 350 L225 150 L425 0 L575 200 Z" fill="#8fd9a8" fill-opacity="0.16"/>
      <path d="M225 350 L375 350 L225 150 Z" fill="#f4efe2" fill-opacity="0.08"/>
    </g>
    <g class="chalk-line" stroke="#f2c14e" stroke-width="3.2">
      <path d="M225 350 L375 350" class="draw"/>
      <path d="M225 350 L225 150" class="draw"/>
      <path d="M375 350 L225 150" class="draw"/>
    </g>
    <path d="M225 328 L247 328 L247 350" fill="none" stroke="rgba(244,239,226,.55)" stroke-width="2"/>
    <text x="300" y="445" text-anchor="middle" fill="#f2c14e">a² = 9</text>
    <text x="122" y="256" text-anchor="middle" fill="#82c8e8">b² = 16</text>
    <text x="398" y="168" text-anchor="middle" fill="#8fd9a8" transform="rotate(-37 398 168)">c² = 25</text>
  </svg>
  <figcaption>3² + 4² = 5²　·　面积，是勾股定理最直白的证据</figcaption>
</figure>"""

    return (
        head(
            "数益坊 · K12 数学动画课",
            "数益坊：用动画与图文精讲拆解 K12 数学公式与定理。从一年级的凑十法，到高中的数列求和，每节课都有文字精讲与练习。",
        )
        + header("", "home")
        + f"""
<main id="main">
  <div class="wrap">
    <section class="hero">
      <div class="hero-inner">
        <div>
          <span class="eyebrow">北师大版 · K12 数学</span>
          <h1>把公式讲<em>明白</em><br>而不是背下来</h1>
          <p class="lead">大多数课从一个生活问题开始：三排桌子、一袋苹果、一把靠墙的梯子。先看见，再理解，最后动手练——公式会自己长出来。</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="lessons.html">开始学习 →</a>
            <a class="btn btn-ghost" href="lesson-gougu.html">看一节示范</a>
          </div>
          <form class="hero-search" action="lessons.html" method="get" role="search">
            <input type="search" name="q" placeholder="搜课时或知识点，如「勾股」「通分」" aria-label="搜索课时">
            <button type="submit">搜索</button>
          </form>
          <div class="hero-stats">
            <div><b>{len(LESSONS)}</b><span>节数学课时</span></div>
            <div><b>{video_count}</b><span>支讲解视频</span></div>
            <div><b>{question_count}</b><span>道随堂练习</span></div>
          </div>
        </div>
        {hero_figure}
      </div>
    </section>

    <section class="section" id="stages">
      <div class="section-head">
        <span class="num">01</span>
        <h2>按学段进入</h2>
        <p>从数感、图形到代数与数列，能配动画的配动画，其余用图文精讲把推导和例题讲透。</p>
      </div>
      <div class="stage-grid">{''.join(stage_cards)}</div>
    </section>

    <section class="section" id="how">
      <div class="section-head">
        <span class="num">02</span>
        <h2>一节课，三步走</h2>
        <p>先看动画或例题建立画面，再读文字理清逻辑，最后用练习暴露问题。</p>
      </div>
      <div class="steps">
        <div class="step reveal">
          <span class="step-num">STEP 01</span>
          <h3>看 · 动画 / 例题</h3>
          <p>能配动画的课时，用分步动画建立画面；图文课时直接从例题拆解入手，一步一步跟着算。</p>
          <span class="step-tag">先给具体例子</span>
        </div>
        <div class="step reveal">
          <span class="step-num">STEP 02</span>
          <h3>学 · 文字精讲</h3>
          <p>把画面里的过程翻译成定义、公式和推导。概念、公式、例题分块呈现，方便对照复习。</p>
          <span class="step-tag">公式有来处</span>
        </div>
        <div class="step reveal">
          <span class="step-num">STEP 03</span>
          <h3>练 · 即时反馈</h3>
          <p>四道随堂题，选完立刻判分并解释原因。做错不可怕，重要的是知道错在哪一步。</p>
          <span class="step-tag">错题当场讲清</span>
        </div>
      </div>
    </section>

    <section class="section" id="lessons">
      <div class="section-head">
        <span class="num">03</span>
        <h2>精选课时</h2>
        <p>每学段精选 3 节 · <a href="lessons.html" style="color:var(--amber-ink);font-weight:600">查看全部 {len(LESSONS)} 节 →</a></p>
      </div>
      <div class="lesson-grid home-featured">{featured}</div>
    </section>

    <section class="lab-strip reveal">
      <div>
        <h2>动手拖一拖，比看十遍更清楚</h2>
        <p>互动实验室里有数轴跳格、竖式进位、面积拼图、乘法点阵和勾股定理拼图。全部是浏览器里直接运行的静态页面，不需要安装任何东西。</p>
      </div>
      <a class="btn btn-primary" href="labs.html">进入实验室 →</a>
    </section>
  </div>
</main>
"""
        + footer()
    )


def build_catalog() -> str:
    groups = []
    for stage in STAGES:
        items = [l for l in LESSONS if l["stage"] == stage["id"]]
        if not items:
            continue
        cards = "".join(lesson_card(l) for l in items)
        groups.append(
            f"""
<section class="catalog-group" id="{stage['id']}" data-stage="{stage['id']}">
  <div class="group-head">
    <h2>{esc(stage['name'])}</h2>
    <span class="count">{len(items)} 节</span>
    <span class="line"></span>
    <span class="count">{len({l['grade'] for l in items})} 个年级</span>
    <span class="rail-hint" aria-hidden="true">左右滑动 →</span>
  </div>
  <div class="lesson-grid lesson-rail">{cards}</div>
</section>"""
        )

    return (
        head("全部课时 · 数益坊", "数益坊全部课时：小学到高中，按学段与年级排列，每节课都配动画、文字精讲与随堂练习。")
        + header("", "lessons")
        + f"""
<main id="main">
  <div class="wrap">
    <header class="catalog-head">
      <h1>全部课时</h1>
      <p>{len(LESSONS)} 节课时，按学段分组。手机上每个学段是一排卡片，左右滑动即可切换；搜索框直接检索全部课时，不区分学段。</p>
      <div class="catalog-tools">
        <label class="search-box">
          <span class="search-ico" aria-hidden="true">⌕</span>
          <input id="lesson-search" type="search" placeholder="搜索全部课时、知识点或年级" autocomplete="off" aria-label="搜索全部课时">
          <button class="search-clear" type="button" data-search-clear hidden aria-label="清除搜索">×</button>
        </label>
      </div>
      <p class="search-status" data-search-status role="status" aria-live="polite"></p>
    </header>
    {''.join(groups)}
    <div class="search-empty" data-search-empty hidden>
      <b>没有找到相关课时</b>
      <p>换个关键词试试，或清空搜索查看全部课时。</p>
    </div>
  </div>
</main>
"""
        + footer()
    )


def build_labs() -> str:
    cards = []
    for lab in LABS:
        cards.append(
            f"""
<article class="lab-card reveal">
  <span class="lab-no">{lab['no']} · {esc(lab['for'])}</span>
  <h3>{esc(lab['title'])}</h3>
  <p>{esc(lab['desc'])}</p>
  <a class="lab-open" href="{lab['href']}">打开实验</a>
</article>"""
        )

    return (
        head("互动实验室 · 数益坊", "数益坊互动实验室：数轴加法、竖式加法、面积拼图、乘法点阵、勾股定理拼图，全部为浏览器内运行的静态页面。")
        + header("", "labs")
        + f"""
<main id="main">
  <div class="wrap">
    <header class="catalog-head">
      <h1>互动实验室</h1>
      <p>视频负责把道理讲清楚，实验室负责让你亲手验证一遍。拖动、旋转、剪拼——数学不是只能看的。</p>
    </header>
    <section class="section">
      <div class="lab-grid">{''.join(cards)}</div>
      <div class="note-panel">
        这些实验是独立的静态页面，直接用浏览器打开即可，支持触摸操作。画布在窄屏上可横向滑动查看，操作体验以电脑或平板为佳。建议先看完对应课时的视频，再回来动手。
      </div>
    </section>
  </div>
</main>
"""
        + footer()
    )


def build_lesson(lesson: dict, prev: dict | None, nxt: dict | None) -> str:
    stage = STAGE_BY_ID[lesson["stage"]]
    seconds = video_seconds(lesson["id"])
    has_vid = seconds > 0
    goals = "".join(f"<li>{esc(g)}</li>" for g in lesson["goals"])
    pitfalls = "".join(f"<li>{esc(p)}</li>" for p in lesson["pitfalls"])
    variations = lesson.get("variations") or []
    lab = lab_link(lesson)

    lab_aside = ""
    if lab:
        href, title, desc = lab
        lab_aside = f"""
      <div class="aside-lab">
        <h3>动手验证</h3>
        <div class="al-title">{esc(title)}</div>
        <p>{esc(desc)}</p>
        <a href="{href}">打开实验 →</a>
      </div>"""

    pager = []
    if prev:
        pager.append(
            f'<a href="{prev["file"]}"><span class="dir">← 上一节</span>'
            f'<span class="title">{esc(prev["title"])}</span></a>'
        )
    if nxt:
        pager.append(
            f'<a class="next" href="{nxt["file"]}"><span class="dir">下一节 →</span>'
            f'<span class="title">{esc(nxt["title"])}</span></a>'
        )

    toc = []
    if has_vid:
        toc.append(("video", "视频讲解"))
    toc.append(("knowledge", "知识精讲"))
    if variations:
        toc.append(("variations", "变式提醒"))
    toc.append(("pitfalls", "易错提醒"))
    toc.append(("practice", "练习巩固"))
    toc_html = "".join(
        f'<li><a href="#{anchor}"><span class="n">{i + 1:02d}</span>{name}</a></li>'
        for i, (anchor, name) in enumerate(toc)
    )

    sections = []
    if has_vid:
        sections.append((
            "video", f"{lesson['title']} 视频讲解", mmss(seconds),
            f"""<div class="video-card">
            <div class="video-wrap">
              <video data-lesson-video controls preload="metadata" playsinline poster="assets/videos/covers/{lesson['id']}.jpg">
                <source src="{lesson['video']}" type="video/mp4">
                你的浏览器不支持视频播放，<a href="{lesson['video']}">点此下载视频</a>。
              </video>
            </div>
          </div>""",
        ))
    sections.append((
        "knowledge", "知识精讲", "概念 · 公式 · 例题",
        knowledge_blocks(lesson) + f"""
          <div class="summary-card">
            <div class="label">一句话记住</div>
            <p>{esc(lesson['summary'])}</p>
          </div>""",
    ))
    if variations:
        vs = "".join(f"<li>{esc(v)}</li>" for v in variations)
        sections.append((
            "variations", "变式提醒", "换个条件，再走一遍",
            f"""<div class="pitfall-card variation-card">
            <h3>同一道题，换三种问法</h3>
            <ul>{vs}</ul>
          </div>""",
        ))
    sections.append((
        "pitfalls", "易错提醒", "先避开，再提速",
        f"""<div class="pitfall-card">
            <h3>这几个坑，考试里最常见</h3>
            <ul>{pitfalls}</ul>
          </div>""",
    ))
    sections.append((
        "practice", "练习巩固", "选完立刻判分",
        quiz(lesson),
    ))
    sections_html = "".join(
        f"""
        <section class="block" id="{anchor}">
          <div class="block-head"><span class="num">{i + 1:02d}</span><h2>{esc(title)}</h2><span class="hint">{esc(hint)}</span></div>
          {body}
        </section>"""
        for i, (anchor, title, hint, body) in enumerate(sections)
    )

    if has_vid:
        meta_html = (
            f"<span>视频 <b>{mmss(seconds)}</b></span>"
            f"<span>建议学习 <b>{lesson['minutes']} 分钟</b></span>"
            f"<span>练习 <b>{len(lesson['questions'])} 题</b></span>"
        )
        aside_note = "视频与页面都可以离线使用。所有内容为教学演示，题目解析按小学、初中、高中的常规解法编写。"
    else:
        meta_html = (
            f"<span>图文精讲 <b>{len(lesson['knowledge'])} 节</b></span>"
            f"<span>建议学习 <b>{lesson['minutes']} 分钟</b></span>"
            f"<span>练习 <b>{len(lesson['questions'])} 题</b></span>"
        )
        aside_note = "本课为图文精讲，页面可离线使用。所有内容为教学演示，题目解析按高中常规解法编写。"

    return (
        head(
            f"{lesson['title']} · {lesson['subtitle']} · 数益坊",
            lesson["brief"],
        )
        + header("", "lessons")
        + f"""
<main id="main">
  <div class="wrap">
    <nav class="crumbs" aria-label="面包屑">
      <a href="index.html">首页</a><span class="sep">/</span>
      <a href="lessons.html">{esc(stage['name'])}</a><span class="sep">/</span>
      <span>{esc(lesson['title'])}</span>
    </nav>

    <header class="lesson-hero">
      <div>
        <div class="chip-row">
          <span class="chip stage {lesson['stage']}">{esc(stage['name'])}</span>
          <span class="chip">{esc(lesson['grade'])}</span>
          <span class="chip">{DIFFICULTY[lesson['difficulty']]}</span>
        </div>
        <h1>{esc(lesson['title'])}</h1>
        <p class="subtitle">{esc(lesson['subtitle'])}</p>
        <p class="brief">{esc(lesson['brief'])}</p>
        <div class="lesson-meta">
          {meta_html}
        </div>
      </div>
      <aside class="keyformula">
        <div class="kf-label">核心公式</div>
        <div class="kf-body">{esc(lesson['keyformula'])}</div>
      </aside>
    </header>

    <div class="lesson-layout">
      <div class="lesson-main">{sections_html}

        <nav class="pager" aria-label="课时翻页">{''.join(pager)}</nav>
      </div>

      <aside class="lesson-aside">
        <div class="aside-inner">
          <div class="aside-card">
            <h3>本页目录</h3>
            <ul class="toc">{toc_html}</ul>
          </div>
          <div class="aside-card">
            <h3>学完能做到</h3>
            <ul class="goal-list">{goals}</ul>
          </div>
          {lab_aside}
          <p class="aside-note">{aside_note}</p>
        </div>
      </aside>
    </div>
  </div>
</main>
"""
        + footer()
    )


def main() -> None:
    (ROOT / "index.html").write_text(build_home(), encoding="utf-8")
    (ROOT / "lessons.html").write_text(build_catalog(), encoding="utf-8")
    (ROOT / "labs.html").write_text(build_labs(), encoding="utf-8")

    for i, lesson in enumerate(LESSONS):
        prev = LESSONS[i - 1] if i > 0 else None
        nxt = LESSONS[i + 1] if i + 1 < len(LESSONS) else None
        (ROOT / lesson["file"]).write_text(build_lesson(lesson, prev, nxt), encoding="utf-8")
        print(f"[OK] {lesson['file']}")

    print(f"[DONE] {len(LESSONS) + 3} pages")


if __name__ == "__main__":
    main()