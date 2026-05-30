import React from 'react'
import { Sparkles, CheckCircle2 } from 'lucide-react'

const pricingPlans = [
  {
    name: 'Nova Essential',
    price: '$19',
    period: '/mo',
    desc: 'Core metabolic modeling and training splits for dedicated physical training.',
    features: [
      'Smart Calorie & Macro Targeter',
      'Access to All 6 Diet Profiles',
      'Dynamic Gym & Home Splits',
      'Hydration Progress Log',
    ],
    highlight: false,
    cta: 'GET STARTED'
  },
  {
    name: 'Nova Elite',
    price: '$49',
    period: '/mo',
    desc: 'Our flagship membership unlocking interactive AI coaching, dynamic plateaus adjustment, and voice mode.',
    features: [
      'Everything in Nova Essential',
      'Coach Nova AI Chatbot Trainer',
      'Adaptive Weekly Calorie Shifts',
      'Interactive Rest Timers & Sound Feedback',
      'Priority AI Response Time',
    ],
    highlight: true,
    cta: 'START ELITE FREE TRIAL'
  },
  {
    name: 'Elite Hybrid',
    price: '$99',
    period: '/mo',
    desc: 'The ultimate training system combining Coach Nova\'s speed with weekly audits from human metabolic coaches.',
    features: [
      'Everything in Nova Elite',
      'Weekly Human Coach Form Audits',
      'Monthly 1-on-1 Video Strategy Call',
      'Dedicated Slack Channel Support',
      'Custom Gym-Specific Adaptations',
    ],
    highlight: false,
    cta: 'APPLY FOR HYBRID'
  }
]

const Pricing = () => {
  return (
    <section id="pricing" className="py-24 px-6 relative select-none">
      {/* Background Glow */}
      <div className="absolute top-10 left-1/2 -translate-x-1/2 w-[700px] h-[700px] bg-electricBlue/5 rounded-full blur-[140px] pointer-events-none -z-10" />

      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> SIMPLE, TRANSPARENT PRICING
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            Choose Your Transformation Plan
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Select the plan suited for your physical transformation. Start training in seconds, adjust or cancel anytime.
          </p>
        </div>

        {/* Pricing Cards Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch max-w-6xl mx-auto">
          {pricingPlans.map((plan, index) => (
            <div
              key={index}
              className={`glass-panel p-8 rounded-3xl flex flex-col justify-between relative overflow-hidden transition-all duration-300 ${
                plan.highlight
                  ? 'border-[#00D2FF]/40 shadow-[0_0_30px_rgba(0,210,255,0.08)] bg-black/40 card-radial-blue scale-100 lg:scale-[1.03] z-10'
                  : 'border-white/5 hover:border-white/15 card-radial-purple opacity-90 hover:opacity-100'
              }`}
            >
              {/* Highlight Badge */}
              {plan.highlight && (
                <div className="absolute top-4 right-4 bg-glow-gradient px-3 py-1 rounded-full text-[9px] font-bold font-outfit text-white tracking-widest uppercase">
                  RECOMMENDED
                </div>
              )}

              <div>
                {/* Plan Name */}
                <h3 className="text-xs font-bold tracking-widest text-gray-500 uppercase font-outfit mb-4">
                  {plan.name}
                </h3>

                {/* Price */}
                <div className="flex items-baseline gap-1 mb-4">
                  <span className="text-5xl font-extrabold font-outfit text-white">
                    {plan.price}
                  </span>
                  <span className="text-xs font-semibold text-gray-500">
                    {plan.period}
                  </span>
                </div>

                {/* Description */}
                <p className="text-xs text-gray-400 leading-relaxed mb-8">
                  {plan.desc}
                </p>

                {/* Divider Line */}
                <div className="h-px bg-white/5 mb-8" />

                {/* Features List */}
                <div className="flex flex-col gap-4">
                  {plan.features.map((feat, fIdx) => (
                    <div key={fIdx} className="flex items-center gap-3 text-xs font-semibold text-gray-300">
                      <CheckCircle2 size={14} className={plan.highlight ? 'text-[#00D2FF]' : 'text-[#9D00FF]'} />
                      <span>{feat}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Call To Action button */}
              <button
                className={`w-full mt-10 py-4 rounded-xl font-semibold text-xs tracking-wider transition-all duration-300 cursor-pointer ${
                  plan.highlight
                    ? 'bg-glow-gradient text-white shadow-[0_0_20px_rgba(0,210,255,0.25)] hover:shadow-[0_0_30px_rgba(0,210,255,0.45)] hover:scale-[1.01]'
                    : 'bg-[#161616] hover:bg-white/5 text-gray-400 hover:text-white border border-white/5 hover:border-white/10'
                }`}
              >
                {plan.cta}
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Pricing

