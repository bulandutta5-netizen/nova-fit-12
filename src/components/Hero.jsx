import React from 'react'
import { Sparkles, ArrowRight, Shield, Zap, Heart } from 'lucide-react'

const Hero = () => {
  const handleScroll = (href) => {
    const element = document.querySelector(href)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <section className="relative min-h-screen flex flex-col justify-center items-center px-6 pt-20 sm:pt-28 md:pt-32 pb-12 overflow-hidden select-none">
      {/* Glow effect backgrounds */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-neonPurple/15 rounded-full blur-[120px] pointer-events-none -z-10" />
      <div className="absolute bottom-10 left-1/4 w-[300px] h-[300px] bg-electricBlue/10 rounded-full blur-[100px] pointer-events-none -z-10" />

      {/* Floating Card UI Element Left */}
      <div className="hidden lg:block absolute left-12 xl:left-24 top-1/3 p-4 glass-panel rounded-2xl glow-border animate-float max-w-[200px] cursor-pointer">
        <div className="flex items-center gap-2 mb-2">
          <div className="p-1.5 bg-electricBlue/20 rounded-lg text-electricBlue">
            <Zap size={16} />
          </div>
          <span className="text-xs font-semibold text-gray-300">Energy Engine</span>
        </div>
        <p className="text-2xl font-bold font-outfit text-white">4,250</p>
        <span className="text-[10px] text-gray-500">KCALS BURNED THIS WEEK</span>
      </div>

      {/* Floating Card UI Element Right */}
      <div className="hidden lg:block absolute right-12 xl:right-24 bottom-1/3 p-4 glass-panel rounded-2xl glow-border animate-float [animation-delay:2s] max-w-[200px] cursor-pointer">
        <div className="flex items-center gap-2 mb-2">
          <div className="p-1.5 bg-[#9D00FF]/20 rounded-lg text-[#9D00FF]">
            <Heart size={16} />
          </div>
          <span className="text-xs font-semibold text-gray-300">Biometrics</span>
        </div>
        <p className="text-2xl font-bold font-outfit text-white">124 <span className="text-xs font-normal text-gray-400">BPM</span></p>
        <span className="text-[10px] text-gray-500">ACTIVE HEART RATE RANGE</span>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl text-center z-10 flex flex-col items-center">
        {/* Sparkle badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 mb-8 animate-pulse-slow">
          <Sparkles size={14} className="text-[#00F0FF]" />
          <span className="text-xs font-semibold tracking-wide text-gray-300 font-outfit uppercase">
            Evolutionary Fitness Protocol
          </span>
        </div>

        {/* Headline */}
        <h1 className="text-3xl sm:text-5xl md:text-6xl font-extrabold font-outfit tracking-tight leading-[1.1] mb-6 text-white">
          Train Smarter <br />
          <span className="bg-glow-gradient bg-clip-text text-transparent">With Precision AI</span>
        </h1>

        {/* Subhead */}
        <p className="text-base sm:text-lg md:text-xl text-gray-400 max-w-2xl leading-relaxed mb-10">
          AI-powered calorie tracking, personalized nutrition, and smart workout protocols designed for your biometrics and goals. Built like Tesla, designed like Apple.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center w-full max-w-md mb-20">
          <button
            onClick={() => handleScroll('#nutrition')}
            className="group w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-4 bg-glow-gradient rounded-full font-semibold text-white shadow-[0_0_30px_rgba(0,210,255,0.25)] hover:shadow-[0_0_40px_rgba(0,210,255,0.45)] hover:scale-[1.02] transition-all duration-300 cursor-pointer"
          >
            Start Journey <ArrowRight size={16} className="group-hover:translate-x-1 transition-transform" />
          </button>
          
          <button
            onClick={() => handleScroll('#chatbot')}
            className="w-full sm:w-auto px-8 py-4 rounded-full border border-white/10 hover:border-white/30 hover:bg-white/5 font-semibold text-gray-300 hover:text-white transition-all duration-300 cursor-pointer"
          >
            Try AI Coach
          </button>
        </div>

        {/* Scroll Indicator */}
        <div className="flex flex-col items-center gap-2 cursor-pointer mb-16" onClick={() => handleScroll('#nutrition')}>
          <span className="text-[10px] text-gray-500 tracking-widest uppercase">Scroll to Initialize</span>
          <div className="w-5 h-8 border border-gray-600 rounded-full flex justify-center p-1.5">
            <div className="w-1 h-2 bg-[#00F0FF] rounded-full animate-bounce" />
          </div>
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 w-full max-w-5xl mt-8">
          <div className="p-6 glass-panel rounded-2xl glow-border card-radial-blue text-left flex flex-col justify-between">
            <h3 className="text-3xl md:text-4xl font-extrabold font-outfit bg-indigo-gradient bg-clip-text text-transparent">150,000+</h3>
            <p className="text-xs font-semibold text-gray-400 mt-2">MEALS ANALYZED</p>
            <span className="text-[10px] text-gray-600 mt-1">Realtime nutrient breakdown scans</span>
          </div>

          <div className="p-6 glass-panel rounded-2xl glow-border card-radial-purple text-left flex flex-col justify-between">
            <h3 className="text-3xl md:text-4xl font-extrabold font-outfit text-white">98.4%</h3>
            <p className="text-xs font-semibold text-gray-400 mt-2">ACCURACY RATE</p>
            <span className="text-[10px] text-gray-600 mt-1">Precise predictive metabolic modeling</span>
          </div>

          <div className="p-6 glass-panel rounded-2xl glow-border card-radial-blue text-left flex flex-col justify-between">
            <h3 className="text-3xl md:text-4xl font-extrabold font-outfit text-white">24/7</h3>
            <p className="text-xs font-semibold text-gray-400 mt-2">AI ADVANTAGE</p>
            <span className="text-[10px] text-gray-600 mt-1">Continuous coaching and support</span>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero
