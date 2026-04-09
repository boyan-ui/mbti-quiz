import FadeIn from './FadeIn'

const painPoints = [
  {
    icon: '⏳',
    title: '花了大把時間，卻做出平庸簡報',
    desc: '不知道從哪裡下手，光是整理資料就耗掉半天，最後還是做出一份說不清楚的 PPT。',
  },
  {
    icon: '🤖',
    title: 'AI 生成的內容根本不能用',
    desc: '問了 ChatGPT 卻得到廢話連篇的回答，不知道怎麼下指令讓 AI 真正幫上忙。',
  },
  {
    icon: '📊',
    title: '缺乏商業邏輯與說服架構',
    desc: '簡報看起來很美，但老闆看完說不知所云。因為缺的不是設計，而是顧問級的思維框架。',
  },
  {
    icon: '🎨',
    title: '設計排版永遠不夠專業',
    desc: '花了很多力氣美化，還是感覺差那麼一口氣。不知道哪裡出了問題，只能一遍遍修改。',
  },
]

export default function PainPoints() {
  return (
    <section id="pain-points" className="py-24 bg-black">
      <div className="max-w-5xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-14">
            <span className="section-badge mb-4">為什麼你需要這堂課</span>
            <h2 className="text-3xl md:text-4xl font-heading text-white tracking-tight leading-[1.2] mt-4">
              明明用了 AI，<br className="md:hidden" />
              做簡報還是好花時間？
            </h2>
            <p className="mt-4 font-body font-light text-white/60 text-sm md:text-base max-w-xl mx-auto">
              AI 不是魔法，不懂架構與指令，只會產出不能用的廢話。
              我們教你真正實用的「極速工作流」。
            </p>
          </div>
        </FadeIn>

        <div className="grid md:grid-cols-2 gap-4">
          {painPoints.map((point, i) => (
            <FadeIn key={i} delay={i * 0.1}>
              <div className="liquid-glass rounded-2xl p-6 h-full">
                <div className="text-3xl mb-3">{point.icon}</div>
                <h3 className="font-heading text-white text-lg font-bold mb-2 tracking-tight leading-[1.2]">
                  {point.title}
                </h3>
                <p className="font-body font-light text-white/60 text-sm leading-relaxed">
                  {point.desc}
                </p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}
