'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { DemoPlayer } from './demo-player';

// 集合交集与并集：韦恩图

function VennScene({ step }: { step: number }) {
  // step0: A={1,2,3} B={2,3,4} ; step1: 交集 ; step2: 并集
  const showInter = step >= 1;
  const showUnion = step >= 2;
  return (
    <div className="mx-auto flex max-w-md flex-col items-center">
      <svg viewBox="0 0 320 220" className="w-full max-w-[300px]">
        <defs>
          <clipPath id="Aclip">
            <circle cx="125" cy="110" r="72" />
          </clipPath>
          <clipPath id="Bclip">
            <circle cx="195" cy="110" r="72" />
          </clipPath>
        </defs>
        {/* 并集阴影 */}
        {showUnion && (
          <g>
            <motion.circle
              cx="125" cy="110" r="72"
              initial={{ opacity: 0 }} animate={{ opacity: 1 }}
              fill="#e8813a55" stroke="none"
            />
            <motion.circle
              cx="195" cy="110" r="72"
              initial={{ opacity: 0 }} animate={{ opacity: 1 }}
              fill="#4f8fd655" stroke="none"
            />
          </g>
        )}
        {/* 交集高亮 */}
        {showInter && (
          <motion.path
            initial={{ opacity: 0 }} animate={{ opacity: 1 }}
            d="M125,38 a72,72 0 0,1 0,144 a72,72 0 0,1 0,-144 M195,38 a-72,72 0 0,0 0,144 a-72,72 0 0,0 0,-144"
            fill="#3a9d8c88"
            stroke="none"
          />
        )}
        {/* 集合边界 */}
        <circle cx="125" cy="110" r="72" fill="none" stroke="#e8813a" strokeWidth="2.5" />
        <circle cx="195" cy="110" r="72" fill="none" stroke="#4f8fd6" strokeWidth="2.5" />
        {/* 元素 */}
        {[
          { x: 75, y: 90, v: '1', c: '#e8813a' },
          { x: 95, y: 140, v: '2', c: '#3a9d8c' },
          { x: 135, y: 160, v: '3', c: '#3a9d8c' },
          { x: 185, y: 140, v: '4', c: '#4f8fd6' },
          { x: 220, y: 100, v: '5', c: '#4f8fd6' },
        ].map((e) => (
          <motion.g key={e.v}>
            <motion.circle cx={e.x} cy={e.y} r="16" fill="#fff" stroke={e.c} strokeWidth="2" />
            <text x={e.x} y={e.y + 4} textAnchor="middle" fontSize="13" fontWeight="bold" fill={e.c}>
              {e.v}
            </text>
          </motion.g>
        ))}
        <text x="60" y="30" fontSize="12" fill="#e8813a" fontWeight="bold">A</text>
        <text x="255" y="30" fontSize="12" fill="#4f8fd6" fontWeight="bold">B</text>
      </svg>

      <div className="mt-3 text-center">
        <AnimatePresence mode="wait">
          <motion.div
            key={step}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className="font-mono text-base font-bold text-foreground"
          >
            {step === 0 && 'A={1,2,3}  B={2,3,4}'}
            {step === 1 && 'A ∩ B = {2, 3}'}
            {step === 2 && 'A ∪ B = {1, 2, 3, 4, 5}'}
          </motion.div>
        </AnimatePresence>
        {showUnion && (
          <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mt-1 text-xs text-muted-foreground">
            并集取「属于 A 或属于 B」的所有元素，重复的只算一次。
          </motion.p>
        )}
      </div>
    </div>
  );
}

export function VennDemo() {
  const steps = [
    '集合 A = {1, 2, 3}，集合 B = {2, 3, 4, 5}。用两个圆表示它们。',
    '两个圆的公共部分（绿色）叫交集 A ∩ B，是既属于 A 又属于 B 的元素：{2, 3}。',
    '两个圆覆盖的全部区域叫并集 A ∪ B，属于 A 或属于 B 的都在里面：{1,2,3,4,5}。',
  ];
  return (
    <DemoPlayer title="集合的交集与并集" steps={steps} autoDuration={3200}>
      {(step) => <VennScene step={step} />}
    </DemoPlayer>
  );
}