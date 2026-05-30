import re

filePath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filePath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Spacing, padding, and Visual Overload Clean-ups in CSS block
# Let's replace the .glass-panel definition with a premium, Stripe/Apple-like, clean matte graphite look.
old_glass_panel = """      .glass-panel {
        background: radial-gradient(120% 120% at 50% 0%, rgba(255, 255, 255, 0.035) 0%, rgba(255, 255, 255, 0.005) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        transition: border-color 0.4s ease, box-shadow 0.4s ease, transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .glass-panel:hover {
        border-color: rgba(0, 210, 255, 0.25);
        box-shadow: 0 20px 45px -15px rgba(0, 0, 0, 0.75), 0 0 35px -5px rgba(0, 210, 255, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.16);
        transform: translateY(-2px);
      }"""

new_glass_panel = """      .glass-panel {
        background: rgba(18, 18, 18, 0.45);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.03);
        transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .glass-panel:hover {
        border-color: rgba(0, 210, 255, 0.12);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transform: translateY(-1px);
      }"""

content = content.replace(old_glass_panel, new_glass_panel)

# Also let's append custom styles for bottom navigation and chatbot bubbles
custom_styles = """
      /* Mobile bottom nav, suggestion tags */
      .mobile-bottom-nav button {
        transition: color 0.2s, transform 0.2s;
      }
      .mobile-bottom-nav button:active {
        transform: scale(0.92);
      }
      .suggestion-tag {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        transition: all 0.2s ease;
      }
      .suggestion-tag:hover {
        background: rgba(0,210,255,0.08);
        border-color: rgba(0,210,255,0.25);
        color: #fff;
        transform: translateY(-0.5px);
      }
"""
content = content.replace("    </style>", custom_styles + "\n    </style>")


# 2. Overhaul Dashboard completely: Replace lines 1207 to 1825 in preview.html
# Let's locate the start and end of Dashboard.
dashboard_pattern = r'const Dashboard = \(\{ user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy \}\) => \{.*?return \(.*?</div>\s*\);\s*\};'

