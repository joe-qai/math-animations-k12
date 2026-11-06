import Link from 'next/link';
import { stages } from '@/lib/data';

export function Header() {
  return (
    <header className="sticky top-0 z-40 border-b border-border/70 bg-background/85 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6">
        <Link href="/" className="flex items-center gap-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary text-primary-foreground shadow-sm">
            <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
              <path d="M4 19c5 0 5-14 10-14s4 14 9 14" />
              <path d="M12 12l3 4 2-6" />
            </svg>
          </span>
          <span className="text-lg font-bold tracking-tight text-foreground">
            数益坊
          </span>
        </Link>
        <nav className="hidden items-center gap-1 sm:flex">
          {stages.map((s) => (
            <Link
              key={s.id}
              href={`/stage/${s.id}`}
              className="rounded-md px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-muted hover:text-foreground"
            >
              {s.name}
            </Link>
          ))}
        </nav>
        <Link
          href="/"
          className="rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-sm transition-colors hover:bg-primary/90"
        >
          开始学习
        </Link>
      </div>
    </header>
  );
}