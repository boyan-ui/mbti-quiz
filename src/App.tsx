import Navbar from '@/components/Navbar'
import Hero from '@/components/Hero'
import PartnersBar from '@/components/PartnersBar'
import PainPoints from '@/components/PainPoints'
import FeaturesChess from '@/components/FeaturesChess'
import Instructor from '@/components/Instructor'
import Stats from '@/components/Stats'
import Reviews from '@/components/Reviews'
import CtaFooter from '@/components/CtaFooter'

export default function App() {
  return (
    <main className="min-h-screen bg-black">
      <Navbar />
      <Hero />
      <PartnersBar />
      <PainPoints />
      <FeaturesChess />
      <Instructor />
      <Stats />
      <Reviews />
      <CtaFooter />
    </main>
  )
}
