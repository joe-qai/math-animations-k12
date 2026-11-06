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