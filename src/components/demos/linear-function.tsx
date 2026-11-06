'use client';

import { motion } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 一次函数 y = 2x - 1 的图像：描点、连线
// 以下为像素坐标，点在直线 y = 150 - m(x-150) 上（m≈0.93），保证"点落在连线上"视觉一致。

const PTS: { px: number; py: number; label: string }[] = [
  { px: 50, py: 243, label: '(-2, ·)' },
  { px: 110, py: 187, label: '(-1, ·)' },
  { px: 150, py: 150, label: '(0,-1)' },
  { px: 190, py: 113, label: '(1, ·)' },
  { px: 250, py: 57, label: '(2, ·)' },
];

function LinearScene({ step }: { step: number }) {
  const showPoints = step >= 1;
  const showLine = step >= 2;
  const showTrend = step >= 3;
  const k = 2;
  const b = -1;

  return (
    <div className="mx-auto max-w-md">
      <div className="text-center">
        <motion.span
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-block rounded-lg bg-primary px-5 py-2 font-mono text-xl font-bold text-primary-foreground"
        >
          y = {k}x {b < 0 ? `− ${-b}` : `+ ${b}`}
        </motion.span>
      </div>

      <svg viewBox="0 0 300 300" className="mx-auto mt-4 w-full max-w-[280px]">
        {/* 坐标轴 */}
        <line x1="150" y1="10" x2="150" y2="290" stroke="#00000044" strokeWidth="1.5" />
        <line x1="10" y1="150" x2="290" y2="150" stroke="#00000044" strokeWidth="1.5" />
        {[-2, -1, 0, 1, 2].map((t) => (
          <g key={t}>
            <line x1={150 + t * 60 - 4} y1="150" x2={150 + t * 60 + 4} y2="150" stroke="#00000044" />
            <line x1="150" y1={150 - t * 60 - 4} x2="150" y2={150 - t * 60 + 4} stroke="#00000044" />
          </g>
        ))}
        <text x="285" y="165" fontSize="10" fill="#888">x</text>
        <text x="158" y="18" fontSize="10" fill="#888">y</text>

        {/* 直线 */}
        {showLine && (
          <motion.line
            x1="0"
            y1="290"
            x2="300"
            y2="10"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1, pathLength: 1 }}
            transition={{ duration: 0.8 }}
            stroke="#2c6b5e"
            strokeWidth="3"
            strokeLinecap="round"
          />
        )}
        {/* 描点 */}
        {showPoints &&
          PTS.map((p, i) => {
            const { px, py } = p;
            return (
              <g key={i}>
                <motion.circle
                  cx={px}
                  cy={py}
                  r="6"
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: i * 0.35, type: 'spring' }}
                  fill="#e8813a"
                />
                {/* 垂直虚线标注 y 随 x */}
                {showTrend && (
                  <motion.g key={`ln${i}`} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.15 }}>
                    <line x1={px} y1="150" x2={px} y2={py} stroke="#e8813a88" strokeDasharray="3 3" />
                    <line x1="150" y1={py} x2={px} y2={py} stroke="#e8813a88" strokeDasharray="3 3" />
                  </motion.g>
                )}
              </g>
            );
          })}
      </svg>

      <div className="mt-2 text-center">
        {showTrend && (
          <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-xs text-muted-foreground">
            k = 2 &gt; 0：x 每增大 1，y 增大 2 —— 图像从左下向右上倾斜。
          </motion.p>
        )}
      </div>
    </div>
  );
}

export function LinearDemo() {
  const steps = [
    '我们要画一次函数 y = 2x − 1 的图像。先取几个 x 值，算出对应的 y。',
    '把这些点描在坐标系上：(-2,-5)、(-1,-3)、(0,-1)、(1,1)、(2,3)。',
    '用一条直线把点连起来 —— 一次函数的图像就是一条直线。',
    '观察 k 的作用：k = 2 > 0，斜率是正的，y 随 x 增大而增大，直线向右上方倾斜。',
  ];
  return (
    <DemoPlayer title="一次函数：描点作图" steps={steps} autoDuration={2800}>
      {(step) => <LinearScene step={step} />}
    </DemoPlayer>
  );
}