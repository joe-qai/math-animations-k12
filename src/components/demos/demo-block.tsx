import { demoRegistry, type DemoKey } from './index';

export function DemoBlock({ demo }: { demo: string }) {
  const Demo = demoRegistry[demo as DemoKey];
  if (!Demo) return null;
  return <Demo />;
}