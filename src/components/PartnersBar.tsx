import FadeIn from './FadeIn'

const partners = ['台灣微軟', '外貿協會', '文策院', '成功大學', '中龍鋼鐵']

export default function PartnersBar() {
  return (
    <section className="py-16 bg-black border-t border-white/5">
      <div className="max-w-5xl mx-auto px-6 flex flex-col items-center gap-8">
        <FadeIn>
          <span className="section-badge">講師曾授課於頂尖企業與機構</span>
        </FadeIn>

        <FadeIn delay={0.15}>
          <div className="flex flex-wrap items-center justify-center gap-x-12 gap-y-6">
            {partners.map((name) => (
              <span
                key={name}
                className="text-xl font-heading text-white/40 hover:text-white/65 transition-colors tracking-wider"
              >
                {name}
              </span>
            ))}
          </div>
        </FadeIn>
      </div>
    </section>
  )
}
