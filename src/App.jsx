import React, { useState } from 'react'
import ParticleBackground from './components/ParticleBackground.jsx'
import Navbar from './components/Navbar.jsx'
import Hero from './components/Hero.jsx'
import Calculator from './components/Calculator.jsx'
import DietPlanner from './components/DietPlanner.jsx'
import WorkoutGenerator from './components/WorkoutGenerator.jsx'
import Chatbot from './components/Chatbot.jsx'
import Dashboard from './components/Dashboard.jsx'
import Testimonials from './components/Testimonials.jsx'
import Pricing from './components/Pricing.jsx'
import FAQ from './components/FAQ.jsx'
import Footer from './components/Footer.jsx'

const App = () => {
  // Global User Biometrics state calculated by Calculator.jsx
  // Scales meal calories/grams in DietPlanner.jsx dynamically
  const [userProfile, setUserProfile] = useState({
    targetCalories: 2100,
    goal: 'maintain',
    gender: 'male',
    weight: '75',
    height: '180',
    age: '25',
    bmi: '23.1',
    bmiCategory: 'Healthy Weight'
  })

  const handleProfileUpdate = (profileData) => {
    setUserProfile(profileData)
  }

  return (
    <div className="relative min-h-screen text-white bg-[#0B0B0B] font-sans selection:bg-[#9D00FF] selection:text-white overflow-hidden">
      {/* Cinematic Mouse Interactive Particles */}
      <ParticleBackground />

      {/* Futuristic Floating Background Gradients */}
      <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-electricBlue/5 rounded-full blur-[140px] pointer-events-none -z-20" />
      <div className="absolute top-[120vh] left-[-200px] w-[500px] h-[500px] bg-neonPurple/5 rounded-full blur-[120px] pointer-events-none -z-20" />
      <div className="absolute bottom-[200vh] right-[-100px] w-[600px] h-[600px] bg-cyanGlow/5 rounded-full blur-[130px] pointer-events-none -z-20" />

      {/* Floating Header */}
      <Navbar />

      {/* Single Page Layout Sections */}
      <main className="relative z-10 w-full">
        {/* Section 1: Hero */}
        <Hero />

        {/* Section 2: AI Calorie Calculator */}
        <Calculator onCalculate={handleProfileUpdate} />

        {/* Section 3: AI Diet Plan Generator */}
        <DietPlanner userProfile={userProfile} />

        {/* Section 4: AI Workout Generator */}
        <WorkoutGenerator />

        {/* Section 6: User Dashboard (moved up for better flow before chatbot) */}
        <Dashboard />

        {/* Section 5: AI Fitness Chatbot */}
        <Chatbot />

        {/* Section 7: Testimonials */}
        <Testimonials />

        {/* Section 8: Pricing */}
        <Pricing />

        {/* Section 9: FAQ */}
        <FAQ />
      </main>

      {/* Section 10: Footer */}
      <Footer />
    </div>
  )
}

export default App