new_dashboard = """const Dashboard = ({ user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy }) => {
        
        const [waterGoal] = useState(14); // 14 cups * 250ml = 3.5L
        const [caloriesLog, setCaloriesLog] = useState(1890);
        const [showRecoveryModal, setShowRecoveryModal] = useState(false);
        
        // Completed Exercises checklist
        const [completedEx, setCompletedEx] = useState({
          ex1: true, ex2: false, ex3: false, ex4: false
        });

        // Current diet selector on dashboard summary
        const [dietProfile, setDietProfile] = useState('highprotein');

        // Dynamically compute a real Recovery Score
        let recoveryScore = 90;
        if (soreness === 'Mild') recoveryScore += 5;
        else if (soreness === 'Moderate') recoveryScore -= 15;
        else recoveryScore -= 35;

        recoveryScore += (sleepHrs - 8) * 4;
        recoveryScore += (energy - 8) * 3;
        recoveryScore = Math.max(20, Math.min(100, recoveryScore));

        let recoveryAdvice = "Great Recovery";
        let recoveryColor = "text-[#00F0FF]";
        let recoveryBg = "bg-[#00F0FF]/15";
        let recoveryIndicator = "stroke-[#00D2FF]";
        if (recoveryScore < 60) {
          recoveryAdvice = "Critical Fatigue";
          recoveryColor = "text-red-400";
          recoveryBg = "bg-red-500/10";
          recoveryIndicator = "stroke-red-500";
        } else if (recoveryScore < 80) {
          recoveryAdvice = "Moderate Recovery";
          recoveryColor = "text-yellow-400";
          recoveryBg = "bg-yellow-500/10";
          recoveryIndicator = "stroke-yellow-500";
        }

        const currentWeight = userProfile?.weight || "78.0";
        const targetCal = userProfile?.targetCalories || 2300;

        const getMacroBreakdown = (diet) => {
          const cals = targetCal;
          let pPct = 0.30, cPct = 0.45, fPct = 0.25;
          if (diet === 'keto') { pPct = 0.25; cPct = 0.05; fPct = 0.70; }
          else if (diet === 'highprotein') { pPct = 0.35; cPct = 0.35; fPct = 0.30; }
          else if (diet === 'vegan') { pPct = 0.20; cPct = 0.55; fPct = 0.25; }
          else if (diet === 'indian') { pPct = 0.25; cPct = 0.50; fPct = 0.25; }
          else if (diet === 'budget') { pPct = 0.22; cPct = 0.50; fPct = 0.28; }
          
          return {
            protein: { pct: Math.round(pPct * 100), grams: Math.round((cals * pPct) / 4) },
            carbs: { pct: Math.round(cPct * 100), grams: Math.round((cals * cPct) / 4) },
            fat: { pct: Math.round(fPct * 100), grams: Math.round((cals * fPct) / 9) }
          };
        };

        const macros = getMacroBreakdown(dietProfile);

        const nextMealData = {
          highprotein: { name: "Chicken & Brown Rice", tag: "High Protein", time: "In 45 min" },
          vegetarian: { name: "Quinoa Buddha Bowl", tag: "Vegetarian Bowl", time: "In 30 min" },
          vegan: { name: "Tempeh Tacos & Salad", tag: "Vegan Macros", time: "In 50 min" },
          keto: { name: "Salmon Omelette", tag: "Healthy Keto Fats", time: "In 15 min" },
          indian: { name: "Paneer Bhurji & Roti", tag: "Protein Pack", time: "In 25 min" },
          budget: { name: "Egg Curry & Brown Rice", tag: "Low Budget Plan", time: "In 40 min" }
        };

        const currentNextMeal = nextMealData[dietProfile] || nextMealData['highprotein'];

        const playBeep = (freq, type = 'sine', dur = 0.1) => {
          try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = type; osc.frequency.value = freq;
            osc.connect(gain); gain.connect(ctx.destination);
            gain.gain.setValueAtTime(0.04, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
            osc.start(); osc.stop(ctx.currentTime + dur);
          } catch (e) {}
        };

        const handleWaterLog = (cups) => {
          setWaterCups(cups);
          playBeep(800, 'triangle', 0.1);
        };

        const toggleExercise = (key) => {
          setCompletedEx(prev => ({ ...prev, [key]: !prev[key] }));
          playBeep(900, 'sine', 0.08);
        };

        const addCalories = (amt) => {
          setCaloriesLog(prev => Math.min(6000, Math.max(0, prev + amt)));
          playBeep(1000, 'sine', 0.1);
        };

        // Dynamically compile active bulletins based on user details
        const getBulletins = () => {
          const alerts = [];
          
          // 1. Goal Calorie Alert
          alerts.push({
            type: "warning",
            icon: "lucide-activity",
            text: `Calorie Deficit Active: Consuming ${caloriesLog.toLocaleString()} kcal against ${Math.round(targetCal).toLocaleString()} target. Keep meals clean!`
          });

          // 2. Recovery score recommendation
          if (recoveryScore >= 80) {
            alerts.push({
              type: "success",
              icon: "lucide-sparkles",
              text: `Recovery High (${recoveryScore}%): Body is fully primed for high-intensity lifting. Consider progressive overload today!`
            });
          } else if (recoveryScore >= 60) {
            alerts.push({
              type: "info",
              icon: "lucide-refresh-cw",
              text: `Recovery Moderate (${recoveryScore}%): Keep compound weights balanced. Focus on warmups and solid technique.`
            });
          } else {
            alerts.push({
              type: "danger",
              icon: "lucide-alert-triangle",
              text: `Fatigue Warning (${recoveryScore}%): Muscle soreness is active. Prioritize hydration and active foam-rolling rest.`
            });
          }

          // 3. Safety/Injury Screening Alert
          if (userProfile?.injuries && userProfile.injuries !== 'None') {
            alerts.push({
              type: "danger",
              icon: "lucide-shield-alert",
              text: `Injury Safety Warning: ${userProfile.injuries.toUpperCase()} flagged. Coach Nova has disabled deep spinal loads & knee sheer layouts.`
            });
          } else {
            alerts.push({
              type: "success",
              icon: "lucide-shield-check",
              text: "Safety Clear: No injuries flagged. Compound training splits are fully unlocked."
            });
          }

          // 4. Hydration Alert
          const L = (waterCups * 0.25).toFixed(1);
          if (waterCups < 8) {
            alerts.push({
              type: "info",
              icon: "lucide-droplet",
              text: `Dehydration Risk: You logged ${L}L water out of 3.5L. Target 4 more cups to protect metabolic rate.`
            });
          }

          return alerts;
        };

        const activeBulletins = getBulletins();

        return (
          <div className="flex flex-col gap-6 w-full text-white animate-bubble-appear select-none">
            
            {/* Row 1: Balanced Welcome Hero + Top Deck Vitals Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-stretch">
              
              {/* Welcome Hero Banner (2/3 width) */}
              <div className="lg:col-span-2 relative glass-panel rounded-2xl p-6 overflow-hidden flex flex-col justify-between min-h-[220px]">
                {/* Purple Halo Circular Neon Ring */}
                <div className="absolute right-[-40px] md:right-[20px] top-[10%] w-56 h-56 rounded-full border border-dashed border-[#9D00FF]/30 animate-[orbital-spin_45s_linear_infinite] pointer-events-none -z-10" />
                <div className="absolute right-[-20px] md:right-[40px] top-[15%] w-48 h-48 rounded-full bg-gradient-to-tr from-[#9D00FF]/15 to-[#00D2FF]/3 blur-[20px] pointer-events-none -z-10" />

                {/* Athlete Render Image */}
                <div className="absolute right-0 bottom-0 h-full w-[40%] pointer-events-none overflow-hidden select-none -z-10 flex items-end justify-end">
                  <img src="./athlete.png" alt="Athlete" className="h-[95%] w-auto object-contain object-bottom filter drop-shadow-[0_0_20px_rgba(157,0,255,0.25)]" />
                </div>

                <div className="max-w-[65%] flex flex-col justify-between h-full gap-4">
                  <div>
                    <span className="text-[10px] text-gray-500 font-extrabold uppercase tracking-wider block font-outfit">Good Morning, {user ? user.name.split(' ')[0] : 'Arjun'}! 👋</span>
                    <h1 className="text-xl sm:text-2xl md:text-3xl font-black font-outfit text-white tracking-tight mt-1 leading-[1.15]">
                      Train Smarter with <br />
                      <span className="bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] bg-clip-text text-transparent">Precision AI Telemetry</span>
                    </h1>
                    <p className="text-xs text-gray-400 mt-2 leading-relaxed max-w-sm">
                      Your metabolic blueprint is live. Today is Legs & Conditioning day.
                    </p>
                  </div>
                  
                  <div className="flex gap-2 flex-wrap mt-2">
                    <button onClick={() => setActiveTab('workouts')} className="shimmer-btn flex items-center justify-center gap-1.5 px-4 py-2 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] hover:shadow-[0_0_15px_rgba(0,210,255,0.3)] text-[10px] font-bold text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer">
                      <i className="lucide-play w-3 h-3 fill-white"></i> Start Today's Split
                    </button>
                    <button onClick={() => setActiveTab('coach')} className="flex items-center justify-center gap-1.5 px-4 py-2 border border-white/5 hover:border-white/10 hover:bg-white/5 text-[10px] font-bold text-gray-400 hover:text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer">
                      <i className="lucide-message-square w-3 h-3"></i> Ask Coach Nova
                    </button>
                  </div>
                </div>
              </div>

              {/* Vitals Top Deck Stack (1/3 width, perfect vertical fit) */}
              <div className="flex flex-col gap-4 justify-between h-full min-h-[220px]">
                
                {/* Calories Burned card */}
                <div className="glass-panel p-4 rounded-xl flex items-center justify-between flex-1">
                  <div className="flex items-center gap-3">
                    <div className="p-2.5 bg-red-500/10 text-red-500 rounded-lg shrink-0"><i className="lucide-activity w-4.5 h-4.5"></i></div>
                    <div>
                      <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block">Calories Burned</span>
                      <span className="text-lg font-black font-outfit text-white block mt-0.5">632 <span className="text-[10px] font-normal text-gray-400">kcal</span></span>
                    </div>
                  </div>
                  <svg className="w-16 h-6 text-[#00D2FF] shrink-0" viewBox="0 0 100 30" fill="none">
                    <path d="M0,25 Q15,10 30,20 T60,5 T90,22 T100,10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                  </svg>
                </div>

                {/* Active Minutes card */}
                <div className="glass-panel p-4 rounded-xl flex items-center justify-between flex-1">
                  <div className="flex items-center gap-3">
                    <div className="p-2.5 bg-amber-500/10 text-amber-500 rounded-lg shrink-0"><i className="lucide-clock w-4.5 h-4.5"></i></div>
                    <div>
                      <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block">Active Minutes</span>
                      <span className="text-lg font-black font-outfit text-white block mt-0.5">78 <span className="text-[10px] font-normal text-gray-400">min</span></span>
                    </div>
                  </div>
                  <svg className="w-16 h-6 text-amber-500 shrink-0" viewBox="0 0 100 30" fill="none">
                    <path d="M0,20 Q15,5 35,25 T70,12 T90,28 T100,18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                  </svg>
                </div>

                {/* Recovery Score card */}
                <div className="glass-panel p-4 rounded-xl flex items-center justify-between flex-1 cursor-pointer hover:border-[#00D2FF]/20" onClick={() => setShowRecoveryModal(true)}>
                  <div className="flex items-center gap-3">
                    <div className="p-2.5 bg-[#00F0FF]/10 text-[#00F0FF] rounded-lg shrink-0"><i className="lucide-sparkles w-4.5 h-4.5"></i></div>
                    <div>
                      <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block">Recovery Rating</span>
                      <span className="text-lg font-black font-outfit text-white block mt-0.5">{recoveryScore}% <span className="text-[8px] font-bold text-emerald-400 uppercase tracking-widest ml-1">{recoveryAdvice}</span></span>
                    </div>
                  </div>
                  <div className="relative w-9 h-9 flex items-center justify-center shrink-0">
                    <svg className="w-full h-full transform -rotate-90">
                      <circle cx="18" cy="18" r="15" className="stroke-white/5" strokeWidth="2.5" fill="transparent" />
                      <circle cx="18" cy="18" r="15" className={recoveryIndicator} strokeWidth="2.5" fill="transparent" strokeDasharray={2*Math.PI*15} strokeDashoffset={2*Math.PI*15*(1 - recoveryScore/100)} strokeLinecap="round" />
                    </svg>
                    <span className="absolute text-[8px] font-black font-outfit text-white">{recoveryScore}</span>
                  </div>
                </div>

              </div>

            </div>

            {/* Row 2: Middle Row Action Center Grid (3 Columns) */}
            <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 items-stretch">
              
              {/* 1. Today's Plan */}
              <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between min-h-[440px]">
                <div className="flex justify-between items-center mb-4">
                  <div>
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Today's Workout Plan</h4>
                    <span className="text-[9px] text-gray-500 font-semibold block mt-0.5">Upper Body Hypertrophy Split • 45 min</span>
                  </div>
                  <span onClick={() => setActiveTab('workouts')} className="text-[9px] font-bold text-gray-400 hover:text-white cursor-pointer transition-colors">
                    Plan Details →
                  </span>
                </div>

                {/* SVG Muscle Highlighting */}
                <div className="flex-1 flex items-center justify-center p-3 relative h-36 bg-black/15 rounded-xl border border-white/5 mb-4">
                  <svg className="h-[95%] w-auto text-gray-600" viewBox="0 0 100 200" fill="none">
                    <circle cx="50" cy="20" r="10" className="stroke-white/10" strokeWidth="1.5" />
                    <path d="M47,30 L53,30 L53,35 L47,35 Z" className="fill-white/10" />
                    <path d="M35,35 L65,35 L60,110 L40,110 Z" className="stroke-white/10 fill-white/5" strokeWidth="1.5" />
                    <path d="M37,42 L63,42 L58,70 L42,70 Z" className="fill-[#00F0FF]/15 stroke-[#00F0FF]/40" strokeWidth="1" />
                    <path d="M35,35 L20,60 L12,90 L18,92 L26,65 L35,50 Z" className="stroke-white/10 fill-white/5" strokeWidth="1.5" />
                    <path d="M65,35 L80,60 L88,90 L82,92 L74,65 L65,50 Z" className="stroke-white/10 fill-white/5" strokeWidth="1.5" />
                    <circle cx="28" cy="45" r="4.5" className="fill-[#9D00FF]/60 stroke-[#9D00FF]" strokeWidth="0.8" />
                    <circle cx="72" cy="45" r="4.5" className="fill-[#9D00FF]/60 stroke-[#9D00FF]" strokeWidth="0.8" />
                    <path d="M22,55 L16,80" className="stroke-[#00D2FF]" strokeWidth="2" strokeLinecap="round" />
                    <path d="M78,55 L84,80" className="stroke-[#00D2FF]" strokeWidth="2" strokeLinecap="round" />
                    <path d="M40,110 L35,160 L30,200 L39,200 L44,162 L48,110 Z" className="stroke-white/10 fill-white/5" strokeWidth="1.5" />
                    <path d="M60,110 L65,160 L70,200 L61,200 L56,162 L52,110 Z" className="stroke-white/10 fill-white/5" strokeWidth="1.5" />
                  </svg>
                  
                  <span className="absolute top-2 left-3 px-1.5 py-0.5 rounded bg-[#00D2FF]/10 border border-[#00D2FF]/20 text-[7px] font-bold text-[#00D2FF] uppercase tracking-wide">Target: Upper Chest / Arms</span>
                  <span className="absolute bottom-2 right-3 px-1.5 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20 text-[7px] font-bold text-emerald-400 uppercase tracking-wide">High Split Volume</span>
                </div>

                {/* Exercises checklist */}
                <div className="flex flex-col gap-1.5 mb-4">
                  {[
                    { key: 'ex1', name: "Dumbbell Chest Bench Press", sets: "4 sets x 12 reps" },
                    { key: 'ex2', name: "Wide Grip Pull Ups", sets: "4 sets x 10 reps" },
                    { key: 'ex3', name: "Shoulder Overhead Press", sets: "3 sets x 12 reps" },
                    { key: 'ex4', name: "Seated Cable Row Split", sets: "4 sets x 12 reps" }
                  ].map((ex) => (
                    <div 
                      key={ex.key} 
                      onClick={() => toggleExercise(ex.key)} 
                      className={`flex items-center justify-between p-2 rounded-xl border transition-all cursor-pointer ${
                        completedEx[ex.key] 
                          ? 'bg-emerald-500/5 border-emerald-500/10 text-gray-400' 
                          : 'bg-[#121212]/30 border-white/5 hover:border-white/10 text-white'
                      }`}
                    >
                      <div className="flex items-center gap-2">
                        <div className={`w-3.5 h-3.5 rounded border flex items-center justify-center transition-all ${
                          completedEx[ex.key] ? 'bg-emerald-500 border-emerald-500 text-white' : 'border-white/20'
                        }`}>
                          {completedEx[ex.key] && <i className="lucide-check w-2.5 h-2.5 stroke-[3px]"></i>}
                        </div>
                        <span className="text-[10px] font-bold">{ex.name}</span>
                      </div>
                      <span className="text-[9px] text-gray-500 font-semibold">{ex.sets}</span>
                    </div>
                  ))}
                </div>

                <div className="flex gap-2">
                  <button onClick={() => setActiveTab('workouts')} className="shimmer-btn flex-1 flex items-center justify-center gap-1.5 py-2.5 rounded-xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] font-bold text-[10px] text-white cursor-pointer uppercase tracking-wider">
                    <i className="lucide-play w-3 h-3 fill-white"></i> Play Split
                  </button>
                  <button onClick={() => setActiveTab('workouts')} className="p-2.5 bg-white/3 border border-white/5 hover:bg-white/10 rounded-xl cursor-pointer text-gray-400 active:scale-95 transition-all">
                    <i className="lucide-calendar w-3.5 h-3.5"></i>
                  </button>
                </div>
              </div>

              {/* 2. Nutrition Summary */}
              <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between min-h-[440px]">
                <div className="flex justify-between items-center mb-4">
                  <div>
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Nutrition & Fuel Balance</h4>
                    <span className="text-[9px] text-gray-500 font-semibold block mt-0.5">Scale calories and macronutrients</span>
                  </div>
                  
                  <select 
                    value={dietProfile} 
                    onChange={(e) => { setDietProfile(e.target.value); playBeep(900, 'sine', 0.08); }} 
                    className="bg-[#121212] border border-white/5 rounded-lg px-2.5 py-1 text-[9px] font-bold text-gray-400 cursor-pointer outline-none hover:border-white/20 transition-all font-outfit"
                  >
                    <option value="highprotein">🍗 High Protein</option>
                    <option value="vegetarian">🥗 Vegetarian</option>
                    <option value="vegan">🌱 Vegan</option>
                    <option value="keto">🥩 Keto</option>
                    <option value="indian">🍛 Indian Diet</option>
                    <option value="budget">🥚 Budget Diet</option>
                  </select>
                </div>

                {/* Calorie Ring Progress */}
                <div className="flex items-center justify-around gap-4 mb-4 bg-black/15 p-4 rounded-xl border border-white/5 flex-wrap">
                  <div className="relative w-24 h-24 flex items-center justify-center shrink-0">
                    <svg className="w-full h-full transform -rotate-90">
                      <circle cx="48" cy="48" r="40" className="stroke-white/5" strokeWidth="5" fill="transparent" />
                      <circle cx="48" cy="48" r="40" className="stroke-[#00D2FF]" strokeWidth="5" fill="transparent" strokeDasharray={2*Math.PI*40} strokeDashoffset={2*Math.PI*40*(1 - Math.min(1.0, caloriesLog / targetCal))} strokeLinecap="round" />
                    </svg>
                    <div className="absolute text-center">
                      <span className="text-base font-black font-outfit text-white leading-none block">{caloriesLog.toLocaleString()}</span>
                      <span className="text-[8px] font-semibold text-gray-500 uppercase tracking-widest block mt-0.5">/ {Math.round(targetCal).toLocaleString()} kcal</span>
                    </div>
                  </div>

                  <div className="flex flex-col gap-1.5 font-outfit shrink-0 min-w-[110px]">
                    <div>
                      <span className="text-[8px] text-[#00D2FF] font-bold block uppercase tracking-wider">🍗 Protein ({macros.protein.pct}%)</span>
                      <span className="text-xs font-black text-white">{macros.protein.grams}g <span className="text-[9px] text-gray-500 font-normal">target</span></span>
                    </div>
                    <div>
                      <span className="text-[8px] text-[#9D00FF] font-bold block uppercase tracking-wider">🍚 Carbs ({macros.carbs.pct}%)</span>
                      <span className="text-xs font-black text-white">{macros.carbs.grams}g <span className="text-[9px] text-gray-500 font-normal">target</span></span>
                    </div>
                    <div>
                      <span className="text-[8px] text-yellow-400 font-bold block uppercase tracking-wider">🥑 Fats ({macros.fat.pct}%)</span>
                      <span className="text-xs font-black text-white">{macros.fat.grams}g <span className="text-[9px] text-gray-500 font-normal">target</span></span>
                    </div>
                  </div>
                </div>

                {/* Quick Calorie Logger */}
                <div className="flex gap-2 mb-4 justify-between items-center px-1 font-outfit">
                  <span className="text-[9px] font-bold text-gray-500 uppercase tracking-wider">Quick Log:</span>
                  <div className="flex gap-1.5">
                    <button onClick={() => addCalories(200)} className="px-2 py-1 rounded-lg bg-white/3 hover:bg-white/5 border border-white/5 text-[9px] font-bold text-gray-300 cursor-pointer transition-all">+200 kcal</button>
                    <button onClick={() => addCalories(500)} className="px-2 py-1 rounded-lg bg-white/3 hover:bg-white/5 border border-white/5 text-[9px] font-bold text-gray-300 cursor-pointer transition-all">+500 kcal</button>
                    <button onClick={() => addCalories(-300)} className="px-2 py-1 rounded-lg bg-white/3 hover:bg-white/5 border border-white/5 text-[9px] font-bold text-red-400 cursor-pointer transition-all">-300 kcal</button>
                  </div>
                </div>

                {/* Next Meal Preview Card */}
                <div className="p-2.5 rounded-xl bg-[#121212]/30 border border-white/5 flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full border border-white/10 bg-black/40 flex items-center justify-center shrink-0 text-lg shadow-[0_0_12px_rgba(255,255,255,0.05)] relative overflow-hidden animate-[pulse_4s_infinite]">
                    🍛
                    <div className="absolute inset-0 bg-gradient-to-tr from-emerald-500/10 to-transparent pointer-events-none" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between" style={{ display: 'flex', justify: 'space-between' }}>
                      <span className="text-[8px] font-bold text-gray-500 uppercase tracking-wider block">Next Meal</span>
                      <span className="text-[8px] font-bold text-emerald-400 uppercase tracking-wider font-outfit">{currentNextMeal.time}</span>
                    </div>
                    <span className="text-[11px] font-bold text-white block mt-0.5 truncate">{currentNextMeal.name}</span>
                    <span className="text-[8px] font-semibold text-gray-400 block mt-0.5 tracking-wide">{currentNextMeal.tag} profile scaled</span>
                  </div>
                </div>

                <button onClick={() => setActiveTab('nutrition')} className="w-full text-center py-2.5 border border-white/5 hover:border-white/10 hover:bg-white/3 rounded-xl text-[10px] font-bold text-gray-300 uppercase tracking-wider cursor-pointer mt-4">
                  Macronutrient Dashboard
                </button>
              </div>

              {/* 3. AI Insights & Bulletins Console */}
              <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between min-h-[440px]">
                <div className="flex justify-between items-center mb-4">
                  <div className="flex items-center gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Coach Nova Bulletins</h4>
                  </div>
                  <span onClick={() => setActiveTab('coach')} className="text-[9px] font-bold text-gray-400 hover:text-white cursor-pointer transition-colors">
                    Speak to Coach →
                  </span>
                </div>

                {/* Bulletins Alert Stack */}
                <div className="flex-1 flex flex-col gap-3 overflow-y-auto max-h-[290px] pr-1">
                  {activeBulletins.map((blt, idx) => {
                    let bCl = "border-white/5 bg-white/3 text-gray-300";
                    let iCl = "text-gray-400 bg-white/5";
                    if (blt.type === "success") { bCl = "border-emerald-500/10 bg-emerald-500/5 text-gray-300"; iCl = "text-emerald-400 bg-emerald-500/10"; }
                    else if (blt.type === "warning") { bCl = "border-electricBlue/10 bg-electricBlue/5 text-gray-300"; iCl = "text-electricBlue bg-electricBlue/10"; }
                    else if (blt.type === "danger") { bCl = "border-red-500/10 bg-red-500/5 text-red-300"; iCl = "text-red-400 bg-red-500/10"; }
                    else if (blt.type === "info") { bCl = "border-amber-500/10 bg-amber-500/5 text-gray-300"; iCl = "text-amber-400 bg-amber-500/10"; }

                    return (
                      <div key={idx} className={`p-3 rounded-xl border flex items-start gap-3 transition-all ${bCl}`}>
                        <div className={`p-2 rounded-lg shrink-0 ${iCl}`}>
                          <i className={`${blt.icon} w-3.5 h-3.5`}></i>
                        </div>
                        <p className="text-[10px] leading-relaxed font-outfit font-medium">{blt.text}</p>
                      </div>
                    );
                  })}
                </div>

                <button onClick={() => setActiveTab('coach')} className="shimmer-btn w-full text-center py-2.5 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] hover:shadow-[0_0_15px_rgba(0,210,255,0.3)] rounded-xl text-[10px] font-bold text-white uppercase tracking-wider cursor-pointer mt-4">
                  Open Coach Chat Console
                </button>
              </div>

            </div>

            {/* Row 3: Metrics Sparlines + Streaks & Hydration side-by-side */}
            <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 items-stretch">
              
              {/* Vitals Progress Metrics Sparklines (2/3 width) */}
              <div className="xl:col-span-2 glass-panel p-5 rounded-2xl flex flex-col justify-between min-h-[180px]">
                <div className="flex justify-between items-center mb-4">
                  <div>
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Weekly Biometric Delta Tracking</h4>
                    <p className="text-[9px] text-gray-500 mt-0.5">Real-time physiological telemetry logs</p>
                  </div>
                  <span className="text-[8px] font-bold text-emerald-400 bg-emerald-500/5 border border-emerald-500/10 px-2 py-0.5 rounded uppercase font-outfit">Vitals Synced</span>
                </div>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 items-center">
                  
                  {/* Weight */}
                  <div className="p-3 bg-black/15 border border-white/5 rounded-xl flex flex-col justify-between h-24 relative overflow-hidden group hover:border-[#00D2FF]/20 transition-all">
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Body Weight</span>
                      <span className="text-sm font-black font-outfit text-white mt-1 block">{currentWeight} <span className="text-[9px] font-normal text-gray-400">kg</span></span>
                      <span className="text-[8px] font-bold text-emerald-400 mt-0.5 block">↓ 1.2 kg delta</span>
                    </div>
                    <svg className="absolute bottom-0 left-0 w-full h-8 text-[#00D2FF] pointer-events-none" viewBox="0 0 100 40">
                      <path d="M0,40 L0,35 Q20,38 40,25 T80,18 T100,5 L100,40 Z" fill="rgba(0, 210, 255, 0.03)" />
                      <path d="M0,35 Q20,38 40,25 T80,18 T100,5" stroke="currentColor" strokeWidth="1.5" fill="none" />
                    </svg>
                  </div>

                  {/* Muscle Mass */}
                  <div className="p-3 bg-black/15 border border-white/5 rounded-xl flex flex-col justify-between h-24 relative overflow-hidden group hover:border-[#9D00FF]/20 transition-all">
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Muscle Mass</span>
                      <span className="text-sm font-black font-outfit text-white mt-1 block">34.2 <span className="text-[9px] font-normal text-gray-400">kg</span></span>
                      <span className="text-[8px] font-bold text-emerald-400 mt-0.5 block">↑ 0.8 kg delta</span>
                    </div>
                    <svg className="absolute bottom-0 left-0 w-full h-8 text-[#9D00FF] pointer-events-none" viewBox="0 0 100 40">
                      <path d="M0,40 L0,32 Q25,28 50,15 T80,8 T100,2 L100,40 Z" fill="rgba(157, 0, 255, 0.03)" />
                      <path d="M0,32 Q25,28 50,15 T80,8 T100,2" stroke="currentColor" strokeWidth="1.5" fill="none" />
                    </svg>
                  </div>

                  {/* Body Fat */}
                  <div className="p-3 bg-black/15 border border-white/5 rounded-xl flex flex-col justify-between h-24 relative overflow-hidden group hover:border-yellow-400/20 transition-all">
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Body Fat</span>
                      <span className="text-sm font-black font-outfit text-white mt-1 block">14.6 <span className="text-[9px] font-normal text-gray-400">%</span></span>
                      <span className="text-[8px] font-bold text-emerald-400 mt-0.5 block">↓ 1.1% delta</span>
                    </div>
                    <svg className="absolute bottom-0 left-0 w-full h-8 text-yellow-400 pointer-events-none" viewBox="0 0 100 40">
                      <path d="M0,40 L0,8 Q20,18 50,22 T80,30 T100,32 L100,40 Z" fill="rgba(250, 204, 21, 0.03)" />
                      <path d="M0,8 Q20,18 50,22 T80,30 T100,32" stroke="currentColor" strokeWidth="1.5" fill="none" />
                    </svg>
                  </div>

                  {/* Strength Score */}
                  <div className="p-3 bg-black/15 border border-white/5 rounded-xl flex flex-col justify-between h-24 relative overflow-hidden group hover:border-emerald-400/20 transition-all">
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Strength Index</span>
                      <span className="text-sm font-black font-outfit text-white mt-1 block">85 <span className="text-[9px] font-normal text-gray-400">/100</span></span>
                      <span className="text-[8px] font-bold text-emerald-400 mt-0.5 block">↑ 5 pts delta</span>
                    </div>
                    <svg className="absolute bottom-0 left-0 w-full h-8 text-emerald-400 pointer-events-none" viewBox="0 0 100 40">
                      <path d="M0,40 L0,30 Q30,28 60,18 T90,5 T100,2 L100,40 Z" fill="rgba(52, 211, 153, 0.03)" />
                      <path d="M0,30 Q30,28 60,18 T90,5 T100,2" stroke="currentColor" strokeWidth="1.5" fill="none" />
                    </svg>
                  </div>

                </div>
              </div>

              {/* streake checklist and water tracking grouped cleanly (1/3 width) */}
              <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between min-h-[180px]">
                <div className="flex justify-between items-center">
                  <div>
                    <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Daily Vitals Streak</span>
                    <span className="text-lg font-black font-outfit text-white block mt-0.5">12 Days</span>
                  </div>
                  <div className="relative w-8 h-8 flex items-center justify-center shrink-0">
                    <div className="absolute w-5 h-5 rounded-full bg-gradient-to-t from-orange-500 to-yellow-400 opacity-20 blur-[8px] pointer-events-none" />
                    <svg className="w-8 h-8 text-orange-500 drop-shadow-[0_0_8px_rgba(249,115,22,0.5)]" viewBox="0 0 24 24" fill="none">
                      <path d="M12,2 C12,2 17,7.5 17,11.5 C17,14.5 14.8,17 12,17 C9.2,17 7,14.5 7,11.5 C7,7.5 12,2 12,2 Z" fill="url(#flameGrad2)" />
                      <defs>
                        <linearGradient id="flameGrad2" x1="0%" y1="100%" x2="0%" y2="0%">
                          <stop offset="0%" stopColor="#EA580C" />
                          <stop offset="60%" stopColor="#F97316" />
                          <stop offset="100%" stopColor="#FACC15" />
                        </linearGradient>
                      </defs>
                    </svg>
                  </div>
                </div>

                {/* Checklist Mon-Sun */}
                <div className="flex justify-between items-center bg-black/15 p-2 rounded-xl border border-white/5 my-3">
                  {[
                    { label: 'M', checked: true },
                    { label: 'T', checked: true },
                    { label: 'W', checked: true },
                    { label: 'T', checked: true },
                    { label: 'F', checked: true },
                    { label: 'S', checked: true },
                    { label: 'S', checked: false }
                  ].map((day, idx) => (
                    <div key={idx} className="flex flex-col items-center gap-1 cursor-pointer">
                      <span className="text-[8px] text-gray-500 font-bold uppercase">{day.label}</span>
                      <div className={`w-4 h-4 rounded-full flex items-center justify-center border transition-all ${
                        day.checked 
                          ? 'bg-gradient-to-r from-orange-500 to-yellow-500 border-transparent text-white shadow-[0_0_6px_rgba(249,115,22,0.3)]' 
                          : 'border-white/10 bg-transparent'
                      }`}>
                        {day.checked && <i className="lucide-check w-2.5 h-2.5 stroke-[2.5px] text-black"></i>}
                      </div>
                    </div>
                  ))}
                </div>

                {/* Hydration tracker */}
                <div className="flex items-center justify-between p-2 rounded-xl bg-black/15 border border-white/5">
                  <div className="flex items-center gap-2">
                    <div className="p-1.5 bg-blue-500/10 text-blue-400 rounded-lg"><i className="lucide-droplet w-3.5 h-3.5"></i></div>
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block">Hydration Daily</span>
                      <span className="text-[10px] font-black text-white">{(waterCups * 0.25).toFixed(2)} / 3.50 L</span>
                    </div>
                  </div>
                  <div className="flex gap-1">
                    <button onClick={() => handleWaterLog(Math.max(0, waterCups - 1))} className="px-2 py-1 rounded-md bg-white/5 border border-white/5 hover:bg-white/10 text-[9px] font-bold text-gray-400 cursor-pointer active:scale-95 transition-all">-</button>
                    <button onClick={() => handleWaterLog(Math.min(24, waterCups + 1))} className="px-2.5 py-1 rounded-md bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-[9px] font-bold text-white cursor-pointer active:scale-95 transition-all">+</button>
                  </div>
                </div>

              </div>

            </div>

            {/* Daily Vital Check-In Modal */}
            {showRecoveryModal && (
              <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-[fade-in_0.3s_ease-out]">
                <div className="glass-panel p-6 rounded-2xl max-w-md w-full relative">
                  <button onClick={() => setShowRecoveryModal(false)} className="absolute top-4 right-4 p-2 text-gray-500 hover:text-white transition-colors cursor-pointer">
                    <i className="lucide-x w-5 h-5"></i>
                  </button>
                  
                  <div className="flex items-center gap-2 mb-4">
                    <div className="p-2 bg-[#00F0FF]/10 text-[#00F0FF] rounded-lg shrink-0"><i className="lucide-sparkles w-4.5 h-4.5"></i></div>
                    <h4 className="text-sm font-bold font-outfit text-white uppercase tracking-wider">Metabolic Vital Check-In</h4>
                  </div>
                  
                  <div className="flex items-center justify-between mb-6 p-4 rounded-xl bg-black/40 border border-white/5">
                    <div>
                      <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">Calculated Recovery</span>
                      <span className={`text-lg font-black font-outfit ${recoveryColor} mt-0.5 block transition-colors`}>{recoveryScore}%</span>
                    </div>
                    <div className={`px-2.5 py-1 rounded-lg text-[8px] font-bold ${recoveryColor} ${recoveryBg} transition-all tracking-wider text-center max-w-[120px] font-outfit uppercase`}>
                      {recoveryAdvice}
                    </div>
                  </div>

                  {/* Sleep Hours Slider */}
                  <div className="mb-4">
                    <div className="flex justify-between items-center text-[10px] text-gray-400 font-bold font-outfit mb-2 uppercase">
                      <span>1. Sleep Quality</span>
                      <span className="text-white">{sleepHrs} Hours</span>
                    </div>
                    <input 
                      type="range" min="4" max="10" step="1" 
                      value={sleepHrs} 
                      onChange={(e) => { setSleepHrs(parseInt(e.target.value)); playBeep(500 + parseInt(e.target.value)*30, 'sine', 0.05); }}
                      className="w-full accent-[#00F0FF] cursor-pointer bg-white/5 rounded-lg appearance-none h-1"
                    />
                  </div>

                  {/* Muscle Soreness Buttons */}
                  <div className="mb-4">
                    <span className="block text-[10px] text-gray-400 font-bold font-outfit mb-2 uppercase">2. Muscle Soreness</span>
                    <div className="grid grid-cols-3 gap-2">
                      {['Mild', 'Moderate', 'Severe'].map(lvl => (
                        <button 
                          key={lvl} 
                          onClick={() => { setSoreness(lvl); playBeep(700, 'triangle', 0.06); }}
                          className={`py-2 rounded-xl text-[9px] font-bold transition-all border outline-none cursor-pointer ${
                            soreness === lvl 
                              ? 'border-[#00D2FF]/40 bg-[#00D2FF]/10 text-white shadow-[0_0_10px_rgba(0,210,255,0.12)]' 
                              : 'border-white/5 bg-white/3 text-gray-400 hover:text-white'
                          }`}
                        >
                          {lvl === 'Mild' ? '🟢 Mild' : lvl === 'Moderate' ? '🟡 Medium' : '🔴 Severe'}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Energy Level Slider */}
                  <div className="mb-6">
                    <div className="flex justify-between items-center text-[10px] text-gray-400 font-bold font-outfit mb-2 uppercase">
                      <span>3. Energy Levels</span>
                      <span className="text-white">{energy} / 10</span>
                    </div>
                    <input 
                      type="range" min="3" max="10" step="1" 
                      value={energy} 
                      onChange={(e) => { setEnergy(parseInt(e.target.value)); playBeep(400 + parseInt(e.target.value)*40, 'sine', 0.05); }}
                      className="w-full accent-[#9D00FF] cursor-pointer bg-white/5 rounded-lg appearance-none h-1"
                    />
                  </div>

                  <button onClick={() => setShowRecoveryModal(false)} className="w-full py-3 rounded-xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-[10px] font-bold text-white transition-all active:scale-[0.98] cursor-pointer text-center uppercase tracking-wider">
                    Update Recovery Score
                  </button>
                </div>
              </div>
            )}

          </div>
        );
      };"""

