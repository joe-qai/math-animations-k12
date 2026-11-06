import type { ComponentType } from 'react';
import { TenFrameDemo } from './ten-frame';
import { FractionPieDemo } from './fraction-pie';
import { EquationBalanceDemo } from './equation-balance';
import { LinearDemo } from './linear-function';
import { VennDemo } from './venn';
import { SineWaveDemo } from './sine-wave';

export type DemoKey =
  | 'ten-frame'
  | 'fraction-pie'
  | 'equation-balance'
  | 'linear-function'
  | 'venn'
  | 'sine-wave';

export const demoRegistry: Record<DemoKey, ComponentType> = {
  'ten-frame': TenFrameDemo,
  'fraction-pie': FractionPieDemo,
  'equation-balance': EquationBalanceDemo,
  'linear-function': LinearDemo,
  venn: VennDemo,
  'sine-wave': SineWaveDemo,
};