'use client';

import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GameLayout } from '@/components/games/game-layout';

// Block types: A=red(big 2x2, goal), B=vertical 1x2, C=horizontal 2x1, D=single 1x1
type BlockType = 'A' | 'B' | 'C' | 'D';
interface Block { id: string; type: BlockType; x: number; y: number; }

const TARGET = { x: 3, y: 4 }; // Red block exit row in 6×5 grid

const PUZZLES: { name: string; blocks: Block[] }[] = [
  {
    name: '横刀立马（入门）',
    blocks: [
      { id: 'A', type: 'A', x: 2, y: 0 },
      { id: 'B1', type: 'B', x: 0, y: 0 }, { id: 'B2', type: 'B', x: 4, y: 0 },
      { id: 'C1', type: 'C', x: 0, y: 2 }, { id: 'C2', type: 'C', x: 3, y: 2 },
      { id: 'D1', type: 'D', x: 2, y: 3 }, { id: 'D2', type: 'D', x: 3, y: 3 },
      { id: 'B3', type: 'B', x: 0, y: 3 }, { id: 'B4', type: 'B', x: 4, y: 3 },
    ],
  },
  {
    name: '兵临城下（进阶）',
    blocks: [
      { id: 'A', type: 'A', x: 2, y: 0 },
      { id: 'B1', type: 'B', x: 0, y: 0 }, { id: 'B2', type: 'B', x: 4, y: 0 },
      { id: 'C1', type: 'C', x: 0, y: 2 }, { id: 'C2', type: 'C', x: 3, y: 2 },
      { id: 'D1', type: 'D', x: 1, y: 2 }, { id: 'D2', type: 'D', x: 2, y: 3 },
      { id: 'B3', type: 'B', x: 0, y: 3 }, { id: 'B4', type: 'B', x: 4, y: 3 },
    ],
  },
  {
    name: '隔岸观火（挑战）',
    blocks: [
      { id: 'A', type: 'A', x: 2, y: 0 },
      { id: 'B1', type: 'B', x: 0, y: 0 }, { id: 'B2', type: 'B', x: 4, y: 0 },
      { id: 'C1', type: 'C', x: 0, y: 2 }, { id: 'C2', type: 'C', x: 3, y: 2 },
      { id: 'D1', type: 'D', x: 1, y: 2 }, { id: 'D2', type: 'D', x: 2, y: 3 },
      { id: 'B3', type: 'B', x: 0, y: 3 }, { id: 'B4', type: 'B', x: 4, y: 3 },
    ],
  },
];

const COLS = 5, ROWS = 6;
const CELL = 64;

