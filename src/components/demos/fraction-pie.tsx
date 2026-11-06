'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 异分母分数加减：1/2 + 1/3，先把两个圆通分成六等份，再同加

function Pie({ fraction, color }: { fraction: [number, number]; color: string }) {
  const [num, den] = fraction;
  const R = 70;
  const cx = 90;
  const cy = 90;
  const sectors = Array.from({ length: den }, (_, i) => i < num);
  const angle = (i: number) => (i / den) * 360;
  return (
    <svg viewBox="0 0 180 180" className="h-full w-full">
      {sectors.map((on, i) => (
        <motion.path
          key={i}
          initial={{ opacity: 0 }}
          animate={{ opacity: on ? 1 : 0.18 }}
          transition={{ delay: i * 0.08 }}
          d={sectorPath(cx, cy, R, angle(i), angle(i + 1))}
          fill={on ? color : '#e5e5e5'}
          stroke="#fff"
          strokeWidth="1.5"
        />
      ))}
      <circle cx={cx} cy={cy} r={R} fill="none" stroke="#00000026" strokeWidth="1" />
    </svg>
  );
}

function sectorPath(cx: number, cy: number, r: number, a0: number, a1: number) {
  const rad = (a: number) => ((a - 90) * Math.PI) / 180;
  const x0 = cx + r * Math.cos(rad(a0));
  const y0 = cy + r * Math.sin(rad(a0));
  const x1 = cx + r * Math.cos(rad(a1));
  const y1 = cy + r * Math.sin(rad(a1));
  const large = a1 - a0 > 180 ? 1 : 0;
  return `M${cx} ${cy} L${x0} ${y0} A${r} ${r} 0 ${large} 1 ${x1} ${y1} Z`;
}

function FractionScene({ step }: { step: number }) {
  const den = step >= 1 ? 6 : 2;
  const num1 = step >= 1 ? 3 : 1; // 1/2 -> 3/6
  const num2 = step >= 1 ? 2 : 1; // 1/3 -> 2/6
  const showSum = step >= 3;
  const sumNum = 5;
  const sumDen = 6;
  return (
    <div className="grid grid-cols-1 items-center gap-6 sm:grid-cols-3">
      <div className="text-center">
        <div className="mx-auto aspect-square w-36">
          <Pie fraction={[num1, den]} color="#e8813a" />
        </div>
        <p className="mt-2 font-mono text-lg font-bold text-foreground">
          {step >= 1 ? '3/6' : '1/2'}
        </p>
      </div>
      <div className="text-center text-2xl font-bold text-muted-foreground">+</div>
      <div className="text-center">
        <div className="mx-auto aspect-square w-36">
          <Pie fraction={[num2, den]} color="#4f8fd6" />
        </div>
        <p className="mt-2 font-mono text-lg font-bold text-foreground">
          {step >= 1 ? '2/6' : '1/3'}
        </p>
      </div>

      {showSum && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="sm:col-span-3 mt-2 text-center"
        >
          <div className="mx-auto aspect-square w-28">
            <Pie fraction={[sumNum, sumDen]} color="#3a9d8c" />
          </div>
          <p className="mt-2 font-mono text-xl font-bold text-foreground">
            3/6 + 2/6 = 5/6
          </p>
          <AnimatePresence>
            {step >= 4 && (
              <motion.p
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="mt-1 text-xs text-muted-foreground"
              >
                通分后分母相同、分子直接相加 —— 这就是"同分母才能相加减"。
              </motion.p>
            )}
          </AnimatePresence>
        </motion.div>
      )}
    </div>
  );
}

export function FractionPieDemo() {
  const steps = [
    '计算 1/2 + 1/3。先把 1/2 看成一个圆的一半（橙色）。',
    '难点：分母不同不能直接加。我们把两个圆都切割成 6 等份 —— 1/2 = 3/6，1/3 = 2/6。',
    '蓝色圆取其中的 2 份，代表 2/6。',
    '现在分母相同了，直接相加：3/6 + 2/6 = 5/6。',
    '最后约分到最简（这里 5/6 已是最简）。答案就是 5/6。',
  ];
  return (
    <DemoPlayer
      title="分数加减的通分原理"
      steps={steps}
      autoDuration={3200}
    >
      {(step) => <FractionScene step={step} />}
    </DemoPlayer>
  );
}