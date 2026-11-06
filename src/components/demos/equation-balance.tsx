'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 解一元一次方程：2x + 3 = 11 的天平模型
// 把等式想象成天平，两边同时减去 3、再除以 2，天平保持平衡。

function BalanceScene({ step }: { step: number }) {
  // step 0: 2x+3 = 11 ; step1: 减3 ; step2: 2x=8 ; step3: 除以2 ; step4: x=4
  const leftBars = step >= 2 ? 2 : 2; // x 个数恒为 2
  const leftOnes = step >= 1 ? 0 : 3; // +3 在 step0 保留，step1 移除
  const rightOnes = step >= 1 ? 8 : 11; // 右侧方块数

  const beamTilt = step === 2 ? 0 : 0; // 平衡

  return (
    <div className="mx-auto max-w-md">
      {/* 天平 */}
      <div className="relative flex flex-col items-center">
        {/* 挂钩 + 横梁 */}
        <div className="relative h-3 w-72 rounded-full bg-primary" style={{ transform: `rotate(${beamTilt}deg)` }} />
        <div className="h-10 w-1.5 bg-primary" />

        <div className="mt-1 flex w-full items-end justify-between gap-4 px-2">
          {/* 左盘 */}
          <div className="flex min-h-[120px] flex-1 flex-col items-center justify-end rounded-lg border-2 border-primary/30 bg-card p-2">
            <div className="flex flex-wrap items-end justify-center gap-1">
              {Array.from({ length: leftBars }).map((_, i) => (
                <motion.div
                  key={`x${i}`}
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: 0.1 + i * 0.1, type: 'spring' }}
                  className="flex h-14 w-9 items-center justify-center rounded-md bg-red-400 font-mono text-sm font-bold text-white shadow"
                >
                  x
                </motion.div>
              ))}
              <AnimatePresence>
                {leftOnes > 0 && (
                  <motion.div
                    initial={{ opacity: 0, scale: 0 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0 }}
                    className="flex h-14 w-9 items-center justify-center rounded-md bg-amber-300 font-mono text-sm font-bold text-foreground shadow"
                  >
                    3
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
            <span className="mt-1 text-xs font-medium text-muted-foreground">
              {step >= 1 ? '2x' : '2x + 3'}
            </span>
          </div>

          {/* 右盘 */}
          <div className="flex min-h-[120px] flex-1 flex-col items-center justify-end rounded-lg border-2 border-primary/30 bg-card p-2">
            <div className="flex flex-wrap items-end justify-center gap-1">
              {Array.from({ length: rightOnes }).map((_, i) => (
                <motion.div
                  key={i}
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: i * 0.03, type: 'spring' }}
                  className="flex h-7 w-7 items-center justify-center rounded-md bg-sky-300 font-mono text-xs font-bold text-foreground shadow"
                >
                  1
                </motion.div>
              ))}
            </div>
            <span className="mt-1 text-xs font-medium text-muted-foreground">
              {rightOnes}
            </span>
          </div>
        </div>
      </div>

      {/* 步骤标注 */}
      <div className="mt-5 text-center">
        <AnimatePresence mode="wait">
          <motion.div
            key={step}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-block rounded-lg bg-muted px-4 py-2 font-mono text-lg font-bold text-foreground"
          >
            {['2x + 3 = 11', '两边同时 − 3', '2x = 8', '两边同时 ÷ 2', 'x = 4'][step]}
          </motion.div>
        </AnimatePresence>
        <AnimatePresence>
          {step >= 1 && step < 3 && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="mt-2 text-xs text-muted-foreground"
            >
              天平两边减去同样的重量，依然平衡 —— 这就是等式的性质。
            </motion.p>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}

export function EquationBalanceDemo() {
  const steps = [
    '把方程 2x + 3 = 11 想象成一架天平：左盘放 2 个 x 和 3，右盘放 11，两边平衡。',
    '要做的是"移项"。天平和等式一样：两边同时减去 3，依然平衡。',
    '3 被移到了右边变成 −3：2x = 11 − 3 = 8。',
    '两边再同时除以 2（权重减半），天平依然平衡。',
    '得到 x = 4。检验：2×4 + 3 = 11，成立！',
  ];
  return (
    <DemoPlayer title="一元一次方程：天平模型" steps={steps} autoDuration={3000}>
      {(step) => <BalanceScene step={step} />}
    </DemoPlayer>
  );
}