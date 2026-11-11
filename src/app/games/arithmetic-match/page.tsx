'use client';

import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GameLayout } from '@/components/games/game-layout';
import { Trophy, RefreshCcw } from 'lucide-react';

type Difficulty = 'easy' | 'medium' | 'hard';

interface Pair {
  id: number;
  expression: string;
  answer: number;
  matched: boolean;
}

const OPERATIONS: Record<Difficulty, { ops: string[]; maxNum: number }> = {
  easy:   { ops: ['+', '-'], maxNum: 20 },
  medium: { ops: ['+', '-', '×'], maxNum: 12 },
  hard:   { ops: ['+', '-', '×', '÷'], maxNum: 12 },
};

function generatePairs(difficulty: Difficulty): Pair[] {
  const { ops, maxNum } = OPERATIONS[difficulty];
  const count = difficulty === 'easy' ? 6 : difficulty === 'medium' ? 8 : 10;
  const pairs: Pair[] = [];

  for (let i = 0; i < count; i++) {
    const op = ops[Math.floor(Math.random() * ops.length)];
    let a: number, b: number, expr: string, answer: number;

    if (op === '+') {
      a = Math.floor(Math.random() * (maxNum - 1)) + 1;
      b = Math.floor(Math.random() * (maxNum - a)) + 1;
      expr = `${a} + ${b}`;
      answer = a + b;
    } else if (op === '-') {
      a = Math.floor(Math.random() * maxNum) + 1;
      b = Math.floor(Math.random() * a) + 1;
      expr = `${a} − ${b}`;
      answer = a - b;
    } else if (op === '×') {
      a = Math.floor(Math.random() * (maxNum - 1)) + 2;
      b = Math.floor(Math.random() * 9) + 2;
      expr = `${a} × ${b}`;
      answer = a * b;
    } else {
      b = Math.floor(Math.random() * 9) + 2;
      answer = Math.floor(Math.random() * (maxNum - 1)) + 1;
      a = b * answer;
      expr = `${a} ÷ ${b}`;
    }

    pairs.push({ id: i, expression: expr, answer, matched: false });
  }
  return pairs;
}

export default function ArithmeticMatchPage() {
  const [difficulty, setDifficulty] = useState<Difficulty>('easy');
  const [pairs, setPairs] = useState<Pair[]>([]);
  const [cards, setCards] = useState<{ id: number; text: string; type: 'expr' | 'ans'; pairId: number }[]>([]);
  const [selected, setSelected] = useState<number | null>(null);
  const [flipped, setFlipped] = useState<Set<number>>(new Set());
  const [correct, setCorrect] = useState(0);
  const [won, setWon] = useState(false);
  const [startScreen, setStartScreen] = useState(true);

  const initGame = useCallback((diff: Difficulty) => {
    const p = generatePairs(diff);
    setPairs(p);
    const items = p.flatMap(pair => [
      { id: pair.id * 2, text: pair.expression, type: 'expr' as const, pairId: pair.id },
      { id: pair.id * 2 + 1, text: String(pair.answer), type: 'ans' as const, pairId: pair.id },
    ]);
    // Fisher-Yates shuffle
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    setCards(items);
    setSelected(null);
    setFlipped(new Set());
    setCorrect(0);
    setWon(false);
    setStartScreen(false);
  }, []);

  const handleCardClick = (idx: number) => {
    if (won || flipped.has(idx) || cards[idx].type === 'expr' && selected !== null) return;

    const newFlipped = new Set(flipped);
    newFlipped.add(idx);
    setFlipped(newFlipped);

    if (selected === null) {
      setSelected(idx);
      return;
    }

    const first = cards[selected];
    const second = cards[idx];

    if (first.pairId === second.pairId) {
      setPairs(prev => prev.map(p => p.id === first.pairId ? { ...p, matched: true } : p));
      setCorrect(c => c + 1);
      setSelected(null);
      setFlipped(new Set());
      if (pairs.every(p => p.matched)) setWon(true);
    } else {
      setTimeout(() => {
        setFlipped(new Set());
        setSelected(null);
      }, 800);
    }
  };

  return (
    <GameLayout title="口算消消乐" emoji="🎯" score={won ? { correct: pairs.length, total: pairs.length } : undefined}>
      {startScreen ? (
        <div className="rounded-xl border border-border/70 bg-card p-8 text-center shadow-sm">
          <p className="mb-6 text-sm text-muted-foreground">点击匹配的算式与答案，消除所有卡片！</p>
          <div className="flex justify-center gap-3">
            {(['easy', 'medium', 'hard'] as Difficulty[]).map(d => (
              <button
                key={d}
                onClick={() => setDifficulty(d)}
                className={`rounded-lg px-4 py-2 text-sm font-semibold transition-colors ${
                  difficulty === d ? 'bg-primary text-primary-foreground' : 'border border-border/70 bg-card text-foreground hover:border-primary/40'
                }`}
              >
                {d === 'easy' ? '简单（加减）' : d === 'medium' ? '中等（加减乘）' : '困难（四则混合）'}
              </button>
            ))}
          </div>
          <button
            onClick={() => initGame(difficulty)}
            className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
          >
            开始游戏
          </button>
        </div>
      ) : won ? (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="rounded-xl border border-primary/20 bg-primary/5 p-8 text-center shadow-sm">
          <Trophy className="mx-auto h-16 w-16 text-accent" />
          <h2 className="mt-4 text-2xl font-extrabold text-foreground">全部消除！</h2>
          <p className="mt-2 text-sm text-muted-foreground">你已成功匹配所有算式！</p>
          <button onClick={() => setStartScreen(true)} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">
            <RefreshCcw className="h-4 w-4" /> 再来一局
          </button>
        </motion.div>
      ) : (
        <div className="grid grid-cols-4 gap-2.5 sm:grid-cols-5 md:grid-cols-6">
          <AnimatePresence>
            {cards.map((card, idx) => {
              const faceUp = flipped.has(idx);
              const isPairMatched = pairs[card.pairId]?.matched;
              return (
                <motion.button
                  key={idx}
                  initial={{ opacity: 0, rotateY: 90 }}
                  animate={{ opacity: isPairMatched ? 0 : 1, rotateY: faceUp ? 0 : 0, scale: isPairMatched ? 0.8 : 1 }}
                  exit={{ scale: 0, opacity: 0 }}
                  transition={{ duration: 0.2 }}
                  onClick={() => !isPairMatched && handleCardClick(idx)}
                  disabled={isPairMatched}
                  className={`aspect-square flex items-center justify-center rounded-xl text-base font-bold transition-all ${
                    isPairMatched
                      ? 'invisible'
                      : faceUp
                      ? 'bg-primary/10 text-primary shadow-md ring-2 ring-primary/40'
                      : 'bg-card border border-border/70 text-transparent hover:border-primary/40 cursor-pointer active:scale-95'
                  }`}
                  style={{ visibility: isPairMatched ? 'hidden' : 'visible' }}
                >
                  {faceUp ? card.text : '?'}
                </motion.button>
              );
            })}
          </AnimatePresence>
        </div>
      )}
    </GameLayout>
  );
}
