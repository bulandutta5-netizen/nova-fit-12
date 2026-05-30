import React, { useState } from 'react'
import { Sparkles, ChevronLeft, ChevronRight, Star, Quote } from 'lucide-react'

const testimonials = [
  {
    name: 'Rohan Mehta',
    role: 'Busy Tech Lead',
    tag: '12-Week Recomp',
    stat: '-12kg Fat / +3.5kg Lean Muscle',
    text: "As a tech lead sitting 10+ hours a day, I'd completely lost control of my health. Nova's calorie calculations and dal/roti tracking fit right into my Indian household meals without stress. Replaced my expensive gym trainer and got me down to 14% body fat. Unbelievable accuracy.",
    rating: 5,
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=120&h=120'
  },
  {
    name: 'Pooja Krishnan',
    role: 'Working Mom',
    tag: 'Home Calisthenics Blueprint',
    stat: '24% → 17% Body Fat',
    text: "I couldn't make it to a commercial gym with two toddlers. Nova set me up with a zero-equipment home calisthenics routine that actually progressively overloaded. The chatbot kept me accountable every single evening when my motivation dipped. My joints feel bulletproof.",
    rating: 5,
    avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=120&h=120'
  },
  {
    name: 'Karan Malhotra',
    role: 'Competitive Powerlifter',
    tag: 'Powerbuilding Split',
    stat: 'Bench +20kg / Squat +35kg',
    text: "I was skeptical about AI for powerlifting, but the math under the hood is extremely solid. The metabolic engine helped me run a calculated lean bulk to scale up to the 83kg class without gaining excess fat. Nova's recovery tracking and fatigue feedback are a game changer.",
    rating: 5,
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=120&h=120'
  }
]

const Testimonials = () => {
  const [activeIdx, setActiveIdx] = useState(0)

  const handlePrev = () => {
    setActiveIdx((prev) => (prev === 0 ? testimonials.length - 1 : prev - 1))
  }

  const handleNext = () => {
    setActiveIdx((prev) => (prev === testimonials.length - 1 ? 0 : prev + 1))
  }

  const active = testimonials[activeIdx]

  return (
    <section className="py-24 px-6 relative select-none">
      <div className="absolute top-1/2 left-10 w-96 h-96 bg-electricBlue/5 rounded-full blur-[100px] pointer-events-none -z-10" />

      <div className="max-w-5xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#9D00FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> REAL TRANSFORMATIONS
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            Athlete Success Stories
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Real results from dedicated individuals who rebuilt their physical power using our precise training and nutrition systems.
          </p>
        </div>

        {/* Testimonial Active Display */}
        <div className="glass-panel p-8 md:p-12 rounded-3xl glow-border card-radial-blue flex flex-col md:flex-row items-center gap-8 relative">
          
          <div className="absolute top-6 right-6 text-white/5 pointer-events-none">
            <Quote size={80} className="fill-white/5" />
          </div>

          {/* User Photo & Metric */}
          <div className="flex flex-col items-center text-center shrink-0">
            <div className="w-24 h-24 rounded-full p-1 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF]">
              <img
                src={active.avatar}
                alt={active.name}
                className="w-full h-full object-cover rounded-full border-2 border-[#0B0B0B]"
              />
            </div>
            <h4 className="text-base font-bold font-outfit text-white mt-4">{active.name}</h4>
            <span className="text-xs text-gray-500 font-medium">{active.role}</span>

            {/* Custom transformation badge */}
            <div className="mt-4 px-3 py-1 rounded-md bg-white/5 border border-white/10 text-[10px] font-bold text-gray-300 font-outfit uppercase">
              {active.tag}
            </div>
          </div>

          {/* User Review Content */}
          <div className="flex-1 flex flex-col justify-between">
            <div>
              {/* Rating stars */}
              <div className="flex gap-1 text-yellow-400 mb-4 justify-center md:justify-start">
                {Array.from({ length: active.rating }).map((_, i) => (
                  <Star key={i} size={14} className="fill-yellow-400" />
                ))}
              </div>

              {/* Transformation Stat Highlight */}
              <span className="text-sm font-extrabold font-outfit text-[#00F0FF] block mb-3 uppercase tracking-wider">
                {active.stat}
              </span>

              {/* Review Text */}
              <p className="text-sm text-gray-300 leading-relaxed font-medium italic">
                "{active.text}"
              </p>
            </div>

            {/* Slide Arrows Container */}
            <div className="flex gap-3 mt-8 justify-center md:justify-start">
              <button
                onClick={handlePrev}
                className="p-2.5 rounded-xl bg-white/5 border border-white/5 hover:border-white/10 hover:bg-white/10 text-gray-400 hover:text-white transition-all cursor-pointer active:scale-95"
              >
                <ChevronLeft size={16} />
              </button>
              <button
                onClick={handleNext}
                className="p-2.5 rounded-xl bg-white/5 border border-white/5 hover:border-white/10 hover:bg-white/10 text-gray-400 hover:text-white transition-all cursor-pointer active:scale-95"
              >
                <ChevronRight size={16} />
              </button>
            </div>
          </div>

        </div>
      </div>
    </section>
  )
}

export default Testimonials

