import os

file_path = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai\preview.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Initial file size:", len(content))

# ----------------------------------------------------
# PATCH 1: Head Viewport & PWA Metadata Injections
# ----------------------------------------------------
head_target = """    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Fit Nova AI — Premium Futuristic AI Gym & Fitness Platform</title>
    <meta name="description" content="Elevate your training with Fit Nova AI. Precision calorie calculations, automated nutrition diets, home/gym workouts, interactive AI chatbot coaching, and custom fitness dashboards.">"""

head_replacement = """    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
    <title>Fit Nova AI — Premium Futuristic AI Gym & Fitness Platform</title>
    <meta name="description" content="Elevate your training with Fit Nova AI. Precision calorie calculations, automated nutrition diets, home/gym workouts, interactive AI chatbot coaching, and custom fitness dashboards.">
    
    <!-- PWA Standalone Meta Tags & Manifest -->
    <link rel="manifest" href="./manifest.json" />
    <meta name="theme-color" content="#08080A" />
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="apple-mobile-web-app-title" content="FitNova AI" />
    <link rel="apple-touch-icon" href="./logo.png" />"""

if head_target in content:
    content = content.replace(head_target, head_replacement)
    print("  [SUCCESS] Patched Head Metadata.")
else:
    print("  [WARNING] Head Target not found.")


# ----------------------------------------------------
# PATCH 2: Custom Styles Insertions
# ----------------------------------------------------
style_target = """    <!-- Custom Styles -->
    <style>
      ::-webkit-scrollbar {"""

style_replacement = """    <!-- Custom Styles -->
    <style>
      /* Safe area paddings for iPhone Notch */
      .pb-safe-bottom {
        padding-bottom: env(safe-area-inset-bottom);
      }
      .pt-safe-top {
        padding-top: env(safe-area-inset-top);
      }

      /* Lock body bounce scrolling on standalone mobile */
      @media (max-width: 1023px) {
        html, body {
          height: 100dvh;
          overflow: hidden;
          position: fixed;
          width: 100vw;
        }
        
        /* Make full chat edge-to-edge on mobile */
        #chatbot {
          position: fixed !important;
          inset: 0 !important;
          z-index: 40 !important;
          background: #08080A !important;
          display: flex !important;
          flex-direction: column !important;
          padding: 0 !important;
          margin: 0 !important;
          height: 100dvh !important;
          padding-top: env(safe-area-inset-top) !important;
          padding-bottom: calc(68px + env(safe-area-inset-bottom)) !important;
        }
        #chatbot > div {
          height: 100% !important;
          max-width: 100% !important;
          margin: 0 !important;
          border-radius: 0 !important;
          border: none !important;
        }
      }

      /* Slide up bottom sheets drawer */
      @keyframes slide-up {
        0% { transform: translateY(100%); }
        100% { transform: translateY(0); }
      }

      /* Bouncing spring scale overlay animation */
      @keyframes spring-scale {
        0% { transform: scale(0.3); opacity: 0; }
        70% { transform: scale(1.1); }
        90% { transform: scale(0.95); }
        100% { transform: scale(1); opacity: 1; }
      }

      /* Swiper Scroll hides */
      .hide-scrollbar::-webkit-scrollbar {
        display: none;
      }
      .hide-scrollbar {
        -ms-overflow-style: none;
        scrollbar-width: none;
      }

      ::-webkit-scrollbar {"""

if style_target in content:
    content = content.replace(style_target, style_replacement)
    print("  [SUCCESS] Patched CSS Custom Styles.")
else:
    print("  [WARNING] CSS Style Target not found.")


# ----------------------------------------------------
# PATCH 3: WorkoutCalendar (completedDays & handleMarkComplete celebration)
# ----------------------------------------------------
cal_vars_target = """        // Dynamic stats that update when workouts are completed
        const [completedDays, setCompletedDays] = useState([2, 4, 7, 9, 11, 14, 16, 18, 21, 23, 25]);
        const [missedDays, setMissedDays] = useState([12, 19]);
        const [streak, setStreak] = useState(3);
        const [hydration, setHydration] = useState(12);"""

cal_vars_replacement = """        // Dynamic stats that update when workouts are completed
        const [completedDays, setCompletedDays] = useState([2, 4, 7, 9, 11, 14, 16, 18, 21, 23, 25]);
        const [missedDays, setMissedDays] = useState([12, 19]);
        const [streak, setStreak] = useState(3);
        const [hydration, setHydration] = useState(12);
        const [celebrationDay, setCelebrationDay] = useState(null);"""

