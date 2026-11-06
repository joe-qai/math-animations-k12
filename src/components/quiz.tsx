'use client';

import { useState } from 'react';
import { CheckCircle2, RotateCcw, XCircle } from 'lucide-react';
import type { QuizQuestion } from '@/lib/data';

export function Quiz({ questions }: { questions: QuizQuestion[] }) {
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [answers, setAnswers] = useState<Record<string, boolean>>({});

  const q = questions[current];
  const answered = selected !== null;
  const isCorrect = answered && selected === q.answer;

  function choose(idx: number) {
    if (answered) return;
    setSelected(idx);
    setAnswers((prev) => ({ ...prev, [q.id]: idx === q.answer }));
  }

  function next() {
    setSelected(null);
    setCurrent((c) => c + 1);
  }

  function reset() {
    setSelected(null);
    setCurrent(0);
    setAnswers({});
  }

  const correctCount = Object.values(answers).filter(Boolean).length;
  const done = current === questions.length;

  if (done) {
    const score = Math.round((correctCount / questions.length) * 100);
    const passed = score >= 60;
    return (
      <div className="rounded-xl border border-border/70 bg-card p-6 text-center shadow-sm">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-primary/10">
          {passed ? (
            <CheckCircle2 className="h-9 w-9 text-primary" />
          ) : (
            <XCircle className="h-9 w-9 text-destructive" />
          )}
        </div>
        <h3 className="mt-4 text-xl font-bold text-foreground">
          {passed ? '做得不错！' : '继续加油！'}
        </h3>
        <p className="mt-2 text-sm text-muted-foreground">
          共 {questions.length} 题，答对 {correctCount} 题，正确率 {score}%。
        </p>
        <p className="mt-1 text-xs text-muted-foreground">
          {passed
            ? '已掌握本节核心，可进入下一课时。'
            : '建议回到知识点部分温习后再试一次。'}
        </p>
        <button
          onClick={reset}
          className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
        >
          <RotateCcw className="h-4 w-4" />
          再练一次
        </button>
      </div>
    );
  }

  return (
    <div className="rounded-xl border border-border/70 bg-card p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium text-muted-foreground">
          第 {current + 1} / {questions.length} 题
        </span>
        <span className="text-xs text-muted-foreground">
          已答对 {correctCount} 题
        </span>
      </div>

      <div className="mt-2 h-1.5 overflow-hidden rounded-full bg-muted">
        <div
          className="h-full rounded-full bg-primary transition-all duration-300"
          style={{ width: `${((current + (answered ? 1 : 0)) / questions.length) * 100}%` }}
        />
      </div>

      <h3 className="mt-5 text-lg font-semibold text-foreground">{q.prompt}</h3>

      <div className="mt-4 space-y-2.5">
        {q.options.map((opt, idx) => {
          const isAns = idx === q.answer;
          let cls =
            'border-border/70 bg-card hover:border-primary/50 hover:bg-muted/50';
          if (answered) {
            if (isAns) cls = 'border-primary/60 bg-primary/10 text-primary';
            else if (idx === selected)
              cls = 'border-destructive/60 bg-destructive/10 text-destructive';
            else cls = 'border-border/70 bg-card opacity-60';
          }
          return (
            <button
              key={idx}
              onClick={() => choose(idx)}
              disabled={answered}
              className={`flex w-full items-center gap-3 rounded-lg border px-4 py-3 text-left text-sm transition-all ${cls}`}
            >
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-muted text-xs font-semibold text-muted-foreground">
                {'ABCD'[idx]}
              </span>
              {opt}
              {answered && isAns && (
                <CheckCircle2 className="ml-auto h-4 w-4 shrink-0 text-primary" />
              )}
              {answered && idx === selected && !isAns && (
                <XCircle className="ml-auto h-4 w-4 shrink-0 text-destructive" />
              )}
            </button>
          );
        })}
      </div>

      {answered && (
        <div className="mt-4 flex items-start gap-2 rounded-lg border border-primary/20 bg-primary/5 p-3 text-sm text-foreground">
          <span className="mt-0.5 shrink-0 font-semibold text-primary">
            解析
          </span>
          <span className="leading-relaxed">{q.explanation}</span>
        </div>
      )}

      {answered && current < questions.length - 1 && (
        <button
          onClick={next}
          className="mt-4 w-full rounded-lg bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
        >
          下一题
        </button>
      )}
      {answered && current === questions.length - 1 && (
        <button
          onClick={next}
          className="mt-4 w-full rounded-lg bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
        >
          查看成绩
        </button>
      )}
    </div>
  );
}