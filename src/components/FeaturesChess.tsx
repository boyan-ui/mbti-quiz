import FadeIn from './FadeIn'
import PlaceholderImage from './PlaceholderImage'

const features = [
  {
    imageRight: true,
    tag: 'Feature 01',
    title: '專屬 AI 逆向工程機器人',
    description:
      '拆解神級簡報架構，只要輸入情境，專屬 AI 機器人一鍵幫你生成具備商業說服力的大綱與腳本。不再從空白頁面開始，讓 AI 成為你最懂你的簡報搭檔。',
    bullets: ['情境輸入一鍵生成', '商業說服架構', '自動腳本產出'],
    imageLabel: 'AI 機器人介面',
  },
  {
    imageRight: false,
    tag: 'Feature 02',
    title: '顧問級 Prompt 實戰型錄',
    description:
      '拒絕無效溝通！獨家整理的高效提示詞庫，讓你從資料搜集、圖表生成到排版建議，徹底釋放 AI 的強大產能。每一條 Prompt 都經過真實專案驗證。',
    bullets: ['資料搜集提示詞', '圖表生成指令', '排版優化建議'],
    imageLabel: 'Prompt 型錄介面',
  },
  {
    imageRight: true,
    tag: 'Feature 03',
    title: '17份即用專業簡報範本',
    description:
      '涵蓋提案、報告、策略規劃等多種情境的顧問級範本，直接套用即可呈現專業質感。告別從頭設計，讓每一份簡報都散發高階感。',
    bullets: ['提案簡報範本', '年度報告版型', '策略規劃框架'],
    imageLabel: '範本庫介面',
  },
]

export default function FeaturesChess() {
  return (
    <section id="features" className="py-24 bg-black">
      <div className="max-w-5xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-16">
            <span className="section-badge mb-4">核心亮點</span>
            <h2 className="text-3xl md:text-4xl font-heading text-white tracking-tight leading-[1.2] mt-4">
              給你的不只是一堂課，是一套實戰武器。
            </h2>
          </div>
        </FadeIn>

        <div className="flex flex-col gap-16">
          {features.map((feat, i) => (
            <FadeIn key={i} delay={0.1}>
              <div
                className={`grid md:grid-cols-2 gap-10 items-center ${
                  !feat.imageRight ? 'md:[&>*:first-child]:order-2' : ''
                }`}
              >
                {/* Text side */}
                <div className="flex flex-col gap-4">
                  <span className="text-xs font-body font-medium text-blue-400 tracking-widest uppercase">
                    {feat.tag}
                  </span>
                  <h3 className="text-2xl md:text-3xl font-heading text-white font-bold tracking-tight leading-[1.2]">
                    {feat.title}
                  </h3>
                  <p className="font-body font-light text-white/60 text-sm md:text-base leading-relaxed">
                    {feat.description}
                  </p>
                  <ul className="flex flex-col gap-2 mt-2">
                    {feat.bullets.map((b, j) => (
                      <li key={j} className="flex items-center gap-2">
                        <span className="w-1.5 h-1.5 rounded-full bg-blue-400 flex-shrink-0" />
                        <span className="font-body text-sm text-white/70">{b}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Image side */}
                <PlaceholderImage
                  className="aspect-[4/3]"
                  label={feat.imageLabel}
                />
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}