content = re.sub(dashboard_pattern, new_dashboard, content, flags=re.DOTALL)


# 3. Add Mobile Bottom Navigation Bar in App component's return layout
# Let's find the closing tag of App viewport main content.
# Main content wrapper:
#               {/* MAIN CONTENT WORKSPACE VIEWPORT */}
#               <main className="flex-1 p-6 overflow-y-auto max-h-[calc(100vh-4rem)] relative z-10 w-full">
#                 
#                 {activeTab === 'dashboard' && (
# ...
#                 )}
#               </main>
# We will append our beautiful mobile bottom navigation bar right before the closing tag of the main content column.
# Let's see: we want to find the `<main>` block and add `mb-16 md:mb-0` to the class, and then place the bottom nav bar right after `</main>`.

old_main_viewport = """              {/* MAIN CONTENT WORKSPACE VIEWPORT */}
              <main className="flex-1 p-6 overflow-y-auto max-h-[calc(100vh-4rem)] relative z-10 w-full">"""

new_main_viewport = """              {/* MAIN CONTENT WORKSPACE VIEWPORT */}
              <main className="flex-1 p-6 overflow-y-auto max-h-[calc(100vh-4rem)] relative z-10 w-full mb-16 md:mb-0">"""

content = content.replace(old_main_viewport, new_main_viewport)

