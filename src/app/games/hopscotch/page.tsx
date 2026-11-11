'use client';

import { useState, useCallback, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GameLayout } from '@/components/games/game-layout';

const GRID_SIZE = 10;

interface Tile {
  x: number;
  y: number;
  value: number;
}

function generateTiles(count: number): Tile[] {
  const tiles: Tile[] = [];
  for (let i = 0; i < count; i++) {
    let x: number, y: number;
    do {
      x = Math.floor(Math.random() * GRID_SIZE);
      y = Math.floor(Math.random() * GRID_SIZE);
    } while (tiles.some(t => t.x === x && t.y === y));
    tiles.push({ x, y, value: i + 1 });
  }
  return tiles;
}

export default function HopscotchPage() {
  const [playerPos, setPlayerPos] = useState({ x: 0, y: 0 });
  const [targetValue, setTargetValue] = useState(1);
  const [tiles, setTiles] = useState<Tile[]>([]);
  const [score, setScore] = useState(0);
  const [moves, setMoves] = useState(0);
  const [won, setWon] = useState(false);
  const [startScreen, setStartScreen] = useState(true);
  const [countdown, setCountdown] = useState(30);
  const [gameActive, setGameActive] = useState(false);
  const [level, setLevel] = useState(1);

  const startGame = () => {
    const tileCount = 5 + level * 2;
    const newTiles = generateTiles(tileCount);
    // Place player on a tile near value 1
    const startTile = newTiles[0];
    setPlayerPos({ x: startTile.x, y: startTile.y });
    setTiles(newTiles);
    setTargetValue(1);
    setScore(0);
    setMoves(0);
    setWon(false);
    setStartScreen(false);
    setGameActive(true);
    setCountdown(30);
  };

  useEffect(() => {
    if (!gameActive || won) return;
    const timer = setInterval(() => {
      setCountdown(prev => {
        if (prev <= 1) { setGameActive(false); return 0; }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [gameActive, won]);

  const movePlayer = useCallback((dx: number, dy: number) => {
    if (!gameActive || won) return;
    const nx = playerPos.x + dx;
    const ny = playerPos.y + dy;
    if (nx < 0 || nx >= GRID_SIZE || ny < 0 || ny >= GRID_SIZE) return;

    setPlayerPos(p => ({ x: nx, y: ny }));
    const newMoves = moves + 1;
    setMoves(newMoves);

    const tile = tiles.find(t => t.x === nx && t.y === ny);
    if (tile) {
      if (tile.value === targetValue) {
        setScore(s => s + tile.value * 10);
        const nextVal = targetValue + 1;
        if (nextVal > tiles.length) {
          setWon(true);
          setGameActive(false);
          setLevel(l => l + 1);
        } else {
          setTargetValue(nextVal);
        }
      }
    }
  }, [gameActive, won, playerPos, tiles, targetValue, moves]);

  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === 'ArrowUp') movePlayer(0, -1);
      else if (e.key === 'ArrowDown') movePlayer(0, 1);
      else if (e.key === 'ArrowLeft') movePlayer(-1, 0);
      else if (e.key === 'ArrowRight') movePlayer(1, 0);
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [movePlayer]);

  const CELL = 56;

  return (
    <GameLayout title="跳格子" emoji="🦘" score={won ? { correct: tiles.length, total: tiles.length } : undefined} timer={gameActive ? countdown : undefined}>
      {startScreen ? (
        <div className="rounded-xl border border-border/70 bg-card p-8 text-center shadow-sm">
          <p className="mb-4 text-lg font-semibold text-foreground">跳格子</p>
          <p className="mb-6 text-sm text-muted-foreground">用方向键控制角色跳到标有数字的格子上，按顺序踩完所有格子！</p>
          <button onClick={startGame} className="inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">开始游戏</button>
        </div>
      ) : !gameActive && won ? (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="rounded-xl border border-primary/20 bg-primary/5 p-8 text-center shadow-sm">
          <div className="text-5xl mb-4">🎉</div>
          <h2 className="text-2xl font-extrabold text-foreground">关卡完成！</h2>
          <p className="mt-2 text-sm text-muted-foreground">用了 {moves} 步，得分 {score}</p>
          <button onClick={startGame} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">下一关</button>
        </motion.div>
      ) : !gameActive && countdown === 0 ? (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="rounded-xl border border-destructive/20 bg-destructive/5 p-8 text-center shadow-sm">
          <div className="text-5xl mb-4">⏰</div>
          <h2 className="text-2xl font-extrabold text-foreground">时间到！</h2>
          <p className="mt-2 text-sm text-muted-foreground">得分 {score}，跳了 {moves} 步</p>
          <button onClick={startGame} className="mt-6 inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm hover:bg-primary/90">再试一次</button>
        </motion.div>
      ) : (
        <div>
          <div className="mb-3 flex items-center justify-between text-sm text-muted-foreground">
            <span>目标：踩到数字 <strong className="text-foreground">{targetValue}</strong></span>
            <span>得分 {score} · 步数 {moves}</span>
          </div>
          <div className="mx-auto flex justify-center">
            <div className="relative overflow-hidden rounded-xl border border-border/70 bg-card shadow-sm" style={{ width: GRID_SIZE * CELL, height: GRID_SIZE * CELL }}>
              {/* Grid lines */}
              {Array.from({ length: GRID_SIZE }).map((_, i) => (
                <div key={`g${i}`} className="absolute bg-border/30" style={{ left: i * CELL, top: 0, width: 1, height: GRID_SIZE * CELL }} />
              ))}
              {Array.from({ length: GRID_SIZE }).map((_, i) => (
                <div key={`gH${i}`} className="absolute bg-border/30" style={{ top: i * CELL, left: 0, height: 1, width: GRID_SIZE * CELL }} />
              ))}

              {/* Tiles */}
              {tiles.map(tile => (
                <motion.div key={tile.value} initial={{ scale: 0 }} animate={{ scale: 1 }}
                  className={`absolute flex items-center justify-center rounded-lg font-bold text-white ${
                    tile.value === targetValue ? 'bg-accent text-accent-foreground ring-2 ring-accent' : 'bg-primary/80'
                  }`}
                  style={{ left: tile.x * CELL + 4, top: tile.y * CELL + 4, width: CELL - 8, height: CELL - 8, fontSize: 14 }}
                >
                  {tile.value}
                </motion.div>
              ))}

              {/* Player */}
              <AnimatePresence>
                <motion.div
                  key={`${playerPos.x}-${playerPos.y}`}
                  initial={false}
                  animate={{ left: playerPos.x * CELL + 8, top: playerPos.y * CELL + 8 }}
                  transition={{ type: 'spring', stiffness: 300, damping: 25 }}
                  className="absolute z-10 flex h-7 w-7 items-center justify-center rounded-full bg-red-500 text-xs font-bold text-white shadow-md"
                >
                  ●
                </motion.div>
              </AnimatePresence>
            </div>
          </div>
          <p className="mt-3 text-center text-xs text-muted-foreground">用 ↑ ↓ ← → 方向键移动</p>
        </div>
      )}
    </GameLayout>
  );
}
