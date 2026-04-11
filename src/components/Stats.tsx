import FadeIn from './FadeIn'

const stats = [
  { value: '17個', label: '實戰單元' },
  { value: '146分鐘', label: '高濃度精華影音' },
  { value: '17份', label: '獨家課程簡報範本' },
  { value: '70%', label: '省下製作時間' },
]

export default function Stats() {
  return (
    <section className="py-24 bg-black border-t border-white/5">
      <div className="max-w-5xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-12">
            <span className="section-badge">課程規格</span>
          </div>
        </FadeIn>

        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 text-center">
          {stats.map((stat, i) => (
            <FadeIn key={i} delay={i * 0.1}>
              <div className="liquid-glass rounded-2xl py-8 px-4">
                <p className="text-4xl lg:text-5xl font-heading text-blue-400 font-bold tracking-tight">
                  {stat.value}
                </p>
                <p className="text-white/60 font-body text-sm mt-3">{stat.label}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}
