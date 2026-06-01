import re

file_path = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai\preview.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original size:", len(content))

# ----------------------------------------------------------------------
# 1. Global Branding Changes (FitNova / Fit Nova -> NovaFit)
# ----------------------------------------------------------------------
content = content.replace("Fit Nova", "NovaFit")
content = content.replace("FitNova", "NovaFit")
content = content.replace("FIT NOVA", "NOVAFIT")
content = content.replace("fit-nova-ai", "novafit-ai")
content = content.replace("fitnova_user", "novafit_user")
content = content.replace("fitnova_avatar", "novafit_avatar")
content = content.replace("FitAI", "NovaFit")  # Matches visual sidebar logo
print("Globally renamed branding to NovaFit.")


# ----------------------------------------------------------------------
# 2. Update Layout Styles & Custom Accent CSS (Theme Colors)
# ----------------------------------------------------------------------
# We shift `#08080A` to deep navy `#070710` and `#0B0B0E` to glass navy `#0A0A18`
content = content.replace("bg-[#08080A]", "bg-[#070710]")
content = content.replace("bg-[#0B0B0E]", "bg-[#0A0A18]")
content = content.replace("bg-[#121215]", "bg-[#0F0F24]")
content = content.replace("bg-darkBg", "bg-[#070710]")
content = content.replace("bg-charcoal", "bg-[#0A0A18]")
content = content.replace("border-white/5", "border-[#1F1F46]/50")
content = content.replace("border-white/10", "border-[#1F1F46]/70")


# ----------------------------------------------------------------------
# 3. Inject Re-engineered Dashboard Component
# ----------------------------------------------------------------------
# Locate the boundaries of the old Dashboard component
# Starts around: const Dashboard = ({ AvatarDisplay, user ...
# Ends around: const calculateBiometrics = ...
start_marker = "            const Dashboard = ({ AvatarDisplay, user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy }) => {"
end_marker = "      const calculateBiometrics = (profile) => {"

start_index = content.find(start_marker)
end_index = content.find(end_marker)

if start_index == -1:
    # Try alternative matching
    start_marker_alt = "            const Dashboard = ({"
    start_index = content.find(start_marker_alt)
    print("Used alternative start marker.")