if cal_vars_target in content:
    content = content.replace(cal_vars_target, cal_vars_replacement)
    print("  [SUCCESS] Patched Calendar state variables.")
else:
    print("  [WARNING] Calendar state variables target not found.")


cal_complete_target = """        // Mark current workout as fully completed
        const handleMarkComplete = (day) => {
          if (completedDays.includes(day)) return;

          setCompletedDays(prev => [...prev, day].sort((a,b)=>a-b));
          setMissedDays(prev => prev.filter(d => d !== day));
          setStreak(prev => prev + 1);
          
          // Play success chime
          try {
            playBeep(900, 'sine', 0.08);
            setTimeout(() => playBeep(1200, 'sine', 0.1), 120);
          } catch(e) {}

          // Refresh details in modal
          setExerciseChecks({});
          setSelectedDay(null);
        };"""

cal_complete_replacement = """        // Mark current workout as fully completed
        const handleMarkComplete = (day) => {
          if (completedDays.includes(day)) return;

          setCompletedDays(prev => [...prev, day].sort((a,b)=>a-b));
          setMissedDays(prev => prev.filter(d => d !== day));
          setStreak(prev => prev + 1);
          
          // Play success chime
          try {
            playBeep(900, 'sine', 0.08);
            setTimeout(() => playBeep(1200, 'sine', 0.1), 120);
          } catch(e) {}

          // Refresh details in modal
          setExerciseChecks({});
          setSelectedDay(null);
          setCelebrationDay(day); // Trigger achievement celebration!
        };"""

if cal_complete_target in content:
    content = content.replace(cal_complete_target, cal_complete_replacement)
    print("  [SUCCESS] Patched handleMarkComplete.")
else:
    print("  [WARNING] handleMarkComplete target not found.")


# ----------------------------------------------------
# PATCH 4: WorkoutCalendar Monthly vs Weekly Swiper
# ----------------------------------------------------
cal_grid_target = """            {/* 31-Day Grid / Weekly Spline Container */}
            {calendarMode === 'monthly' ? (
              <div className="grid grid-cols-2 sm:grid-cols-7 gap-4 w-full bg-black/10 p-1 rounded-3xl">
                {renderDaysGrid()}
              </div>
            ) : (
              <div className="flex flex-col gap-3 w-full bg-black/10 p-2 rounded-3xl max-w-xl mx-auto">
                <div className="flex items-center justify-between border-b border-white/5 pb-2 px-1 mb-1 font-mono text-[9px] text-gray-500 font-bold select-none uppercase">
                  <span>Simulated Rolling Week View</span>
                  <span>Swipe or scroll below</span>
                </div>
                {renderWeeklyListView()}
              </div>
            )}"""

