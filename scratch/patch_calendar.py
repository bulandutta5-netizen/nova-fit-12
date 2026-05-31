filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Declare the WorkoutCalendar sub-component right after InteractiveRoadmapCard
print("Injecting WorkoutCalendar sub-component...")

target_roadmap_end = """        return (
          <div className="mt-3 p-4 bg-[#121215]/80 border border-white/5 rounded-2xl relative overflow-hidden select-none hover:border-[#00D2FF]/20 transition-all font-sans text-left">
            <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold tracking-wider text-[#00F0FF] bg-[#00F0FF]/10 border-b border-l border-white/5 uppercase rounded-bl font-mono">
              PHYSIOLOGY TIMELINE
            </div>

            <div className="flex items-center gap-2 mb-3.5">
              <i className="lucide-line-chart text-[#00D2FF] w-4 h-4"></i>
              <div>
                <h4 className="text-[12px] font-bold text-white font-outfit">12-Week Physiological Roadmap</h4>
                <p className="text-[9px] text-gray-500 font-semibold uppercase font-mono mt-0.5">estimated weight prediction spline</p>
              </div>
            </div>

            {/* Line graph rendered elegantly via styled CSS SVG */}
            <div className="h-28 bg-white/[0.01] border border-white/5 p-2 rounded-xl mb-3.5 relative flex flex-col justify-end">
              <div className="absolute top-2 left-3 text-[8px] font-bold text-gray-500 font-mono">WEIGHT DEVIATION (KG)</div>
              
              {/* Elegant curved SVG line graph */}
              <svg className="w-full h-20 overflow-visible z-10" viewBox="0 0 100 40" preserveAspectRatio="none">
                <defs>
                  <linearGradient id="glowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stopColor="#00D2FF" stopOpacity="0.25" />
                    <stop offset="100%" stopColor="#00D2FF" stopOpacity="0.0" />
                  </linearGradient>
                </defs>
                {/* Weight projection path */}
                <path
                  d={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? "M 5,5 Q 50,18 95,35" 
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? "M 5,35 Q 50,22 95,5" 
                        : "M 5,20 Q 50,22 95,25"
                  }
                  fill="none"
                  stroke="url(#glowGrad)"
                  strokeWidth="4"
                />
                <path
                  d={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? "M 5,5 Q 50,18 95,35" 
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? "M 5,35 Q 50,22 95,5" 
                        : "M 5,20 Q 50,22 95,25"
                  }
                  fill="none"
                  stroke="#00D2FF"
                  strokeWidth="1.2"
                  strokeLinecap="round"
                />
                {/* Visual marker dot */}
                <circle
                  cx={progressWeek === 1 ? 5 : progressWeek === 4 ? 30 : progressWeek === 8 ? 60 : 95}
                  cy={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? (progressWeek === 1 ? 5 : progressWeek === 4 ? 14 : progressWeek === 8 ? 24 : 35)
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? (progressWeek === 1 ? 35 : progressWeek === 4 ? 26 : progressWeek === 8 ? 16 : 5)
                        : (progressWeek === 1 ? 20 : progressWeek === 4 ? 21 : progressWeek === 8 ? 23 : 25)
                  }
                  r="2.5"
                  fill="#9D00FF"
                  stroke="#fff"
                  strokeWidth="0.8"
                  className="animate-pulse"
                />
              </svg>

              {/* X axis labels */}
              <div className="flex justify-between text-[8px] text-gray-600 font-bold font-mono mt-1.5 px-1 pt-1.5 border-t border-white/5">
                <span>Wk 1 ({startW}kg)</span>
                <span>Wk 4</span>
                <span>Wk 8</span>
                <span>Wk 12 ({weightData[6].w.toFixed(1)}kg)</span>
              </div>
            </div>

            {/* Slider to interact with predictions */}
            <div className="bg-white/[0.01] border border-white/5 p-2.5 rounded-xl mb-4 text-[9.5px] font-mono leading-normal">
              <div className="flex justify-between items-center mb-1">
                <span className="text-gray-500">Timeline Phase:</span>
                <span className="text-white font-bold font-outfit text-[10px]">
                  {progressWeek <= 4 ? "Phase 1: CNS Prep" : progressWeek <= 8 ? "Phase 2: Lipid Burn" : "Phase 3: SubQ Lock"}
                </span>
              </div>
              <div className="flex justify-between items-center mb-2.5">
                <span className="text-gray-500">Predicted Mass:</span>
                <span className="text-[#00D2FF] font-black text-[11px]">{currentEstW} kg</span>
              </div>

              <input
                type="range"
                min="1"
                max="12"
                value={progressWeek}
                onChange={(e) => {
                  setProgressWeek(parseInt(e.target.value));
                  if (parseInt(e.target.value) % 3 === 0) {
                    try { playBeep(1000, 'sine', 0.03); } catch (ev) {}
                  }
                }}
                className="w-full h-1 bg-white/10 rounded-lg appearance-none cursor-pointer accent-[#9D00FF]"
              />
              <div className="flex justify-between text-[7px] text-gray-500 font-bold mt-1 uppercase">
                <span>Week 1</span>
                <span>Week 6</span>
                <span>Week 12</span>
              </div>
            </div>

            <div className="flex justify-end pt-2 border-t border-white/5">
              <button
                type="button"
                onClick={handlePdfDownload}
                disabled={pdfStatus === 'generating'}
                className="text-[9px] font-bold text-white font-outfit uppercase tracking-wider px-3.5 py-1.5 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] rounded-lg shadow-md hover:shadow-[0_0_12px_rgba(0,210,255,0.3)] transition-all flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                {pdfStatus === 'generating' ? (
                  <>
                    <span className="w-2 h-2 border border-white border-t-transparent rounded-full animate-spin" />
                    Generating...
                  </>
                ) : pdfStatus === 'success' ? (
                  <>
                    <i className="lucide-check w-3 h-3 text-emerald-400"></i>
                    PDF Downloaded
                  </>
                ) : (
                  <>
                    <i className="lucide-file-text w-3 h-3"></i>
                    Download PDF
                  </>
                )}
              </button>
            </div>
          </div>
        );
      };"""