if start_index != -1 and end_index != -1:
    print(f"Found Dashboard boundaries. Replacing lines from index {start_index} to {end_index}...")
    
    # Newly designed high-fidelity Dashboard component matching the reference image layout
    new_dashboard_code = """            const Dashboard = ({ AvatarDisplay, user, userProfile, setProfile, setActiveTab, waterCups, setWaterCups, sleepHrs, setSleepHrs, soreness, setSoreness, energy, setEnergy }) => {
        
        const [waterGoal] = useState(12); // Cups (matches 3.0L)
        const [caloriesLog, setCaloriesLog] = useState(632); // Matches 632 kcal in reference image
        const [completedEx, setCompletedEx] = useState({
          ex1: true, ex2: false, ex3: false, ex4: false
        });

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

        const toggleExercise = (key) => {
          setCompletedEx(prev => ({ ...prev, [key]: !prev[key] }));
          playBeep(900, 'sine', 0.08);
        };

        const handleWaterLog = (cups) => {
          setWaterCups(cups);
          playBeep(800, 'triangle', 0.1);
        };

        // Static parameters exactly matching the reference image values
        const caloriesBurned = 632;
        const activeMinutes = 78;
        const recoveryScore = 82;
        const streakDays = 12;
        const stepsToday = "8,432";
        const waterLogged = "1.8 L";
        const targetCal = 2200;

        return (
          <div className="w-full text-white select-none animate-bubble-appear">
            
            {/* ==================================================================
               1. TABLET & DESKTOP DASHBOARD (HIDDEN ON MOBILE, viewports >= 1024px)
               ================================================================== */}
            <div className="hidden lg:flex flex-col gap-6 w-full pb-8">
              
              {/* Main greeting and bold header block */}
              <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div className="text-left font-outfit">
                  <span className="text-xs font-bold text-gray-500 uppercase tracking-widest block">Good Morning, {user ? user.name.split(' ')[0] : 'Arjun'} 👋</span>
                  <h1 className="text-3xl md:text-4xl lg:text-5xl font-black text-white mt-1 leading-[1.1]">
                    Ready to crush <br />
                    <span className="bg-gradient-to-r from-[#A78BFA] to-[#00D2FF] bg-clip-text text-transparent">your goals today?</span>
                  </h1>
                </div>
                
                {/* Search Bar, Notifications bell, and User Chip mounted at top of Dashboard */}
                <div className="flex items-center gap-4 shrink-0 max-md:w-full max-md:justify-end">
                  <div className="flex items-center gap-2.5 bg-[#0F0F24] border border-[#1F1F46]/50 px-3 py-2 rounded-xl text-xs text-gray-500 w-56">
                    <i className="lucide-search w-3.5 h-3.5 text-gray-400"></i>
                    <input type="text" placeholder="Search anything..." className="bg-transparent border-none outline-none flex-1 text-white text-xs placeholder-gray-600" />
                  </div>
                  
                  {/* Notifications bell with indicator */}
                  <button className="p-3 bg-[#0F0F24] border border-[#1F1F46]/50 rounded-xl text-gray-400 hover:text-white relative active:scale-95 transition-all cursor-pointer">
                    <i className="lucide-bell w-4 h-4"></i>
                    <span className="absolute top-2 right-2 w-2 h-2 rounded-full bg-[#9D00FF] shadow-[0_0_8px_#9D00FF]" />
                  </button>
                  
                  {/* User Profile Chip */}
                  <div className="flex items-center gap-2.5 bg-[#0F0F24] border border-[#1F1F46]/50 px-3 py-1.5 rounded-xl">
                    <AvatarDisplay size="sm" />
                    <div className="flex flex-col text-left font-outfit min-w-[70px]">
                      <span className="text-xs font-black text-white leading-none truncate max-w-[85px]">{user ? user.name : 'Arjun Verma'}</span>
                      <span className="text-[8px] text-gray-500 font-bold uppercase mt-0.5 tracking-wider">Premium Member</span>
                    </div>
                    <i className="lucide-chevron-down w-3.5 h-3.5 text-gray-500 shrink-0"></i>
                  </div>
                </div>
              </div>

              {/* TOP KPI Vitals Cards Row (4 Columns Grid) */}
              <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 items-stretch">
                
                {/* 1. Calories Burned */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center gap-4">
                  <div className="w-12 h-12 rounded-xl bg-[#8B5CF6]/10 text-[#8B5CF6] flex items-center justify-center shrink-0">
                    <i className="lucide-flame w-5.5 h-5.5 fill-[#8B5CF6]/10"></i>
                  </div>
                  <div>
                    <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block font-outfit">Calories Burned</span>
                    <span className="text-xl font-black font-outfit text-white block mt-0.5">{caloriesBurned} <span className="text-xs font-normal text-gray-400 font-sans">kcal</span></span>
                  </div>
                </div>

                {/* 2. Active Minutes */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center gap-4">
                  <div className="w-12 h-12 rounded-xl bg-orange-500/10 text-orange-500 flex items-center justify-center shrink-0">
                    <i className="lucide-clock w-5.5 h-5.5"></i>
                  </div>
                  <div>
                    <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block font-outfit">Active Minutes</span>
                    <span className="text-xl font-black font-outfit text-white block mt-0.5">{activeMinutes} <span className="text-xs font-normal text-gray-400 font-sans">min</span></span>
                  </div>
                </div>

                {/* 3. Recovery Score circular bar */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center justify-between gap-4 cursor-pointer hover:border-[#8B5CF6]/30" onClick={() => setShowRecoveryModal(true)}>
                  <div className="flex items-center gap-4">
                    <div className="relative w-12 h-12 flex items-center justify-center shrink-0">
                      <svg className="w-full h-full transform -rotate-90">
                        <circle cx="24" cy="24" r="20" className="stroke-white/5" strokeWidth="3.5" fill="transparent" />
                        <circle cx="24" cy="24" r="20" className="stroke-[#00D2FF]" strokeWidth="3.5" fill="transparent" strokeDasharray={2*Math.PI*20} strokeDashoffset={2*Math.PI*20*(1 - recoveryScore/100)} strokeLinecap="round" />
                      </svg>
                      <span className="absolute text-[9px] font-black font-outfit text-white">{recoveryScore}%</span>
                    </div>
                    <div>
                      <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block font-outfit">Recovery Score</span>
                      <span className="text-xl font-black font-outfit text-white block mt-0.5">{recoveryScore}/100</span>
                    </div>
                  </div>
                  <span className="text-[8px] font-bold text-emerald-400 uppercase tracking-widest bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded font-outfit shrink-0 self-center">Great</span>
                </div>

                {/* 4. Workout Streak Flame */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center justify-between gap-4">
                  <div>
                    <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block font-outfit">Workout Streak</span>
                    <span className="text-xl font-black font-outfit text-white block mt-0.5">{streakDays} Days</span>
                  </div>
                  <div className="w-10 h-10 rounded-xl bg-orange-500/10 flex items-center justify-center shrink-0 relative overflow-hidden group">
                    <i className="lucide-flame w-6 h-6 text-orange-500 fill-orange-500/20 group-hover:scale-110 transition-transform duration-300 animate-pulse"></i>
                  </div>
                </div>

              </div>

              {/* MIDDLE ROW WIDGETS (3 Columns Grid: Weekly Progress | Today's Plan | AI Coach) */}
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-stretch">
                
                {/* 1. Weekly Progress custom SVG chart */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[300px]">
                  <div className="flex justify-between items-center mb-4 select-none">
                    <h4 className="text-xs font-bold font-outfit text-white uppercase tracking-wider">Weekly Progress</h4>
                    <div className="flex items-center gap-1 text-[9px] font-bold text-gray-400 border border-[#1F1F46]/50 rounded-lg px-2 py-1 bg-[#0A0A18]/50 cursor-pointer">
                      <span>This Week</span>
                      <i className="lucide-chevron-down w-3 h-3 text-gray-500"></i>
                    </div>
                  </div>
                  
                  {/* Custom drawing high-fidelity smooth line chart matching reference */}
                  <div className="w-full flex-1 flex flex-col justify-end relative h-40">
                    <svg className="w-full h-full" viewBox="0 0 240 100" preserveAspectRatio="none">
                      <defs>
                        <linearGradient id="purpleGlowGrad" x1="0" y1="0" x2="0" y2="1">
                          <stop offset="0%" stopColor="#8B5CF6" stopOpacity="0.25" />
                          <stop offset="100%" stopColor="#8B5CF6" stopOpacity="0.0" />
                        </linearGradient>
                      </defs>
                      {/* Grid background lines */}
                      <line x1="20" y1="20" x2="230" y2="20" className="stroke-white/5" strokeWidth="0.5" />
                      <line x1="20" y1="50" x2="230" y2="50" className="stroke-white/5" strokeWidth="0.5" />
                      <line x1="20" y1="80" x2="230" y2="80" className="stroke-white/5" strokeWidth="0.5" />
                      
                      {/* Purple Filled Area */}
                      <path d="M 20 80 C 37 72, 38 65, 55 65 C 72 65, 73 72, 90 72 C 107 72, 108 35, 125 35 C 142 35, 143 50, 160 50 C 177 50, 178 20, 195 20 C 212 20, 213 45, 230 45 L 230 100 L 20 100 Z" fill="url(#purpleGlowGrad)" />
                      
                      {/* Glowing Line */}
                      <path d="M 20 80 C 37 72, 38 65, 55 65 C 72 65, 73 72, 90 72 C 107 72, 108 35, 125 35 C 142 35, 143 50, 160 50 C 177 50, 178 20, 195 20 C 212 20, 213 45, 230 45" stroke="#8B5CF6" strokeWidth="2.5" fill="none" strokeLinecap="round" style={{ filter: 'drop-shadow(0 4px 10px rgba(139,92,246,0.45))' }} />
                      
                      {/* Circle Nodes */}
                      <circle cx="20" cy="80" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                      <circle cx="55" cy="65" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                      <circle cx="90" cy="72" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                      <circle cx="125" cy="35" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                      <circle cx="160" cy="50" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                      <circle cx="195" cy="20" r="3.5" className="fill-[#00F0FF] stroke-[#8B5CF6]" strokeWidth="1.5" />
                      <circle cx="230" cy="45" r="3" className="fill-[#8B5CF6] stroke-black" strokeWidth="1" />
                    </svg>
                    
                    {/* Saturday Active Progress Bubble overlay exactly matching image */}
                    <div className="absolute top-[8px] left-[175px] bg-[#8B5CF6] text-white border border-white/20 rounded-lg px-1.5 py-0.5 text-[8.5px] font-black font-outfit shadow-lg shadow-purple-500/20 animate-bounce select-none">
                      78%
                    </div>
                  </div>
                  
                  {/* X Axis Labels */}
                  <div className="flex justify-between items-center text-[9px] text-gray-500 font-bold font-outfit px-1 mt-3">
                    <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
                  </div>
                </div>

                {/* 2. Today's Plan banner card */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[300px] relative overflow-hidden group">
                  <div className="flex justify-between items-center shrink-0">
                    <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider">Today's Plan</h4>
                    <span onClick={() => setActiveTab('workouts')} className="text-[9px] font-bold text-[#8B5CF6] hover:text-white cursor-pointer transition-colors uppercase tracking-wider">
                      View All
                    </span>
                  </div>
                  
                  {/* Athlete image rendering merged on right side of card */}
                  <div className="absolute right-[-10px] bottom-[50px] w-48 h-56 pointer-events-none select-none overflow-hidden rounded-xl opacity-90 transition-transform duration-300 group-hover:scale-[1.02]">
                    <img src="./athlete.png" alt="Athlete" className="w-full h-full object-contain object-right-bottom filter drop-shadow-[0_0_20px_rgba(139,92,246,0.3)]" />
                    <div className="absolute inset-0 bg-gradient-to-r from-[#0F0F24] via-[#0F0F24]/30 to-transparent" />
                    <div className="absolute inset-0 bg-gradient-to-t from-[#0F0F24]/90 via-transparent to-[#0F0F24]/40" />
                  </div>

                  <div className="my-auto z-10 text-left">
                    <h2 className="text-lg font-black font-outfit text-white uppercase tracking-wide leading-none">Push Day</h2>
                    <p className="text-[10px] text-gray-400 mt-1 font-semibold">Chest • Shoulders • Triceps</p>
                    
                    <div className="flex items-center gap-3 mt-4 text-[9px] text-gray-500 font-mono font-bold uppercase select-none">
                      <span className="flex items-center gap-1"><i className="lucide-clock w-3 h-3 text-[#8B5CF6]"></i> 45 min</span>
                      <span className="flex items-center gap-1"><i className="lucide-dumbbell w-3 h-3 text-[#8B5CF6]"></i> 6 Exercises</span>
                    </div>
                  </div>

                  <button onClick={() => setActiveTab('workouts')} className="shimmer-btn w-full py-3 bg-gradient-to-r from-[#8B5CF6] to-[#6366F1] hover:shadow-[0_0_20px_rgba(139,92,246,0.4)] text-[10px] font-bold uppercase tracking-wider text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer flex items-center justify-center gap-1 z-10">
                    <i className="lucide-play w-3 h-3 fill-white"></i> Start Workout <i className="lucide-chevron-right w-3.5 h-3.5 ml-1"></i>
                  </button>
                </div>

                {/* 3. AI Coach card */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[300px]">
                  <div className="flex items-center gap-3 shrink-0">
                    <div className="w-9 h-9 rounded-full bg-gradient-to-r from-[#8B5CF6] to-[#00D2FF] p-0.5 flex items-center justify-center shrink-0 relative overflow-hidden">
                      <div className="w-full h-full rounded-full bg-[#0B0B0C] flex items-center justify-center">
                        <i className="lucide-bot text-[#00F0FF] w-4.5 h-4.5"></i>
                      </div>
                    </div>
                    <div className="text-left">
                      <h4 className="text-xs font-bold text-white font-outfit uppercase">AI Coach</h4>
                      <div className="flex items-center gap-1 mt-0.5">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
                        <span className="text-[7.5px] font-bold text-emerald-400 uppercase tracking-widest font-mono">Online</span>
                      </div>
                    </div>
                  </div>

                  <div className="my-auto text-left py-4">
                    <p className="text-[12px] text-gray-300 font-medium font-sans leading-relaxed">
                      "Your form was excellent yesterday! Let's increase intensity today."
                    </p>
                  </div>

                  <button onClick={() => setActiveTab('coach')} className="shimmer-btn w-full py-3 bg-[#13132D]/85 hover:bg-[#8B5CF6]/15 border border-[#8B5CF6]/30 text-[10px] font-bold uppercase tracking-wider text-[#8B5CF6] hover:text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer flex items-center justify-center gap-1.5">
                    Chat with Coach <i className="lucide-chevron-right w-3.5 h-3.5 ml-1"></i>
                  </button>
                </div>

              </div>

              {/* BOTTOM ROW WIDGETS (3 Columns Grid: Nutrition Summary | Upcoming Workouts | Recent Activity) */}
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-stretch">
                
                {/* 1. Nutrition Summary */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[350px]">
                  <div className="flex justify-between items-center mb-2.5">
                    <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider">Nutrition Summary</h4>
                  </div>
                  
                  {/* Left circular donut and right legend stacked side-by-side */}
                  <div className="flex items-center justify-center gap-6 my-auto">
                    {/* SVG circular donut */}
                    <div className="relative w-24 h-24 flex items-center justify-center shrink-0">
                      <svg className="w-full h-full transform -rotate-90">
                        <circle cx="48" cy="48" r="38" className="stroke-white/5" strokeWidth="5.5" fill="transparent" />
                        <circle cx="48" cy="48" r="38" className="stroke-[#00D2FF]" strokeWidth="5.5" fill="transparent" strokeDasharray={2*Math.PI*38} strokeDashoffset={2*Math.PI*38*(1 - 0.82)} strokeLinecap="round" />
                      </svg>
                      <div className="absolute text-center select-none font-outfit">
                        <span className="text-[12px] font-black text-white leading-none block">1,890</span>
                        <span className="text-[7.5px] font-semibold text-gray-500 uppercase tracking-wider block mt-0.5">/ 2,300 kcal</span>
                      </div>
                    </div>
                    
                    {/* Legend Split metrics */}
                    <div className="flex flex-col gap-2 font-outfit shrink-0 min-w-[100px] text-left">
                      <div className="flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-[#00D2FF]" />
                        <div>
                          <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Carbs (45%)</span>
                          <span className="text-[10px] font-black text-white">212g</span>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-orange-500" />
                        <div>
                          <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Protein (30%)</span>
                          <span className="text-[10px] font-black text-white">142g</span>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-[#8B5CF6]" />
                        <div>
                          <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Fats (25%)</span>
                          <span className="text-[10px] font-black text-white">65g</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Next Meal Sub-Card at bottom */}
                  <div className="p-3 bg-white/[0.02] border border-white/5 rounded-2xl flex items-center gap-3 mt-4">
                    <div className="w-9 h-9 rounded-full bg-[#0B0B0C] border border-[#1F1F46]/50 flex items-center justify-center shrink-0 text-md relative overflow-hidden animate-[pulse_5s_infinite]">
                      🍛
                    </div>
                    <div className="flex-1 min-w-0 text-left">
                      <div className="flex items-center justify-between">
                        <span className="text-[7px] font-bold text-gray-500 uppercase tracking-wider">Next Meal</span>
                        <span className="text-[8px] font-bold text-[#8B5CF6] uppercase tracking-wider">In 45 min</span>
                      </div>
                      <span className="text-[10px] font-bold text-white block mt-0.5 truncate">Chicken & Brown Rice</span>
                      <span className="text-[7px] font-semibold text-gray-500 block mt-0.5 tracking-wide">High Protein</span>
                    </div>
                  </div>
                </div>

                {/* 2. Upcoming Workouts table */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[350px]">
                  <div className="flex justify-between items-center mb-3">
                    <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider">Upcoming Workouts</h4>
                  </div>
                  
                  <div className="flex flex-col gap-2.5 my-auto text-left">
                    {[
                      { day: 'Tue', name: 'Pull Day', detail: 'Back • Biceps', badge: 'Tomorrow' },
                      { day: 'Wed', name: 'Leg Day', detail: 'Quads • Hamstrings', date: '2 Aug' },
                      { day: 'Thu', name: 'Core Day', detail: 'Abs • Lower Back', date: '3 Aug' }
                    ].map((row, index) => (
                      <div key={index} className="p-3 bg-white/[0.01] border border-white/5 rounded-xl flex items-center justify-between text-[11px] font-mono leading-normal select-none">
                        <div className="flex items-center gap-3 min-w-0">
                          <span className="text-[12px] font-bold text-gray-500 font-mono w-8 shrink-0">{row.day}</span>
                          <div className="truncate">
                            <h4 className="text-[10px] font-bold text-white font-outfit uppercase tracking-wide truncate">{row.name}</h4>
                            <p className="text-[7.5px] text-gray-500 font-semibold uppercase mt-0.5 truncate">{row.detail}</p>
                          </div>
                        </div>
                        {row.badge ? (
                          <span className="text-[7px] font-black uppercase bg-[#8B5CF6]/15 text-[#8B5CF6] border border-[#8B5CF6]/20 px-2 py-0.5 rounded font-sans">
                            {row.badge}
                          </span>
                        ) : (
                          <span className="text-[7.5px] font-mono font-bold text-gray-500">{row.date}</span>
                        )}
                      </div>
                    ))}
                  </div>
                  
                  <button onClick={() => setActiveTab('calendar')} className="w-full text-center py-2.5 text-[9.5px] font-bold text-[#8B5CF6] hover:text-white transition-all uppercase tracking-wider cursor-pointer mt-4">
                    View Full Calendar
                  </button>
                </div>

                {/* 3. Recent Activity */}
                <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[350px]">
                  <div className="flex justify-between items-center mb-3">
                    <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider">Recent Activity</h4>
                    <span className="text-[9px] font-bold text-gray-500 hover:text-white cursor-pointer uppercase tracking-wider transition-colors">
                      View All
                    </span>
                  </div>
                  
                  <div className="flex flex-col gap-2 my-auto text-left">
                    {[
                      { icon: 'lucide-dumbbell', text: 'Push Day Completed', time: 'Today, 8:15 AM', checked: true, color: 'text-[#8B5CF6] bg-[#8B5CF6]/10' },
                      { icon: 'lucide-activity', text: '10,254 Steps', time: 'Today, 6:30 AM', color: 'text-[#00D2FF] bg-[#00D2FF]/10' },
                      { icon: 'lucide-utensils', text: 'Meal Logged', time: 'Today, 1:15 PM', color: 'text-orange-500 bg-orange-500/10' },
                      { icon: 'lucide-moon', text: '7.5h Sleep', time: 'Yesterday', color: 'text-[#8B5CF6] bg-[#8B5CF6]/10' }
                    ].map((act, index) => (
                      <div key={index} className="p-2.5 bg-white/[0.01] border border-white/5 rounded-xl flex items-center justify-between select-none">
                        <div className="flex items-center gap-3 min-w-0">
                          <div className={`w-8 h-8 rounded-lg ${act.color} flex items-center justify-center shrink-0`}>
                            <i className={`${act.icon} w-4 h-4`}></i>
                          </div>
                          <div className="truncate">
                            <h4 className="text-[10px] font-bold text-white font-outfit uppercase tracking-wide truncate">{act.text}</h4>
                            <p className="text-[7.5px] text-gray-500 font-semibold uppercase mt-0.5 truncate">{act.time}</p>
                          </div>
                        </div>
                        {act.checked && (
                          <div className="w-4 h-4 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center border border-emerald-500/30">
                            <i className="lucide-check w-2.5 h-2.5 stroke-[3px]"></i>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

              </div>

            </div>

            {/* ==================================================================
               2. MOBILE STANDALONE APP LAYOUT (HIDDEN ON DESKTOP, viewports < 1024px)
               ================================================================== */}
            <div className="lg:hidden flex flex-col gap-5 w-full pb-8 select-none">
              
              {/* Profile Greeting Status pill */}
              <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center justify-between">
                <div className="flex items-center gap-3 text-left">
                  <AvatarDisplay size="sm" />
                  <div className="font-outfit">
                    <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider block">ATHLETE STATUS</span>
                    <span className="text-sm font-black text-white leading-none mt-0.5 block">Good Morning, {user ? user.name.split(' ')[0] : 'Arjun'} 👋</span>
                  </div>
                </div>
                
                {/* Notification Bell */}
                <button className="p-2.5 bg-[#0F0F24] border border-[#1F1F46]/50 rounded-xl text-gray-400 relative active:scale-95 transition-all cursor-pointer">
                  <i className="lucide-bell w-4 h-4"></i>
                  <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-[#9D00FF] shadow-[0_0_8px_#9D00FF]" />
                </button>
              </div>

              {/* AI Coach Card */}
              <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col gap-4 text-left">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-gradient-to-r from-[#8B5CF6] to-[#00D2FF] p-0.5 flex items-center justify-center shrink-0 relative overflow-hidden">
                    <div className="w-full h-full rounded-full bg-[#0B0B0C] flex items-center justify-center">
                      <i className="lucide-bot text-[#00F0FF] w-4 h-4"></i>
                    </div>
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-white font-outfit uppercase">AI Coach</h4>
                    <div className="flex items-center gap-1 mt-0.5">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
                      <span className="text-[7px] font-bold text-emerald-400 uppercase tracking-widest font-mono">Online</span>
                    </div>
                  </div>
                </div>

                <p className="text-[11.5px] text-gray-300 font-medium font-sans leading-relaxed">
                  "Your recovery is optimal today. Ready to crush your workout? 💪"
                </p>

                <button onClick={() => setActiveTab('coach')} className="shimmer-btn w-full py-3 bg-[#13132D]/85 border border-[#8B5CF6]/30 text-[10px] font-bold uppercase tracking-wider text-[#8B5CF6] hover:text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer flex items-center justify-center gap-1.5">
                  Chat with Coach <i className="lucide-chevron-right w-3.5 h-3.5 ml-1"></i>
                </button>
              </div>

              {/* Today's Workout Card */}
              <div className="glass-panel p-5 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex flex-col justify-between min-h-[220px] relative overflow-hidden group text-left">
                <div className="flex justify-between items-center">
                  <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider">Today's Plan</h4>
                  <span onClick={() => setActiveTab('workouts')} className="text-[9px] font-bold text-[#8B5CF6] uppercase tracking-wider">
                    View All
                  </span>
                </div>
                
                {/* Athlete photo merged in background */}
                <div className="absolute right-[-10px] bottom-[40px] w-36 h-44 pointer-events-none select-none overflow-hidden rounded-xl opacity-90">
                  <img src="./athlete.png" alt="Athlete" className="w-full h-full object-contain object-right-bottom filter drop-shadow-[0_0_20px_rgba(139,92,246,0.3)]" />
                  <div className="absolute inset-0 bg-gradient-to-r from-[#0F0F24] via-[#0F0F24]/30 to-transparent" />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0F0F24]/90 via-transparent to-[#0F0F24]/40" />
                </div>

                <div className="my-auto z-10">
                  <h2 className="text-md font-black font-outfit text-white uppercase tracking-wide leading-none">Push Day</h2>
                  <p className="text-[9px] text-gray-400 mt-1 font-semibold">Chest • Shoulders • Triceps</p>
                  
                  <div className="flex items-center gap-3 mt-3 text-[8.5px] text-gray-500 font-mono font-bold uppercase select-none">
                    <span className="flex items-center gap-1"><i className="lucide-clock w-3 h-3 text-[#8B5CF6]"></i> 45 min</span>
                    <span className="flex items-center gap-1"><i className="lucide-dumbbell w-3 h-3 text-[#8B5CF6]"></i> 6 Exercises</span>
                  </div>
                </div>

                <button onClick={() => setActiveTab('workouts')} className="shimmer-btn w-full py-3 bg-gradient-to-r from-[#8B5CF6] to-[#6366F1] hover:shadow-[0_0_20px_rgba(139,92,246,0.4)] text-[10px] font-bold uppercase tracking-wider text-white rounded-xl transition-all active:scale-[0.98] cursor-pointer flex items-center justify-center gap-1 z-10 mt-3">
                  <i className="lucide-play w-3 h-3 fill-white"></i> Start Workout <i className="lucide-chevron-right w-3.5 h-3.5 ml-1"></i>
                </button>
              </div>

              {/* Activitys Overview (2x2 Grid) */}
              <div className="flex flex-col gap-3 text-left">
                <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider pl-1">Activitys Overview</h4>
                
                <div className="grid grid-cols-2 gap-4">
                  
                  {/* Calories */}
                  <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-xl flex items-center justify-between">
                    <div>
                      <span className="text-[8.5px] text-gray-500 font-bold uppercase block tracking-wider font-outfit">Calories</span>
                      <span className="text-[13px] font-black font-outfit text-white block mt-1">{caloriesLog}</span>
                      <span className="text-[8px] text-gray-500 block">/ 2,200 kcal</span>
                    </div>
                    <i className="lucide-flame w-4.5 h-4.5 text-orange-500 fill-orange-500/10"></i>
                  </div>

                  {/* Steps */}
                  <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-xl flex items-center justify-between">
                    <div>
                      <span className="text-[8.5px] text-gray-500 font-bold uppercase block tracking-wider font-outfit">Steps</span>
                      <span className="text-[13px] font-black font-outfit text-white block mt-1">{stepsToday}</span>
                      <span className="text-[8px] text-gray-500 block">/ 10,000</span>
                    </div>
                    <i className="lucide-footprints w-4.5 h-4.5 text-[#8B5CF6]"></i>
                  </div>

                  {/* Workout */}
                  <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-xl flex items-center justify-between">
                    <div>
                      <span className="text-[8.5px] text-gray-500 font-bold uppercase block tracking-wider font-outfit">Workout</span>
                      <span className="text-[13px] font-black font-outfit text-white block mt-1">4/5</span>
                      <span className="text-[8px] text-gray-500 block">This Week</span>
                    </div>
                    <i className="lucide-dumbbell w-4.5 h-4.5 text-[#00D2FF]"></i>
                  </div>

                  {/* Water */}
                  <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-xl flex items-center justify-between">
                    <div>
                      <span className="text-[8.5px] text-gray-500 font-bold uppercase block tracking-wider font-outfit">Water</span>
                      <span className="text-[13px] font-black font-outfit text-white block mt-1">{waterLogged}</span>
                      <span className="text-[8px] text-gray-500 block">/ 3.0 L</span>
                    </div>
                    <i className="lucide-droplet w-4.5 h-4.5 text-blue-500"></i>
                  </div>

                </div>
              </div>

              {/* Progress Card Section */}
              <div className="flex flex-col gap-3 text-left">
                <h4 className="text-xs font-bold font-outfit text-gray-500 uppercase tracking-wider pl-1">Progress</h4>
                
                <div className="glass-panel p-4 bg-[#0F0F24]/60 border border-[#1F1F46]/50 rounded-2xl flex items-center justify-between min-h-[100px]">
                  <div>
                    <span className="text-[8px] text-gray-500 font-bold uppercase tracking-wider block font-outfit">Weight</span>
                    <span className="text-base font-black font-outfit text-white mt-1 block">{currentWeight} <span className="text-xs font-normal text-gray-400">kg</span></span>
                    <span className="text-[8.5px] font-bold text-emerald-400 mt-0.5 block flex items-center gap-0.5">↓ 1.2 kg <span className="text-gray-500 font-normal">weekly trend</span></span>
                  </div>
                  
                  {/* Glowing purple Weight sparkline graph */}
                  <div className="w-32 h-14 relative shrink-0">
                    <svg className="w-full h-full" viewBox="0 0 100 40" preserveAspectRatio="none">
                      <path d="M0,40 L0,32 Q25,28 50,15 T80,8 T100,2 L100,40 Z" fill="rgba(139, 92, 246, 0.03)" />
                      <path d="M0,32 Q25,28 50,15 T80,8 T100,2" stroke="#8B5CF6" strokeWidth="2" fill="none" strokeLinecap="round" style={{ filter: 'drop-shadow(0 2px 4px rgba(139,92,246,0.3))' }} />
                      <circle cx="100" cy="2" r="2.5" className="fill-[#00F0FF] stroke-[#8B5CF6]" strokeWidth="1" />
                    </svg>
                  </div>
                </div>
              </div>

            </div>

          </div>
        );
      };
"""
    
    # Complete replacement
    content = content[:start_index] + new_dashboard_code + content[end_index:]
    print("Injected re-engineered Dashboard component successfully!")
else:
    print("  [ERROR] Dashboard component boundaries could not be located in preview.html.")


# Save patched contents
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Final size:", len(content))
print("Patched successfully!")
