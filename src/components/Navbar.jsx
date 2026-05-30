import React, { useState, useEffect } from 'react'
import { Menu, X, Sparkles, User } from 'lucide-react'

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        setScrolled(true)
      } else {
        setScrolled(false)
      }
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const navLinks = [
    { name: 'Training', href: '#workout' },
    { name: 'Nutrition', href: '#nutrition' },
    { name: 'Intelligence', href: '#chatbot' },
    { name: 'Dashboard', href: '#dashboard' },
    { name: 'Pricing', href: '#pricing' },
  ]

  const handleLinkClick = (href) => {
    setIsOpen(false)
    const element = document.querySelector(href)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <>
      <nav className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 ${
        scrolled 
          ? 'py-2 bg-[#0B0B0B]/80 backdrop-blur-md border-b border-white/5' 
          : 'py-3.5 bg-transparent'
      }`}>
        <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
          {/* Logo */}
          <a href="#" className="flex items-center gap-2 font-outfit tracking-wider text-white">
            <img src="./logo.png?v=5" alt="FIT NOVA" className="h-8 sm:h-11 md:h-16 w-auto object-contain" />
          </a>

          {/* Desktop Nav Links */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                onClick={(e) => {
                  e.preventDefault()
                  handleLinkClick(link.href)
                }}
                className="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-200"
              >
                {link.name}
              </a>
            ))}
          </div>

          {/* Desktop CTA Buttons */}
          <div className="hidden md:flex items-center gap-4">
            <a
              href="./login.html"
              className="flex items-center justify-center gap-1.5 text-sm font-medium text-gray-300 hover:text-white px-4 py-2 rounded-full border border-white/10 hover:bg-white/5 transition-all duration-200"
            >
              <User size={14} /> Login
            </a>
            <a
              href="#nutrition"
              onClick={(e) => {
                e.preventDefault()
                handleLinkClick('#nutrition')
              }}
              className="text-sm font-semibold text-white px-5 py-2.5 rounded-full bg-glow-gradient hover:shadow-[0_0_20px_rgba(0,210,255,0.4)] transition-all duration-300"
            >
              Get Started
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 text-gray-400 hover:text-white focus:outline-none"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </nav>

      {/* Mobile Drawer Overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 md:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Mobile Drawer */}
      <div className={`fixed top-0 right-0 h-full w-72 bg-[#0B0B0B] border-l border-white/10 p-6 z-50 transform transition-transform duration-300 ease-in-out md:hidden ${
        isOpen ? 'translate-x-0' : 'translate-x-full'
      }`}>
        <div className="flex justify-between items-center mb-10">
          <img src="./logo.png?v=5" alt="FIT NOVA" className="h-8 w-auto object-contain" />
          <button
            onClick={() => setIsOpen(false)}
            className="p-2 text-gray-400 hover:text-white focus:outline-none"
          >
            <X size={20} />
          </button>
        </div>

        <div className="flex flex-col gap-6">
          {navLinks.map((link) => (
            <a
              key={link.name}
              href={link.href}
              onClick={(e) => {
                e.preventDefault()
                handleLinkClick(link.href)
              }}
              className="text-lg font-medium text-gray-400 hover:text-white transition-colors duration-200"
            >
              {link.name}
            </a>
          ))}
          <div className="h-px bg-white/10 my-4" />
          <a
            href="./login.html"
            className="flex items-center justify-center gap-1.5 w-full py-3 rounded-full border border-white/10 hover:bg-white/5 transition-all text-sm font-semibold text-gray-300 hover:text-white"
          >
            <User size={14} /> Login
          </a>
          <a
            href="#nutrition"
            onClick={(e) => {
              e.preventDefault()
              handleLinkClick('#nutrition')
            }}
            className="w-full text-center py-3 rounded-full bg-glow-gradient font-semibold text-sm hover:shadow-[0_0_20px_rgba(0,210,255,0.4)] transition-all text-white"
          >
            Get Started
          </a>
        </div>
      </div>
    </>
  )
}

export default Navbar
