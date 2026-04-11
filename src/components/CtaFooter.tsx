import { ArrowRight } from 'lucide-react'
import FadeIn from './FadeIn'

export default function CtaFooter() {
  return (
    <section id="cta" className="py-32 bg-black relative overflow-hidden">
      {/* Glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 70% 50% at 50% 60%, rgba(30, 64, 175, 0.2) 0%, rgba(59,130,246,0.05) 50%, transparent 70%)',
        }}
      />

      <div className="relative z-10 max-w-3xl mx-auto px-6 text-center flex flex-col items-center gap-6">
        <FadeIn>
          <span className="section-badge">限時優惠</span>
        </FadeIn>

        <FadeIn delay={0.1}>
          <h2 className="text-3xl md:text-5xl font-heading text-white font-bold tracking-tight leading-[1.2]">
            將 AI 轉化為你的職場超能力
          </h2>
        </FadeIn>

        <FadeIn delay={0.2}>
          <p className="font-body font-light text-white/60 text-sm md:text-base leading-relaxed max-w-lg">
            原價 NT$4,599，限時 45 折優惠至 4/7。
            <br />
            馬上加入，拿回你的工作主導權！
          </p>
        </FadeIn>

        <FadeIn delay={0.3}>
          <div className="flex flex-col items-center gap-4 mt-2">
            <a
              href="#"
              className="bg-blue-600 hover:bg-blue-500 text-white rounded-full px-8 py-4 text-lg font-body font-bold transition-colors flex items-center gap-2 group"
            >
              解鎖極速工作流 (NT$ 2,069)
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </a>

            <div className="liquid-glass rounded-full px-5 py-2.5">
              <p className="font-body text-white/50 text-sm">
                Podcast 專屬折扣碼「
                <span className="text-blue-400 font-medium">AIwork</span>
                」再折 $400
              </p>
            </div>
          </div>
        </FadeIn>

        {/* Guarantee */}
        <FadeIn delay={0.4}>
          <div className="flex items-center gap-6 mt-4">
            <div className="flex items-center gap-2 text-white/30 text-xs font-body">
              <span>🔒</span>
              <span>安全付款</span>
            </div>
            <div className="flex items-center gap-2 text-white/30 text-xs font-body">
              <span>♾️</span>
              <span>終身觀看</span>
            </div>
            <div className="flex items-center gap-2 text-white/30 text-xs font-body">
              <span>📱</span>
              <span>手機可用</span>
            </div>
          </div>
        </FadeIn>
      </div>

      {/* Footer bottom */}
      <div className="mt-20 border-t border-white/5 pt-8 max-w-5xl mx-auto px-6">
        <p className="text-center font-body text-white/20 text-xs">
          © 2025 經理人・新商業學校｜AI 簡報極速工作流
        </p>
      </div>
    </section>
  )
}
