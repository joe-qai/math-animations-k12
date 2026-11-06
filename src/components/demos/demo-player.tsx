'use client';

import { useCallback, useEffect, useState, type ReactNode } from 'react';
import { Pause, Play, RefreshCcw, StepForward } from 'lucide-react';

interface DemoPlayerProps {
  title: string;
  steps: string[];
  children: (step: number) => ReactNode;
  /** 单步自动演示间隔 ms，0 表示不自动播放 */
  autoDuration?: number;
}

export function DemoPlayer({ title, steps, children, autoDuration = 0 }: DemoPlayerProps) {
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(autoDuration > 0);
  const total = steps.length;

  const reset = useCallback(() => {
    setPlaying(false);
    setStep(0);
  }, []);

  const next = useCallback(() => {
    setStep((s) => {
      if (s >= total - 1) {
        setPlaying(false);
        return s;
      }
      return s + 1;
    });
  }, [total]);

  useEffect(() => {
    if (!playing || autoDuration <= 0) return;
    if (step >= total - 1) {
      setPlaying(false);
      return;
    }
    const t = setTimeout(next, autoDuration);
    return () => clearTimeout(t);
  }, [playing, step, autoDuration, total, next]);

  return (
    <div className="overflow-hidden rounded-xl border border-border/70 bg-card shadow-sm">
      <div className="flex items-center gap-2 border-b border-border/60 bg-muted/40 px-4 py-3">
        <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-primary text-xs font-semibold text-primary-foreground">
          ▶
        </span>
        <h3 className="text-sm font-bold text-foreground">{title}</h3>
        <span className="ml-auto text-xs text-muted-foreground">
          {step + 1} / {total}
        </span>
      </div>

      <div className="p-4 sm:p-6">{children(step)}</div>

      {/* 步骤说明与进度 */}
      <div className="border-t border-border/60 px-4 py-3 sm:px-6">
        <p className="text-sm text-foreground/85">
          <span className="mr-1.5 inline-flex h-5 w-5 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary">
            {step + 1}
          </span>
          {steps[step]}
        </p>
        <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-muted">
          <div
            className="h-full rounded-full bg-primary transition-all duration-300"
            style={{ width: `${((step + 1) / total) * 100}%` }}
          />
        </div>
        <div className="mt-3 flex items-center gap-2">
          <button
            onClick={playing ? () => setPlaying(false) : () => setPlaying(true)}
            className="inline-flex items-center gap-1.5 rounded-lg bg-primary px-3 py-1.5 text-xs font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
          >
            {playing ? <Pause className="h-3.5 w-3.5" /> : <Play className="h-3.5 w-3.5" />}
            {playing ? '暂停' : '自动播放'}
          </button>
          <button
            onClick={next}
            disabled={step >= total - 1}
            className="inline-flex items-center gap-1.5 rounded-lg border border-border/70 bg-card px-3 py-1.5 text-xs font-semibold text-foreground shadow-sm transition-colors hover:border-primary/40 disabled:cursor-not-allowed disabled:opacity-40"
          >
            <StepForward className="h-3.5 w-3.5" />
            下一步
          </button>
          <button
            onClick={reset}
            className="ml-auto inline-flex items-center gap-1.5 rounded-lg border border-border/70 bg-card px-3 py-1.5 text-xs font-semibold text-foreground shadow-sm transition-colors hover:border-primary/40"
          >
            <RefreshCcw className="h-3.5 w-3.5" />
            重播
          </button>
        </div>
      </div>
    </div>
  );
}