import Navbar from '@/components/Navbar'
import Hero from '@/components/Hero'
import PartnersBar from '@/components/PartnersBar'
import PainPoints from '@/components/PainPoints'
import FeaturesChess from '@/components/FeaturesChess'
import Instructor from '@/components/Instructor'
import Stats from '@/components/Stats'
import Reviews from '@/components/Reviews'
import CtaFooter from '@/components/CtaFooter'
import ImageGenerator from '@/components/ImageGenerator'

export default function App() {
  return (
    <main className="min-h-screen bg-black">
      <Navbar />
      <Hero />
      <PartnersBar />
      <PainPoints />
      <FeaturesChess />
      <ImageGenerator />
      <Instructor />
      <Stats />
      <Reviews />
      <CtaFooter />
    </main>
  )
}