workout_calendar_component = """        return (
          <div className="mt-3 p-4 bg-[#121215]/80 border border-white/5 rounded-2xl relative overflow-hidden select-none hover:border-[#00D2FF]/20 transition-all font-sans text-left">
            <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold tracking-wider text-[#00F0FF] bg-[#00F0FF]/10 border-b border-l border-white/5 uppercase rounded-bl font-mono">
              PHYSIOLOGY TIMELINE
            </div>

            <div className="flex items-center gap-2 mb-3.5">
              <i className="lucide-line-chart text-[#00D2FF] w-4 h-4"></i>
              <div>
                <h4 className="text-[12px] font-bold text-white font-outfit">12-Week Physiological Roadmap</h4>
                <p className="text-[9px] text-gray-500 font-semibold uppercase font-mono mt-0.5">estimated weight prediction spline</p>
              </div>
            </div>

            {/* Line graph rendered elegantly via styled SVG */}
            <div className="h-28 bg-white/[0.01] border border-white/5 p-2 rounded-xl mb-3.5 relative flex flex-col justify-end">
              <div className="absolute top-2 left-3 text-[8px] font-bold text-gray-500 font-mono">WEIGHT DEVIATION (KG)</div>
              
              {/* Elegant curved SVG line graph */}
              <svg className="w-full h-20 overflow-visible z-10" viewBox="0 0 100 40" preserveAspectRatio="none">
                <defs>
                  <linearGradient id="glowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stopColor="#00D2FF" stopOpacity="0.25" />
                    <stop offset="100%" stopColor="#00D2FF" stopOpacity="0.0" />
                  </linearGradient>
                </defs>
                {/* Weight projection path */}
                <path
                  d={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? "M 5,5 Q 50,18 95,35" 
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? "M 5,35 Q 50,22 95,5" 
                        : "M 5,20 Q 50,22 95,25"
                  }
                  fill="none"
                  stroke="url(#glowGrad)"
                  strokeWidth="4"
                />
                <path
                  d={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? "M 5,5 Q 50,18 95,35" 
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? "M 5,35 Q 50,22 95,5" 
                        : "M 5,20 Q 50,22 95,25"
                  }
                  fill="none"
                  stroke="#00D2FF"
                  strokeWidth="1.2"
                  strokeLinecap="round"
                />
                {/* Visual marker dot */}
                <circle
                  cx={progressWeek === 1 ? 5 : progressWeek === 4 ? 30 : progressWeek === 8 ? 60 : 95}
                  cy={
                    goal === 'shred' || goal.toLowerCase().includes('loss')
                      ? (progressWeek === 1 ? 5 : progressWeek === 4 ? 14 : progressWeek === 8 ? 24 : 35)
                      : goal === 'bulk' || goal.toLowerCase().includes('gain')
                        ? (progressWeek === 1 ? 35 : progressWeek === 4 ? 26 : progressWeek === 8 ? 16 : 5)
                        : (progressWeek === 1 ? 20 : progressWeek === 4 ? 21 : progressWeek === 8 ? 23 : 25)
                  }
                  r="2.5"
                  fill="#9D00FF"
                  stroke="#fff"
                  strokeWidth="0.8"
                  className="animate-pulse"
                />
              </svg>

              {/* X axis labels */}
              <div className="flex justify-between text-[8px] text-gray-600 font-bold font-mono mt-1.5 px-1 pt-1.5 border-t border-white/5">
                <span>Wk 1 ({startW}kg)</span>
                <span>Wk 4</span>
                <span>Wk 8</span>
                <span>Wk 12 ({weightData[6].w.toFixed(1)}kg)</span>
              </div>
            </div>

            {/* Slider to interact with predictions */}
            <div className="bg-white/[0.01] border border-white/5 p-2.5 rounded-xl mb-4 text-[9.5px] font-mono leading-normal">
              <div className="flex justify-between items-center mb-1">
                <span className="text-gray-500">Timeline Phase:</span>
                <span className="text-white font-bold font-outfit text-[10px]">
                  {progressWeek <= 4 ? "Phase 1: CNS Prep" : progressWeek <= 8 ? "Phase 2: Lipid Burn" : "Phase 3: SubQ Lock"}
                </span>
              </div>
              <div className="flex justify-between items-center mb-2.5">
                <span className="text-gray-500">Predicted Mass:</span>
                <span className="text-[#00D2FF] font-black text-[11px]">{currentEstW} kg</span>
              </div>

              <input
                type="range"
                min="1"
                max="12"
                value={progressWeek}
                onChange={(e) => {
                  setProgressWeek(parseInt(e.target.value));
                  if (parseInt(e.target.value) % 3 === 0) {
                    try { playBeep(1000, 'sine', 0.03); } catch (ev) {}
                  }
                }}
                className="w-full h-1 bg-white/10 rounded-lg appearance-none cursor-pointer accent-[#9D00FF]"
              />
              <div className="flex justify-between text-[7px] text-gray-500 font-bold mt-1 uppercase">
                <span>Week 1</span>
                <span>Week 6</span>
                <span>Week 12</span>
              </div>
            </div>

            <div className="flex justify-end pt-2 border-t border-white/5">
              <button
                type="button"
                onClick={handlePdfDownload}
                disabled={pdfStatus === 'generating'}
                className="text-[9px] font-bold text-white font-outfit uppercase tracking-wider px-3.5 py-1.5 bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] rounded-lg shadow-md hover:shadow-[0_0_12px_rgba(0,210,255,0.3)] transition-all flex items-center gap-1.5 cursor-pointer disabled:opacity-50"
              >
                {pdfStatus === 'generating' ? (
                  <>
                    <span className="w-2 h-2 border border-white border-t-transparent rounded-full animate-spin" />
                    Generating...
                  </>
                ) : pdfStatus === 'success' ? (
                  <>
                    <i className="lucide-check w-3 h-3 text-emerald-400"></i>
                    PDF Downloaded
                  </>
                ) : (
                  <>
                    <i className="lucide-file-text w-3 h-3"></i>
                    Download PDF
                  </>
                )}
              </button>
            </div>
          </div>
        );
      };

      // ======================================================
      // NEW COMPONENT: PREMIUM WORKOUT CALENDAR SYSTEM
      // ======================================================
      const WorkoutCalendar = ({ profile }) => {
        const level = profile.level || 'Intermediate';
        const location = profile.location || 'Gym';
        const injuries = profile.injuries || 'None';
        const calcs = profile.calculations || { targetCalories: 2200, targetProtein: 140 };

        const [calendarMode, setCalendarMode] = useState('monthly'); // 'monthly', 'weekly'
        const [selectedDay, setSelectedDay] = useState(null);
        const [reschedulingDay, setReschedulingDay] = useState(null);
        
        // Dynamic stats that update when workouts are completed
        const [completedDays, setCompletedDays] = useState([2, 4, 7, 9, 11, 14, 16, 18, 21, 23, 25]);
        const [missedDays, setMissedDays] = useState([12, 19]);
        const [streak, setStreak] = useState(3);
        const [hydration, setHydration] = useState(12);

        // Core base routines mapping for May 2026
        const [schedule, setSchedule] = useState(() => {
          const s = {};
          const daysInMonth = 31;
          
          let cycle = [];
          if (location === 'Home') {
            if (level === 'Beginner') {
              cycle = [
                { type: 'workout', name: 'Full Body A', duration: 35, cals: 210, exercises: ['Bodyweight Squats (3x15)', 'Incline Pushups (3x10)', 'Doorframe Towel Pulls (3x12)'], difficulty: 'Beginner', focus: 'CNS Prep' },
                { type: 'rest', name: 'Active Recovery', duration: 15, cals: 50, exercises: ['Mobility stretch (10m)', 'Light Core Plank (3x30s)'], difficulty: 'Rest', focus: 'Cellular Restoration' },
                { type: 'workout', name: 'Full Body B', duration: 40, cals: 240, exercises: ['Glute Bridges (3x15)', 'Chair Dips (3x8)', 'Backpack Rows (3x10)'], difficulty: 'Beginner', focus: 'CNS Prep' },
                { type: 'rest', name: 'Active Recovery', duration: 15, cals: 50, exercises: ['Dynamic Mobility Flow', 'Plank Walkholds (3x30s)'], difficulty: 'Rest', focus: 'Cellular Restoration' }
              ];
            } else {
              // Advanced/Intermediate Home
              cycle = [
                { type: 'workout', name: 'Upper Split', duration: 50, cals: 360, exercises: ['Regular Pushups (4x15)', 'Archer Pushups (3x8)', 'Backpack Rows (4x12)', 'Towel Facepulls (3x15)'], difficulty: 'Hard', focus: 'Upper Hypertrophy' },
                { type: 'workout', name: 'Lower Split', duration: 45, cals: 320, exercises: ['Bulgarian Split Squats (4x12)', 'Pistol Squats (3x6)', 'Single-Leg Calf Raises (4x15)'], difficulty: 'Intense', focus: 'Lower Hypertrophy' },
                { type: 'rest', name: 'Recovery Stretch', duration: 20, cals: 60, exercises: ['Stretching & Decompression', 'Yoga Flow (15m)', '15m Fasted Walk'], difficulty: 'Rest', focus: 'Joint Care' },
                { type: 'workout', name: 'Core & HIIT', duration: 35, cals: 300, exercises: ['Plank Walks (3x45s)', 'Burpees (4x45s)', 'Russian Twists (3x30/side)'], difficulty: 'Medium', focus: 'Core / Stamina' }
              ];
            }
          } else {
            // Gym Setup
            if (level === 'Beginner') {
              cycle = [
                { type: 'workout', name: 'Full Body A', duration: 45, cals: 290, exercises: ['Barbell Squats (3x8)', 'Barbell Bench Press (3x8)', 'Lat Pulldowns (3x10)'], difficulty: 'Beginner', focus: 'Strength Base' },
                { type: 'rest', name: 'Active Recovery', duration: 20, cals: 65, exercises: ['Joint mobility', 'Hanging Leg Raises (3x12)'], difficulty: 'Rest', focus: 'Restoration' },
                { type: 'workout', name: 'Posterior & Pulls', duration: 50, cals: 320, exercises: ['Romanian Deadlifts (3x10)', 'Seated Cable Rows (3x10)', 'Overhead Dumbbell Press (3x10)'], difficulty: 'Beginner', focus: 'Pull / Posterior' },
                { type: 'rest', name: 'Active Recovery', duration: 20, cals: 65, exercises: ['Dynamic Core Planks', 'Fasted morning LISS Walk'], difficulty: 'Rest', focus: 'Restoration' }
              ];
            } else if (level === 'Advanced') {
              cycle = [
                { type: 'workout', name: 'Push Hypertrophy', duration: 60, cals: 450, exercises: ['Incline Barbell Bench (4x8)', 'Flat DB Chest Press (3x10)', 'Dumbbell Lateral Raises (4x15)', 'Overhead Tricep Extension (3x12)'], difficulty: 'Extreme', focus: 'Anabolic Push' },
                { type: 'workout', name: 'Pull Hypertrophy', duration: 60, cals: 430, exercises: ['Weighted Pullups (4x6)', 'Barbell Bent Rows (4x8)', 'Chest-Supported DB Rows (3x12)', 'Hammer DB Curls (3x12)'], difficulty: 'Extreme', focus: 'Anabolic Pull' },
                { type: 'workout', name: 'Legs Performance', duration: 65, cals: 520, exercises: ['Barbell Back Squats (4x6)', 'Romanian Deadlifts (4x8)', 'Leg Extensions (3x15)', 'Seated Calf Raises (4x20)'], difficulty: 'Brutal', focus: 'Anabolic Lower' },
                { type: 'rest', name: 'Rest / Active Mobility', duration: 20, cals: 70, exercises: ['CNS Rest', 'Rotator Cuff exercises', '10m foam rolling'], difficulty: 'Rest', focus: 'CNS Reset' }
              ];
            } else {
              // Intermediate Gym
              cycle = [
                { type: 'workout', name: 'Upper A Split', duration: 55, cals: 380, exercises: ['Barbell Bench Press (4x6)', 'Barbell Bent Rows (4x8)', 'Incline DB Press (3x10)', 'Lateral DB Raises (3x12)'], difficulty: 'Hard', focus: 'Upper Strength' },
                { type: 'workout', name: 'Lower A Split', duration: 50, cals: 390, exercises: ['Barbell Back Squats (4x6)', 'Romanian Deadlifts (3x8)', 'Leg Press (3x12)', 'Calf Raises (4x15)'], difficulty: 'Hard', focus: 'Lower Strength' },
                { type: 'rest', name: 'Recovery Stretch', duration: 20, cals: 60, exercises: ['Stretching & Decompression', 'Dynamic Mobility flow (10m)'], difficulty: 'Rest', focus: 'CNS Downregulate' },
                { type: 'workout', name: 'Upper B Split', duration: 50, cals: 360, exercises: ['Overhead Press (OHP) (4x6)', 'Wide Grip Pullups (4x8)', 'DB Incline Flyes (3x12)', 'Hammer Curls (3x12)'], difficulty: 'Hard', focus: 'Upper Hypertrophy' }
              ];
            }
          }

          // Distribute the cycle rolling over the 31 days
          for (let d = 1; d <= daysInMonth; d++) {
            s[d] = { ...cycle[(d - 1) % cycle.length], dayNum: d };
          }
          return s;
        });

        // Current open day details
        const selectedDayDetails = selectedDay ? schedule[selectedDay] : null;

        // Interactive checking states in modal panel
        const [exerciseChecks, setExerciseChecks] = useState({});

        // Calculate consistency score dynamically
        const totalPastDays = completedDays.length + missedDays.length;
        const consistencyScore = totalPastDays > 0 ? Math.round((completedDays.length / totalPastDays) * 100) : 100;

        // Toggle checkbox inside detail panel
        const toggleExerciseCheck = (exName) => {
          setExerciseChecks(prev => ({ ...prev, [exName]: !prev[exName] }));
          try { playBeep(700, 'triangle', 0.05); } catch(e) {}
        };

        // Mark current workout as fully completed
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
        };

        // Reschedule action: Shift to tomorrow (swaps schedule item with tomorrow's rest or shifts everything)
        const handleReschedule = (day) => {
          const targetDay = day === 31 ? 30 : day + 1;
          
          setSchedule(prev => {
            const copy = { ...prev };
            const temp = copy[day];
            copy[day] = { ...copy[targetDay], dayNum: day };
            copy[targetDay] = { ...temp, dayNum: targetDay };
            return copy;
          });

          // Play click sound
          try { playBeep(600, 'sine', 0.08); } catch(e) {}
          setReschedulingDay(null);
          setSelectedDay(null);
          alert(`Success: Workout rescheduled. Swapped Day ${day} with Day ${targetDay}!`);
        };

        // Apply injury adaptations to exercises inside detail panel
        const getAdaptedExercises = (dayItem) => {
          if (!dayItem || !dayItem.exercises) return [];
          return dayItem.exercises.map(ex => {
            let name = ex;
            let isModified = false;

            if (injuries.toLowerCase().includes('knee') && ex.includes('Back Squats')) {
              name = "Box Squats (Knee-Safe option)";
              isModified = true;
            } else if (injuries.toLowerCase().includes('back') && (ex.includes('Deadlift') || ex.includes('Back Squats'))) {
              name = ex.includes('Deadlift') ? "Chest-Supported DB Rows" : "Goblet Squats (Spine-Safe)";
              isModified = true;
            } else if (injuries.toLowerCase().includes('shoulder') && (ex.includes('Bench Press') || ex.includes('OHP') || ex.includes('Overhead'))) {
              name = "Neutral DB Press (Shoulder-Safe)";
              isModified = true;
            }
            return { raw: ex, name, isModified };
          });
        };

        // Render Calendar Grid (31 Days of May 2026)
        const renderDaysGrid = () => {
          const dayElements = [];
          for (let d = 1; d <= 31; d++) {
            const item = schedule[d];
            const isCompleted = completedDays.includes(d);
            const isMissed = missedDays.includes(d);
            const isRest = item.type === 'rest';
            const isToday = d === 29; // Today's coordinate

            let borderStyle = "border-white/5 hover:border-[#00D2FF]/20";
            let bgStyle = "bg-[#121215]/40 hover:bg-[#121215]/80";
            let indicatorColor = "text-gray-500";
            let labelBadge = null;

            if (isCompleted) {
              borderStyle = "border-emerald-500/30 hover:border-emerald-500/50";
              bgStyle = "bg-emerald-500/5 hover:bg-emerald-500/10";
              indicatorColor = "text-emerald-400";
              labelBadge = "✓";
            } else if (isMissed) {
              borderStyle = "border-red-500/20 hover:border-red-500/40";
              bgStyle = "bg-red-500/5 hover:bg-red-500/10";
              indicatorColor = "text-red-400";
              labelBadge = "!";
            } else if (isRest) {
              borderStyle = "border-blue-500/10 hover:border-blue-500/35";
              bgStyle = "bg-blue-500/[0.02] hover:bg-blue-500/5";
              indicatorColor = "text-blue-500";
            }

            if (isToday) {
              borderStyle = "border-[#00D2FF] shadow-[0_0_15px_rgba(0,210,255,0.25)] ring-1 ring-[#00D2FF]/30";
              bgStyle = "bg-gradient-to-br from-[#121215]/90 to-[#0B0B0C]";
            }

            dayElements.push(
              <div
                key={d}
                onClick={() => {
                  playBeep(900, 'sine', 0.04);
                  setSelectedDay(d);
                }}
                className={`p-3 rounded-2xl border ${borderStyle} ${bgStyle} cursor-pointer transition-all duration-300 flex flex-col justify-between aspect-square select-none relative group`}
              >
                <div className="flex justify-between items-start">
                  <span className={`text-[11px] font-bold font-mono ${isToday ? 'text-[#00D2FF]' : 'text-gray-400'}`}>
                    {d}
                  </span>
                  {labelBadge && (
                    <span className={`text-[9px] font-black font-mono shrink-0 px-1 rounded uppercase ${
                      isCompleted ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'
                    }`}>
                      {labelBadge}
                    </span>
                  )}
                </div>

                <div className="text-left mt-auto">
                  <span className="text-[7.5px] font-bold font-outfit uppercase tracking-wide block truncate text-gray-500 group-hover:text-white transition-colors">
                    {item.name}
                  </span>
                  <span className={`text-[7px] font-mono block truncate ${indicatorColor} font-bold mt-0.5 uppercase`}>
                    {isRest ? "REST & RECOVER" : item.focus}
                  </span>
                </div>

                {isToday && (
                  <span className="absolute top-1 right-1.5 flex h-1.5 w-1.5 shrink-0">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#00D2FF] opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-1.5 w-1.5 bg-[#00D2FF]"></span>
                  </span>
                )}
              </div>
            );
          }
          return dayElements;
        };

        // Render Weekly List view for simulated mobile swiping
        const renderWeeklyListView = () => {
          const daysOfWeek = [];
          // Render days 25 to 31 (current week in May 2026)
          for (let d = 25; d <= 31; d++) {
            const item = schedule[d];
            const isCompleted = completedDays.includes(d);
            const isMissed = missedDays.includes(d);
            const isToday = d === 29;
            const isRest = item.type === 'rest';

            let borderStyle = "border-white/5";
            let bgStyle = "bg-[#121215]/50";
            let indicator = <div className="w-2 h-2 rounded-full bg-gray-600" />;

            if (isCompleted) {
              borderStyle = "border-emerald-500/20";
              bgStyle = "bg-emerald-500/5";
              indicator = <i className="lucide-check-circle2 text-emerald-400 w-4 h-4"></i>;
            } else if (isMissed) {
              borderStyle = "border-red-500/10";
              bgStyle = "bg-red-500/5";
              indicator = <i className="lucide-alert-circle text-red-400 w-4 h-4"></i>;
            } else if (isRest) {
              borderStyle = "border-blue-500/10";
              bgStyle = "bg-blue-500/[0.02]";
              indicator = <i className="lucide-battery-charging text-blue-500 w-4 h-4"></i>;
            }

            if (isToday) {
              borderStyle = "border-[#00D2FF]";
              bgStyle = "bg-gradient-to-r from-[#121215] to-[#0A0A0C]";
              indicator = <span className="w-2.5 h-2.5 rounded-full bg-[#00D2FF] shadow-[0_0_8px_#00D2FF] animate-pulse" />;
            }

            daysOfWeek.push(
              <div
                key={d}
                onClick={() => setSelectedDay(d)}
                className={`p-4 rounded-2xl border ${borderStyle} ${bgStyle} cursor-pointer transition-all duration-300 flex items-center justify-between select-none`}
              >
                <div className="flex items-center gap-3">
                  <span className={`text-[12px] font-bold font-mono ${isToday ? 'text-[#00D2FF]' : 'text-gray-400'}`}>
                    Day {d}
                  </span>
                  <div>
                    <h4 className="text-[11px] font-bold text-white font-outfit uppercase tracking-wide">{item.name}</h4>
                    <p className="text-[8.5px] text-gray-500 font-semibold uppercase mt-0.5">{isRest ? 'Rest / Mobility' : item.focus}</p>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className="text-[9px] text-gray-500 font-mono font-bold uppercase">{item.duration} min | {item.cals} kcal</span>
                  {indicator}
                </div>
              </div>
            );
          }
          return daysOfWeek;
        };

        return (
          <div className="flex flex-col gap-6 max-w-5xl mx-auto p-1 text-left select-none relative z-10">
            {/* Calendar Dashboard Stats Header */}
            <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 w-full">
              {/* Streaks Card */}
              <div className="glass-panel p-4 rounded-2xl glow-border card-radial-blue border-white/5 flex items-center gap-4">
                <div className="p-3 bg-orange-500/15 text-orange-500 rounded-xl shrink-0"><i className="lucide-flame w-5 h-5 fill-orange-500/10"></i></div>
                <div>
                  <span className="text-[9px] text-gray-500 font-bold block uppercase tracking-wider">Active Streak</span>
                  <span className="text-lg font-black font-outfit text-white mt-0.5 block">{streak} Days Solid</span>
                </div>
              </div>

              {/* Consistency Card */}
              <div className="glass-panel p-4 rounded-2xl glow-border card-radial-purple border-white/5 flex items-center gap-4">
                <div className="p-3 bg-[#00F0FF]/10 text-[#00F0FF] rounded-xl shrink-0"><i className="lucide-activity w-5 h-5"></i></div>
                <div>
                  <span className="text-[9px] text-gray-500 font-bold block uppercase tracking-wider">Consistency Rating</span>
                  <span className="text-lg font-black font-outfit text-white mt-0.5 block">{consistencyScore}% Target Lock</span>
                </div>
              </div>

              {/* Hydration cups tracker */}
              <div className="glass-panel p-4 rounded-2xl glow-border card-radial-blue border-white/5 flex items-center gap-4">
                <div className="p-3 bg-blue-500/15 text-blue-500 rounded-xl shrink-0"><i className="lucide-droplet w-5 h-5 fill-blue-500/10"></i></div>
                <div className="flex-1">
                  <div className="flex justify-between items-center pr-2">
                    <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block">Hydration Habit</span>
                    <button 
                      onClick={() => { setHydration(prev => Math.min(18, prev + 1)); try { playBeep(800, 'sine', 0.05); } catch(e) {} }}
                      className="text-[8px] font-black uppercase text-[#00F0FF] bg-[#00F0FF]/15 border border-[#00F0FF]/30 px-1.5 py-0.5 rounded cursor-pointer transition-all"
                    >
                      + Cup
                    </button>
                  </div>
                  <span className="text-lg font-black font-outfit text-white mt-0.5 block">{hydration} / 14 Cups Logged</span>
                </div>
              </div>

              {/* Workout splits overview card */}
              <div className="glass-panel p-4 rounded-2xl glow-border card-radial-purple border-white/5 flex items-center gap-4">
                <div className="p-3 bg-[#9D00FF]/10 text-[#9D00FF] rounded-xl shrink-0"><i className="lucide-dumbbell w-5 h-5"></i></div>
                <div>
                  <span className="text-[9px] text-gray-500 font-bold block uppercase tracking-wider">Target Level Split</span>
                  <span className="text-lg font-black font-outfit text-white mt-0.5 block truncate uppercase">{level} {location}</span>
                </div>
              </div>
            </div>

            {/* Mode Selector Tab & Title Header */}
            <div className="glass-panel p-4 rounded-3xl border-white/5 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-black/20">
              <div className="flex items-center gap-2.5">
                <i className="lucide-calendar text-[#00D2FF] w-5 h-5"></i>
                <div>
                  <h3 className="text-md font-bold text-white font-outfit">AI Performance Calendar</h3>
                  <p className="text-[10px] text-gray-500 font-semibold uppercase font-mono mt-0.5">May 2026 Transformation block</p>
                </div>
              </div>

              {/* View switch toggles */}
              <div className="flex bg-white/5 p-1 rounded-xl border border-white/5 gap-1 shrink-0 self-start sm:self-auto select-none">
                {[
                  { id: 'monthly', label: 'Monthly Grid' },
                  { id: 'weekly', label: 'Weekly Swiper' }
                ].map(tab => (
                  <button
                    key={tab.id}
                    type="button"
                    onClick={() => { playBeep(900, 'sine', 0.05); setCalendarMode(tab.id); }}
                    className={`px-3 py-1.5 rounded-lg text-[9.5px] font-bold uppercase tracking-wider transition-all cursor-pointer ${
                      calendarMode === tab.id 
                        ? 'bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white shadow-sm' 
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    {tab.label}
                  </button>
                ))}
              </div>
            </div>

            {/* 31-Day Grid / Weekly Spline Container */}
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
            )}

            {/* Recovery Recap bulletin card */}
            <div className="glass-panel p-5 rounded-3xl border-white/5 card-radial-blue flex flex-col sm:flex-row sm:items-center justify-between gap-5 relative overflow-hidden">
              <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold text-[#00F0FF] bg-[#00F0FF]/15 uppercase font-mono rounded-bl border-b border-l border-white/5">
                Weekly Summary
              </div>
              <div className="flex gap-4 items-center">
                <div className="p-3 bg-[#00F0FF]/10 text-[#00F0FF] rounded-xl shrink-0"><i className="lucide-sparkles w-5 h-5"></i></div>
                <div>
                  <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit">Coach Nova Vitals Recap</h4>
                  <p className="text-[11px] text-gray-400 leading-normal mt-1 max-w-xl font-sans">
                    "Your weekly consistency is locked at **{consistencyScore}%**. Hydration coordinates are solid. Under your **{injuries}** joint limits, always focus on slow eccentric execution. Let's conquer the next block."
                  </p>
                </div>
              </div>

              <div className="flex gap-3 text-center shrink-0 font-mono text-[10px] text-gray-500 font-semibold">
                <div className="bg-white/[0.01] border border-white/5 p-2 px-3.5 rounded-xl">
                  <span className="block text-[7px] font-bold uppercase tracking-wider text-gray-500">Target kcal</span>
                  <span className="text-white font-bold font-outfit text-sm mt-0.5 block">{calcs.targetCalories}</span>
                </div>
                <div className="bg-white/[0.01] border border-white/5 p-2 px-3.5 rounded-xl">
                  <span className="block text-[7px] font-bold uppercase tracking-wider text-gray-500">Protein</span>
                  <span className="text-[#00D2FF] font-bold font-outfit text-sm mt-0.5 block">{calcs.targetProtein}g</span>
                </div>
              </div>
            </div>

            {/* ============================================================== */}
            {/* WORKOUT DETAIL SLIDE-OVER / MODAL CONTAINER */}
            {/* ============================================================== */}
            {selectedDayDetails && (() => {
              const isRest = selectedDayDetails.type === 'rest';
              const isCompleted = completedDays.includes(selectedDay);
              const isMissed = missedDays.includes(selectedDay);
              const adaptedExercises = getAdaptedExercises(selectedDayDetails);

              // Calculate checkbox completion score inside modal
              const checkedCount = adaptedExercises.filter(ex => exerciseChecks[ex.name]).length;
              const percentFinished = adaptedExercises.length > 0 ? Math.round((checkedCount / adaptedExercises.length) * 100) : 0;
              const allChecked = checkedCount === adaptedExercises.length && adaptedExercises.length > 0;

              return (
                <div className="fixed inset-0 w-full h-full flex items-center justify-center bg-black/80 backdrop-blur-sm z-50 p-4 select-none animate-bubble-appear">
                  <div className="relative w-full max-w-md p-6 glass-panel rounded-3xl glow-border border-white/5 card-radial-purple flex flex-col gap-4 text-left">
                    {/* Close Trigger */}
                    <button 
                      onClick={() => { setSelectedDay(null); setExerciseChecks({}); setReschedulingDay(null); }}
                      className="absolute top-4 right-4 p-2 bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white rounded-full cursor-pointer transition-colors"
                    >
                      <i className="lucide-x w-4.5 h-4.5"></i>
                    </button>

                    {/* Modal Title */}
                    <div className="flex items-center gap-3">
                      <div className={`p-3 rounded-xl shrink-0 ${isRest ? 'bg-blue-500/10 text-blue-500' : 'bg-[#9D00FF]/15 text-[#9D00FF]'}`}>
                        <i className={isRest ? 'lucide-battery-charging w-5 h-5' : 'lucide-dumbbell w-5 h-5'}></i>
                      </div>
                      <div>
                        <span className="text-[8px] font-bold tracking-widest text-[#00F0FF] uppercase font-mono block">
                          Day {selectedDay} — Calibrating Split
                        </span>
                        <h4 className="text-md font-bold text-white font-outfit mt-0.5 uppercase tracking-wide">
                          {selectedDayDetails.name}
                        </h4>
                      </div>
                    </div>

                    <div className="h-px bg-white/5" />

                    {/* Specifications Grid */}
                    <div className="grid grid-cols-3 gap-2 font-mono text-[9.5px]">
                      <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                        <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Difficulty</span>
                        <span className={`font-bold font-outfit mt-0.5 block ${isRest ? 'text-blue-500' : 'text-[#00F0FF]'}`}>{selectedDayDetails.difficulty}</span>
                      </div>
                      <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                        <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Duration</span>
                        <span className="text-white font-bold font-outfit mt-0.5 block">{selectedDayDetails.duration} Min</span>
                      </div>
                      <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                        <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Metabolic Burn</span>
                        <span className="text-white font-bold font-outfit mt-0.5 block">{selectedDayDetails.cals} KCALS</span>
                      </div>
                    </div>

                    {/* Progress indicator */}
                    {!isRest && !isCompleted && adaptedExercises.length > 0 && (
                      <div className="bg-white/5 border border-white/5 p-2.5 rounded-xl text-[9px] font-mono select-none leading-normal">
                        <div className="flex justify-between items-center mb-1.5 font-bold">
                          <span className="text-gray-400">SESSION TRACKING PROGRESS:</span>
                          <span className="text-[#00F0FF]">{percentFinished}%</span>
                        </div>
                        <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                          <div className="h-full bg-[#00D2FF] rounded-full transition-all duration-500" style={{ width: `${percentFinished}%` }} />
                        </div>
                      </div>
                    )}

                    {/* Exercises Checklist block */}
                    <div className="flex flex-col gap-2.5">
                      <span className="text-[8px] text-gray-500 font-bold uppercase tracking-widest font-mono">
                        {isRest ? "Mobility Protocol Options" : "Required Exercise Check"}
                      </span>
                      
                      <div className="flex flex-col gap-2 max-h-[160px] overflow-y-auto pr-1">
                        {adaptedExercises.map((ex, idx) => {
                          const isChecked = !!exerciseChecks[ex.name];
                          return (
                            <div 
                              key={idx}
                              onClick={() => { if (!isCompleted && !isRest) toggleExerciseCheck(ex.name); }}
                              className={`p-2.5 rounded-xl border flex items-center justify-between transition-all select-none text-[11px] font-mono leading-normal ${
                                isCompleted
                                  ? 'border-white/5 bg-white/[0.01] opacity-75'
                                  : isRest
                                    ? 'border-blue-500/10 bg-blue-500/[0.02]'
                                    : isChecked 
                                      ? 'border-[#00D2FF]/40 bg-[#00D2FF]/10 text-white shadow-sm' 
                                      : 'border-white/5 bg-[#121215]/80 hover:border-white/10 cursor-pointer text-gray-300'
                              }`}
                            >
                              <div className="flex items-center gap-2.5">
                                {!isCompleted && !isRest && (
                                  <div className={`w-3.5 h-3.5 rounded border flex items-center justify-center shrink-0 transition-all ${
                                    isChecked ? 'bg-[#00D2FF] border-[#00D2FF] text-black' : 'border-white/20 bg-transparent'
                                  }`}>
                                    {isChecked && <i className="lucide-check w-2.5 h-2.5 stroke-[4]"></i>}
                                  </div>
                                )}
                                <span className={isChecked ? 'line-through text-gray-500' : ''}>
                                  {ex.name}
                                </span>
                              </div>
                              
                              {ex.isModified && !isRest && (
                                <span className="text-[7px] font-black uppercase bg-amber-500/10 text-amber-500 border border-amber-500/20 px-1 rounded shrink-0 font-sans">
                                  Safe Swap
                                </span>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    </div>

                    {/* AI Coach Tips Bulletin */}
                    <div className="bg-black/35 border border-white/5 p-3 rounded-2xl text-[9px] text-gray-400 leading-normal font-sans text-left">
                      <span className="text-[#00F0FF] font-bold uppercase tracking-wider block mb-1">COACH NOVA ADAPTATION</span>
                      {isRest 
                        ? `"Your central nervous system (CNS) requires down-regulation today, champion. Drink 4L+ of water and focus on dynamic leg/hip mobility to drain waste lactic acids."` 
                        : injuries !== 'None' 
                          ? `"Active safeguard override is enabled for: ${injuries}. Standard compound movements have been substituted with joint-safe splits. Do not load past failure."`
                          : `"Your consistency rating is logged at ${consistencyScore}%. Recovery reserves are completely optimal. Apply a progressive +5% weight overload target on your compound lifts today!"`
                      }
                    </div>

                    {/* Interactive Completion and Reschedule Triggers */}
                    <div className="flex items-center justify-between gap-3 pt-3 border-t border-white/5">
                      {/* Reschedule Button */}
                      {!isCompleted && (
                        <div className="relative shrink-0">
                          {reschedulingDay === selectedDay ? (
                            <div className="absolute bottom-11 left-0 bg-[#121215] border border-white/10 p-2 rounded-xl flex flex-col gap-1.5 shadow-xl w-36 z-50 animate-bubble-appear select-none">
                              <span className="text-[7.5px] text-gray-500 font-bold uppercase tracking-wide text-center">MOVE WORKOUT</span>
                              <button 
                                onClick={() => handleReschedule(selectedDay)}
                                className="w-full text-center py-1 bg-white/5 hover:bg-white/10 text-[9px] font-bold rounded-lg cursor-pointer uppercase tracking-wider text-[#00D2FF]"
                              >
                                Move Tomorrow
                              </button>
                            </div>
                          ) : null}
                          <button
                            type="button"
                            onClick={() => {
                              try { playBeep(800, 'sine', 0.05); } catch(e) {}
                              setReschedulingDay(prev => (prev === selectedDay ? null : selectedDay));
                            }}
                            className={`text-[9.5px] font-bold uppercase tracking-wider px-3 py-2.5 rounded-xl border transition-all cursor-pointer flex items-center gap-1 ${
                              reschedulingDay === selectedDay ? 'bg-white/10 border-white/20 text-white' : 'bg-white/5 border-white/5 text-gray-400 hover:text-white'
                            }`}
                          >
                            <i className="lucide-calendar-range w-3.5 h-3.5"></i>
                            Reschedule
                          </button>
                        </div>
                      )}

                      {/* Complete / Status Action Button */}
                      {isCompleted ? (
                        <div className="flex-1 text-center py-2.5 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-xl font-bold uppercase tracking-wider text-[10px] flex items-center justify-center gap-1.5">
                          <i className="lucide-check w-3.5 h-3.5 stroke-[3]"></i> Completed session
                        </div>
                      ) : isRest ? (
                        <button
                          type="button"
                          onClick={() => {
                            setSelectedDay(null);
                            try { playBeep(1100, 'sine', 0.08); } catch(e) {}
                          }}
                          className="flex-1 text-center py-2.5 bg-[#00D2FF]/10 hover:bg-[#00D2FF]/20 border border-[#00D2FF]/30 text-[#00D2FF] rounded-xl font-bold uppercase tracking-wider text-[10px] cursor-pointer transition-all"
                        >
                          Lock recovery complete
                        </button>
                      ) : (
                        <button
                          type="button"
                          onClick={() => handleMarkComplete(selectedDay)}
                          disabled={!allChecked}
                          className={`flex-1 text-center py-2.5 rounded-xl font-bold uppercase tracking-wider text-[10px] transition-all flex items-center justify-center gap-1.5 cursor-pointer ${
                            allChecked 
                              ? 'bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white shadow-md shadow-[#9D00FF]/20 active:scale-[0.98]' 
                              : 'bg-white/5 text-gray-500 border border-white/5 cursor-not-allowed opacity-65'
                          }`}
                        >
                          <i className="lucide-check w-3.5 h-3.5"></i>
                          {allChecked ? "Complete Workout" : "Check Exercises First"}
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              );
            })()}
          </div>
        );
      };"""

if target_roadmap_end in code:
    code = code.replace(target_roadmap_end, workout_calendar_component)
    print("WorkoutCalendar React component injected successfully.")
else:
    print("ERROR: target_roadmap_end not found.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Calendar component injection complete.")