cal_grid_replacement = """            {/* 31-Day Grid / Weekly Spline Container */}
            {calendarMode === 'monthly' ? (
              <div className="grid grid-cols-2 sm:grid-cols-7 gap-4 w-full bg-black/10 p-1 rounded-3xl">
                {renderDaysGrid()}
              </div>
            ) : (
              <div className="flex flex-col gap-4 w-full bg-black/10 p-3 rounded-3xl max-w-xl mx-auto">
                {/* Desktop vertical weekly list */}
                <div className="hidden lg:flex flex-col gap-3 w-full">
                  <div className="flex items-center justify-between border-b border-white/5 pb-2 px-1 mb-1 font-mono text-[9px] text-gray-500 font-bold select-none uppercase">
                    <span>Simulated Rolling Week View</span>
                    <span>Scroll below</span>
                  </div>
                  {renderWeeklyListView()}
                </div>
                
                {/* Mobile horizontal weekly swiper */}
                <div className="lg:hidden flex flex-col gap-3 w-full">
                  <span className="text-[8.5px] text-gray-500 font-bold uppercase tracking-wider font-mono px-1 block text-center">Swipe horizontally to inspect days</span>
                  <div className="flex gap-2.5 overflow-x-auto hide-scrollbar py-2 px-1 snap-x">
                    {(() => {
                      const days = [];
                      for (let d = 1; d <= 31; d++) {
                        const item = schedule[d];
                        const isCompleted = completedDays.includes(d);
                        const isMissed = missedDays.includes(d);
                        const isToday = d === 29;
                        const isRest = item.type === 'rest';
                        
                        let borderCl = "border-white/5";
                        let bgCl = "bg-[#121215]/50";
                        let statusEmoji = "📅";
                        if (isCompleted) { borderCl = "border-emerald-500/20"; bgCl = "bg-emerald-500/10"; statusEmoji = "✅"; }
                        else if (isMissed) { borderCl = "border-red-500/10"; bgCl = "bg-red-500/10"; statusEmoji = "⚠️"; }
                        else if (isRest) { borderCl = "border-blue-500/10"; bgCl = "bg-blue-500/5"; statusEmoji = "💤"; }
                        
                        if (isToday) { borderCl = "border-[#00D2FF]"; bgCl = "bg-[#00D2FF]/10 shadow-[0_0_10px_rgba(0,210,255,0.15)]"; }
                        
                        days.push(
                          <button 
                            key={d}
                            onClick={() => { setSelectedDay(d); try { playBeep(900, 'sine', 0.04); } catch(e) {} }}
                            className={`flex flex-col items-center justify-between p-3 rounded-2xl border ${borderCl} ${bgCl} min-w-[76px] aspect-[4/5] shrink-0 snap-center transition-all cursor-pointer active:scale-95`}
                          >
                            <span className={`text-[9px] font-mono font-bold ${isToday ? 'text-[#00D2FF]' : 'text-gray-500'}`}>DAY {d}</span>
                            <span className="text-lg my-1">{statusEmoji}</span>
                            <span className="text-[7.5px] font-bold font-outfit text-white uppercase block truncate w-full text-center">{item.name.split(' ')[0]}</span>
                          </button>
                        );
                      }
                      return days;
                    })()}
                  </div>
                  
                  {/* Highlight box for selected day details inside weekly mode */}
                  <div className="bg-[#121215]/40 border border-white/5 p-4 rounded-2xl text-center mt-1">
                    <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-widest">Active Workout</span>
                    <h4 className="text-xs font-bold text-[#00F0FF] mt-1 font-outfit uppercase">May 29 (Today) Split</h4>
                    <p className="text-[10px] text-gray-400 mt-1 leading-relaxed">Today is 🏋️ {schedule[29].name}. Tap any day bubble in the swiper above to execute progressive volume telemetry.</p>
                  </div>
                </div>
              </div>
            )}"""

if cal_grid_target in content:
    content = content.replace(cal_grid_target, cal_grid_replacement)
    print("  [SUCCESS] Patched Calendar Weekly Swiper Grid.")
else:
    print("  [WARNING] Calendar Weekly Swiper Grid target not found.")


# ----------------------------------------------------
# PATCH 5: WorkoutCalendar Detail Modal to Bottom Sheet slide drawer
# ----------------------------------------------------
cal_modal_target = """              return (
                <div className="fixed inset-0 w-full h-full flex items-center justify-center bg-black/80 backdrop-blur-sm z-50 p-4 select-none animate-bubble-appear">
                  <div className="relative w-full max-w-md p-6 glass-panel rounded-3xl glow-border border-white/5 card-radial-purple flex flex-col gap-4 text-left">"""

cal_modal_replacement = """              return (
                <div className="fixed inset-0 w-full h-full flex items-end lg:items-center justify-center bg-black/70 backdrop-blur-xs z-50 lg:p-4 select-none animate-bubble-appear">
                  {/* Backdrop click closer */}
                  <div className="absolute inset-0 z-0" onClick={() => { setSelectedDay(null); setExerciseChecks({}); setReschedulingDay(null); }} />
                  
                  <div className="relative w-full max-lg:max-w-none lg:max-w-md p-6 bg-[#0E0E12]/95 backdrop-blur-lg border-t border-white/10 lg:border border-white/5 rounded-t-3xl lg:rounded-3xl card-radial-purple flex flex-col gap-4 text-left z-10 animate-[slide-up_0.3s_cubic-bezier(0.16,1,0.3,1)] lg:animate-none pb-safe-bottom max-h-[90vh] overflow-y-auto">
                    {/* iOS style drag handle bar */}
                    <div className="w-12 h-1 bg-white/15 rounded-full mx-auto mb-2 lg:hidden shrink-0" />"""

if cal_modal_target in content:
    content = content.replace(cal_modal_target, cal_modal_replacement)
    print("  [SUCCESS] Patched Calendar modal to bottom sheet.")
else:
    print("  [WARNING] Calendar modal to bottom sheet target not found.")


# ----------------------------------------------------
# PATCH 6: WorkoutCalendar (confetti celebration integration before closing </div>)
# ----------------------------------------------------
cal_end_target = """                    </div>
                  </div>
                </div>
              );
            })()}

          </div>
        );
      };"""

