'use client';

import { motion } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 正弦函数 y = sin x：单位圆投影出波形

function SineScene({ step }: { step: number }) {
  const trail = [0, 1, 2, 3, 4, 5, 6, 7, 8].filter((i) => step >= i / 2);
  const R = 40;
  return (
    <div className="mx-auto max-w-lg">
      <div className="text-center">
        <motion.span
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-block rounded-lg bg-primary px-5 py-2 font-mono text-2xl font-bold text-primary-foreground"
        >
          y = sin x
        </motion.span>
      </div>

      <svg viewBox="0 0 460 150" className="mx-auto mt-4 w-full">
        {/* 波形轴线 */}
        <line x1="20" y1="75" x2="450" y2="75" stroke="#00000040" strokeWidth="1.5" />

        {/* 单位圆（左）与正弦波（右） */}
        <circle cx="60" cy="75" r={R} fill="#e8813a22" stroke="#e8813a" strokeWidth="2" />
        <text x="60" y="140" fontSize="10" textAnchor="middle" fill="#888">单位圆</text>

        {/* 波形 x 轴（右移） */}
        <line x1="130" y1="75" x2="450" y2="75" stroke="#00000040" strokeWidth="0.5" />

        {/* trail 采样点 + 投影 */}
        {trail.map((t) => {
          const theta = (t / 8) * 2 * Math.PI;
          // 单位圆上的点
          const cxp = 60 + R * Math.cos(theta);
          const cyp = 75 - R * Math.sin(theta);
          // 波形上的点（向右展开一个周期 320px）
          const wx = 140 + (theta / (2 * Math.PI)) * 320;
          const wy = 75 - 40 * Math.sin(theta);
          return (
            <g key={t}>
              <motion.circle cx={cxp} cy={cyp} r="4" fill="#e8813a" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: t * 0.15 }} />
              <motion.line
                x1={cxp} y1={cyp} x2={wx} y2={cyp}
                initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: t * 0.15 }}
                stroke="#e8813a55" strokeDasharray="3 3"
              />
              <motion.circle cx={wx} cy={wy} r="4" fill="#2c6b5e" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: t * 0.15 + 0.1 }} />
            </g>
          );
        })}

        {/* 最终描出的正弦曲线 */}
        <motion.path
          d="M140,75 C150,20 175,10 180,15 C205,60 235,90 270,75 C305,60 330,20 340,5 C360,40 390,80 420,75 L460,75"
          fill="none"
          stroke="#2c6b5e"
          strokeWidth="2.5"
          strokeLinecap="round"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: 1 }}
          transition={{ duration: 1.2, delay: 0.3 }}
        />
        <text x="450" y="88" fontSize="10" fill="#888">x</text>
      </svg>

      <div className="mt-2 text-center text-xs text-muted-foreground">
        单位圆上半径转动一圈，竖坐标 y 的投影就是正弦值 —— 形成波浪形的周期函数。
      </div>
    </div>
  );
}

export function SineWaveDemo() {
  const steps = [
    '正弦函数 sin x 可以看成"单位圆上半径转动的竖坐标投影"。',
    '随着角度 θ 从 0 增大到 2π，圆上的点绕一整圈，竖坐标 sin θ 从 0 → 1 → 0 → −1 → 0。',
    '把每一步的竖坐标画在横轴上，连起来就是波浪形的正弦曲线。',
    '每转一圈（2π）就重复一次 —— 这就是周期 T = 2π 的含义。',
  ];
  return (
    <DemoPlayer title="正弦函数：单位圆与波形" steps={steps} autoDuration={3000}>
      {(step) => <SineScene step={step} />}
    </DemoPlayer>
  );
}