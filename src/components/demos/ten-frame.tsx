'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 凑十法：9 + 5 的十格框演示
// 用红色点表示已有的 9，蓝色点表示要加的 5；将 5 中的一个"借"去补齐 10。

const CELL = 52; // 格宽
const GAP = 8;
const X0 = 52;
const Y0 = 60;

function cellPos(i: number) {
  const row = Math.floor(i / 5);
  const col = i % 5;
  return { x: X0 + col * (CELL + GAP), y: Y0 + row * (CELL + GAP) };
}

function RedPoint({ i, step }: { i: number; step: number }) {
  const visible = step >= 1 && i < 9;
  const { x, y } = cellPos(i);
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          key={`r${i}`}
          initial={{ opacity: 0, scale: 0.3 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: (i % 5) * 0.08, type: 'spring', stiffness: 300, damping: 20 }}
          className="absolute flex h-10 w-10 items-center justify-center rounded-full bg-red-400 shadow-sm"
          style={{ left: x + 4, top: y + 4 }}
        >
          <span className="text-xs font-bold text-white">{i + 1}</span>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function BlueDots({ step }: { step: number }) {
  // 5 个蓝色点，当 step>=2 出现；step>=3 时第一个蓝点飞向补十格
  const dots = [0, 1, 2, 3, 4];
  const target = cellPos(9);
  return (
    <>
      {dots.map((j, idx) => {
        if (step < 2) return null;
        if (idx === 0 && step >= 3) {
          // 第一个蓝点飞入第 10 格，变为绿色"补齐"
          return (
            <motion.div
              key={`b${j}`}
              initial={{ left: X0 + idx * 60 + 4, top: Y0 + 180 + 4 }}
              animate={{ left: target.x + 4, top: target.y + 4 }}
              transition={{ duration: 0.9, delay: 0.2, ease: 'easeInOut' }}
              className={`absolute flex h-10 w-10 items-center justify-center rounded-full shadow-md ${
                step >= 4 ? 'bg-green-500' : 'bg-sky-400'
              }`}
            >
              <span className="text-xs font-bold text-white">
                {step >= 4 ? '10' : j + 1}
              </span>
            </motion.div>
          );
        }
        const x = X0 + idx * 60 + 4;
        const y = Y0 + 180 + 4;
        return (
          <motion.div
            key={`b${j}`}
            initial={{ opacity: 0, scale: 0.3 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: idx * 0.1, type: 'spring', stiffness: 300, damping: 20 }}
            className="absolute flex h-10 w-10 items-center justify-center rounded-full bg-sky-400 shadow-sm"
            style={{ left: x, top: y }}
          >
            <span className="text-xs font-bold text-white">{j + 1}</span>
          </motion.div>
        );
      })}
    </>
  );
}

function TenFrameScene({ step }: { step: number }) {
  return (
    <div className="relative mx-auto w-full max-w-sm">
      {/* 算式区 */}
      <div className="mb-4 text-center">
        <AnimatePresence mode="wait">
          <motion.span
            key={step}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-block rounded-lg bg-primary px-5 py-2 font-mono text-2xl font-bold text-primary-foreground"
          >
            {step >= 4 ? '9 + 5 = 14' : '9 + 5 = ?'}
          </motion.span>
        </AnimatePresence>
      </div>

      {/* 十格框 2 行 x 5 列 */}
      <div className="relative mx-auto h-[300px]">
        {/* 网格 */}
        {Array.from({ length: 10 }).map((_, i) => {
          const { x, y } = cellPos(i);
          return (
            <div
              key={i}
              className={`absolute rounded-lg border-2 transition-colors duration-300 ${
                i === 9 && step >= 3 ? 'border-green-500 bg-green-100/50' : 'border-black/25 bg-white/60'
              }`}
              style={{ left: x, top: y, width: CELL, height: CELL }}
            />
          );
        })}
        <RedPoint i={0} step={step} />
        <BlueDots step={step} />
        {/* 蓝点标签 */}
        <div className="absolute" style={{ left: X0, top: Y0 + 210 }}>
          <span className="text-xs font-medium text-muted-foreground">
            {step >= 2 ? '5 个（蓝色）：要加上的数' : ''}
          </span>
          {step >= 3 && (
            <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="ml-2 text-xs font-medium text-green-600">
              借 1 个补齐 10！
            </motion.span>
          )}
        </div>
      </div>
    </div>
  );
}

export function TenFrameDemo() {
  const steps = [
    '9 表示有 9 个一（红色点）。我们要算 9 + 5。',
    '5 表示再拿来 5 个一（蓝色点），排成一列。',
    '凑十法：从 5 个里借出 1 个，飞去补齐第 10 格，凑成一个完整的"十"。',
    '现在有 1 个"十"（绿色，代表 10），还剩下 4 个"一"（蓝色）。',
    '10 + 4 = 14，所以 9 + 5 = 14。凑十把难算的进位加，变成了简单的"十加几"。',
  ];
  return (
    <DemoPlayer title="凑十法：9 + 5 动画演示" steps={steps} autoDuration={2600}>
      {(step) => <TenFrameScene step={step} />}
    </DemoPlayer>
  );
}