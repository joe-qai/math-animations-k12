// K12 数学学习网站 · 课程内容数据

export type StageId = 'xiaoxue' | 'chuzhong' | 'gaozhong';

export interface QuizQuestion {
  id: string;
  prompt: string;
  options: string[];
  answer: number;
  explanation: string;
}

export interface KnowledgeBlock {
  title: string;
  kind: 'concept' | 'formula' | 'example';
  body: string;
}

export interface Lesson {
  id: string;
  stage: StageId;
  grade: string;
  title: string;
  brief: string;
  difficulty: 1 | 2 | 3; // 1 基础 / 2 进阶 / 3 挑战
  estimatedMinutes: number;
  tags: string[];
  demo: string; // 对应原理动画演示组件 key
  knowledge: KnowledgeBlock[];
  questions: QuizQuestion[];
}

export interface Stage {
  id: StageId;
  name: string;
  tagline: string;
  emoji: string;
  color: string; // tailwind 文本/边框色
  chip: string; // 标签底色类
  grades: { label: string; range: string }[];
}

export const stages: Stage[] = [
  {
    id: 'xiaoxue',
    name: '小学数学',
    tagline: '建立数感与图形直觉，打好计算与应用的基础',
    emoji: '✏️',
    color: 'text-amber-700',
    chip: 'bg-amber-100/70 border-amber-300/60',
    grades: [
      { label: '一年级', range: '20 以内加减法 · 认识图形' },
      { label: '二年级', range: '乘法口诀 · 长度测量' },
      { label: '三年级', range: '多位乘除法 · 分数初步' },
      { label: '四年级', range: '大数 · 几何图形 · 运算律' },
      { label: '五年级', range: '小数 · 分数 · 立体图形' },
      { label: '六年级', range: '比与比例 · 圆的面积 · 百分数' },
    ],
  },
  {
    id: 'chuzhong',
    name: '初中数学',
    tagline: '从算术走向代数，理解函数与几何证明',
    emoji: '📐',
    color: 'text-sky-700',
    chip: 'bg-sky-100/70 border-sky-300/60',
    grades: [
      { label: '七年级', range: '有理数 · 整式 · 一元一次方程' },
      { label: '八年级', range: '三角形 · 全等 · 一次函数' },
      { label: '九年级', range: '二次函数 · 圆 · 概率初步' },
    ],
  },
  {
    id: 'gaozhong',
    name: '高中数学',
    tagline: '构建抽象思维，掌握函数、几何与数列方法',
    emoji: '🧮',
    color: 'text-teal-800',
    chip: 'bg-teal-100/70 border-teal-300/60',
    grades: [
      { label: '高一', range: '集合 · 函数 · 三角函数' },
      { label: '高二', range: '数列 · 立体几何 · 解析几何' },
      { label: '高三', range: '综合复习 · 压轴专题' },
    ],
  },
];

export const stageMap: Record<StageId, Stage> = Object.fromEntries(
  stages.map((s) => [s.id, s]),
) as Record<StageId, Stage>;

