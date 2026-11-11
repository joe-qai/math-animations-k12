import type { Metadata } from 'next';
import Link from 'next/link';
import { ArrowRight, Brain, Puzzle, Target, Trophy } from 'lucide-react';

export const metadata: Metadata = {
  title: '数学游戏',
  description: '数益坊 · K12 数学游戏，在玩中学数学',
};

const GAMES = [
  {
    slug: 'arithmetic-match',
    title: '口算消消乐',
    emoji: '🎯',
    desc: '匹配算式与答案，消除所有卡片。支持加减乘除四则混合运算，适合练习心算速度。',
    icon: Target,
    grade: '小学 1~4 年级',
    color: 'text-emerald-600',
    chip: 'bg-emerald-100/70 border-emerald-300/60',
  },
  {
    slug: 'number-guess',
    title: '猜数迷',
    emoji: '🔢',
    desc: '猜一个数字，系统告诉你几个数字位置对（牛）几个数字对但位置错（cow）。锻炼逻辑推理能力。',
    icon: Brain,
    grade: '小学 3~6 年级',
    color: 'text-sky-600',
    chip: 'bg-sky-100/70 border-sky-300/60',
  },
  {
    slug: 'hopscotch',
    title: '跳格子',
    emoji: '🦘',
    desc: '用方向键控制角色按顺序踩完所有数字格子！在规定时间内完成挑战，训练反应力和数感。',
    icon: Trophy,
    grade: '小学 1~3 年级',
    color: 'text-amber-600',
    chip: 'bg-amber-100/70 border-amber-300/60',
  },
  {
    slug: 'sudoku',
    title: '数独',
    emoji: '🧩',
    desc: '经典数独游戏，简单/中等/困难三档难度。在方格中填入 1~9，使每行、每列、每宫均不重复。',
    icon: Puzzle,
    grade: '小学 4 年级 ~ 高中',
    color: 'text-teal-600',
    chip: 'bg-teal-100/70 border-teal-300/60',
  },
  {
    slug: 'huarongdao',
    title: '数学华容道',
    emoji: '🏯',
    desc: '拖动方块把红色主公移到出口。融合空间推理与规划思维，含三个递进关卡。',
    icon: Puzzle,
    grade: '小学 4 年级 ~ 初中',
    color: 'text-rose-600',
    chip: 'bg-rose-100/70 border-rose-300/60',
  },
];

export default function GamesPage() {
  return (
    <div>
      <section className="border-b border-border/70 bg-[radial-gradient(ellipse_at_top,rgba(44,107,94,0.08),transparent_60%)]">
        <div className="mx-auto max-w-6xl px-4 py-14 sm:px-6 sm:py-20">
          <span className="inline-flex items-center gap-1.5 rounded-full bg-accent/50 px-3 py-1 text-xs font-medium text-accent-foreground">
            <Trophy className="h-3.5 w-3.5" />
            玩中学数学
          </span>
          <h1 className="mt-5 max-w-2xl text-4xl font-extrabold leading-tight tracking-tight text-foreground sm:text-5xl">
            数学游戏<span className="text-primary">乐园</span>
          </h1>
          <p className="mt-5 max-w-xl text-lg leading-8 text-muted-foreground">
            把数学藏在游戏里——口算消消乐、猜数迷、跳格子、数独、华容道，边玩边练，越玩越聪明。
          </p>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-4 py-14 sm:px-6">
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {GAMES.map(g => {
            const Icon = g.icon;
            return (
              <Link
                key={g.slug}
                href={`/games/${g.slug}`}
                className="group relative overflow-hidden rounded-2xl border border-border/70 bg-card p-7 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-lg"
              >
                <div className="flex items-start justify-between">
                  <span className="text-4xl">{g.emoji}</span>
                  <span className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-medium ${g.chip}`}>
                    {g.grade}
                  </span>
                </div>
                <h2 className={`mt-5 text-xl font-bold ${g.color} group-hover:text-primary transition-colors`}>
                  {g.title}
                </h2>
                <p className="mt-2 text-sm leading-6 text-muted-foreground">
                  {g.desc}
                </p>
                <div className="mt-5 flex items-center gap-1 text-sm font-medium text-primary opacity-0 transition-opacity group-hover:opacity-100">
                  开始游戏
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </div>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
