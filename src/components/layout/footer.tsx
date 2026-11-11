import Link from 'next/link';
import { stages } from '@/lib/data';

export function SiteFooter() {
  return (
    <footer className="border-t border-border/70 bg-card">
      <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6">
        <div className="grid gap-8 sm:grid-cols-3">
          <div>
            <div className="flex items-center gap-2">
              <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                <svg viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                  <path d="M4 19c5 0 5-14 10-14s4 14 9 14" />
                  <path d="M12 12l3 4 2-6" />
                </svg>
              </span>
              <span className="text-base font-bold">数益坊</span>
            </div>
            <p className="mt-3 max-w-xs text-sm leading-6 text-muted-foreground">
              面向 K12 中小学的数学学习园地，用清晰的讲解和即时的练习，让每道题都有迹可循。
            </p>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-foreground">学段导航</h4>
            <ul className="mt-3 space-y-2">
              {stages.map((s) => (
                <li key={s.id}>
                  <Link
                    href={`/stage/${s.id}`}
                    className="text-sm text-muted-foreground transition-colors hover:text-foreground"
                  >
                    {s.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-semibold text-foreground">数学游戏</h4>
            <ul className="mt-3 space-y-2">
              {[
                { label: '口算消消乐', href: '/games/arithmetic-match' },
                { label: '猜数迷', href: '/games/number-guess' },
                { label: '跳格子', href: '/games/hopscotch' },
                { label: '数独', href: '/games/sudoku' },
                { label: '华容道', href: '/games/huarongdao' },
              ].map(g => (
                <li key={g.label}>
                  <Link href={g.href} className="text-sm text-muted-foreground transition-colors hover:text-foreground">
                    {g.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <div className="mt-10 border-t border-border/60 pt-6 text-center text-xs text-muted-foreground">
          © {new Date().getFullYear()} 数益坊 · 让数学成为看得见的力量
        </div>
      </div>
    </footer>
  );
}