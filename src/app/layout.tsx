import type { Metadata } from 'next';
import './globals.css';
import { Header } from '@/components/layout/header';
import { SiteFooter } from '@/components/layout/footer';

export const metadata: Metadata = {
  title: {
    default: '数益坊 · K12 中小学数学学习',
    template: '%s · 数益坊',
  },
  description:
    '数益坊是面向 K12 中小学的数学学习网站，覆盖小学、初中、高中，按年级组织知识点讲解与交互练习，构建「学 — 练 — 测」的完整闭环。',
  keywords: [
    'K12 数学',
    '小学数学',
    '初中数学',
    '高中数学',
    '数学学习',
    '数学练习',
    '知识点',
    '在线学习',
  ],
  authors: [{ name: '数益坊' }],
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body className={`antialiased`}>
        <div className="flex min-h-screen flex-col">
          <Header />
          <main className="flex-1">{children}</main>
          <SiteFooter />
        </div>
      </body>
    </html>
  );
}
