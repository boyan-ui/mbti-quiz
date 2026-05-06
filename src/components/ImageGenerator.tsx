import { useState, useRef } from 'react'
import FadeIn from './FadeIn'

export default function ImageGenerator() {
  const [prompt, setPrompt] = useState('')
  const [imageUrl, setImageUrl] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const imgRef = useRef<HTMLImageElement>(null)

  function buildUrl(text: string) {
    const encoded = encodeURIComponent(text)
    return `https://image.pollinations.ai/prompt/${encoded}?width=1024&height=1024&nologo=true&seed=${Date.now()}`
  }

  function handleGenerate() {
    if (!prompt.trim()) return
    setError(null)
    setLoading(true)
    setImageUrl(null)
    const url = buildUrl(prompt.trim())
    setImageUrl(url)
  }

  function handleImageLoad() {
    setLoading(false)
  }

  function handleImageError() {
    setLoading(false)
    setError('圖片生成失敗，請稍後再試。')
    setImageUrl(null)
  }

  return (
    <section id="image-generator" className="py-24 bg-black">
      <div className="max-w-3xl mx-auto px-6">
        <FadeIn>
          <div className="text-center mb-10">
            <span className="section-badge mb-4">AI 繪圖</span>
            <h2 className="text-3xl md:text-4xl font-heading text-white tracking-tight leading-[1.2] mt-4">
              輸入描述，AI 幫你畫
            </h2>
            <p className="mt-4 font-body font-light text-white/60 text-sm md:text-base">
              輸入任何想像的畫面，AI 即時為你生成專屬圖片。
            </p>
          </div>
        </FadeIn>

        <FadeIn delay={0.1}>
          <div className="flex flex-col gap-4">
            <div className="flex gap-3">
              <input
                type="text"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleGenerate()}
                placeholder="例如：一隻會飛的貓咪在星空下"
                className="flex-1 rounded-xl bg-white/5 border border-white/10 px-4 py-3 text-sm font-body text-white placeholder:text-white/30 focus:outline-none focus:border-blue-500/60 transition-colors"
              />
              <button
                onClick={handleGenerate}
                disabled={loading || !prompt.trim()}
                className="liquid-glass-strong rounded-xl px-6 py-3 text-white font-body font-semibold text-sm hover:bg-white/10 transition-colors disabled:opacity-40 disabled:cursor-not-allowed whitespace-nowrap"
              >
                {loading ? '生成中…' : '生成圖片'}
              </button>
            </div>

            <div className="relative min-h-[420px] rounded-2xl liquid-glass flex items-center justify-center overflow-hidden">
              {!imageUrl && !loading && (
                <p className="font-body text-white/25 text-sm">圖片將在這裡顯示</p>
              )}

              {loading && (
                <div className="flex flex-col items-center gap-3">
                  <div className="w-8 h-8 border-2 border-blue-400 border-t-transparent rounded-full animate-spin" />
                  <p className="font-body text-white/50 text-sm">AI 正在創作中…</p>
                </div>
              )}

              {imageUrl && (
                <img
                  ref={imgRef}
                  src={imageUrl}
                  alt={prompt}
                  onLoad={handleImageLoad}
                  onError={handleImageError}
                  className={`w-full h-full object-contain transition-opacity duration-500 ${loading ? 'opacity-0 absolute' : 'opacity-100'}`}
                />
              )}

              {error && (
                <p className="font-body text-red-400 text-sm">{error}</p>
              )}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}
