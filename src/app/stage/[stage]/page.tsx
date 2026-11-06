import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { ChevronLeft } from 'lucide-react';
import { stageMap, lessonsByStage, type StageId } from '@/lib/data';
import { LessonCard } from '@/components/lesson-card';

interface Props {
  params: Promise<{ stage: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { stage } = await params;
  const s = stageMap[stage as StageId];
  return { title: s ? s.name : '学段' };
}

export default async function StagePage({ params }: Props) {
  const { stage } = await params;
  const s = stageMap[stage as StageId];
  if (!s) notFound();

  const list = lessonsByStage(s.id);

  // 按年级聚合
  const grouped: Record<string, typeof list> = {};
  for (const l of list) {
    (grouped[l.grade] = grouped[l.grade] || []).push(l);
  }

  return (
    <div>
      <section className={`border-b border-border/70 bg-gradient-to-b ${s.chip} bg-opacity-30`}>
        <div className="mx-auto max-w-6xl px-4 py-14 sm:px-6">
          <Link
            href="/"
            className="inline-flex items-center gap-1 text-sm text-muted-foreground transition-colors hover:text-foreground"
          >
            <ChevronLeft className="h-4 w-4" /> 返回首页
          </Link>
          <div className="mt-4 flex items-center gap-3">
            <span className="text-4xl">{s.emoji}</span>
            <div>
              <h1 className={`text-3xl font-extrabold tracking-tight ${s.color}`}>
                {s.name}
              </h1>
              <p className="mt-1 text-sm text-muted-foreground">{s.tagline}</p>
            </div>
          </div>
          <div className="mt-6 flex flex-wrap gap-2">
            {s.grades.map((g) => (
              <span
                key={g.label}
                className="rounded-lg border border-border/60 bg-background/70 px-3 py-1.5 text-xs text-foreground"
              >
                {g.label}
                <span className="ml-1.5 text-muted-foreground">{g.range}</span>
              </span>
            ))}
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-4 py-12 sm:px-6">
        {Object.entries(grouped).length === 0 ? (
          <div className="rounded-2xl border border-dashed border-border bg-card p-16 text-center">
            <p className="text-muted-foreground">
              该学段课时正在编写中，敬请期待。
            </p>
          </div>
        ) : (
          Object.entries(grouped).map(([grade, items]) => (
            <div key={grade} className="mb-10 last:mb-0">
              <div className="flex items-center gap-3">
                <h2 className="text-xl font-bold text-foreground">{grade}</h2>
                <div className="h-px flex-1 bg-border" />
                <span className="text-xs text-muted-foreground">
                  {items.length} 个课时
                </span>
              </div>
              <div className="mt-5 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {items.map((l) => (
                  <LessonCard key={l.id} lesson={l} />
                ))}
              </div>
            </div>
          ))
        )}
      </section>
    </div>
  );
}