# Now, let's find the end of `</main>` and insert the mobile bottom navigation bar.
# In the `App` component return block:
#               {/* MAIN CONTENT WORKSPACE VIEWPORT */}
#               <main className="... mb-16 md:mb-0">
#                 ...
#               </main>
#               
#               {/* MOBILE BOTTOM NAVIGATION BAR */}
#               ...

old_main_end = """              </main>
            </div>"""

new_main_end = """              </main>

              {/* MOBILE BOTTOM NAVIGATION BAR */}
              <div className="flex md:hidden fixed bottom-0 left-0 w-full bg-[#0A0A0C]/90 backdrop-blur-lg border-t border-white/5 py-3 px-6 justify-between items-center z-50 shadow-[0_-10px_30px_rgba(0,0,0,0.8)] select-none mobile-bottom-nav" style={{ display: 'flex', justifyContent: 'space-between' }}>
                <button onClick={() => setActiveTab('dashboard')} className={`flex flex-col items-center gap-1.5 cursor-pointer outline-none bg-transparent border-none ${activeTab === 'dashboard' ? 'text-electricBlue' : 'text-gray-500 hover:text-gray-300'}`}>
                  <i className="lucide-layout-dashboard w-5 h-5"></i>
                  <span className="text-[8px] font-bold uppercase tracking-wider font-outfit">Home</span>
                </button>
                <button onClick={() => setActiveTab('coach')} className={`flex flex-col items-center gap-1.5 cursor-pointer outline-none bg-transparent border-none ${activeTab === 'coach' ? 'text-[#9D00FF]' : 'text-gray-500 hover:text-gray-300'}`}>
                  <i className="lucide-sparkles w-5 h-5"></i>
                  <span className="text-[8px] font-bold uppercase tracking-wider font-outfit">Nova AI</span>
                </button>
                <button onClick={() => setActiveTab('workouts')} className={`flex flex-col items-center gap-1.5 cursor-pointer outline-none bg-transparent border-none ${activeTab === 'workouts' ? 'text-electricBlue' : 'text-gray-500 hover:text-gray-300'}`}>
                  <i className="lucide-dumbbell w-5 h-5"></i>
                  <span className="text-[8px] font-bold uppercase tracking-wider font-outfit">Train</span>
                </button>
                <button onClick={() => setActiveTab('nutrition')} className={`flex flex-col items-center gap-1.5 cursor-pointer outline-none bg-transparent border-none ${activeTab === 'nutrition' ? 'text-electricBlue' : 'text-gray-500 hover:text-gray-300'}`}>
                  <i className="lucide-apple w-5 h-5"></i>
                  <span className="text-[8px] font-bold uppercase tracking-wider font-outfit">Fuel</span>
                </button>
              </div>
            </div>"""

