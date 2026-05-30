import React from 'react'
import { Sparkles, Linkedin, Mail, Smartphone, ShieldCheck } from 'lucide-react'

const Footer = () => {
  const currentYear = new Date().getFullYear()

  const handleScroll = (e, href) => {
    e.preventDefault()
    const element = document.querySelector(href)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <footer className="border-t border-white/5 bg-black/40 backdrop-blur-md py-16 px-6 relative select-none">
      <div className="max-w-7xl mx-auto flex flex-col gap-12">
        {/* Top Split */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          {/* Logo & Bio */}
          <div className="flex flex-col gap-4">
            <a href="#" className="flex items-center gap-2 font-outfit tracking-wider text-white">
              <img src="./logo.png?v=5" alt="FIT NOVA" className="h-8 sm:h-11 md:h-16 w-auto object-contain" />
            </a>
            <p className="text-xs text-gray-500 leading-relaxed font-semibold">
              Engineered metabolic modeling systems for elite physical performance and biometric transformation.
            </p>
          </div>

          {/* Quick Links */}
          <div className="flex flex-col gap-3.5">
            <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit">Quick Links</h4>
            <div className="flex flex-col gap-2.5 text-xs text-gray-400 font-semibold">
              <a href="#workout" onClick={(e) => handleScroll(e, '#workout')} className="hover:text-white transition-colors">Training Engine</a>
              <a href="#nutrition" onClick={(e) => handleScroll(e, '#nutrition')} className="hover:text-white transition-colors">Calorie Diagnostics</a>
              <a href="#chatbot" onClick={(e) => handleScroll(e, '#chatbot')} className="hover:text-white transition-colors">Nova AI Coach</a>
              <a href="#dashboard" onClick={(e) => handleScroll(e, '#dashboard')} className="hover:text-white transition-colors">Biometric Dashboard</a>
            </div>
          </div>

          {/* Contact Details */}
          <div className="flex flex-col gap-3.5">
            <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit">Connect With Us</h4>
            <div className="flex flex-col gap-3 text-xs text-gray-400 font-semibold">
              <a href="mailto:support@fitnova.ai" className="flex items-center gap-2 hover:text-white transition-colors">
                <Mail size={14} className="text-[#00F0FF]" /> support@fitnova.ai
              </a>
              <span className="flex items-center gap-2">
                <Smartphone size={14} className="text-[#9D00FF]" /> +91 93302 84675
              </span>
              <span className="flex items-center gap-2">
                <ShieldCheck size={14} className="text-emerald-400" /> Secure SSL Server
              </span>
            </div>
          </div>

          {/* Newsletter Signup */}
          <div className="flex flex-col gap-3.5">
            <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit">The Daily Digest</h4>
            <p className="text-xs text-gray-500 font-semibold">Subscribe for daily scientific research digests.</p>
            <form onSubmit={(e) => e.preventDefault()} className="flex gap-2 mt-2">
              <input
                type="email"
                placeholder="node@network.com"
                className="bg-[#121212] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-3 py-2 text-xs text-white outline-none w-full transition-all"
                required
              />
              <button 
                type="submit" 
                className="px-4 py-2 bg-glow-gradient rounded-xl text-xs font-bold text-white cursor-pointer active:scale-95 transition-transform"
              >
                JOIN
              </button>
            </form>
          </div>

        </div>

        {/* Divider Line */}
        <div className="h-px bg-white/5" />

        {/* Bottom copyright details */}
        <div className="flex flex-col sm:flex-row justify-between items-center gap-6 text-[10px] text-gray-500 font-semibold">
          <p>© {currentYear} Fit Nova AI Precision Systems. All rights reserved.</p>
          
          <div className="flex items-center gap-6">
            <a href="#" className="hover:text-white transition-colors">Privacy Protocol</a>
            <a href="#" className="hover:text-white transition-colors">Terms of Operations</a>
            <a href="https://www.linkedin.com/in/vikrant-dutta-5758b040a/" target="_blank" className="flex items-center gap-1 hover:text-white transition-colors">
              <Linkedin size={12} /> Creator LinkedIn
            </a>
          </div>
        </div>

      </div>
    </footer>
  )
}

export default Footer