export const lessons: Lesson[] = [
  // ===== 小学 =====
  {
    id: 'xiaoxue-yi-jiajianfa',
    stage: 'xiaoxue',
    grade: '一年级',
    title: '20 以内的加减法',
    brief: '从数数到凑十法，掌握 20 以内加减的算理与口算技巧。',
    difficulty: 1,
    estimatedMinutes: 15,
    tags: ['计算', '口算'],
    demo: 'ten-frame',
    knowledge: [
      {
        title: '数的组成',
        kind: 'concept',
        body: '11 是由 1 个十和 1 个一组成。理解十位与个位的含义，是理解进位与借位的基础。比如 13 = 10 + 3，十位上的 1 表示 1 个十。',
      },
      {
        title: '凑十法',
        kind: 'formula',
        body: '计算 9 + 5 时，先把 5 拆成 1 和 4，9 + 1 = 10，10 + 4 = 14。凑十法把"进位加"转化为"十加几"，化难为易。',
      },
      {
        title: '破十法',
        kind: 'formula',
        body: '计算 15 - 9 时，把 15 拆成 10 和 5，先用 10 - 9 = 1，再算 1 + 5 = 6。破十法是借位减的核心技巧。',
      },
      {
        title: '例题：8 + 6 = ？',
        kind: 'example',
        body: '用凑十法：把 6 拆成 2 和 4，8 + 2 = 10，10 + 4 = 14，所以 8 + 6 = 14。',
      },
    ],
    questions: [
      {
        id: 'xy-a1',
        prompt: '计算：7 + 6 = ？',
        options: ['13', '12', '11', '14'],
        answer: 0,
        explanation: '凑十法：7 + 3 = 10，6 拆成 3 和 3，10 + 3 = 13。',
      },
      {
        id: 'xy-a2',
        prompt: '计算：15 - 7 = ？',
        options: ['7', '6', '8', '9'],
        answer: 2,
        explanation: '破十法：10 - 7 = 3，3 + 5 = 8。',
      },
      {
        id: 'xy-a3',
        prompt: '12 由几个十和几个一组成？',
        options: ['1 个十、1 个一', '1 个十、2 个一', '2 个十、1 个一', '2 个一、1 个十'],
        answer: 1,
        explanation: '12 的十位是 1，个位是 2，所以是 1 个十和 2 个一。',
      },
      {
        id: 'xy-a4',
        prompt: '用凑十法算 9 + 7，应该把 7 拆成哪两个数？',
        options: ['1 和 6', '2 和 5', '3 和 4', '7 和 0'],
        answer: 0,
        explanation: '9 差 1 到 10，所以把 7 拆成 1 和 6，先算 9 + 1 = 10，再算 10 + 6 = 16。',
      },
      {
        id: 'xy-a5',
        prompt: '小明做 8 + 5，他把 5 拆成了 2 和 3，第一步算什么？',
        options: ['8 + 3', '8 + 2', '5 + 2', '10 + 3'],
        answer: 1,
        explanation: '凑十法先看大数，8 缺 2 到 10，所以第一步算 8 + 2 = 10。',
      },
      {
        id: 'xy-a6',
        prompt: '下面哪个算式的结果是 11？',
        options: ['6 + 4', '7 + 3', '8 + 3', '9 + 1'],
        answer: 2,
        explanation: '8 + 3：把 3 拆成 2 和 1，8 + 2 = 10，10 + 1 = 11。',
      },
    ],
  },
  {
    id: 'xiaoxue-wu-fenshu',
    stage: 'xiaoxue',
    grade: '五年级',
    title: '分数的意义与运算',
    brief: '理解分数的含义，掌握同分母与异分母分数的加减法。',
    difficulty: 2,
    estimatedMinutes: 20,
    tags: ['分数', '运算'],
    demo: 'fraction-pie',
    knowledge: [
      {
        title: '分数的意义',
        kind: 'concept',
        body: '把一个整体平均分成若干份，表示其中一份或几份的数叫分数。如 3/4 表示把一个整体平均分成 4 份，取其中 3 份。',
      },
      {
        title: '分数与除法的关系',
        kind: 'formula',
        body: '分数的分子相当于除法中的被除数，分母相当于除数。a ÷ b = a/b（b ≠ 0）。分子比分母大时叫假分数。',
      },
      {
        title: '同分母分数加减',
        kind: 'formula',
        body: '同分母分数相加减，分母不变，只把分子相加减。如 3/7 + 2/7 = 5/7。',
      },
      {
        title: '异分母分数加减',
        kind: 'example',
        body: '1/2 + 1/3：先通分找到公分母 6，1/2 = 3/6，1/3 = 2/6，再相加 3/6 + 2/6 = 5/6。',
      },
    ],
    questions: [
      {
        id: 'xw-f1',
        prompt: '5/8 + 2/8 = ？',
        options: ['3/8', '7/16', '7/8', '3/16'],
        answer: 2,
        explanation: '同分母相加，分母不变，分子相加：5 + 2 = 7，得 7/8。',
      },
      {
        id: 'xw-f2',
        prompt: '2/3 + 1/6 = ？',
        options: ['3/9', '1/2', '5/6', '3/6'],
        answer: 2,
        explanation: '通分：2/3 = 4/6，4/6 + 1/6 = 5/6。',
      },
      {
        id: 'xw-f3',
        prompt: '1/2 ÷ 3 用分数表示为（a ÷ b = a/b）下面哪个正确？',
        options: ['1/2 ÷ 3 = 3/2', '1/2 ÷ 3 = 1/2', '1/2 ÷ 3 = 1/6', '1/2 ÷ 3 = 2/3'],
        answer: 2,
        explanation: '除以一个整数等于乘它的倒数：1/2 × 1/3 = 1/6。',
      },
      {
        id: 'xw-f4',
        prompt: '3/4 - 1/4 = ？',
        options: ['2/4', '2/8', '1/2', '3/8'],
        answer: 2,
        explanation: '同分母相减，分母不变，分子相减：3 - 1 = 2，得 2/4 = 1/2。',
      },
      {
        id: 'xw-f5',
        prompt: '1/3 + 1/5 的通分公分母是多少？',
        options: ['8', '15', '5', '3'],
        answer: 1,
        explanation: '3 和 5 的最小公倍数是 15，所以公分母是 15。',
      },
      {
        id: 'xw-f6',
        prompt: '下列分数中，最大的是？',
        options: ['1/3', '1/4', '1/5', '1/6'],
        answer: 0,
        explanation: '分子相同，分母越小分数越大，所以 1/3 最大。',
      },
    ],
  },
  // ===== 初中 =====
  {
    id: 'chuzhong-qi-yiyuan',
    stage: 'chuzhong',
    grade: '七年级',
    title: '一元一次方程',
    brief: '从算式思维到方程思维，学会移项与化系数为 1 解方程。',
    difficulty: 2,
    estimatedMinutes: 25,
    tags: ['方程', '代数'],
    demo: 'equation-balance',
    knowledge: [
      {
        title: '方程的意义',
        kind: 'concept',
        body: '含有未知数的等式叫方程。如 2x + 3 = 11。能使方程左右两边相等的未知数的值，叫做方程的解。',
      },
      {
        title: '等式的性质',
        kind: 'formula',
        body: '等式两边同时加上或减去同一个数，或同时乘除以同一个非零数，等式仍成立。这是移项与化系数为 1 的理论依据。',
      },
      {
        title: '解方程步骤',
        kind: 'formula',
        body: '①去分母 ②去括号 ③移项（把含未知数的项移到一边）④合并同类项 ⑤系数化为 1。',
      },
      {
        title: '例题：2x + 3 = 11',
        kind: 'example',
        body: '移项得 2x = 11 - 3 = 8，系数化为 1 得 x = 4。检验：2×4 + 3 = 11，成立。',
      },
    ],
    questions: [
      {
        id: 'cq-e1',
        prompt: '解方程：3x - 5 = 16，x = ？',
        options: ['6', '7', '5', '11'],
        answer: 1,
        explanation: '移项 3x = 21，x = 7。',
      },
      {
        id: 'cq-e2',
        prompt: '方程 x/2 = 8 的解是？',
        options: ['x = 4', 'x = 16', 'x = 8', 'x = 10'],
        answer: 1,
        explanation: '两边同乘 2，x = 16。',
      },
      {
        id: 'cq-e3',
        prompt: '把 2x + 5 = 17 进行移项，正确的是？',
        options: ['2x = 17 - 5', '2x = 17 + 5', 'x = 17 + 5', '2x + 5 = 17 不能移项'],
        answer: 0,
        explanation: '把 +5 移到右边变 -5，得 2x = 17 - 5。',
      },
      {
        id: 'cq-e4',
        prompt: '解方程：4(x - 2) = 20，x = ？',
        options: ['x = 3', 'x = 5', 'x = 7', 'x = 8'],
        answer: 2,
        explanation: '去括号：4x - 8 = 20，移项得 4x = 28，x = 7。',
      },
      {
        id: 'cq-e5',
        prompt: '方程 5x + 3 = 2x + 12 的解是？',
        options: ['x = 1', 'x = 2', 'x = 3', 'x = 5'],
        answer: 2,
        explanation: '移项：5x - 2x = 12 - 3，即 3x = 9，x = 3。',
      },
      {
        id: 'cq-e6',
        prompt: '某数的 3 倍减去 7 等于 20，这个数是？',
        options: ['7', '8', '9', '10'],
        answer: 2,
        explanation: '设该数为 x：3x - 7 = 20，3x = 27，x = 9。',
      },
    ],
  },
  {
    id: 'chuzhong-ba-yici',
    stage: 'chuzhong',
    grade: '八年级',
    title: '一次函数的图像与性质',
    brief: '掌握 y = kx + b 的图像、斜率的直观意义与实际问题建模。',
    difficulty: 2,
    estimatedMinutes: 25,
    tags: ['函数', '图像'],
    demo: 'linear-function',
    knowledge: [
      {
        title: '一次函数定义',
        kind: 'concept',
        body: '形如 y = kx + b（k、b 是常数，k ≠ 0）的函数叫一次函数。当 b = 0 时是正比例函数 y = kx。',
      },
      {
        title: '斜率 k 的意义',
        kind: 'concept',
        body: 'k 决定直线的倾斜方向：k > 0 时 y 随 x 增大而增大，直线从左下到右上；k < 0 时相反。',
      },
      {
        title: '截距 b 的意义',
        kind: 'concept',
        body: 'b 是直线与 y 轴的交点纵坐标。图像经过点 (0, b)。',
      },
      {
        title: '确定一次函数',
        kind: 'example',
        body: '已知 y = kx + b 过点 (1,3) 和 (2,5)，代入得方程: k + b = 3 与 2k + b = 5，解得 k = 2、b = 1，即 y = 2x + 1。',
      },
    ],
    questions: [
      {
        id: 'cb-f1',
        prompt: '一次函数 y = 3x + 1，当 x = 2 时 y 的值为？',
        options: ['5', '7', '6', '8'],
        answer: 1,
        explanation: '代入：y = 3×2 + 1 = 7。',
      },
      {
        id: 'cb-f2',
        prompt: '一次函数 y = -2x + 5 的图像，随 x 增大 y 如何变化？',
        options: ['增大', '减小', '不变', '先增后减'],
        answer: 1,
        explanation: 'k = -2 < 0，y 随 x 增大而减小。',
      },
      {
        id: 'cb-f3',
        prompt: '一次函数 y = kx + 3 过点 (2, 7)，则 k = ？',
        options: ['1', '2', '3', '4'],
        answer: 1,
        explanation: '代入 7 = 2k + 3，2k = 4，k = 2。',
      },
      {
        id: 'cb-f4',
        prompt: '一次函数 y = -x + 4 与 x 轴的交点是？',
        options: ['(0, 4)', '(4, 0)', '(-4, 0)', '(0, -4)'],
        answer: 1,
        explanation: '与 x 轴交点令 y = 0：-x + 4 = 0，x = 4，得 (4, 0)。',
      },
      {
        id: 'cb-f5',
        prompt: '下列哪个是一次函数 y = 2x - 3 的图像经过的点？',
        options: ['(1, 1)', '(2, 1)', '(0, 2)', '(3, 0)'],
        answer: 1,
        explanation: '代入验证：x = 2 时 y = 2×2 - 3 = 1，点 (2, 1) 在图像上。',
      },
      {
        id: 'cb-f6',
        prompt: '直线 y = kx + b 过点 (0, -2) 且斜率为 3，其解析式是？',
        options: ['y = 3x + 2', 'y = 3x - 2', 'y = -2x + 3', 'y = 2x - 3'],
        answer: 1,
        explanation: 'b = -2（与 y 轴交点），k = 3，所以 y = 3x - 2。',
      },
    ],
  },
  // ===== 高中 =====
  {
    id: 'gaozhong-gao-jiehe',
    stage: 'gaozhong',
    grade: '高一',
    title: '集合与集合基本运算',
    brief: '理解集合、子集、交集与并集的概念与表示方法。',
    difficulty: 1,
    estimatedMinutes: 20,
    tags: ['集合', '基础'],
    demo: 'venn',
    knowledge: [
      {
        title: '集合的概念',
        kind: 'concept',
        body: '集合是确定的、互不相同的对象构成的整体。构成集合的每个对象叫元素。集合有确定性、互异性、无序性三大特性。',
      },
      {
        title: '常用数集',
        kind: 'formula',
        body: 'N 表示自然数集，N* 表示正整数集，Z 表示整数集，Q 表示有理数集，R 表示实数集。',
      },
      {
        title: '交集与并集',
        kind: 'formula',
        body: '交集 A ∩ B 表示既属于 A 又属于 B 的元素全体；并集 A ∪ B 表示属于 A 或属于 B 的元素全体。',
      },
      {
        title: '例题',
        kind: 'example',
        body: 'A = {1, 2, 3}，B = {2, 3, 4}。A ∩ B = {2, 3}，A ∪ B = {1, 2, 3, 4}。补集是相对全集而言，如 U - A 中不属于 A 的元素。',
      },
    ],
    questions: [
      {
        id: 'gj-j1',
        prompt: 'A = {1, 2, 3}，B = {2, 4}，A ∩ B = ？',
        options: ['{1, 2, 3, 4}', '{2}', '{1, 3}', '∅'],
        answer: 1,
        explanation: '交集是两者的公共元素，只有 2。',
      },
      {
        id: 'gj-j2',
        prompt: 'A = {1, 2}，B = {2, 3}，A ∪ B = ？',
        options: ['{1, 2}', '{1, 2, 3}', '{2, 3}', '{2}'],
        answer: 1,
        explanation: '并集取全部元素且去重：{1, 2, 3}。',
      },
      {
        id: 'gj-j3',
        prompt: '全集 U = {1, 2, 3, 4, 5}，A = {1, 3}，则 ∁U A = ？',
        options: ['{1, 3}', '{2, 4}', '{2, 4, 5}', '∅'],
        answer: 2,
        explanation: '补集是 U 中不属于 A 的元素：{2, 4, 5}。',
      },
      {
        id: 'gj-j4',
        prompt: '下列关系中，正确的是？',
        options: ['0 ∈ ∅', '∅ ⊂ {0}', '{0} = ∅', 'a ∈ {a, b}'],
        answer: 3,
        explanation: 'a 是集合 {a, b} 的元素，选 D。A错因为0不是空集元素，B错符号应为⊆，C错{0}有1个元素空集有0个。',
      },
      {
        id: 'gj-j5',
        prompt: '已知 A = {x | -1 < x < 3}，B = {x | 0 < x < 4}，则 A ∩ B = ？',
        options: ['{x | -1 < x < 4}', '{x | 0 < x < 3}', '{x | -1 < x < 0}', '{x | 3 < x < 4}'],
        answer: 1,
        explanation: '取两区间的公共部分：0 < x < 3。',
      },
      {
        id: 'gj-j6',
        prompt: '集合 A = {1, 2, 3} 的子集共有多少个？',
        options: ['3', '6', '8', '4'],
        answer: 2,
        explanation: 'n 个元素的子集数为 2ⁿ，2³ = 8 个子集（含空集和自身）。',
      },
    ],
  },
  {
    id: 'gaozhong-gao-sanjiaohan',
    stage: 'gaozhong',
    grade: '高一',
    title: '三角函数的图像与性质',
    brief: '掌握正弦、余弦函数图像的周期性与最值特点。',
    difficulty: 3,
    estimatedMinutes: 30,
    tags: ['三角函数', '图像'],
    demo: 'sine-wave',
    knowledge: [
      {
        title: '正弦函数',
        kind: 'formula',
        body: 'y = sin x 的定义域为 R，值域为 [-1, 1]，最小正周期 T = 2π。图像为波浪形（正弦曲线）。',
      },
      {
        title: '余弦函数',
        kind: 'formula',
        body: 'y = cos x 值域同样为 [-1, 1]，周期 T = 2π。余弦曲线可由正弦曲线向左平移 π/2 得到。',
      },
      {
        title: '最值与周期',
        kind: 'concept',
        body: 'sin x 与 cos x 的最大值都是 1，最小值都是 -1。周期的含义是函数值重复出现的最小正距离。',
      },
      {
        title: '同名角关系',
        kind: 'example',
        body: 'sin(π - x) = sin x，cos(-x) = cos x（偶函数）。sin²x + cos²x = 1 是最基本的恒等式。',
      },
    ],
    questions: [
      {
        id: 'gj-s1',
        prompt: '函数 y = sin x 的最小正周期是？',
        options: ['π', '2π', 'π/2', '4π'],
        answer: 1,
        explanation: 'sin x 的最小正周期为 2π。',
      },
      {
        id: 'gj-s2',
        prompt: 'sin²α + cos²α 恒等于？',
        options: ['0', '1', '2', '-1'],
        answer: 1,
        explanation: '这是最常用的三角恒等式，值为 1。',
      },
      {
        id: 'gj-s3',
        prompt: '函数 y = 2cos x 的最大值是？',
        options: ['1', '2', '3', '-2'],
        answer: 1,
        explanation: 'cos x 最大为 1，所以 2cos x 最大为 2。',
      },
      {
        id: 'gj-s4',
        prompt: 'sin(π/2 - α) 等于？',
        options: ['sin α', 'cos α', '-cos α', '-sin α'],
        answer: 1,
        explanation: '诱导公式：sin(π/2 - α) = cos α。',
      },
      {
        id: 'gj-s5',
        prompt: '函数 y = sin 2x 的最小正周期是？',
        options: ['2π', 'π', 'π/2', '4π'],
        answer: 1,
        explanation: 'T = 2π/ω = 2π/2 = π。',
      },
      {
        id: 'gj-s6',
        prompt: 'cos(π + α) 等于？',
        options: ['cos α', '-cos α', 'sin α', '-sin α'],
        answer: 1,
        explanation: '诱导公式：cos(π + α) = -cos α（第三象限余弦为负）。',
      },
    ],
  },
  // ===== 新增课时：覆盖更多年级 =====
  {
    id: 'xiaoxue-san-chengchu',
    stage: 'xiaoxue',
    grade: '三年级',
    title: '多位数乘一位数',
    brief: '从口算到竖式，理解进位的每一步，把复杂计算拆成简单步骤。',
    difficulty: 2,
    estimatedMinutes: 20,
    tags: ['计算', '乘法'],
    demo: '',
    knowledge: [
      {
        title: '口算技巧',
        kind: 'concept',
        body: '把多位数看成几个十、几个百。比如 23 × 3，先算 20 × 3 = 60，再算 3 × 3 = 9，最后 60 + 9 = 69。',
      },
      {
        title: '竖式写法',
        kind: 'formula',
        body: '相同数位对齐，从个位乘起，哪一位上乘得的积满几十就向前一位进几。进位的小数字写小一点，别忘了加。',
      },
      {
        title: '例题：47 × 6 = ？',
        kind: 'example',
        body: '7 × 6 = 42，写 2 进 4；4 × 6 = 24，加进位 4 得 28。所以 47 × 6 = 282。',
      },
    ],
    questions: [
      {
        id: 'xs-c1',
        prompt: '计算：36 × 4 = ？',
        options: ['144', '124', '134', '148'],
        answer: 0,
        explanation: '6×4=24，写4进2；3×4=12，加2得14，结果 144。',
      },
      {
        id: 'xs-c2',
        prompt: '计算：58 × 7 = ？',
        options: ['406', '396', '416', '386'],
        answer: 0,
        explanation: '8×7=56，写6进5；5×7=35，加5得40，结果 406。',
      },
      {
        id: 'xs-c3',
        prompt: '25 × 4 的结果是？',
        options: ['100', '90', '80', '110'],
        answer: 0,
        explanation: '25 × 4 = 100。这是常用组合，记住它计算更快。',
      },
      {
        id: 'xs-c4',
        prompt: '下面哪个算式的结果是 210？',
        options: ['35 × 6', '30 × 8', '42 × 5', '28 × 7'],
        answer: 2,
        explanation: '42 × 5：40×5=200，2×5=10，合计 210。',
      },
      {
        id: 'xs-c5',
        prompt: '306 × 5 的积中间有几个 0？',
        options: ['0 个', '1 个', '2 个', '3 个'],
        answer: 1,
        explanation: '306×5：6×5=30 写0进3，0×5+3=3，3×5=15，结果 1530，中间有 1 个 0。',
      },
      {
        id: 'xs-c6',
        prompt: '一个数乘以 10，积的末尾会有几个 0？',
        options: ['0 个', '1 个', '取决于原数', '2 个'],
        answer: 1,
        explanation: '任何整数乘 10，末尾添 1 个 0，如 37 × 10 = 370。',
      },
    ],
  },
  {
    id: 'xiaoxue-liu-yuan',
    stage: 'xiaoxue',
    grade: '六年级',
    title: '圆的面积与周长',
    brief: '从分割拼接到公式推导，理解 πr² 和 2πr 的来源，会解决实际问题。',
    difficulty: 2,
    estimatedMinutes: 20,
    tags: ['圆', '几何'],
    demo: '',
    knowledge: [
      {
        title: '圆的周长',
        kind: 'formula',
        body: 'C = πd = 2πr，其中 d 是直径，r 是半径。圆周率 π ≈ 3.14159…，通常取 3.14 计算。',
      },
      {
        title: '圆的面积',
        kind: 'formula',
        body: 'S = πr²。可以把圆切成许多小扇形，拼成一个近似长方形：长是 πr，宽是 r，面积 = πr × r = πr²。',
      },
      {
        title: '例题：r = 5 cm',
        kind: 'example',
        body: '周长 C = 2 × 3.14 × 5 = 31.4 cm；面积 S = 3.14 × 5² = 3.14 × 25 = 78.5 cm²。',
      },
    ],
    questions: [
      {
        id: 'xl-y1',
        prompt: '圆的半径 r = 3 cm，周长是多少？（π 取 3.14）',
        options: ['18.84 cm', '28.26 cm', '9.42 cm', '12.56 cm'],
        answer: 0,
        explanation: 'C = 2πr = 2 × 3.14 × 3 = 18.84 cm。',
      },
      {
        id: 'xl-y2',
        prompt: '圆的直径 d = 10 cm，面积是多少？（π 取 3.14）',
        options: ['78.5 cm²', '314 cm²', '157 cm²', '31.4 cm²'],
        answer: 2,
        explanation: 'r = 5 cm，S = πr² = 3.14 × 25 = 78.5 cm²。',
      },
      {
        id: 'xl-y3',
        prompt: '半径扩大 2 倍，圆的面积扩大多少倍？',
        options: ['2 倍', '4 倍', '6 倍', '不变'],
        answer: 1,
        explanation: '面积 S = πr²，半径扩大 2 倍则面积扩大 2² = 4 倍。',
      },
      {
        id: 'xl-y4',
        prompt: '一个圆形花坛半径 4 m，绕一周要走多少米？（π 取 3.14）',
        options: ['25.12 m', '50.24 m', '12.56 m', '16 m'],
        answer: 0,
        explanation: 'C = 2πr = 2 × 3.14 × 4 = 25.12 m。',
      },
      {
        id: 'xl-y5',
        prompt: '圆的周长是 31.4 cm，它的半径是多少？（π 取 3.14）',
        options: ['5 cm', '10 cm', '3.14 cm', '15.7 cm'],
        answer: 0,
        explanation: 'C = 2πr，31.4 = 2 × 3.14 × r，r = 31.4 ÷ 6.28 = 5 cm。',
      },
      {
        id: 'xl-y6',
        prompt: '下面哪种说法正确？',
        options: ['圆的半径扩大 3 倍，周长也扩大 3 倍', '圆的半径扩大 3 倍，面积扩大 3 倍', '直径是半径的 2 倍，所以面积也是 2 倍', '以上都对'],
        answer: 0,
        explanation: '周长与半径成正比（C = 2πr），半径扩大几倍周长也扩大几倍；面积与半径平方成正比。',
      },
    ],
  },
  {
    id: 'chuzhong-jiu-erci',
    stage: 'chuzhong',
    grade: '九年级',
    title: '二次函数的图像与最值',
    brief: '从一般式到顶点式，掌握开口方向、对称轴和最值的判断方法。',
    difficulty: 2,
    estimatedMinutes: 25,
    tags: ['二次函数', '图像'],
    demo: '',
    knowledge: [
      {
        title: '二次函数定义',
        kind: 'concept',
        body: '形如 y = ax² + bx + c（a ≠ 0）的函数叫二次函数。图像是一条抛物线。a > 0 开口向上，有最低点；a < 0 开口向下，有最高点。',
      },
      {
        title: '顶点式与最值',
        kind: 'formula',
        body: 'y = a(x - h)² + k，顶点为 (h, k)。当 a > 0 时 x = h 处取得最小值 k；当 a < 0 时 x = h 处取得最大值 k。',
      },
      {
        title: '配方法求顶点',
        kind: 'example',
        body: 'y = x² - 4x + 3：配方得 y = (x - 2)² - 1，顶点 (2, -1)，对称轴 x = 2，最小值为 -1。',
      },
    ],
    questions: [
      {
        id: 'cj-q1',
        prompt: '二次函数 y = 2x² - 4x + 1 的开口方向是？',
        options: ['向上', '向下', '向左', '向右'],
        answer: 0,
        explanation: 'a = 2 > 0，抛物线开口向上。',
      },
      {
        id: 'cj-q2',
        prompt: '函数 y = -(x - 3)² + 5 的最大值是？',
        options: ['3', '5', '-3', '-5'],
        answer: 1,
        explanation: '顶点式为 y = a(x-h)²+k，这里 a = -1 < 0 开口向下，顶点 (3, 5)，最大值为 5。',
      },
      {
        id: 'cj-q3',
        prompt: '将 y = x² + 6x + 5 配方，正确的是？',
        options: ['y = (x+3)² - 4', 'y = (x+3)² + 4', 'y = (x-3)² - 4', 'y = (x+3)² - 14'],
        answer: 0,
        explanation: 'x² + 6x + 5 = (x+3)² - 9 + 5 = (x+3)² - 4。',
      },
      {
        id: 'cj-q4',
        prompt: '抛物线 y = x² - 2x - 3 的对称轴是？',
        options: ['x = 1', 'x = -1', 'x = 3', 'x = -3'],
        answer: 0,
        explanation: '对称轴 x = -b/(2a) = -(-2)/(2×1) = 1。',
      },
      {
        id: 'cj-q5',
        prompt: '函数 y = -x² + 4x 在什么位置取得最大值？',
        options: ['x = 2', 'x = 4', 'x = 0', 'x = -2'],
        answer: 0,
        explanation: '对称轴 x = -b/(2a) = -4/(-2) = 2，此时 y = -4 + 8 = 4 为最大值。',
      },
      {
        id: 'cj-q6',
        prompt: '已知抛物线过点 (1,0)、(3,0)、(0,3)，其解析式是？',
        options: ['y = -x² + 4x - 3', 'y = x² - 4x + 3', 'y = -x² - 4x - 3', 'y = x² + 4x + 3'],
        answer: 1,
        explanation: '设 y = a(x-1)(x-3)，代入 (0,3)：3 = a·(-1)·(-3) = 3a，a = 1。展开得 y = x² - 4x + 3，验证：过三点均成立。',
      },
    ],
  },
  {
    id: 'gaozhong-er-shulie',
    stage: 'gaozhong',
    grade: '高二',
    title: '等差数列的通项与前n项和',
    brief: '从阶梯图形倒序相加，理解等差数列公式的来源，能做综合应用题。',
    difficulty: 2,
    estimatedMinutes: 25,
    tags: ['数列', '代数'],
    demo: '',
    knowledge: [
      {
        title: '等差数列定义',
        kind: 'concept',
        body: '从第二项起，每一项与前一项的差等于同一个常数 d（公差）。通项公式：aₙ = a₁ + (n - 1)d。',
      },
      {
        title: '前 n 项和公式',
        kind: 'formula',
        body: 'Sₙ = n(a₁ + aₙ)/2 = na₁ + n(n-1)d/2。推导方法：正序写一遍、倒序写一遍，对应项相加都等于 a₁ + aₙ，共 n 对，除以 2 即得。',
      },
      {
        title: '例题',
        kind: 'example',
        body: '等差数列 3, 7, 11, 15, …，a₁ = 3，d = 4。第 10 项：a₁₀ = 3 + 9×4 = 39。前 10 项和：S₁₀ = 10×(3 + 39)/2 = 210。',
      },
    ],
    questions: [
      {
        id: 'ge-s1',
        prompt: '等差数列 2, 5, 8, 11, … 的第 10 项是？',
        options: ['29', '32', '27', '30'],
        answer: 0,
        explanation: 'a₁ = 2，d = 3，a₁₀ = 2 + 9×3 = 29。',
      },
      {
        id: 'ge-s2',
        prompt: '等差数列首项 a₁ = 5，公差 d = -2，前 8 项和 S₈ = ？',
        options: ['16', '20', '24', '28'],
        answer: 0,
        explanation: 'a₈ = 5 + 7×(-2) = -9，S₈ = 8×(5 + (-9))/2 = 8×(-4)/2 = -16。首项为正公差为负，和先增后减。',
      },
      {
        id: 'ge-s3',
        prompt: '已知等差数列 a₃ = 7，a₇ = 19，则公差 d = ？',
        options: ['2', '3', '4', '6'],
        answer: 1,
        explanation: 'a₇ - a₃ = 4d = 19 - 7 = 12，d = 3。',
      },
      {
        id: 'ge-s4',
        prompt: '等差数列前 n 项和 Sₙ = 3n² + 2n，首项 a₁ = ？',
        options: ['5', '3', '2', '1'],
        answer: 0,
        explanation: 'a₁ = S₁ = 3×1² + 2×1 = 5。',
      },
      {
        id: 'ge-s5',
        prompt: '等差数列中，a₁ + a₁₀ = a₄ + a₇ 是否成立？',
        options: ['成立', '不成立', '仅当 d = 0 时成立', '无法判断'],
        answer: 1,
        explanation: '逐项列出：a₁=10, a₂=7, a₃=4, a₄=1, a₅=-2。a₄=1 仍为正，a₅=-2 第一个为负数，所以从第 5 项开始变负。',
      },
      {
        id: 'ge-s5',
        prompt: '等差数列中，a₁ + a₁₀ = a₄ + a₇ 是否成立？',
        options: ['成立', '不成立', '仅当 d = 0 时成立', '无法判断'],
        answer: 0,
        explanation: 'a₁ + a₁₀ = 2a₁ + 9d，a₄ + a₇ = (a₁+3d) + (a₁+6d) = 2a₁ + 9d，两边相等，恒成立。',
      },
      {
        id: 'ge-s6',
        prompt: '等差数列 {aₙ} 满足 a₁ = 10，d = -3，从第几项开始变为负数？',
        options: ['第 4 项', '第 5 项', '第 3 项', '第 6 项'],
        answer: 1,
    ],
  },
  // 补充更多年级练习专题
  {
    id: 'xiaoxue-er-koujue',
    stage: 'xiaoxue',
    grade: '二年级',
    title: '乘法口诀与表内乘法',
    brief: '从加法到乘法，理解乘法口诀的意义，熟练背诵并能灵活运用。',
    difficulty: 1,
    estimatedMinutes: 15,
    tags: ['乘法', '口诀'],
    demo: '',
    knowledge: [
      {
        title: '乘法的意义',
        kind: 'concept',
        body: '乘法是相同加数连加的简便运算。3 × 4 表示 4 个 3 相加：3 + 3 + 3 + 3 = 12，或者 3 个 4 相加：4 + 4 + 4 = 12。',
      },
      {
        title: '交换律',
        kind: 'formula',
        body: 'a × b = b × a。比如 3 × 5 = 5 × 3 = 15，横着看和竖着看总数一样，点阵转个方向行数变了但总数不变。',
      },
      {
        title: '重点口诀',
        kind: 'example',
        body: '三七二十一（3×7=21）、四七二十八（4×7=28）、五七三十五（5×7=35）。背口诀时按行或列一组组记，比死记硬背更快。',
      },
    ],
    questions: [
      {
        id: 'xe-k1',
        prompt: '5 × 6 = ？',
        options: ['30', '25', '35', '36'],
        answer: 0,
        explanation: '五六三十，5 × 6 = 30。',
      },
      {
        id: 'xe-k2',
        prompt: '下列算式中，结果等于 24 的是？',
        options: ['4 × 6', '3 × 7', '4 × 7', '3 × 9'],
        answer: 0,
        explanation: '四六二十四：4 × 6 = 24。其他选项分别为 21、28、27。',
      },
      {
        id: 'xe-k3',
        prompt: '7 × 8 = ？',
        options: ['56', '54', '63', '48'],
        answer: 0,
        explanation: '七八五十六：7 × 8 = 56。',
      },
      {
        id: 'xe-k4',
        prompt: '3 × 9 = 9 × ？',
        options: ['3', '9', '27', '12'],
        answer: 0,
        explanation: '乘法交换律：3 × 9 = 9 × 3，两者都等于 27。',
      },
      {
        id: 'xe-k5',
        prompt: '每排坐 6 人，坐了 5 排，一共有多少人？',
        options: ['30 人', '11 人', '24 人', '36 人'],
        answer: 0,
        explanation: '总人数 = 6 × 5 = 30 人。',
      },
      {
        id: 'xe-k6',
        prompt: '2 × 7 + 2 = ？',
        options: ['16', '14', '12', '20'],
        answer: 0,
        explanation: '2×7=14，14+2=16。也可以理解为 2×8=16。',
      },
    ],
  },
  {
    id: 'chuzhong-qi-youli',
    stage: 'chuzhong',
    grade: '七年级',
    title: '有理数的加减混合运算',
    brief: '掌握正负数的加减规则，能正确处理去括号和符号变化。',
    difficulty: 2,
    estimatedMinutes: 20,
    tags: ['有理数', '运算'],
    demo: '',
    knowledge: [
      {
        title: '同号两数相加',
        kind: 'formula',
        body: '取相同的符号，并把绝对值相加。如 (-3) + (-5) = -(3+5) = -8。',
      },
      {
        title: '异号两数相加',
        kind: 'formula',
        body: '取绝对值较大加数的符号，并用较大的绝对值减去较小的绝对值。如 (-7) + 4 = -(7-4) = -3。',
      },
      {
        title: '去括号法则',
        kind: 'example',
        body: '括号前面是"+"号，去掉括号符号不变：a + (b - c) = a + b - c。括号前面是"-"号，去掉括号各项变号：a - (b - c) = a - b + c。',
      },
    ],
    questions: [
      {
        id: 'cy-r1',
        prompt: '(-5) + (+3) = ？',
        options: ['-2', '2', '-8', '8'],
        answer: 0,
        explanation: '异号相加，取大绝对值符号（负），7-5=2，结果为 -2。',
      },
      {
        id: 'cy-r2',
        prompt: '(-8) - (-3) = ？',
        options: ['-5', '-11', '5', '11'],
        answer: 0,
        explanation: '减去一个负数等于加上它的相反数：(-8) + 3 = -5。',
      },
      {
        id: 'cy-r3',
        prompt: '12 - 7 + (-5) = ？',
        options: ['0', '10', '-10', '4'],
        answer: 0,
        explanation: '从左到右依次计算：12 - 7 = 5，5 + (-5) = 0。',
      },
      {
        id: 'cy-r4',
        prompt: '化简 -(a - b + c) 得？',
        options: ['-a + b - c', '-a - b + c', 'a - b + c', '-a - b - c'],
        answer: 0,
        explanation: '去括号，括号前是负号，各项变号：-a + b - c。',
      },
      {
        id: 'cy-r5',
        prompt: '温度从 -3℃ 上升了 8℃，现在的温度是？',
        options: ['5℃', '-11℃', '11℃', '-5℃'],
        answer: 0,
        explanation: '-3 + 8 = 5℃。上升用加法。',
      },
      {
        id: 'cy-r6',
        prompt: '(-2) × 3 + (-5) = ？',
        options: ['-11', '-1', '1', '-7'],
        answer: 0,
        explanation: '先乘后加：(-2)×3 = -6，-6 + (-5) = -11。',
      },
    ],
  },
  {
    id: 'gaozhong-san-zonghe',
    stage: 'gaozhong',
    grade: '高三',
    title: '导数的综合应用——求切线与单调区间',
    brief: '掌握导数的几何意义，会用导数求切线方程和函数的单调性。',
    difficulty: 3,
    estimatedMinutes: 30,
    tags: ['导数', '综合'],
    demo: '',
    knowledge: [
      {
        title: '导数的几何意义',
        kind: 'concept',
        body: '函数 f(x) 在点 x₀ 处的导数 f\'(x₀) 就是曲线在该点处切线的斜率。切线方程：y - f(x₀) = f\'(x₀)(x - x₀)。',
      },
      {
        title: '单调性与导数',
        kind: 'formula',
        body: '若在某个区间上 f\'(x) > 0，则 f(x) 在该区间单调递增；若 f\'(x) < 0，则单调递减。先求定义域，再解不等式找单调区间。',
      },
      {
        title: '例题',
        kind: 'example',
        body: 'f(x) = x³ - 3x，f\'(x) = 3x² - 3 = 3(x+1)(x-1)。令 f\'(x) = 0 得 x = ±1。f\'(x) > 0 当 x < -1 或 x > 1（增）；f\'(x) < 0 当 -1 < x < 1（减）。',
      },
    ],
    questions: [
      {
        id: 'gz-d1',
        prompt: '函数 f(x) = x² 在点 (1, 1) 处的切线斜率是？',
        options: ['2', '1', '3', '-2'],
        answer: 0,
        explanation: 'f\'(x) = 2x，f\'(1) = 2，切线斜率为 2。',
      },
      {
        id: 'gz-d2',
        prompt: '函数 f(x) = x³ - 3x 的单调递增区间是？',
        options: ['(-∞, -1) ∪ (1, +∞)', '(-1, 1)', '(-∞, +∞)', '(1, +∞)'],
        answer: 0,
        explanation: 'f\'(x) = 3x² - 3 = 3(x+1)(x-1)，f\'(x) > 0 解得 x < -1 或 x > 1。',
      },
      {
        id: 'gz-d3',
        prompt: '曲线 y = eˣ 在点 (0, 1) 处的切线方程是？',
        options: ['y = x + 1', 'y = x', 'y = e·x', 'y = 1'],
        answer: 0,
        explanation: 'y\' = eˣ，y\'(0) = 1，切线：y - 1 = 1×(x - 0)，即 y = x + 1。',
      },
      {
        id: 'gz-d4',
        prompt: '函数 f(x) = ln x 在 x = e 处的导数值是？',
        options: ['1/e', 'e', '1', 'ln e'],
        answer: 0,
        explanation: 'f\'(x) = 1/x，f\'(e) = 1/e。',
      },
      {
        id: 'gz-d5',
        prompt: '函数 f(x) = x³ - 6x² + 9x + 1 的极大值是？',
        options: ['5', '1', '0', '4'],
        answer: 0,
        explanation: 'f\'(x) = 3x² - 12x + 9 = 3(x-1)(x-3)。x=1 是极大值点，f(1) = 1-6+9+1 = 5。',
      },
      {
        id: 'gz-d6',
        prompt: '已知 f(x) = ax² + bx 在 x = 1 处有极值 2，则 a + b = ？',
        options: ['2', '-2', '4', '0'],
        answer: 0,
        explanation: 'f\'(x) = 2ax + b，f\'(1) = 0 ⇒ 2a + b = 0；f(1) = 2 ⇒ a + b = 2。联立解得 a = -2，b = 4，a + b = 2。',
      },
    ],
  },
];

export const lessonMap: Record<string, Lesson> = Object.fromEntries(
  lessons.map((l) => [l.id, l]),
);

export function lessonsByStage(stage: StageId): Lesson[] {
  return lessons.filter((l) => l.stage === stage);
}

export function lessonsByGrade(stage: StageId, grade: string): Lesson[] {
  return lessons.filter((l) => l.stage === stage && l.grade === grade);
}