content = content.replace(old_main_end, new_main_end)


# 4. Chatbot suggestions refinements inside Chatbot component (lines 2224 onwards)
# Let's add suggestion tags inside Chatbot component just above the input form, which allows the user to click one of three quick questions:
# "💡 Bench with shoulder pain?", "💡 Indian protein snacks?", "💡 Skip biometrics".
# Let's inspect the input block in Chatbot in preview.html.
# Currently, it has a div wrap with form:
#             <form onSubmit={handleSend} className="flex gap-2 relative mt-4">
#               ...
#             </form>
# Let's find this form block in Chatbot.
# To find it, let's look at the surrounding code of the form onSubmit.
# Let's replace the form wrapping in Chatbot with our suggestions + form wrap!

chatbot_form_pattern = r'<form onSubmit=\{handleSend\} className="flex gap-2 relative mt-4">.*?<input.*?type="text".*?placeholder=\{placeholderText\}.*?/>.*?<button.*?>.*?</form>'

new_chatbot_form = """{/* Suggestion tags above input */}
            <div className="flex gap-1.5 overflow-x-auto py-1 mb-2 select-none" style={{ scrollbarWidth: 'none' }}>
              <button 
                type="button" 
                onClick={() => {
                  setInput("💡 Suggest an Indian high protein snack plan.");
                  playBeep(800, 'sine', 0.08);
                }}
                className="suggestion-tag shrink-0 px-2.5 py-1 rounded-full text-[9px] font-bold text-gray-400 font-outfit cursor-pointer border border-white/5 active:scale-95"
              >
                🍛 Indian Protein Snack
              </button>
              <button 
                type="button" 
                onClick={() => {
                  setInput("💡 How do I modify squats with knee joint issues?");
                  playBeep(800, 'sine', 0.08);
                }}
                className="suggestion-tag shrink-0 px-2.5 py-1 rounded-full text-[9px] font-bold text-gray-400 font-outfit cursor-pointer border border-white/5 active:scale-95"
              >
                🩹 Squats & Knee Pain
              </button>
              <button 
                type="button" 
                onClick={() => {
                  setInput("💡 Skip biometrics diagnostic");
                  playBeep(800, 'sine', 0.08);
                }}
                className="suggestion-tag shrink-0 px-2.5 py-1 rounded-full text-[9px] font-bold text-gray-400 font-outfit cursor-pointer border border-white/5 active:scale-95"
              >
                ⏩ Skip Diagnostics
              </button>
            </div>

            <form onSubmit={handleSend} className="flex gap-2 relative">
              <input 
                type="text" 
                value={input} 
                onChange={(e) => setInput(e.target.value)} 
                placeholder={placeholderText} 
                className="flex-1 bg-[#121212] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4.5 py-3 text-xs text-white outline-none w-full pr-24 transition-all"
                disabled={activeStep > totalSteps || typing}
              />
              <div className="absolute right-2 top-1/2 -translate-y-1/2 flex items-center gap-1">
                {mode === 'full' && (
                  <button 
                    type="button" 
                    onClick={toggleVoice} 
                    className={`p-1.5 rounded-lg border transition-all cursor-pointer ${
                      voiceEnabled 
                        ? 'bg-[#00D2FF]/10 border-[#00D2FF]/20 text-[#00D2FF]' 
                        : 'bg-white/3 border-white/5 text-gray-500 hover:text-white'
                    }`}
                    title="Toggle Speech Synthesis Voice output"
                  >
                    <i className="lucide-volume-2 w-3.5 h-3.5"></i>
                  </button>
                )}
                <button 
                  type="submit" 
                  className="p-1.5 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white rounded-lg cursor-pointer hover:shadow-[0_0_10px_rgba(0,210,255,0.4)] active:scale-95 transition-all border-none outline-none"
                  disabled={activeStep > totalSteps || typing}
                >
                  <i className="lucide-send w-3.5 h-3.5"></i>
                </button>
              </div>
            </form>"""

# Let's replace the form in Chatbot
content = re.sub(chatbot_form_pattern, new_chatbot_form, content, flags=re.DOTALL)

with open(filePath, "w", encoding="utf-8") as f:
    f.write(content)

print("Dashboard, mobile bottom-nav, visual glow cleaning, and Chatbot suggestion upgrades applied successfully to preview.html!")
