export default function Navbar() {
  const links = [
    { label: '課程介紹', href: '#intro' },
    { label: '講師陣容', href: '#instructor' },
    { label: '核心亮點', href: '#features' },
    { label: '學員評價', href: '#reviews' },
  ]

  return (
    <nav className="fixed top-4 left-0 right-0 z-50 flex justify-center px-4">
      <div className="liquid-glass rounded-full px-6 py-3 flex items-center gap-6">
        {links.map((link) => (
          <a
            key={link.href}
            href={link.href}
            className="text-sm font-body text-white/90 hover:text-white transition-colors whitespace-nowrap hidden md:block"
          >
            {link.label}
          </a>
        ))}
        <a
          href="#cta"
          className="bg-blue-500 hover:bg-blue-400 text-white text-sm font-body font-medium rounded-full px-5 py-2 transition-colors whitespace-nowrap"
        >
          限時 45 折購課
        </a>
      </div>
    </nav>
  )
}
