import FadeIn from './FadeIn'

const reviews = [
  {
    name: '陳經理',
    role: '科技業產品主管',
    rating: 5,
    text: '以前做一份提案簡報要花兩天，現在用課程裡的 AI 工作流，半天就搞定，而且說服力更強。這門課真的值回票價。',
  },
  {
    name: '李小姐',
    role: '新創公司行銷總監',
    rating: 5,
    text: '林柏源老師的 Prompt 型錄簡直是寶典。每個提示詞都能直接套用，再也不用花時間揣摩 AI 要怎麼下指令。',
  },
  {
    name: '王先生',
    role: '顧問公司資深顧問',
    rating: 5,
    text: '顧問級架構這個部分讓我大開眼界。我做了十年顧問，這套框架讓我重新審視自己的簡報邏輯，效果立竿見影。',
  },
]

export default function Reviews() {
  return (
    <section id="reviews" className="py-24 bg-black">
      <div className="max-w-5xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-14">
            <span className="section-badge mb-4">學員評價</span>
            <h2 className="text-3xl md:text-4xl font-heading text-white tracking-tight leading-[1.2] mt-4">
              他們都拿回了工作主導權
            </h2>
          </div>
        </FadeIn>

        <div className="grid md:grid-cols-3 gap-5">
          {reviews.map((r, i) => (
            <FadeIn key={i} delay={i * 0.1}>
              <div className="liquid-glass rounded-2xl p-6 h-full flex flex-col gap-4">
                {/* Stars */}
                <div className="flex gap-0.5">
                  {Array.from({ length: r.rating }).map((_, j) => (
                    <span key={j} className="text-yellow-400 text-sm">
                      ★
                    </span>
                  ))}
                </div>

                <p className="font-body font-light text-white/70 text-sm leading-relaxed flex-1">
                  「{r.text}」
                </p>

                <div className="flex items-center gap-3 pt-2 border-t border-white/5">
                  <div className="w-8 h-8 rounded-full liquid-glass flex items-center justify-center text-xs font-heading text-blue-400 font-bold">
                    {r.name[0]}
                  </div>
                  <div>
                    <p className="text-sm font-body font-medium text-white/80">
                      {r.name}
                    </p>
                    <p className="text-xs font-body text-white/40">{r.role}</p>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}