cal_end_replacement = """                    </div>
                  </div>
                </div>
              );
            })()}

            {/* Standalone Full Screen Celebration Achievement locked Overlay */}
            {celebrationDay && (
              <div className="fixed inset-0 w-full h-full bg-[#08080A]/95 backdrop-blur-md z-[60] flex flex-col items-center justify-center p-6 text-center select-none animate-[fade-in_0.35s_ease-out]">
                {/* Floating particle glows */}
                <div className="absolute top-1/4 left-1/4 w-80 h-80 bg-[#00D2FF]/10 rounded-full blur-[100px] pointer-events-none" />
                <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-[#9D00FF]/10 rounded-full blur-[100px] pointer-events-none" />
                
                {/* Glowing checkmark badge with spring bounce */}
                <div className="w-28 h-28 rounded-full bg-gradient-to-tr from-[#00D2FF] to-[#9D00FF] p-1 shadow-[0_0_50px_rgba(0,210,255,0.35)] animate-[spring-scale_0.8s_cubic-bezier(0.175,0.885,0.32,1.275)_forwards] mb-8 flex items-center justify-center">
                  <div className="w-full h-full rounded-full bg-[#0B0B0E] flex items-center justify-center border-4 border-black text-5xl">
                    🔥
                  </div>
                </div>

                <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase block mb-3 font-outfit">
                  ACHIEVEMENT LOCKED
                </span>
                <h2 className="text-3xl md:text-5xl font-black font-outfit text-white tracking-tight mb-4 leading-none uppercase">
                  Workout Completed!
                </h2>
                
                <p className="text-xs text-gray-400 max-w-xs mx-auto leading-relaxed mb-8">
                  Day {celebrationDay} logged successfully under safe-swap protocols. Your physical volume telemetry has been updated in real-time.
                </p>

                {/* Celebration Streak Tracker */}
                <div className="glass-panel p-4 py-3 rounded-2xl border-white/5 bg-black/40 flex items-center justify-center gap-6 mb-10 w-full max-w-xs mx-auto animate-[fade-in-up_0.6s_ease-out_forwards]">
                  <div className="text-center border-r border-white/5 pr-6">
                    <span className="text-[7.5px] text-gray-500 font-bold uppercase tracking-wider block">New Streak</span>
                    <span className="text-lg font-black font-outfit text-white mt-0.5 block">{streak} Days Solid</span>
                  </div>
                  <div className="text-center">
                    <span className="text-[7.5px] text-gray-500 font-bold uppercase tracking-wider block">Consistency</span>
                    <span className="text-lg font-black font-outfit text-emerald-400 mt-0.5 block">+{consistencyScore}% Perfect</span>
                  </div>
                </div>

                <button 
                  onClick={() => {
                    setCelebrationDay(null);
                    try { playBeep(1000, 'sine', 0.05); } catch(e) {}
                  }}
                  className="shimmer-btn px-8 py-4 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] hover:shadow-[0_0_20px_rgba(0,210,255,0.3)] rounded-2xl text-[11px] font-black text-white uppercase tracking-wider cursor-pointer active:scale-95 transition-all"
                >
                  Calibrate Metabolic Dashboard
                </button>
              </div>
            )}

          </div>
        );
      };"""

if cal_end_target in content:
    content = content.replace(cal_end_target, cal_end_replacement)
    print("  [SUCCESS] Patched Calendar celebration overlay.")
else:
    print("  [WARNING] Calendar celebration overlay target not found.")


# ----------------------------------------------------
# PATCH 7: Dashboard Mobile card deck & concentrics
# ----------------------------------------------------
dash_vars_target = "            const Dashboard = ({ user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy }) => {"
dash_vars_replacement = """            const Dashboard = ({ user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy }) => {
        const [waterGoal] = useState(14);""" # Keeping variables inside

# Let's inspect where return block starts in Dashboard. Line 3073 starts it.
dash_return_target = """        const activeBulletins = getBulletins();

        return (
          <div className="flex flex-col gap-6 w-full text-white animate-bubble-appear select-none">"""

dash_return_replacement = """        const activeBulletins = getBulletins();

        return (
          <div className="flex flex-col gap-6 w-full text-white animate-bubble-appear select-none">
            
            {/* 1. DESKTOP LAYOUT (HIDDEN ON MOBILE) */}
            <div className="hidden lg:flex flex-col gap-6 w-full">"""

# And find where the Dashboard ends: line 3578
dash_end_target = """            )}

          </div>
        );
      };"""

