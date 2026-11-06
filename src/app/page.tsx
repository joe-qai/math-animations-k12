import type { Metadata } from 'next';
import Link from 'next/link';
import { BookOpen, CheckCircle2, Lightbulb, PenLine, ThumbsUp } from 'lucide-react';
import { stages, lessons } from '@/lib/data';
import { LessonCard } from '@/components/lesson-card';

export const metadata: Metadata = {
  title: '首页',
  description: '数益坊 · K12 中小学数学学习网站',
};

export default function Home() {
  const featured = lessons.slice(0, 3);
  const totalLessons = lessons.length;

  return (
    <div>
      {/* Hero */}
      <section className="border-b border-border/70 bg-[radial-gradient(ellipse_at_top,rgba(44,107,94,0.08),transparent_60%)]">
        <div className="mx-auto max-w-6xl px-4 py-20 sm:px-6 sm:py-28">
          <span className="inline-flex items-center gap-1.5 rounded-full bg-accent/50 px-3 py-1 text-xs font-medium text-accent-foreground">
            <Lightbulb className="h-3.5 w-3.5" />
            覆盖小学 · 初中 · 高中
          </span>
          <h1 className="mt-6 max-w-3xl text-4xl font-extrabold leading-tight tracking-tight text-foreground sm:text-5xl">
            让每一道数学题，
            <br />
            <span className="text-primary">都有迹可循。</span>
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-8 text-muted-foreground">
            数益坊面向 K12 中小学生，按年级组织核心知识点。先读概念与公式，再看例题演算，
            最后用交互练习即时检验——完成「学 — 练 — 测」的完整闭环。
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Link
              href="#stages"
              className="inline-flex items-center gap-2 rounded-lg bg-primary px-5 py-3 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
            >
              <BookOpen className="h-4 w-4" />
              选择学段开始
            </Link>
            <Link
              href="#featured"
              className="inline-flex items-center gap-2 rounded-lg border border-border/70 bg-card px-5 py-3 text-sm font-semibold text-foreground shadow-sm transition-colors hover:border-primary/40"
            >
              浏览精选课时
            </Link>
          </div>
        </div>
      </section>

      {/* 学段入口 */}
      <section id="stages" className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <div className="flex items-end justify-between">
          <div>
            <h2 className="text-2xl font-bold text-foreground">选择学段</h2>
            <p className="mt-2 text-sm text-muted-foreground">
              循序渐进，找到适合你的切入点
            </p>
          </div>
        </div>
        <div className="mt-8 grid gap-6 sm:grid-cols-3">
          {stages.map((s) => (
            <Link
              key={s.id}
              href={`/stage/${s.id}`}
              className="group relative overflow-hidden rounded-2xl border border-border/70 bg-card p-7 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-lg"
            >
              <div className="flex items-center justify-between">
                <span className="text-4xl">{s.emoji}</span>
                <span className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-medium ${s.chip}`}>
                  点击进入 →
                </span>
              </div>
              <h3 className={`mt-5 text-xl font-bold ${s.color}`}>{s.name}</h3>
              <p className="mt-2 text-sm leading-6 text-muted-foreground">
                {s.tagline}
              </p>
              <div className="mt-4 flex flex-wrap gap-1.5">
                {s.grades.map((g) => (
                  <span
                    key={g.label}
                    className="rounded-md bg-muted px-2 py-0.5 text-xs text-muted-foreground"
                  >
                    {g.label}
                  </span>
                ))}
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* 学习方法 */}
      <section className="border-y border-border/70 bg-card/50">
        <div className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
          <h2 className="text-center text-2xl font-bold text-foreground">
            三步学习法
          </h2>
          <p className="mt-2 text-center text-sm text-muted-foreground">
            每一个课时都遵循同样的认知路径，重复带来熟稔
          </p>
          <div className="mt-10 grid gap-8 sm:grid-cols-3">
            {[
              {
                icon: BookOpen,
                step: '01',
                title: '读懂概念',
                desc: '用清晰的语言讲透每一个核心概念与公式的来源，先理解算理，再看结论。',
              },
              {
                icon: PenLine,
                step: '02',
                title: '演算例题',
                desc: '跟着例题一步步推演，在纸上动手验算，把方法变成自己的肌肉记忆。',
              },
              {
                icon: CheckCircle2,
                step: '03',
                title: '练习自测',
                desc: '完成交互练习，提交即得正误反馈与解析，针对性查漏补缺。',
              },
            ].map((f) => (
              <div key={f.step} className="text-center">
                <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                  <f.icon className="h-7 w-7" />
                </div>
                <div className="mt-4 text-xs font-semibold tracking-widest text-primary">
                  {f.step}
                </div>
                <h3 className="mt-1 text-lg font-bold text-foreground">{f.title}</h3>
                <p className="mt-2 text-sm leading-6 text-muted-foreground">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 精选课时 */}
      <section id="featured" className="mx-auto max-w-6xl px-4 py-16 sm:px-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-foreground">精选课时</h2>
            <p className="mt-2 text-sm text-muted-foreground">
              已开放 {totalLessons} 个高质量课时，持续更新中
            </p>
          </div>
          <Link
            href="/stage/xiaoxue"
            className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline"
          >
            查看全部
            <ThumbsUp className="h-4 w-4" />
          </Link>
        </div>
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {featured.map((l) => (
            <LessonCard key={l.id} lesson={l} />
          ))}
        </div>
      </section>
    </div>
  );
}