export default function HuarongDaoPage() {
  const [puzzleIdx, setPuzzleIdx] = useState(0);
  const [blocks, setBlocks] = useState<Block[]>([]);
  const [moves, setMoves] = useState(0);
  const [won, setWon] = useState(false);
  const [selected, setSelected] = useState<string | null>(null);
  const [startScreen, setStartScreen] = useState(true);

  const startGame = useCallback((idx: number) => {
    const pb = PUZZLES[idx].blocks.map(b => ({ ...b }));
    setBlocks(pb);
    setMoves(0);
    setWon(false);
    setStartScreen(false);
    setSelected(null);
    setPuzzleIdx(idx);
  }, []);

  const getBlockSize = (type: BlockType): [number, number] => {
    if (type === 'A') return [2, 2];
    if (type === 'B') return [1, 2];
    if (type === 'C') return [2, 1];
    return [1, 1];
  };

  const canMove = useCallback((bl: Block, dx: number, dy: number): boolean => {
    const [w, h] = getBlockSize(bl.type);
    const nx = bl.x + dx, ny = bl.y + dy;
    if (nx < 0 || ny < 0 || nx + w > COLS || ny + h > ROWS) return false;
    const others = blocks.filter(b => b.id !== bl.id);
    for (const ob of others) {
      const [ow, oh] = getBlockSize(ob.type);
      if (nx < ob.x + ow && nx + w > ob.x && ny < ob.y + oh && ny + h > ob.y) return false;
    }
    return true;
  }, [blocks]);

  const tryMove = useCallback((dx: number, dy: number) => {
    if (won || !selected) return;
    const bl = blocks.find(b => b.id === selected);
    if (!bl || !canMove(bl, dx, dy)) return;
    setBlocks(prev => prev.map(b => b.id === selected ? { ...b, x: b.x + dx, y: b.y + dy } : b));
    setMoves(m => m + 1);
    const red = blocks.find(b => b.type === 'A')!;
    const moved = { ...red, x: red.x + dx, y: red.y + dy };
    if (moved.x === TARGET.x && moved.y === TARGET.y) setWon(true);
  }, [won, selected, blocks, canMove]);

  const renderCellBg = () => {
    const cells = [];
    for (let y = 0; y < ROWS; y++)
      for (let x = 0; x < COLS; x++)
        cells.push(
          <div key={`${x}-${y}`} className="border border-border/20" style={{ gridColumn: x + 1, gridRow: y + 1 }} />
        );
    return cells;
  };

  return (
    <GameLayout title="数学华容道" emoji="🧩" score={won ? { correct: 1, total: 1 } : undefined}>
      {startScreen ? (
        <div className="rounded-xl border border-border/70 bg-card p-8 text-center shadow-sm">
          <p className="mb-2 text-lg font-semibold text-foreground">华容道</p>
          <p className="mb-6 text-sm text-muted-foreground">拖动方块，把红色大方块从底部出口移出去！每次只能滑动一个方块到相邻空位。</p>
          <div className="space-y-2">
            {PUZZLES.map((p, i) => (
              <button key={i} onClick={() => startGame(i)}
                className="w-full rounded-lg border border-border/70 bg-card px-4 py-3 text-left text-sm font-medium text-foreground shadow-sm transition-colors hover:border-primary/40 hover:bg-primary/5">
                {p.name}
              </button>
            ))}
          </div>
        </div>
      ) : won ? (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="rounded-xl border border-primary/20 bg-primary/5 p-8 text-center shadow-sm">
          <div className="text-5xl mb-4">🎊</div>
          <h2 className="text-2xl font-extrabold text-foreground">成功逃脱！</h2>
          <p className="mt-2 text-sm text-muted-foreground">共移动 {moves} 步</p>
          <div className="mt-6 flex justify-center gap-3">
            {puzzleIdx > 0 && <button onClick={() => startGame(puzzleIdx - 1)} className="rounded-lg border border-border/70 bg-card px-4 py-2 text-sm font-semibold text-foreground shadow-sm hover:border-primary/40">上一关</button>}
            <button onClick={() => startGame(puzzleIdx)} className="rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">重玩本关</button>
            {puzzleIdx < PUZZLES.length - 1 && <button onClick={() => startGame(puzzleIdx + 1)} className="rounded-lg border border-border/70 bg-card px-4 py-2 text-sm font-semibold text-foreground shadow-sm hover:border-primary/40">下一关</button>}
          </div>
        </motion.div>
      ) : (
        <div className="flex flex-col items-center">
          <div className="mb-3 text-sm text-muted-foreground">步数：<strong className="text-foreground">{moves}</strong> · 拖拽方块将红色区域移出底部出口</div>
          <div className="relative" style={{ width: COLS * CELL, height: ROWS * CELL }}>
            {/* Grid */}
            <div className="absolute inset-0 grid" style={{ gridTemplateColumns: `repeat(${COLS}, ${CELL}px)`, gridTemplateRows: `repeat(${ROWS}, ${CELL}px)` }}>
              {renderCellBg()}
            </div>

            {/* Exit marker */}
            <div className="absolute bottom-0 left-0 right-0 flex justify-center">
              <div className="border-x-2 border-dashed border-primary/50 bg-primary/5" style={{ width: 2 * CELL, height: 4 }} />
            </div>

            {/* Blocks */}
            <AnimatePresence initial={false}>
              {blocks.map(bl => {
                const [bw, bh] = getBlockSize(bl.type);
                const isRed = bl.type === 'A';
                const isSelected = bl.id === selected;
                return (
                  <motion.div
                    key={bl.id}
                    drag={true}
                    dragConstraints={{ left: 0, right: (COLS - bw) * CELL, top: 0, bottom: (ROWS - bh) * CELL }}
                    dragElastic={0.1}
                    onDragEnd={(_, info) => {
                      const dx = Math.round(info.offset.x / CELL);
                      const dy = Math.round(info.offset.y / CELL);
                      if (dx !== 0 || dy !== 0) tryMove(dx, dy);
                    }}
                    whileTap={{ scale: 1.03 }}
                    animate={{ x: bl.x * CELL, y: bl.y * CELL }}
                    transition={{ type: 'spring', stiffness: 400, damping: 28 }}
                    className={`absolute cursor-grab rounded-lg border-2 shadow-sm ${
                      isRed
                        ? 'border-red-400 bg-red-500'
                        : isSelected
                        ? 'border-primary/60 bg-sky-400'
                        : 'border-sky-300 bg-sky-200'
                    }`}
                    style={{ width: bw * CELL - 4, height: bh * CELL - 4 }}
                  >
                    <div className="flex h-full items-center justify-center text-xs font-bold text-white/90">
                      {isRed ? '主公' : bl.type === 'B' ? '竖' : bl.type === 'C' ? '横' : ''}
                    </div>
                  </motion.div>
                );
              })}
            </AnimatePresence>
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={() => startGame(puzzleIdx)} className="rounded-lg border border-border/70 bg-card px-3 py-1.5 text-xs font-semibold text-foreground shadow-sm hover:border-primary/40">重置</button>
          </div>
        </div>
      )}
    </GameLayout>
  );
}