# Wait, let's find the exact match for dash_end_target
# Dashboard ends right before calculateBiometrics (line 3583)
dash_end_target_full = """            )}

          </div>
        );
      };


      const calculateBiometrics = (profile) => {"""

dash_end_replacement_full = """            )}

            </div> {/* END DESKTOP CONTAINER */}

            {/* 2. MOBILE STANDALONE APP LAYOUT (HIDDEN ON DESKTOP) */}
            <div className="lg:hidden flex flex-col gap-5 w-full pb-8">
              
              {/* Profile Status Pill */}
              <div className="glass-panel p-4 rounded-2xl flex items-center justify-between border-white/5 bg-black/40">
                <div className="flex items-center gap-3">
                  <AvatarDisplay size="sm" />
                  <div>
                    <span className="text-[10px] text-gray-500 font-bold block uppercase tracking-wider">ATHLETE STATUS</span>
                    <span className="text-sm font-black font-outfit text-white leading-none mt-0.5 block">Hey, {user ? user.name.split(' ')[0] : 'Arjun'}! ⚡</span>
                  </div>
                </div>
                {/* Glowing Streak count */}
                <div className="flex items-center gap-1.5 bg-gradient-to-r from-orange-500/15 to-yellow-500/10 border border-orange-500/20 px-3 py-1.5 rounded-full shadow-[0_0_12px_rgba(249,115,22,0.06)] active:scale-95 transition-all cursor-pointer">
                  <span className="text-orange-500 text-xs">🔥</span>
                  <span className="text-[10px] font-black font-outfit text-white">12 Day Streak</span>
                </div>
              </div>

              {/* Concentric Metabolic Rings Card */}
              <div className="glass-panel p-5 rounded-3xl border-white/5 bg-gradient-to-br from-[#0B0B0E] via-[#0B0B0E]/90 to-transparent flex items-center gap-6">
                <div className="relative shrink-0 flex items-center justify-center">
                  <svg className="w-28 h-28 transform -rotate-90">
                    <circle cx="56" cy="56" r="38" className="stroke-white/5" strokeWidth="5.5" fill="transparent" />
                    <circle cx="56" cy="56" r="28" className="stroke-white/5" strokeWidth="5.5" fill="transparent" />
                    <circle cx="56" cy="56" r="18" className="stroke-white/5" strokeWidth="5.5" fill="transparent" />
                    <circle cx="56" cy="56" r="38" className="stroke-[#00D2FF] drop-shadow-[0_0_4px_#00D2FF]" strokeWidth="5.5" fill="transparent" strokeDasharray={2*Math.PI*38} strokeDashoffset={2*Math.PI*38*(1 - Math.min(1.0, caloriesLog / targetCal))} strokeLinecap="round" />
                    <circle cx="56" cy="56" r="28" className="stroke-[#9D00FF] drop-shadow-[0_0_4px_#9D00FF]" strokeWidth="5.5" fill="transparent" strokeDasharray={2*Math.PI*28} strokeDashoffset={2*Math.PI*28*(1 - Math.min(1.0, waterCups / waterGoal))} strokeLinecap="round" />
                    <circle cx="56" cy="56" r="18" className="stroke-[#F97316] drop-shadow-[0_0_4px_#F97316]" strokeWidth="5.5" fill="transparent" strokeDasharray={2*Math.PI*18} strokeDashoffset={2*Math.PI*18*(1 - Math.min(1.0, sleepHrs / 8))} strokeLinecap="round" />
                  </svg>
                  {/* Floating core visual inside rings */}
                  <span className="absolute text-md">⚡</span>
                </div>
                
                <div className="flex-1 flex flex-col gap-2 font-outfit min-w-0">
                  <span className="text-[8px] text-gray-500 font-bold uppercase tracking-widest block">METABOLIC BALANCES</span>
                  <div className="flex flex-col gap-1.5">
                    <div className="flex justify-between items-center text-[10px] font-bold">
                      <span className="text-[#00D2FF] flex items-center gap-1"><i className="lucide-activity w-3 h-3"></i> Energy</span>
                      <span className="text-white">{caloriesLog} / {targetCal} kcal</span>
                    </div>
                    <div className="flex justify-between items-center text-[10px] font-bold">
                      <span className="text-[#9D00FF] flex items-center gap-1"><i className="lucide-droplet w-3 h-3"></i> Water</span>
                      <span className="text-white">{(waterCups * 0.25).toFixed(1)} / 3.5 L</span>
                    </div>
                    <div className="flex justify-between items-center text-[10px] font-bold">
                      <span className="text-[#F97316] flex items-center gap-1"><i className="lucide-clock w-3 h-3"></i> Sleep</span>
                      <span className="text-white">{sleepHrs} / 8.0 hrs</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Today's Workout checklist card */}
              <div className="glass-panel p-5 rounded-3xl border-white/5 bg-black/40">
                <div className="flex justify-between items-center mb-3">
                  <div>
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Today's Workout Plan</h4>
                    <span className="text-[8.5px] text-gray-500 font-semibold block mt-0.5">Upper Body Hypertrophy Split • 45 min</span>
                  </div>
                  <span onClick={() => setActiveTab('workouts')} className="text-[9px] font-bold text-gray-400 hover:text-white cursor-pointer transition-colors">
                    Edit Split →
                  </span>
                </div>

                <div className="flex flex-col gap-2 mb-4">
                  {[
                    { key: 'ex1', name: "Dumbbell Chest Bench Press", sets: "4 sets x 12 reps" },
                    { key: 'ex2', name: "Wide Grip Pull Ups", sets: "4 sets x 10 reps" },
                    { key: 'ex3', name: "Shoulder Overhead Press", sets: "3 sets x 12 reps" },
                    { key: 'ex4', name: "Seated Cable Row Split", sets: "4 sets x 12 reps" }
                  ].map((ex) => (
                    <div 
                      key={ex.key} 
                      onClick={() => toggleExercise(ex.key)} 
                      className={`flex items-center justify-between p-3 rounded-xl border transition-all cursor-pointer ${
                        completedEx[ex.key] 
                          ? 'bg-emerald-500/5 border-emerald-500/10 text-gray-400' 
                          : 'bg-[#121212]/30 border-white/5 hover:border-white/10 text-white'
                      }`}
                    >
                      <div className="flex items-center gap-2.5">
                        <div className={`w-3.5 h-3.5 rounded border flex items-center justify-center transition-all ${
                          completedEx[ex.key] ? 'bg-emerald-500 border-emerald-500 text-white' : 'border-white/20'
                        }`}>
                          {completedEx[ex.key] && <i className="lucide-check w-2.5 h-2.5 stroke-[3px]"></i>}
                        </div>
                        <span className="text-[10px] font-bold truncate max-w-[200px]">{ex.name}</span>
                      </div>
                      <span className="text-[9px] text-gray-500 font-semibold">{ex.sets}</span>
                    </div>
                  ))}
                </div>

                <div className="flex gap-3">
                  <button onClick={() => setActiveTab('workouts')} className="shimmer-btn flex-1 flex items-center justify-center gap-1.5 py-3 rounded-2xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] font-bold text-[10px] text-white cursor-pointer uppercase tracking-wider active:scale-95 transition-all">
                    <i className="lucide-play w-3 h-3 fill-white"></i> Play Workout
                  </button>
                  <button onClick={() => setActiveTab('calendar')} className="p-3 bg-white/3 border border-white/5 hover:bg-white/10 rounded-2xl cursor-pointer text-gray-400 active:scale-95 transition-all">
                    <i className="lucide-calendar w-4 h-4"></i>
                  </button>
                </div>
              </div>

              {/* Interactive Hydration Tracker Widget */}
              <div className="glass-panel p-5 rounded-3xl border-white/5 bg-black/40 flex items-center justify-between gap-6">
                <div className="flex items-center gap-3">
                  <div className="p-3 bg-blue-500/10 text-blue-400 rounded-2xl shrink-0"><i className="lucide-droplet w-5 h-5"></i></div>
                  <div>
                    <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">Hydration Daily</span>
                    <span className="text-[11px] font-black text-white block mt-0.5">{(waterCups * 0.25).toFixed(2)} / 3.50 L Logged</span>
                  </div>
                </div>
                <div className="flex gap-2">
                  <button onClick={() => handleWaterLog(Math.max(0, waterCups - 1))} className="w-10 h-10 flex items-center justify-center rounded-xl bg-white/3 border border-white/5 hover:bg-white/5 text-sm font-bold text-gray-400 cursor-pointer active:scale-90 transition-all">-</button>
                  <button onClick={() => handleWaterLog(Math.min(24, waterCups + 1))} className="px-4 py-2 flex items-center gap-1.5 rounded-xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-[10px] font-bold text-white cursor-pointer active:scale-90 transition-all shadow-md">
                    <span>+ Cup</span>
                  </button>
                </div>
              </div>

              {/* Coach Nova Insights Banner */}
              <div className="glass-panel p-5 rounded-3xl border-white/5 card-radial-blue relative overflow-hidden">
                <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold text-[#00F0FF] bg-[#00F0FF]/15 uppercase font-mono rounded-bl border-b border-l border-white/5">
                  AI COACH INSIGHT
                </div>
                <div className="flex items-center gap-4">
                  <div className="p-3 bg-[#00F0FF]/10 text-[#00F0FF] rounded-2xl shrink-0"><i className="lucide-sparkles w-5 h-5"></i></div>
                  <div className="min-w-0 flex-1">
                    <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit">Coach Nova Insights</h4>
                    <p className="text-[10px] text-gray-400 leading-relaxed mt-1">
                      {recoveryScore >= 80 
                        ? "Recovery score is highly optimal (90%). Muscles are prime for progressive loading splits. Add +2.5kg to chest presses!" 
                        : "Fatigue warning activated. Prioritize joint mobility and maintain target calorie splits."}
                    </p>
                  </div>
                </div>
              </div>

              {/* Recovery Vitals sliders directly on Mobile Dashboard! */}
              <div className="glass-panel p-5 rounded-3xl border-white/5 bg-black/40">
                <div className="flex items-center gap-2 mb-3">
                  <div className="p-2 bg-[#00F0FF]/10 text-[#00F0FF] rounded-lg shrink-0"><i className="lucide-sparkles w-4 h-4"></i></div>
                  <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Physiological Vitals</h4>
                </div>
                <div className="flex flex-col gap-3 font-outfit">
                  <div className="flex justify-between items-center text-[9px] text-gray-400 font-bold uppercase">
                    <span>Sleep Quality</span>
                    <span className="text-[#00D2FF] font-mono">{sleepHrs} Hours</span>
                  </div>
                  <input 
                    type="range" min="4" max="10" step="1" 
                    value={sleepHrs} 
                    onChange={(e) => { setSleepHrs(parseInt(e.target.value)); playBeep(500 + parseInt(e.target.value)*30, 'sine', 0.05); }}
                    className="w-full accent-[#00F0FF] cursor-pointer bg-white/5 rounded-lg appearance-none h-1 mb-2"
                  />
                  <div className="flex justify-between items-center text-[9px] text-gray-400 font-bold uppercase">
                    <span>Muscle Soreness</span>
                    <span className="text-[#9D00FF] font-mono">{soreness}</span>
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    {['Mild', 'Moderate', 'Severe'].map(lvl => (
                      <button 
                        key={lvl} 
                        onClick={() => { setSoreness(lvl); playBeep(700, 'triangle', 0.06); }}
                        className={`py-2 rounded-xl text-[9px] font-bold transition-all border outline-none cursor-pointer ${
                          soreness === lvl 
                            ? 'border-[#00D2FF]/40 bg-[#00D2FF]/10 text-white shadow-sm' 
                            : 'border-white/5 bg-white/3 text-gray-400 hover:text-white'
                        }`}
                      >
                        {lvl === 'Mild' ? '🟢 Mild' : lvl === 'Moderate' ? '🟡 Med' : '🔴 Sev'}
                      </button>
                    ))}
                  </div>
                </div>
              </div>

            </div>

          </div>
        );
      };


      const calculateBiometrics = (profile) => {"""

