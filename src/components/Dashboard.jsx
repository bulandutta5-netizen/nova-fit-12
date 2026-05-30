import React, { useState } from 'react'
import { Sparkles, Activity, Flame, Droplet, Plus, Minus, Trophy, TrendingUp, CalendarCheck, Bell, Check } from 'lucide-react'
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip } from 'recharts'

// Localized mock graph data
const weeklyGraphData = [
  { day: 'Mon', burned: 450, consumed: 1950 },
  { day: 'Tue', burned: 620, consumed: 2100 },
  { day: 'Wed', burned: 350, consumed: 1850 },
  { day: 'Thu', burned: 710, consumed: 2300 },
  { day: 'Fri', burned: 580, consumed: 2050 },
  { day: 'Sat', burned: 820, consumed: 2400 },
  { day: 'Sun', burned: 500, consumed: 1900 },
]

const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className="glass-panel p-4 rounded-xl border border-white/10 text-xs font-semibold">
        <p className="text-gray-300 font-outfit mb-2">{label}</p>
        <p className="text-[#00D2FF]">Burned: {payload[0].value} kcal</p>
        <p className="text-[#9D00FF]">Consumed: {payload[1].value} kcal</p>
      </div>
    )
  }
  return null
}

const Dashboard = () => {
  const [waterCups, setWaterCups] = useState(2)
  const waterGoal = 14 // 14 cups * 250ml = 3.5L
  
  // ── Daily Vital Check-In & Dynamic Recovery States ──────────────────────────
  const [sleepHrs, setSleepHrs] = useState(8)
  const [soreness, setSoreness] = useState('Mild') // 'Mild', 'Moderate', 'Severe'
  const [energy, setEnergy] = useState(8) // 1-10
  const [alertAccepted, setAlertAccepted] = useState(false)
  const [showRewardsMsg, setShowRewardsMsg] = useState(false)

  // Dynamically compute a real Recovery Score!
  let recoveryScore = 90
  if (soreness === 'Mild') recoveryScore += 5
  else if (soreness === 'Moderate') recoveryScore -= 15
  else recoveryScore -= 35

  recoveryScore += (sleepHrs - 8) * 4
  recoveryScore += (energy - 8) * 3
  recoveryScore = Math.max(20, Math.min(100, recoveryScore))

  let recoveryAdvice = "Ready for high-intensity lifting!"
  let recoveryColor = "text-[#00F0FF]"
  let recoveryBg = "bg-[#00F0FF]/15"
  if (recoveryScore < 60) {
    recoveryAdvice = "Critical fatigue. Focus on mobility & active rest."
    recoveryColor = "text-red-400"
    recoveryBg = "bg-red-500/10"
  } else if (recoveryScore < 80) {
    recoveryAdvice = "Moderate recovery. Maintain form & load weights gently."
    recoveryColor = "text-yellow-400"
    recoveryBg = "bg-yellow-500/10"
  }

  const currentWeight = "74.8"
  const targetCal = 2200
  const startWeight = 78.5
  const goalWeight = 72.0

  const playBeep = (freq, dur = 0.1) => {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)()
      const osc = ctx.createOscillator()
      const gain = ctx.createGain()
      osc.type = 'sine'; osc.frequency.value = freq
      osc.connect(gain); gain.connect(ctx.destination)
      gain.gain.setValueAtTime(0.04, ctx.currentTime)
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur)
      osc.start(); osc.stop(ctx.currentTime + dur)
    } catch (e) {}
  }

  const handleWaterLog = (cups) => {
    setWaterCups(cups)
    playBeep(800, 0.1)
  }

  return (
    <section id="dashboard" className="py-24 px-6 relative select-none">
      <div className="absolute top-10 right-20 w-80 h-80 bg-neonPurple/5 rounded-full blur-[100px] pointer-events-none -z-10" />
      <div className="max-w-7xl mx-auto">
        
        {/* Header Title */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> HABITS & METRIC TRACKERS
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">Your Daily Progress Hub</h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">Track your daily habits, energy balance, active calories, hydration levels, and weight trends as you close in on your target weight.</p>
        </div>

        {/* Lived-in Coach Alerts / Notification Banner */}
        {!alertAccepted && (
          <div className="glass-panel border-amber-500/20 bg-amber-500/5 p-5 rounded-2xl glow-border mb-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 animate-[pulse_3s_infinite_alternate]">
            <div className="flex gap-3">
              <div className="p-2.5 bg-amber-500/10 text-amber-500 rounded-xl shrink-0 mt-0.5">
                <Bell size={18} />
              </div>
              <div>
                <span className="text-[9px] font-bold text-amber-500 uppercase tracking-widest block font-outfit">Active Coach Alert</span>
                <p className="text-xs text-gray-300 mt-1 leading-relaxed">
                  <strong>Coach Nova:</strong> "Hey champion, you missed yesterday's training block (*Legs A - Hypertrophy*). Don't sweat it — consistency isn't about being perfect; it's about getting back on track. Let's adjust today's session so we stay aligned."
                </p>
              </div>
            </div>
            <div className="flex gap-2.5 shrink-0 self-end md:self-center font-outfit">
              <button onClick={() => { setAlertAccepted(true); playBeep(880, 0.12); }} className="px-4 py-2 bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 rounded-xl text-xs font-bold transition-all border border-amber-500/10 cursor-pointer">ADJUST TODAY'S VOLUME</button>
              <button onClick={() => { setAlertAccepted(true); playBeep(700, 0.08); }} className="px-3.5 py-2 text-gray-500 hover:text-gray-300 rounded-xl text-xs font-bold transition-all cursor-pointer">DISMISS</button>
            </div>
          </div>
        )}

        {/* Summary 4-Column Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          
          {/* 1. Streak Tracker with Rewards Progress */}
          <div className="glass-panel p-6 rounded-3xl glow-border flex flex-col justify-between card-radial-blue relative overflow-hidden">
            <div className="flex items-center gap-4">
              <div className="p-3.5 bg-yellow-500/15 text-yellow-500 rounded-2xl shrink-0"><Flame size={24} className="fill-yellow-500/10" /></div>
              <div>
                <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block">Active Streak</span>
                <span className="text-2xl font-extrabold font-outfit text-white mt-0.5 block">6 Days</span>
              </div>
            </div>
            <div className="mt-4">
              <div className="flex justify-between items-center text-[9px] text-gray-400 font-semibold mb-1">
                <span>Streak Level: Gold Prep</span>
                <span className="text-[#00F0FF]">85%</span>
              </div>
              <div className="w-full h-1.5 bg-white/5 rounded-full overflow-hidden">
                <div className="h-full bg-gradient-to-r from-yellow-500 to-orange-500 rounded-full" style={{ width: '85%' }} />
              </div>
              <span 
                onClick={() => { playBeep(1000, 0.15); setShowRewardsMsg(prev => !prev); }}
                className="text-[8px] text-emerald-400 font-bold mt-1.5 block uppercase tracking-wider cursor-pointer hover:underline"
              >
                🔥 Reward unlocked on Day 7: Premium Rest Tones
              </span>
              {showRewardsMsg && (
                <span className="text-[8px] text-gray-400 block mt-1 leading-relaxed">
                  Consistency unlocks premium rest buzzer synthesized sound waves and customizable voice packs. Keep it up!
                </span>
              )}
            </div>
          </div>

          {/* 2. Active Burn */}
          <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple flex flex-col justify-between">
            <div className="flex justify-between items-start mb-4">
              <div>
                <span className="text-[10px] text-gray-500 font-bold uppercase block tracking-wider">Active Burn</span>
                <span className="text-2xl font-extrabold font-outfit text-white mt-1 block">680 / <span className="text-xs text-gray-400 font-normal">800 kcal</span></span>
              </div>
              <div className="p-3 bg-red-500/15 text-red-500 rounded-xl"><Activity size={18} /></div>
            </div>
            <div className="w-full h-2 bg-white/5 rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-red-500 to-orange-500 rounded-full" style={{ width: '85%' }} />
            </div>
          </div>

          {/* 3. Calorie Intake */}
          <div className="glass-panel p-6 rounded-3xl glow-border card-radial-blue flex flex-col justify-between">
            <div className="flex justify-between items-start mb-4">
              <div>
                <span className="text-[10px] text-gray-500 font-bold uppercase block tracking-wider">Calorie Intake</span>
                <span className="text-2xl font-extrabold font-outfit text-white mt-1 block">1,750 / <span className="text-xs text-gray-400 font-normal">{targetCal} kcal</span></span>
              </div>
              <div className="p-3 bg-emerald-500/15 text-emerald-500 rounded-xl"><CalendarCheck size={18} /></div>
            </div>
            <div className="w-full h-2 bg-white/5 rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full" style={{ width: `${Math.min(100, Math.round((1750 / targetCal) * 100))}%` }} />
            </div>
          </div>

          {/* 4. Current Weight */}
          <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple flex items-center gap-5">
            <div className="p-4 bg-[#00F0FF]/15 text-[#00F0FF] rounded-2xl"><TrendingUp size={24} /></div>
            <div>
              <span className="text-[10px] text-gray-500 font-bold uppercase block tracking-wider">Current Weight</span>
              <span className="text-2xl font-extrabold font-outfit text-white mt-1 block">{currentWeight} <span className="text-xs text-gray-400 font-normal">kg</span></span>
              <span className="text-[10px] text-gray-500 mt-0.5 block">Start: {startWeight.toFixed(1)}kg • Goal: {goalWeight.toFixed(1)}kg</span>
            </div>
          </div>
        </div>

        {/* Core Layout Split Grid: Graph & History (Left) | Check-in & Water (Right) */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
          
          {/* LEFT SPLIT (2 Cols): Recharts Graph & Workout History */}
          <div className="lg:col-span-2 flex flex-col gap-8 justify-between">
            
            {/* Recharts Area Chart */}
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-blue flex-1 flex flex-col justify-between min-h-[350px]">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <h4 className="text-base font-bold font-outfit text-white">Metabolic Energy Balance</h4>
                  <p className="text-xs text-gray-500 mt-0.5">Calories Burned vs Calories Consumed</p>
                </div>
                <div className="flex items-center gap-4 text-[10px] font-semibold">
                  <span className="flex items-center gap-1.5 text-gray-400">
                    <span className="w-2.5 h-2.5 rounded-full bg-[#00D2FF]" /> Burned
                  </span>
                  <span className="flex items-center gap-1.5 text-gray-400">
                    <span className="w-2.5 h-2.5 rounded-full bg-[#9D00FF]" /> Consumed
                  </span>
                </div>
              </div>

              {/* Recharts Graph */}
              <div className="w-full h-60 text-xs">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={weeklyGraphData} margin={{ top: 10, right: 5, left: -25, bottom: 0 }}>
                    <defs>
                      <linearGradient id="colorBurned" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#00D2FF" stopOpacity={0.2}/>
                        <stop offset="95%" stopColor="#00D2FF" stopOpacity={0}/>
                      </linearGradient>
                      <linearGradient id="colorConsumed" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#9D00FF" stopOpacity={0.2}/>
                        <stop offset="95%" stopColor="#9D00FF" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <XAxis dataKey="day" stroke="#555" axisLine={false} tickLine={false} />
                    <YAxis stroke="#555" axisLine={false} tickLine={false} />
                    <Tooltip content={<CustomTooltip />} cursor={{ stroke: 'rgba(255,255,255,0.05)', strokeWidth: 1 }} />
                    <Area type="monotone" dataKey="burned" stroke="#00D2FF" strokeWidth={2} fillOpacity={1} fill="url(#colorBurned)" />
                    <Area type="monotone" dataKey="consumed" stroke="#9D00FF" strokeWidth={2} fillOpacity={1} fill="url(#colorConsumed)" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Recently Completed Workout Logs */}
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple">
              <div className="flex justify-between items-center mb-5">
                <div>
                  <h4 className="text-base font-bold font-outfit text-white">Recently Completed Workouts</h4>
                  <p className="text-xs text-gray-500 mt-0.5">Logs of your completed physical blocks</p>
                </div>
                <span className="text-[9px] font-bold text-gray-500 uppercase tracking-widest border border-white/5 px-2 py-1 rounded bg-white/3">VERIFIED SEED</span>
              </div>

              <div className="flex flex-col gap-3 font-sans">
                {[
                  { name: "Push A - Shoulder & Chest Hypertrophy Focus", time: "Completed yesterday", kcal: "520 kcal", type: "Gym Session" },
                  { name: "Legs A - Quadriceps Compound Strength Split", time: "Completed 3 days ago", kcal: "640 kcal", type: "Gym Session" },
                  { name: "Active Recovery & Dynamic Joint Mobility Block", time: "Completed 5 days ago", kcal: "180 kcal", type: "Home Workout" }
                ].map((item, idx) => (
                  <div key={idx} className="flex items-center justify-between p-4 rounded-2xl bg-[#121212]/30 border border-white/5 hover:border-white/10 transition-all">
                    <div className="flex gap-3 items-center">
                      <div className="p-2.5 bg-emerald-500/10 text-emerald-400 rounded-xl shrink-0"><Check size={16} /></div>
                      <div>
                        <span className="text-xs font-bold text-white block">{item.name}</span>
                        <span className="text-[10px] text-gray-500 mt-0.5 block">{item.type} • {item.time}</span>
                      </div>
                    </div>
                    <span className="text-xs font-bold font-outfit text-emerald-400 shrink-0">{item.kcal}</span>
                  </div>
                ))}
              </div>
            </div>

          </div>

          {/* RIGHT SPLIT (1 Col): Vital Check-In & Hydration Log */}
          <div className="flex flex-col gap-8">
            
            {/* Daily Vital Check-In & Recovery Console (Fully Interactive!) */}
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple flex flex-col justify-between relative overflow-hidden">
              <div className="absolute inset-0 bg-[#00D2FF]/3 w-full h-full pointer-events-none" />
              
              <div className="w-full">
                <div className="flex items-center gap-2 mb-4">
                  <div className="p-2.5 bg-[#00F0FF]/10 text-[#00F0FF] rounded-xl shrink-0"><Sparkles size={18} /></div>
                  <h4 className="text-sm font-bold font-outfit text-white">Daily Vital Check-In</h4>
                </div>
                
                {/* Sub-header dynamic recovery score display */}
                <div className="flex items-center justify-between mb-6 p-4.5 rounded-2xl bg-black/40 border border-white/5">
                  <div>
                    <span className="text-[9px] text-gray-500 font-bold block uppercase tracking-wider">Dynamic Recovery</span>
                    <span className={`text-2xl font-black font-outfit ${recoveryColor} mt-0.5 block transition-colors`}>{recoveryScore}%</span>
                  </div>
                  <div className={`px-3 py-1.5 rounded-xl text-[9px] font-bold ${recoveryColor} ${recoveryBg} transition-all tracking-wider text-center max-w-[120px] font-outfit uppercase`}>
                    {recoveryAdvice}
                  </div>
                </div>

                {/* Vital 1: Sleep Hours */}
                <div className="mb-4">
                  <div className="flex justify-between items-center text-xs text-gray-400 font-bold font-outfit mb-2 uppercase px-1">
                    <span>1. Sleep Quality</span>
                    <span className="text-white">{sleepHrs} Hours</span>
                  </div>
                  <input 
                    type="range" min="4" max="10" step="1" 
                    value={sleepHrs} 
                    onChange={(e) => { setSleepHrs(parseInt(e.target.value)); playBeep(500 + parseInt(e.target.value)*30, 0.05); }}
                    className="w-full accent-[#00F0FF] cursor-pointer bg-white/5 rounded-lg appearance-none h-1"
                  />
                </div>

                {/* Vital 2: Muscle Soreness Buttons */}
                <div className="mb-4">
                  <span className="block text-xs text-gray-400 font-bold font-outfit mb-2 uppercase px-1">2. Muscle Soreness</span>
                  <div className="grid grid-cols-3 gap-2">
                    {['Mild', 'Moderate', 'Severe'].map(level => (
                      <button 
                        key={level} 
                        onClick={() => { setSoreness(level); playBeep(700, 0.06); }}
                        className={`py-2 rounded-xl text-[10px] font-bold transition-all border outline-none cursor-pointer ${
                          soreness === level 
                            ? 'border-[#00D2FF]/40 bg-[#00D2FF]/10 text-white shadow-[0_0_10px_rgba(0,210,255,0.12)]' 
                            : 'border-white/5 bg-white/3 text-gray-400 hover:text-white'
                        }`}
                      >
                        {level === 'Mild' ? '🟢 Mild' : level === 'Moderate' ? '🟡 Medium' : '🔴 Severe'}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Vital 3: Energy Rating */}
                <div className="mb-2">
                  <div className="flex justify-between items-center text-xs text-gray-400 font-bold font-outfit mb-2 uppercase px-1">
                    <span>3. Energy Levels</span>
                    <span className="text-white">{energy} / 10</span>
                  </div>
                  <input 
                    type="range" min="3" max="10" step="1" 
                    value={energy} 
                    onChange={(e) => { setEnergy(parseInt(e.target.value)); playBeep(400 + parseInt(e.target.value)*40, 0.05); }}
                    className="w-full accent-[#9D00FF] cursor-pointer bg-white/5 rounded-lg appearance-none h-1"
                  />
                </div>

              </div>
            </div>

            {/* Water Tracker */}
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple flex flex-col justify-between items-center">
              <div className="w-full">
                <div className="flex items-center gap-2 justify-center mb-6">
                  <div className="p-2 bg-blue-500/15 text-blue-500 rounded-xl">
                    <Droplet size={16} className="fill-blue-500/10" />
                  </div>
                  <h4 className="text-sm font-bold font-outfit text-white">Daily Water Log</h4>
                </div>
                <div className="text-center my-6">
                  <span className="text-4xl font-extrabold font-outfit text-white">{(waterCups * 0.25).toFixed(2)}</span>
                  <span className="text-[10px] text-gray-400 font-semibold block mt-1 uppercase tracking-wider">Liters logged / 3.5L goal</span>
                </div>
                <div className="flex justify-center gap-1.5 flex-wrap max-w-[200px] mx-auto mb-6">
                  {Array.from({ length: waterGoal }).map((_, i) => (
                    <div key={i} className={`w-3 h-5 rounded-sm border transition-all duration-300 ${
                      i < waterCups ? 'bg-[#00D2FF] border-[#00D2FF] shadow-[0_0_8px_rgba(0,210,255,0.4)]' : 'border-white/10 bg-transparent'
                    }`} />
                  ))}
                </div>
              </div>

              <div className="flex gap-4 w-full justify-center mt-2">
                <button onClick={() => handleWaterLog(Math.max(0, waterCups - 1))} className="p-3.5 rounded-2xl bg-white/5 border border-white/5 hover:bg-white/10 text-gray-400 cursor-pointer active:scale-95 transition-all"><Minus size={16} /></button>
                <button onClick={() => handleWaterLog(Math.min(waterGoal+4, waterCups + 1))} className="flex-1 flex items-center justify-center gap-2 py-3.5 px-6 rounded-2xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] font-bold text-xs text-white cursor-pointer active:scale-[0.99] hover:shadow-[0_0_15px_rgba(0,210,255,0.25)] transition-all"><Plus size={14} /> Log Cup</button>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>
  )
}

export default Dashboard
