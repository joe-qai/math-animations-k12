import Link from 'next/link';
import { ArrowRight, Clock, Gauge } from 'lucide-react';
import type { Lesson } from '@/lib/data';

const difficultyLabel = ['', '基础', '进阶', '挑战'];

export function LessonCard({ lesson }: { lesson: Lesson }) {
  return (
    <Link
      href={`/lesson/${lesson.id}`}
      className="group flex flex-col rounded-xl border border-border/70 bg-card p-5 shadow-sm transition-all hover:-translate-y-0.5 hover:border-primary/40 hover:shadow-md"
    >
      <div className="flex items-center justify-between">
        <span className="inline-flex items-center rounded-full bg-muted px-2.5 py-0.5 text-xs font-medium text-muted-foreground">
          {lesson.grade}
        </span>
        <span className="inline-flex items-center gap-1 rounded-full bg-accent/50 px-2.5 py-0.5 text-xs font-medium text-accent-foreground">
          <Gauge className="h-3 w-3" />
          {difficultyLabel[lesson.difficulty]}
        </span>
      </div>
      <h3 className="mt-3 text-lg font-bold text-foreground transition-colors group-hover:text-primary">
        {lesson.title}
      </h3>
      <p className="mt-1.5 flex-1 text-sm leading-relaxed text-muted-foreground">
        {lesson.brief}
      </p>
      <div className="mt-4 flex items-center justify-between text-xs text-muted-foreground">
        <span className="inline-flex items-center gap-1">
          <Clock className="h-3.5 w-3.5" />
          约 {lesson.estimatedMinutes} 分钟
        </span>
        <span className="inline-flex items-center gap-1 font-medium text-primary">
          开始学习
          <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
        </span>
      </div>
    </Link>
  );
}