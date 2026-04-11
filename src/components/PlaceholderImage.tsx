import { cn } from '@/lib/utils'

interface PlaceholderImageProps {
  className?: string
  label?: string
}

export default function PlaceholderImage({ className, label = 'Course Preview' }: PlaceholderImageProps) {
  return (
    <div
      className={cn(
        'liquid-glass rounded-2xl flex items-center justify-center overflow-hidden',
        className,
      )}
      style={{ minHeight: 280 }}
    >
      {/* Fake screenshot UI */}
      <div className="w-full h-full p-4 flex flex-col gap-3">
        {/* Fake window chrome */}
        <div className="flex items-center gap-1.5 mb-2">
          <div className="w-2.5 h-2.5 rounded-full bg-white/10" />
          <div className="w-2.5 h-2.5 rounded-full bg-white/10" />
          <div className="w-2.5 h-2.5 rounded-full bg-white/10" />
          <div className="flex-1 ml-2 h-4 rounded-full bg-white/5" />
        </div>
        {/* Fake slide content */}
        <div className="flex-1 rounded-xl bg-white/[0.02] border border-white/5 p-4 flex flex-col gap-3">
          <div className="h-3 rounded-full bg-blue-500/30 w-3/4" />
          <div className="h-2 rounded-full bg-white/10 w-full" />
          <div className="h-2 rounded-full bg-white/10 w-5/6" />
          <div className="h-2 rounded-full bg-white/10 w-4/6" />
          <div className="mt-2 grid grid-cols-3 gap-2">
            <div className="h-14 rounded-lg bg-blue-500/10 border border-blue-500/20" />
            <div className="h-14 rounded-lg bg-blue-500/10 border border-blue-500/20" />
            <div className="h-14 rounded-lg bg-blue-500/10 border border-blue-500/20" />
          </div>
          <div className="h-2 rounded-full bg-white/10 w-2/3 mt-1" />
        </div>
        <p className="text-xs font-body text-white/20 text-center">{label}</p>
      </div>
    </div>
  )
}
