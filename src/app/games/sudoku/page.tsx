'use client';

import { useState, useCallback, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { GameLayout } from '@/components/games/game-layout';

type Difficulty = 'easy' | 'medium' | 'hard';

const CLS: Record<Difficulty, { label: string; remove: number; chip: string }> = {
  easy:   { label: '简单', remove: 30, chip: 'bg-emerald-100/70 text-emerald-700 border-emerald-300/60' },
  medium: { label: '中等', remove: 40, chip: 'bg-amber-100/70 text-amber-700 border-amber-300/60' },
  hard:   { label: '困难', remove: 50, chip: 'bg-red-100/70 text-red-700 border-red-300/60' },
};

function makeFullBoard(): number[][] {
  const board = Array.from({ length: 9 }, () => Array(9).fill(0));
  function solve(b: number[][]): boolean {
    for (let r = 0; r < 9; r++)
      for (let c = 0; c < 9; c++) {
        if (b[r][c] !== 0) continue;
        const nums = shuffle([...Array(9).keys()].map(i => i + 1));
        for (const n of nums) {
          if (isValid(b, r, c, n)) { b[r][c] = n; if (solve(b)) return true; b[r][c] = 0; }
        }
        return false;
      }
    return true;
  }
  function shuffle<T>(a: T[]): T[] { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function isValid(b: number[][], row: number, col: number, num: number): boolean {
    for (let i = 0; i < 9; i++) { if (b[row][i] === num || b[i][col] === num) return false; }
    const br = Math.floor(row / 3) * 3, bc = Math.floor(col / 3) * 3;
    for (let r = br; r < br + 3; r++) for (let c = bc; c < bc + 3; c++) if (b[r][c] === num) return false;
    return true;
  }
  solve(board);
  return board;
}

export default function SudokuPage() {
  const [difficulty, setDifficulty] = useState<Difficulty>('easy');
  const [puzzle, setPuzzle] = useState<number[][]>([]);
  const [board, setBoard] = useState<number[][]>([]);
  const [fixed, setFixed] = useState<boolean[][]>([]);
  const [selected, setSelected] = useState<[number, number] | null>(null);
  const [won, setWon] = useState(false);
  const [mistakes, setMistakes] = useState(0);
  const [startScreen, setStartScreen] = useState(true);
  const wonRef = useRef(false);
  const selectedRef = useRef<[number, number] | null>(null);
  const puzzleRef = useRef<number[][]>([]);
  const boardRef = useRef<number[][]>([]);
  const fixedRef = useRef<boolean[][]>([]);
  useEffect(() => { wonRef.current = won; }, [won]);
  useEffect(() => { selectedRef.current = selected; }, [selected]);
  useEffect(() => { puzzleRef.current = puzzle; }, [puzzle]);
  useEffect(() => { boardRef.current = board; }, [board]);
  useEffect(() => { fixedRef.current = fixed; }, [fixed]);

  const initGame = useCallback((diff: Difficulty) => {
    const full = makeFullBoard();
    const clone = full.map(r => [...r]);
    const toRemove = CLS[diff].remove;
    const fixedArr = Array.from({ length: 9 }, () => Array(9).fill(true));
    let removed = 0;
    while (removed < toRemove) {
      const r = Math.floor(Math.random() * 9), c = Math.floor(Math.random() * 9);
      if (clone[r][c] !== 0) { clone[r][c] = 0; fixedArr[r][c] = false; removed++; }
    }
    setPuzzle(clone.map(r => [...r]));
    setBoard(clone.map(r => [...r]));
    setFixed(fixedArr.map(r => [...r]));
    setSelected(null);
    setWon(false);
    setMistakes(0);
    setStartScreen(false);
  }, []);

  const checkWin = useCallback((b: number[][]) => {
    for (let r = 0; r < 9; r++) for (let c = 0; c < 9; c++) if (b[r][c] === 0) return false;
    return true;
  }, []);

  const handleNumClick = (num: number) => {
    if (!selected || won) return;
    const [r, c] = selected;
    if (fixed[r][c]) return;
    const newBoard = board.map(row => [...row]);
    newBoard[r][c] = num;
    setBoard(newBoard);
    if (num !== puzzle[r][c]) { setMistakes(m => m + 1); return; }
    if (checkWin(newBoard)) setWon(true);
  };

  const handleKey = useCallback((e: KeyboardEvent) => {
    if (wonRef.current || !selectedRef.current) return;
    const n = parseInt(e.key);
    if (n < 1 || n > 9) return;
    const [r, c] = selectedRef.current;
    if (puzzleRef.current[r][c] === n || fixedRef.current[r]?.[c]) return; // fixed cell — cannot edit
    const newBoard = boardRef.current.map(row => [...row]);
    newBoard[r][c] = n;
    setBoard(newBoard);
    if (n !== puzzleRef.current[r][c]) setMistakes(m => m + 1);
    else {
      const allFilled = newBoard.every(row => row.every(v => v !== 0));
      if (allFilled) setWon(true);
    }
  }, []);

  useEffect(() => { window.addEventListener('keydown', handleKey); return () => window.removeEventListener('keydown', handleKey); }, [handleKey]);

  return (
    <GameLayout title="数独" emoji="🔢" score={won ? { correct: 81 - mistakes, total: 81 } : undefined}>
      {startScreen ? (
        <div className="rounded-xl border border-border/70 bg-card p-8 text-center shadow-sm">
          <p className="mb-6 text-sm text-muted-foreground">在空格中填入 1~9，使每行、每列、每个 3×3 宫格均不重复。</p>
          <div className="flex justify-center gap-3">
            {(['easy', 'medium', 'hard'] as Difficulty[]).map(d => (
              <button key={d} onClick={() => setDifficulty(d)}
                className={`rounded-lg px-4 py-2 text-sm font-semibold transition-colors ${difficulty === d ? 'bg-primary text-primary-foreground' : 'border border-border/70 bg-card text-foreground hover:border-primary/40'}`}>
                {CLS[d].label}
              </button>
            ))}
          </div>
          <button onClick={() => initGame(difficulty)} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">开始游戏</button>
        </div>
      ) : won ? (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="rounded-xl border border-primary/20 bg-primary/5 p-8 text-center shadow-sm">
          <div className="text-5xl mb-4">🏆</div>
          <h2 className="text-2xl font-extrabold text-foreground">恭喜通关！</h2>
          <p className="mt-2 text-sm text-muted-foreground">错误 {mistakes} 次</p>
          <button onClick={() => setStartScreen(true)} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">再来一局</button>
        </motion.div>
      ) : (
        <div>
          <div className="mb-3 flex items-center justify-between text-sm text-muted-foreground">
            <span><span className={`inline-flex rounded-full border px-2 py-0.5 text-xs font-medium ${CLS[difficulty].chip}`}>{CLS[difficulty].label}</span></span>
            <span>错误 {mistakes} 次</span>
          </div>

          <div className="mx-auto flex justify-center">
            <div className="inline-grid grid-cols-9 rounded-xl border-2 border-primary/60 overflow-hidden shadow-md" style={{ width: 'min(100%, 405px)' }}>
              {board.map((row, ri) => row.map((cell, ci) => {
                const isFixed = fixed[ri]?.[ci];
                const isSelected = selected?.[0] === ri && selected?.[1] === ci;
                const isRelated = selected && (selected[0] === ri || selected[1] === ci ||
                  (Math.floor(selected[0] / 3) === Math.floor(ri / 3) && Math.floor(selected[1] / 3) === Math.floor(ci / 3)));
                const hasError = cell !== 0 && cell !== puzzle[ri][ci];
                const borderRight = ci === 2 || ci === 5 ? 'border-r-2 border-r-primary/40' : '';
                const borderBottom = ri === 2 || ri === 5 ? 'border-b-2 border-b-primary/40' : '';
                return (
                  <motion.button key={`${ri}-${ci}`} initial={false} animate={{
                    backgroundColor: isSelected ? 'rgb(44 107 94 / 0.2)' : hasError ? 'rgb(239 68 68 / 0.1)' : isRelated ? 'rgb(44 107 94 / 0.06)' : 'transparent',
                  }}
                    onClick={() => setSelected([ri, ci])}
                    className={`aspect-square flex items-center justify-center text-base font-semibold transition-colors ${isFixed ? 'font-bold text-foreground' : 'text-primary cursor-pointer'} ${borderRight} ${borderBottom}`}
                    style={{ fontSize: 'clamp(14px, 4vw, 20px)' }}
                  >
                    {cell || ''}
                  </motion.button>
                );
              }))}
            </div>
          </div>

          <div className="mt-4 flex justify-center gap-2">
            {[1, 2, 3, 4, 5, 6, 7, 8, 9].map(n => (
              <button key={n} onClick={() => handleNumClick(n)} disabled={won}
                className="h-10 w-10 rounded-lg border border-border/70 bg-card text-base font-bold text-foreground shadow-sm transition-all hover:border-primary/40 hover:bg-primary/5 disabled:opacity-40 active:scale-95">
                {n}
              </button>
            ))}
          </div>
          <p className="mt-2 text-center text-xs text-muted-foreground">点击格子后用数字键或下方按钮填入</p>
        </div>
      )}
    </GameLayout>
  );
}
