'use client';

import Link from 'next/link';
import { ChevronLeft, RefreshCcw, Trophy, Clock } from 'lucide-react';

interface GameLayoutProps {
  title: string;
  emoji: string;
  backTo?: string;
  children: React.ReactNode;
  score?: { correct: number; total: number };
  timer?: number;
  onRestart?: () => void;
}

export function GameLayout({ title, emoji, backTo = '/games', children, score, timer, onRestart }: GameLayoutProps) {
  return (
    <div className="min-h-screen bg-background">
      <div className="mx-auto max-w-3xl px-4 py-6 sm:px-6">
        <Link href={backTo} className="inline-flex items-center gap-1 text-sm text-muted-foreground transition-colors hover:text-foreground">
          <ChevronLeft className="h-4 w-4" /> 返回游戏列表
        </Link>

        <div className="mt-4 flex items-center gap-3">
          <span className="text-3xl">{emoji}</span>
          <h1 className="text-2xl font-extrabold text-foreground">{title}</h1>
          {onRestart && (
            <button
              onClick={onRestart}
              className="ml-auto inline-flex items-center gap-1.5 rounded-lg border border-border/70 bg-card px-3 py-1.5 text-xs font-semibold text-foreground shadow-sm transition-colors hover:border-primary/40"
            >
              <RefreshCcw className="h-3.5 w-3.5" /> 重新开始
            </button>
          )}
        </div>

        {(score || timer !== undefined) && (
          <div className="mt-4 flex items-center gap-4 text-sm text-muted-foreground">
            {score && (
              <span className="inline-flex items-center gap-1">
                <Trophy className="h-4 w-4 text-accent" />
                {score.correct}/{score.total}
              </span>
            )}
            {timer !== undefined && (
              <span className="inline-flex items-center gap-1">
                <Clock className="h-4 w-4" />
                {timer}s
              </span>
            )}
          </div>
        )}

        <div className="mt-6">{children}</div>
      </div>
    </div>
  );
}