if dash_return_target in content:
    content = content.replace(dash_return_target, dash_return_replacement)
    print("  [SUCCESS] Patched Dashboard component return start.")
else:
    print("  [WARNING] Dashboard component return start target not found.")

if dash_end_target_full in content:
    content = content.replace(dash_end_target_full, dash_end_replacement_full)
    print("  [SUCCESS] Patched Dashboard component return end + Mobile Deck.")
else:
    print("  [WARNING] Dashboard component return end target not found.")


# ----------------------------------------------------
# PATCH 8: Mobile Bottom Navigation Bar & SW Register
# ----------------------------------------------------
bottom_nav_target = """              {/* MOBILE BOTTOM NAVIGATION BAR */}
              <nav className="lg:hidden h-14 border-t border-white/5 bg-[#0B0B0E]/90 backdrop-blur-md flex items-center justify-around z-30 select-none font-outfit text-gray-400">
                <button onClick={() => setActiveTab('dashboard')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'dashboard' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-layout-dashboard w-4.5 h-4.5"></i>
                  <span>Dashboard</span>
                </button>
                <button onClick={() => setActiveTab('coach')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'coach' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-sparkles w-4.5 h-4.5"></i>
                  <span>AI Coach</span>
                </button>
                <button onClick={() => setActiveTab('workouts')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'workouts' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-dumbbell w-4.5 h-4.5"></i>
                  <span>Workouts</span>
                </button>
                <button onClick={() => setActiveTab('nutrition')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'nutrition' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-apple w-4.5 h-4.5"></i>
                  <span>Nutrition</span>
                </button>
                <button onClick={() => setActiveTab('calendar')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'calendar' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-calendar w-4.5 h-4.5"></i>
                  <span>Calendar</span>
                </button>
              </nav>"""

