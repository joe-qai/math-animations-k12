import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { ChevronLeft, Clock, Gauge } from 'lucide-react';
import { lessonMap, stageMap, type KnowledgeBlock } from '@/lib/data';
import { Quiz } from '@/components/quiz';
import { DemoBlock } from '@/components/demos/demo-block';

interface Props {
  params: Promise<{ id: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const lesson = lessonMap[id];
  return { title: lesson ? lesson.title : '课时' };
}

const kindStyle: Record<KnowledgeBlock['kind'], { label: string; cls: string }> = {
  concept: { label: '概念', cls: 'bg-sky-100/70 text-sky-800 border-sky-300/60' },
  formula: { label: '公式', cls: 'bg-amber-100/70 text-amber-800 border-amber-300/60' },
  example: { label: '例题', cls: 'bg-teal-100/70 text-teal-800 border-teal-300/60' },
};

const difficultyLabel = ['', '基础', '进阶', '挑战'];

function Block({ block }: { block: KnowledgeBlock }) {
  const meta = kindStyle[block.kind];
  return (
    <article className="rounded-xl border border-border/70 bg-card p-5 shadow-sm">
      <div className="flex items-center gap-2">
        <span className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium ${meta.cls}`}>
          {meta.label}
        </span>
        <h3 className="font-bold text-foreground">{block.title}</h3>
      </div>
      <p className="mt-3 text-[15px] leading-7 text-foreground/85">{block.body}</p>
    </article>
  );
}

export default async function LessonPage({ params }: Props) {
  const { id } = await params;
  const lesson = lessonMap[id];
  if (!lesson) notFound();

  const stage = stageMap[lesson.stage];

  return (
    <div>
      <section className="border-b border-border/70 bg-[radial-gradient(ellipse_at_top,rgba(44,107,94,0.08),transparent_60%)]">
        <div className="mx-auto max-w-4xl px-4 py-12 sm:px-6">
          <div className="flex items-center gap-2 text-sm text-muted-foreground">
            <Link href="/" className="hover:text-foreground">
              首页
            </Link>
            <span>/</span>
            <Link href={`/stage/${lesson.stage}`} className="hover:text-foreground">
              {stage.name}
            </Link>
            <span>/</span>
            <span className="text-foreground">{lesson.grade}</span>
          </div>
          <div className="mt-5 flex flex-wrap items-center gap-2">
            <span className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium ${stage.chip}`}>
              {stage.name} · {lesson.grade}
            </span>
            <span className="inline-flex items-center gap-1 rounded-full bg-muted px-2.5 py-0.5 text-xs font-medium text-muted-foreground">
              <Gauge className="h-3 w-3" />
              {difficultyLabel[lesson.difficulty]}
            </span>
            <span className="inline-flex items-center gap-1 rounded-full bg-muted px-2.5 py-0.5 text-xs font-medium text-muted-foreground">
              <Clock className="h-3 w-3" />
              约 {lesson.estimatedMinutes} 分钟
            </span>
          </div>
          <h1 className="mt-4 text-3xl font-extrabold tracking-tight text-foreground">
            {lesson.title}
          </h1>
          <p className="mt-3 text-base leading-7 text-muted-foreground">
            {lesson.brief}
          </p>
          <div className="mt-4 flex flex-wrap gap-1.5">
            {lesson.tags.map((t) => (
              <span key={t} className="rounded-md bg-muted px-2 py-0.5 text-xs text-muted-foreground">
                #{t}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* 原理动画：先看懂 */}
      <section className="mx-auto max-w-4xl px-4 pt-12 sm:px-6">
        <h2 className="flex items-center gap-2 text-xl font-bold text-foreground">
          <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-primary text-xs font-semibold text-primary-foreground">
            看
          </span>
          动画看懂原理
        </h2>
        <p className="mt-2 text-sm text-muted-foreground">
          先通过动画理解背后的数学原理，再进入文字讲解 —— 看得懂，才算真的会。
        </p>
        <div className="mt-6">
          <DemoBlock demo={lesson.demo} />
        </div>
      </section>

      {/* 知识点讲解 */}
      <section className="mx-auto max-w-4xl px-4 py-12 sm:px-6">
        <h2 className="flex items-center gap-2 text-xl font-bold text-foreground">
          <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-primary text-xs font-semibold text-primary-foreground">
            学
          </span>
          知识精讲
        </h2>
        <div className="mt-6 space-y-4">
          {lesson.knowledge.map((b, i) => (
            <Block key={i} block={b} />
          ))}
        </div>

        {/* 练习 */}
        <div className="mt-14">
          <h2 className="flex items-center gap-2 text-xl font-bold text-foreground">
            <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-primary text-xs font-semibold text-primary-foreground">
              练
            </span>
            随堂练习
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            选出正确答案，提交后即时查看解析与成绩。
          </p>
          <div className="mt-6">
            <Quiz questions={lesson.questions} />
          </div>
        </div>

        <div className="mt-12 flex justify-between border-t border-border/60 pt-6">
          <Link
            href={`/stage/${lesson.stage}`}
            className="inline-flex items-center gap-1.5 rounded-lg border border-border/70 bg-card px-4 py-2 text-sm font-medium text-foreground shadow-sm transition-colors hover:border-primary/40"
          >
            <ChevronLeft className="h-4 w-4" />
            返回{stage.name}
          </Link>
          <Link
            href="/"
            className="inline-flex items-center rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
          >
            学习更多
          </Link>
        </div>
      </section>
    </div>
  );
}