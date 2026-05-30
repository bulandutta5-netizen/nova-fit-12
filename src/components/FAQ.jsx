import React, { useState } from 'react'
import { Sparkles, Plus, Minus } from 'lucide-react'

const faqData = [
  {
    q: 'Can I actually build muscle with home workouts alone, or do I need a gym membership?',
    a: '100%. While heavy barbells are great, muscles grow from tension and fatigue. Our Home Protocols use progressive calisthenics angles, high-intensity intervals, and mechanical disadvantage splits. Coach Nova teaches you how to force muscle hypertrophy with zero weights.'
  },
  {
    q: 'What if I have knee pain, a bad lower back, or shoulder issues?',
    a: 'Injury prevention and structural longevity are our top priorities. During setup, simply flag your joint limitations. Coach Nova instantly adapts your training split to replace high-impact loaded exercises with joint-friendly, spine-sparing alternatives (like swapping heavy back squats for goblet squats or single-leg bridges) so you can keep training safely.'
  },
  {
    q: 'Can the nutrition plans accommodate traditional Indian home-cooked meals?',
    a: 'Yes. We don\'t believe in forcing you to eat only plain chicken breast and broccoli. Our specialized Indian Diet Profile tracks macro-accurate options like dal, roti, paneer, chickpea curries, and basmati rice. Coach Nova calculates the exact portions to hit your daily protein targets without abandoning your family table.'
  },
  {
    q: 'How does the metabolic engine adjust when I hit a weight loss or muscle building plateau?',
    a: 'Metabolic adaptation is real. As you log your weekly weights and scale metrics in your dashboard, our engine tracks your exact progress rate. If your fat loss stalls or strength plateaus, Coach Nova dynamically shifts your daily calorie targets and macro splits by small, sustainable increments—mimicking a high-level human coach.'
  },
  {
    q: 'Do I need to buy expensive supplements like protein powders, creatine, or pre-workouts?',
    a: 'Absolutely not. Supplements are just the final 5% of the equation. We prioritize clean, whole foods first. If you want to optimize your recovery, Coach Nova will guide you on the science-backed basics (like whey isolate for convenience and creatine monohydrate for power), but we never push sponsored pills or unnecessary junk.'
  }
]

const FAQ = () => {
  const [openIdx, setOpenIdx] = useState(null)

  const toggleFAQ = (index) => {
    setOpenIdx((prev) => (prev === index ? null : index))
  }

  return (
    <section className="py-24 px-6 relative select-none">
      <div className="absolute bottom-10 left-10 w-96 h-96 bg-neonPurple/5 rounded-full blur-[100px] pointer-events-none -z-10" />

      <div className="max-w-4xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#9D00FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> FAQ
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            Got Questions? We've Got Real Answers.
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Everything you need to know about our science-backed training protocols, nutrition strategies, and coaching features.
          </p>
        </div>

        {/* FAQ Accordion Stack */}
        <div className="flex flex-col gap-4">
          {faqData.map((item, index) => {
            const isOpen = openIdx === index
            return (
              <div
                key={index}
                className="glass-panel rounded-2xl glow-border card-radial-blue overflow-hidden transition-all duration-300"
              >
                {/* Accordion Trigger Header */}
                <button
                  onClick={() => toggleFAQ(index)}
                  className="w-full flex items-center justify-between p-6 text-left focus:outline-none cursor-pointer"
                >
                  <span className="text-sm font-bold font-outfit text-white">
                    {item.q}
                  </span>
                  <span className={`p-1.5 rounded-lg bg-white/5 text-gray-400 transition-transform duration-300 ${isOpen ? 'rotate-18 rotate-180 text-white' : ''}`}>
                    {isOpen ? <Minus size={14} /> : <Plus size={14} />}
                  </span>
                </button>

                {/* Accordion Drawer Content */}
                <div
                  className={`transition-all duration-300 ease-in-out ${
                    isOpen ? 'max-h-[300px] border-t border-white/5 opacity-100' : 'max-h-0 opacity-0 pointer-events-none'
                  }`}
                >
                  <p className="p-6 text-xs text-gray-400 leading-relaxed font-semibold">
                    {item.a}
                  </p>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}

export default FAQ