bottom_nav_replacement = """              {/* MOBILE BOTTOM NAVIGATION BAR */}
              {(() => {
                const bottomTabs = [
                  { key: 'dashboard', name: 'Home', icon: 'lucide-layout-dashboard' },
                  { key: 'coach', name: 'AI Coach', icon: 'lucide-sparkles' },
                  { key: 'workouts', name: 'Workout Plan', icon: 'lucide-dumbbell' },
                  { key: 'calendar', name: 'Calendar', icon: 'lucide-calendar' },
                  { key: 'progress', name: 'Progress', icon: 'lucide-trending-up' },
                  { key: 'settings', name: 'Profile', icon: 'lucide-user-circle' },
                ];
                const activeIndex = bottomTabs.findIndex(t => t.key === activeTab);
                
                return (
                  <nav className="fixed bottom-0 left-0 right-0 lg:hidden h-[68px] border-t border-white/5 bg-[#0B0B0E]/80 backdrop-blur-lg flex items-center justify-around z-50 select-none pb-safe-bottom px-2 shadow-[0_-8px_32px_rgba(0,0,0,0.5)]">
                    {/* Active Sliding Indicator Bubble */}
                    <div 
                      className="absolute top-1.5 bottom-1.5 bg-gradient-to-r from-[#00D2FF]/10 to-[#9D00FF]/10 border border-[#00D2FF]/20 rounded-2xl transition-all duration-300 ease-[cubic-bezier(0.25,0.8,0.25,1)] pointer-events-none"
                      style={{
                        width: 'calc(16.66% - 8px)',
                        left: `calc(${activeIndex !== -1 ? activeIndex * 16.66 : 0}% + 4px)`,
                        opacity: activeIndex !== -1 ? 1 : 0,
                        boxShadow: '0 0 15px rgba(0, 210, 255, 0.05)'
                      }}
                    />
                    
                    {bottomTabs.map((tab) => {
                      const isActive = activeTab === tab.key;
                      return (
                        <button 
                          key={tab.key}
                          onClick={() => { setActiveTab(tab.key); }}
                          className={`flex flex-col items-center justify-center gap-1 flex-1 py-2 rounded-xl transition-all duration-200 cursor-pointer relative z-10 active:scale-90 ${
                            isActive 
                              ? 'text-white font-extrabold font-outfit' 
                              : 'text-gray-400 font-medium'
                          }`}
                        >
                          <i className={`${tab.icon} w-5 h-5 transition-transform duration-300 ${isActive ? 'text-[#00D2FF] scale-110' : 'text-gray-500'}`}></i>
                          <span className="text-[9px] tracking-wide block truncate">{tab.name}</span>
                          {isActive && (
                            <span className="absolute bottom-1 w-1.5 h-1.5 rounded-full bg-[#00D2FF] shadow-[0_0_8px_#00D2FF] animate-pulse" />
                          )}
                        </button>
                      );
                    })}
                  </nav>
                );
              })()}"""

if bottom_nav_target in content:
    content = content.replace(bottom_nav_target, bottom_nav_replacement)
    print("  [SUCCESS] Patched Bottom Navigation Bar.")
else:
    print("  [WARNING] Bottom Navigation Bar target not found.")


sw_mount_target = """      ReactDOM.createRoot(document.getElementById('root')).render(<App />);
    </script>
  </body>
</html>"""

sw_mount_replacement = """      ReactDOM.createRoot(document.getElementById('root')).render(<App />);

      // Register PWA Service Worker
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('./sw.js').then((reg) => {
            console.log('ServiceWorker registered successfully with scope:', reg.scope);
          }).catch((err) => {
            console.log('ServiceWorker registration failed:', err);
          });
        });
      }
    </script>
  </body>
</html>"""

if sw_mount_target in content:
    content = content.replace(sw_mount_target, sw_mount_replacement)
    print("  [SUCCESS] Patched Service Worker registration in preview.html.")
else:
    print("  [WARNING] Service Worker registration target not found in preview.html.")


# Save the updated file contents
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Final file size:", len(content))
print("Patched successfully!")
