import { ArrowRight } from 'lucide-react'
import BlurText from './BlurText'
import FadeIn from './FadeIn'

export default function Hero() {
  return (
    <section
      id="intro"
      className="relative min-h-[900px] flex items-center justify-center overflow-hidden bg-black"
      style={{ paddingTop: '150px', paddingBottom: '80px' }}
    >
      {/* Radial glow background */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 80% 60% at 50% 40%, rgba(30, 64, 175, 0.18) 0%, rgba(59, 130, 246, 0.06) 40%, transparent 70%)',
        }}
      />

      {/* Subtle grid overlay */}
      <div
        className="absolute inset-0 pointer-events-none opacity-[0.025]"
        style={{
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.5) 1px, transparent 1px)',
          backgroundSize: '60px 60px',
        }}
      />

      <div className="relative z-10 max-w-5xl mx-auto px-6 text-center flex flex-col items-center gap-6">
        {/* Badge pill */}
        <FadeIn delay={0.1}>
          <div className="liquid-glass rounded-full px-4 py-2 inline-flex items-center gap-2">
            <span className="bg-blue-500 text-white text-xs font-body font-semibold rounded-full px-2.5 py-0.5">
              熱銷中
            </span>
            <span className="text-sm font-body text-white/70">
              經理人・新商業學校
            </span>
          </div>
        </FadeIn>

        {/* Main heading with BlurText */}
        <h1 className="text-5xl md:text-7xl font-heading text-white font-bold tracking-tight leading-[1.2] mb-0">
          <BlurText text="AI 簡報極速工作流" delay={200} />
        </h1>

        {/* Sub-heading */}
        <FadeIn delay={0.5}>
          <h2 className="text-2xl md:text-3xl font-heading text-blue-400 tracking-tight leading-[1.2]">
            顧問級架構 ╳ 專業設計 ╳ 商業說服力
          </h2>
        </FadeIn>

        {/* Body text */}
        <FadeIn delay={0.65}>
          <p className="max-w-2xl font-body font-light text-white/70 text-sm md:text-base leading-relaxed">
            如果你總是花很多時間在做簡報，這堂課會幫你把時間與專業拿回來。省下 7
            成製作時間，把簡報變成真正能幫助你做決策的工具！
          </p>
        </FadeIn>

        {/* CTA buttons */}
        <FadeIn delay={0.8}>
          <div className="flex flex-col sm:flex-row items-center gap-4 mt-2">
            <a
              href="#cta"
              className="liquid-glass-strong rounded-full px-8 py-4 text-white font-body font-semibold text-base flex items-center gap-2 hover:bg-white/10 transition-colors group"
            >
              立即搶購 NT$2,069
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </a>
            <a
              href="#features"
              className="text-sm font-body text-white/50 hover:text-white/80 transition-colors"
            >
              了解課程內容 ↓
            </a>
          </div>
        </FadeIn>

        {/* Social proof numbers */}
        <FadeIn delay={0.95}>
          <div className="flex items-center gap-8 mt-4">
            <div className="text-center">
              <p className="text-2xl font-heading text-white font-bold">4,300+</p>
              <p className="text-xs font-body text-white/40 mt-0.5">學員已加入</p>
            </div>
            <div className="w-px h-10 bg-white/10" />
            <div className="text-center">
              <p className="text-2xl font-heading text-white font-bold">4.9★</p>
              <p className="text-xs font-body text-white/40 mt-0.5">課程評分</p>
            </div>
            <div className="w-px h-10 bg-white/10" />
            <div className="text-center">
              <p className="text-2xl font-heading text-white font-bold">70%</p>
              <p className="text-xs font-body text-white/40 mt-0.5">節省製作時間</p>
            </div>
          </div>
        </FadeIn>
      </div>

      {/* Bottom fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-black to-transparent pointer-events-none" />
    </section>
  )
}
