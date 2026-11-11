'use client';

import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GameLayout } from '@/components/games/game-layout';

type Difficulty = 'easy' | 'medium' | 'hard';

const CONFIG: Record<Difficulty, { digits: number; range: [number, number]; hintCount: number }> = {
  easy:   { digits: 3, range: [100, 999], hintCount: 3 },
  medium: { digits: 4, range: [1000, 9999], hintCount: 2 },
  hard:   { digits: 5, range: [10000, 99999], hintCount: 1 },
};

export default function NumberGuessPage() {
  const [difficulty, setDifficulty] = useState<Difficulty>('easy');
  const [secret, setSecret] = useState('');
  const [guesses, setGuesses] = useState<{ num: string; bulls: number; cows: number }[]>([]);
  const [input, setInput] = useState('');
  const [won, setWon] = useState(false);
  const [started, setStarted] = useState(false);
  const [hintsUsed, setHintsUsed] = useState(0);
  const [feedback, setFeedback] = useState<string>('');

  const genSecret = useCallback((digits: number) => {
    const arr = Array.from({ length: digits }, (_, i) => i);
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr.join('');
  }, []);

  const startGame = (diff: Difficulty) => {
    const cfg = CONFIG[diff];
    const s = genSecret(cfg.digits);
    setSecret(s);
    setGuesses([]);
    setInput('');
    setWon(false);
    setStarted(true);
    setHintsUsed(0);
    setFeedback(`猜一个 ${cfg.digits} 位数，每个数字不重复。牛=数字正确且位置对， cow=数字正确但位置不对。`);
    setDifficulty(diff);
  };

  const submitGuess = () => {
    const cfg = CONFIG[difficulty];
    if (input.length !== cfg.digits || new Set(input).size !== cfg.digits) {
      setFeedback('请输入不重复的指定位数数字！');
      return;
    }
    let bulls = 0, cows = 0;
    for (let i = 0; i < cfg.digits; i++) {
      if (input[i] === secret[i]) bulls++;
      else if (secret.includes(input[i])) cows++;
    }
    const newGuesses = [{ num: input, bulls, cows }];
    setGuesses(prev => [...prev, ...newGuesses]);
    setInput('');
    if (bulls === cfg.digits) {
      setWon(true);
      setFeedback(`🎉 猜对了！共用了 ${newGuesses.length} 次机会！`);
    } else {
      setFeedback(`${bulls} 头牛 ${cows} 只 cow`);
    }
  };

  const giveHint = () => {
    if (hintsUsed >= CONFIG[difficulty].hintCount) { setFeedback('提示次数已用完！'); return; }
    const pos = Math.floor(Math.random() * secret.length);
    setFeedback(`提示：第 ${pos + 1} 位是「${secret[pos]}」`);
    setHintsUsed(h => h + 1);
  };

  return (
    <GameLayout title="猜数迷" emoji="🔢" score={won ? { correct: guesses.length, total: 0 } : undefined}>
      {!started ? (
        <div className="rounded-xl border border-border/70 bg-card p-8 text-center shadow-sm">
          <p className="mb-2 text-lg font-semibold text-foreground">猜猜我心里想的数</p>
          <p className="mb-6 text-sm text-muted-foreground">我给一个数字，你来猜——每次猜测后我会告诉你几个数字位置和值都对（牛），几个数字对但位置错（cow）。</p>
          <div className="flex justify-center gap-3 mb-6">
            {(['easy', 'medium', 'hard'] as Difficulty[]).map(d => (
              <button key={d} onClick={() => setDifficulty(d)}
                className={`rounded-lg px-4 py-2 text-sm font-semibold transition-colors ${difficulty === d ? 'bg-primary text-primary-foreground' : 'border border-border/70 bg-card text-foreground hover:border-primary/40'}`}>
                {d === 'easy' ? '3 位数' : d === 'medium' ? '4 位数' : '5 位数'}
              </button>
            ))}
          </div>
          <button onClick={() => startGame(difficulty)} className="inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">开始游戏</button>
        </div>
      ) : won ? (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="rounded-xl border border-primary/20 bg-primary/5 p-8 text-center shadow-sm">
          <motion.div initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ type: 'spring', delay: 0.1 }} className="text-6xl mb-4">🎉</motion.div>
          <h2 className="text-2xl font-extrabold text-foreground">猜对了！</h2>
          <p className="mt-2 text-sm text-muted-foreground">答案是 <span className="font-mono font-bold text-primary">{secret}</span>，共用了 {guesses.length} 次机会</p>
          <button onClick={() => setStarted(false)} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">再来一局</button>
        </motion.div>
      ) : (
        <div>
          <div className="rounded-xl border border-border/70 bg-card p-4 shadow-sm mb-4">
            <p className="text-sm text-muted-foreground">{feedback}</p>
          </div>

          <div className="flex gap-2 mb-4">
            <input value={input} onChange={e => setInput(e.target.value.replace(/\D/g, '').slice(0, CONFIG[difficulty].digits))}
              onKeyDown={e => e.key === 'Enter' && submitGuess()}
              placeholder={`输入 ${CONFIG[difficulty].digits} 位数字`}
              className="flex-1 rounded-lg border border-border/70 bg-card px-4 py-2.5 text-center text-lg font-mono font-bold text-foreground outline-none focus:ring-2 focus:ring-primary/40"
              autoFocus
            />
            <button onClick={submitGuess} className="rounded-lg bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">提交</button>
          </div>

          <div className="flex justify-between mb-4">
            <button onClick={giveHint} disabled={hintsUsed >= CONFIG[difficulty].hintCount}
              className="rounded-lg border border-border/70 bg-card px-3 py-1.5 text-xs font-semibold text-foreground shadow-sm transition-colors hover:border-primary/40 disabled:cursor-not-allowed disabled:opacity-40">
              💡 提示 ({CONFIG[difficulty].hintCount - hintsUsed} 次剩余)
            </button>
            <button onClick={() => setStarted(false)} className="text-xs text-muted-foreground hover:text-foreground">重新开始</button>
          </div>

          <div className="space-y-2">
            <AnimatePresence initial={false}>
              {[...guesses].reverse().map((g, i) => (
                <motion.div key={i} initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} className="flex items-center justify-between rounded-lg border border-border/70 bg-card px-4 py-3">
                  <span className="font-mono text-lg font-bold text-foreground">{g.num}</span>
                  <div className="flex gap-3 text-sm">
                    <span className="text-emerald-600">🐂 {g.bulls}</span>
                    <span className="text-sky-600">🐄 {g.cows}</span>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
            {guesses.length === 0 && <p className="text-center text-sm text-muted-foreground">还没有猜测记录，快来试试吧！</p>}
          </div>
        </div>
      )}
    </GameLayout>
  );
}
