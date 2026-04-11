import { CheckCircle } from 'lucide-react'
import FadeIn from './FadeIn'

const achievements = [
  '突破 4,300 位學員的 AI 工作流人氣講師',
  '第 48 屆金鼎獎優良出版品獎得主',
  '全台第一個對話式 AI 領導教練打造者',
  '《經理人月刊》數位內容主編，深耕商業媒體逾十年',
  '橫跨台灣微軟、外貿協會、成功大學等頂尖機構授課',
]

export default function Instructor() {
  return (
    <section id="instructor" className="py-24 bg-black">
      <div className="max-w-5xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-10">
            <span className="section-badge mb-4">講師陣容</span>
          </div>
        </FadeIn>

        <FadeIn delay={0.15}>
          <div className="liquid-glass rounded-3xl p-10 md:p-14 max-w-4xl mx-auto">
            <div className="flex flex-col md:flex-row gap-10 items-start">
              {/* Avatar placeholder */}
              <div className="flex-shrink-0 flex flex-col items-center gap-4">
                <div
                  className="w-28 h-28 rounded-full liquid-glass flex items-center justify-center border border-white/10"
                  style={{
                    background:
                      'radial-gradient(circle, rgba(59,130,246,0.15) 0%, rgba(255,255,255,0.03) 100%)',
                  }}
                >
                  <span className="text-4xl font-heading text-blue-400 font-bold">
                    柏
                  </span>
                </div>
                <div className="text-center">
                  <p className="text-xs font-body text-white/40 tracking-wider">
                    INSTRUCTOR
                  </p>
                </div>
              </div>

              {/* Info */}
              <div className="flex-1">
                <h2 className="text-2xl md:text-3xl font-heading text-white font-bold tracking-tight leading-[1.2] mb-2">
                  林柏源
                </h2>
                <p className="font-body text-blue-400 text-sm font-medium mb-6 tracking-wide">
                  《經理人》數位內容主編
                </p>

                <ul className="flex flex-col gap-3">
                  {achievements.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <CheckCircle className="w-4 h-4 text-blue-400 flex-shrink-0 mt-0.5" />
                      <span className="font-body font-light text-white/70 text-sm leading-relaxed">
                        {item}
                      </span>
                    </li>
                  ))}
                </ul>

                {/* Quote */}
                <div className="mt-8 liquid-glass rounded-xl p-4 border-l-2 border-blue-500/50">
                  <p className="font-body font-light text-white/60 text-sm italic leading-relaxed">
                    「我設計這堂課，是因為我親眼看過太多聰明的人，花了太多時間在做沒有說服力的簡報。我想幫你把這些時間省下來，用在真正重要的事情上。」
                  </p>
                </div>
              </div>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}
