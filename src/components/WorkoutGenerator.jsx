import React, { useState, useEffect } from 'react'
import { Sparkles, Dumbbell, Home, Zap, Timer, Play, Pause, RotateCcw, CheckCircle2 } from 'lucide-react'

// Localized workouts database
const getWorkoutPlan = (type, level) => {
  const plans = {
    gym: {
      beginner: [
        {
          day: 'Day 1',
          focus: 'Full Body Push',
          exercises: [
            { name: 'Barbell Bench Press', sets: 3, reps: '10-12', rest: 60, cal: 110, icon: '💪' },
            { name: 'Dumbbell Shoulder Press', sets: 3, reps: '12', rest: 60, cal: 85, icon: '🏋️' },
            { name: 'Leg Press', sets: 3, reps: '12-15', rest: 90, cal: 120, icon: '🦵' },
            { name: 'Triceps Rope Pushdowns', sets: 3, reps: '15', rest: 45, cal: 60, icon: '⚡' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Full Body Pull',
          exercises: [
            { name: 'Lat Pulldowns', sets: 3, reps: '12', rest: 60, cal: 95, icon: '💪' },
            { name: 'Seated Cable Rows', sets: 3, reps: '12', rest: 60, cal: 90, icon: '🏋️' },
            { name: 'Lying Leg Curls', sets: 3, reps: '15', rest: 60, cal: 80, icon: '🦵' },
            { name: 'Dumbbell Bicep Curls', sets: 3, reps: '15', rest: 45, cal: 55, icon: '⚡' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'Core & Endurance',
          exercises: [
            { name: 'Plank Hold', sets: 3, reps: '45 sec', rest: 45, cal: 40, icon: '🧘' },
            { name: 'Hanging Knee Raises', sets: 3, reps: '15', rest: 45, cal: 50, icon: '⚡' },
            { name: 'Leg Extensions', sets: 3, reps: '15', rest: 60, cal: 75, icon: '🦵' },
            { name: 'Incline Treadmill Walk', sets: 1, reps: '20 mins', rest: 0, cal: 180, icon: '🏃' }
          ]
        }
      ],
      intermediate: [
        {
          day: 'Day 1',
          focus: 'Hypertrophy Chest & Triceps',
          exercises: [
            { name: 'Incline Dumbbell Bench Press', sets: 4, reps: '8-10', rest: 90, cal: 140, icon: '🏋️' },
            { name: 'Flat Barbell Bench Press', sets: 4, reps: '10', rest: 90, cal: 130, icon: '💪' },
            { name: 'Cable Chest Flys', sets: 3, reps: '12-15', rest: 60, cal: 90, icon: '⚡' },
            { name: 'Weighted Dips', sets: 3, reps: '10', rest: 75, cal: 95, icon: '💪' },
            { name: 'Skull Crushers', sets: 3, reps: '12', rest: 60, cal: 75, icon: '⚡' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Hypertrophy Back & Biceps',
          exercises: [
            { name: 'Bent Over Barbell Rows', sets: 4, reps: '8-10', rest: 90, cal: 150, icon: '🏋️' },
            { name: 'Wide Grip Pullups', sets: 4, reps: 'AMRAP', rest: 90, cal: 120, icon: '💪' },
            { name: 'Single Arm Dumbbell Rows', sets: 3, reps: '12', rest: 60, cal: 100, icon: '🏋️' },
            { name: 'Incline Dumbbell Curls', sets: 3, reps: '12', rest: 60, cal: 65, icon: '⚡' },
            { name: 'Preacher Curls', sets: 3, reps: '15', rest: 45, cal: 60, icon: '💪' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'Hypertrophy Legs & Shoulders',
          exercises: [
            { name: 'Barbell Back Squats', sets: 4, reps: '8-10', rest: 120, cal: 210, icon: '🦵' },
            { name: 'Romanian Deadlifts', sets: 4, reps: '10', rest: 90, cal: 180, icon: '🏋️' },
            { name: 'Standing Military Press', sets: 4, reps: '8-10', rest: 90, cal: 130, icon: '🏋️' },
            { name: 'Dumbbell Lateral Raises', sets: 3, reps: '15', rest: 45, cal: 70, icon: '⚡' },
            { name: 'Leg Press Calf Raises', sets: 4, reps: '15-20', rest: 60, cal: 85, icon: '🦵' }
          ]
        }
      ],
      advanced: [
        {
          day: 'Day 1',
          focus: 'Push Power / Strength',
          exercises: [
            { name: 'Heavy Bench Press', sets: 5, reps: '5', rest: 180, cal: 190, icon: '🏋️' },
            { name: 'Overhead Press', sets: 5, reps: '5', rest: 150, cal: 160, icon: '🏋️' },
            { name: 'Close-Grip Bench Press', sets: 4, reps: '8', rest: 90, cal: 120, icon: '💪' },
            { name: 'Weighted Chest Dips', sets: 4, reps: '8-10', rest: 90, cal: 135, icon: '💪' },
            { name: 'Dumbbell Lateral Raises', sets: 4, reps: '12-15', rest: 45, cal: 85, icon: '⚡' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Pull Power / Strength',
          exercises: [
            { name: 'Deadlifts', sets: 5, reps: '5', rest: 180, cal: 290, icon: '🏋️' },
            { name: 'Weighted Pullups', sets: 5, reps: '6-8', rest: 120, cal: 150, icon: '💪' },
            { name: 'Heavy T-Bar Rows', sets: 4, reps: '8', rest: 90, cal: 145, icon: '🏋️' },
            { name: 'Barbell Bicep Curls', sets: 4, reps: '8-10', rest: 75, cal: 80, icon: '⚡' },
            { name: 'Face Pulls', sets: 4, reps: '15', rest: 45, cal: 65, icon: '🧠' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'Squat Power / Strength',
          exercises: [
            { name: 'Barbell Back Squats', sets: 5, reps: '5', rest: 180, cal: 280, icon: '🦵' },
            { name: 'Front Squats', sets: 4, reps: '8', rest: 120, cal: 185, icon: '🦵' },
            { name: 'Standing Calf Raises', sets: 4, reps: '12', rest: 60, cal: 75, icon: '🦶' },
            { name: 'Hanging Leg Raises', sets: 4, reps: '15', rest: 45, cal: 60, icon: '🧘' },
            { name: 'Ab Wheel Rollouts', sets: 4, reps: '12', rest: 60, cal: 70, icon: '⚡' }
          ]
        }
      ]
    },
    home: {
      beginner: [
        {
          day: 'Day 1',
          focus: 'Full Body Cardio & Burn',
          exercises: [
            { name: 'Bodyweight Squats', sets: 3, reps: '15', rest: 45, cal: 70, icon: '🦵' },
            { name: 'Standard Pushups (Knees OK)', sets: 3, reps: '10-12', rest: 45, cal: 60, icon: '💪' },
            { name: 'Jumping Jacks', sets: 3, reps: '30 sec', rest: 30, cal: 90, icon: '🏃' },
            { name: 'Plank Hold', sets: 3, reps: '30 sec', rest: 45, cal: 35, icon: '🧘' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Core & Mobility',
          exercises: [
            { name: 'Glute Bridges', sets: 3, reps: '15', rest: 45, cal: 50, icon: '🦵' },
            { name: 'Bird Dogs', sets: 3, reps: '12 per side', rest: 30, cal: 40, icon: '🧘' },
            { name: 'Mountain Climbers', sets: 3, reps: '30 sec', rest: 30, cal: 85, icon: '🏃' },
            { name: 'Bicycle Crunches', sets: 3, reps: '15', rest: 45, cal: 45, icon: '⚡' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'Lower Body Endurance',
          exercises: [
            { name: 'Forward Lunges', sets: 3, reps: '10 per side', rest: 45, cal: 65, icon: '🦵' },
            { name: 'Wall Sit Hold', sets: 3, reps: '30 sec', rest: 45, cal: 50, icon: '🧘' },
            { name: 'Calf Raises', sets: 3, reps: '20', rest: 30, cal: 40, icon: '🦶' },
            { name: 'Flutter Kicks', sets: 3, reps: '30 sec', rest: 30, cal: 45, icon: '⚡' }
          ]
        }
      ],
      intermediate: [
        {
          day: 'Day 1',
          focus: 'Calisthenics Push & Core',
          exercises: [
            { name: 'Decline Pushups', sets: 4, reps: '15', rest: 60, cal: 95, icon: '💪' },
            { name: 'Standard Pushups', sets: 4, reps: '20', rest: 45, cal: 85, icon: '💪' },
            { name: 'Dips (Chair/Bench)', sets: 3, reps: '15', rest: 45, cal: 75, icon: '⚡' },
            { name: 'Pike Pushups', sets: 3, reps: '10', rest: 60, cal: 80, icon: '🏋️' },
            { name: 'Bicycle Crunches', sets: 4, reps: '20', rest: 45, cal: 55, icon: '🧘' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Calisthenics Pull & Legs',
          exercises: [
            { name: 'Doorframe Pulls / Inverted Rows', sets: 4, reps: '12', rest: 60, cal: 90, icon: '💪' },
            { name: 'Jump Squats', sets: 4, reps: '15', rest: 60, cal: 130, icon: '🦵' },
            { name: 'Walking Lunges', sets: 3, reps: '20 steps', rest: 45, cal: 80, icon: '🦵' },
            { name: 'Supermans', sets: 3, reps: '12', rest: 45, cal: 40, icon: '🧘' },
            { name: 'Plank to Pushup', sets: 3, reps: '10', rest: 45, cal: 70, icon: '⚡' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'HIIT Fat Burner',
          exercises: [
            { name: 'Burpees', sets: 4, reps: '12', rest: 60, cal: 140, icon: '🏃' },
            { name: 'Mountain Climbers', sets: 4, reps: '45 sec', rest: 30, cal: 110, icon: '🏃' },
            { name: 'High Knees', sets: 4, reps: '45 sec', rest: 30, cal: 100, icon: '🏃' },
            { name: 'Russian Twists', sets: 4, reps: '24 reps', rest: 45, cal: 50, icon: '🧘' },
            { name: 'Standard Plank Hold', sets: 3, reps: '60 sec', rest: 45, cal: 45, icon: '🧘' }
          ]
        }
      ],
      advanced: [
        {
          day: 'Day 1',
          focus: 'Sovereign Calisthenics (Push/Core)',
          exercises: [
            { name: 'Handstand Pushups (Wall)', sets: 4, reps: '6-8', rest: 90, cal: 120, icon: '🏋️' },
            { name: 'Diamond Pushups', sets: 4, reps: '20-25', rest: 60, cal: 105, icon: '💪' },
            { name: 'Archer Pushups', sets: 3, reps: '12', rest: 60, cal: 95, icon: '💪' },
            { name: 'Single-Arm Tricep Extension', sets: 3, reps: '12', rest: 45, cal: 60, icon: '⚡' },
            { name: 'Hanging Leg Raises / V-Ups', sets: 4, reps: '20', rest: 45, cal: 70, icon: '🧘' }
          ]
        },
        {
          day: 'Day 2',
          focus: 'Sovereign Calisthenics (Pull/Legs)',
          exercises: [
            { name: 'Pistol Squats (Single Leg)', sets: 4, reps: '8 per side', rest: 90, cal: 160, icon: '🦵' },
            { name: 'Strict Pullups', sets: 5, reps: '10-12', rest: 90, cal: 120, icon: '💪' },
            { name: 'Chin-ups (Close Grip)', sets: 4, reps: '12', rest: 75, cal: 100, icon: '💪' },
            { name: 'Bulgarian Split Squats (Jumping)', sets: 4, reps: '12 per side', rest: 75, cal: 140, icon: '🦵' },
            { name: 'Hamstring Slider Curls', sets: 4, reps: '15', rest: 60, cal: 90, icon: '🦵' }
          ]
        },
        {
          day: 'Day 3',
          focus: 'Hyper HIIT Conditioning',
          exercises: [
            { name: 'Burpee Broad Jumps', sets: 4, reps: '12', rest: 60, cal: 170, icon: '🏃' },
            { name: 'Plyo Pushups (Clapping)', sets: 4, reps: '12-15', rest: 60, cal: 110, icon: '💪' },
            { name: 'Tuck Jumps', sets: 4, reps: '15', rest: 45, cal: 135, icon: '🦵' },
            { name: 'L-Sit Hold', sets: 4, reps: '20 sec', rest: 45, cal: 50, icon: '🧘' },
            { name: 'Dragon Flags', sets: 4, reps: '8-10', rest: 60, cal: 80, icon: '🧘' }
          ]
        }
      ]
    }
  }

  return plans[type]?.[level] || plans['gym']['intermediate']
}

const WorkoutGenerator = () => {
  const [workoutType, setWorkoutType] = useState('gym') // gym, home
  const [level, setLevel] = useState('intermediate') // beginner, intermediate, advanced
  const [workoutPlan, setWorkoutPlan] = useState([])
  const [activeDayIdx, setActiveDayIdx] = useState(0)
  
  // Timer State
  const [timerDuration, setTimerDuration] = useState(60) // in seconds
  const [timeLeft, setTimeLeft] = useState(60)
  const [isTimerRunning, setIsTimerRunning] = useState(false)
  const [activeTimerLabel, setActiveTimerLabel] = useState('Rest Period')

  // Check-off exercises state
  const [completedExercises, setCompletedExercises] = useState({})

  useEffect(() => {
    const plan = getWorkoutPlan(workoutType, level)
    setWorkoutPlan(plan)
    setActiveDayIdx(0)
    setCompletedExercises({})
  }, [workoutType, level])

  // Timer Effect
  useEffect(() => {
    let interval = null
    if (isTimerRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((prev) => prev - 1)
      }, 1000)
    } else if (timeLeft === 0 && isTimerRunning) {
      setIsTimerRunning(false)
      // Visual/Beep notification could trigger
      if (typeof window !== 'undefined') {
        try {
          const audioCtx = new (window.AudioContext || window.webkitAudioContext)()
          const osc = audioCtx.createOscillator()
          const gain = audioCtx.createGain()
          osc.type = 'sine'
          osc.frequency.setValueAtTime(880, audioCtx.currentTime) // 880Hz A5 note
          gain.gain.setValueAtTime(0.1, audioCtx.currentTime)
          osc.connect(gain)
          gain.connect(audioCtx.destination)
          osc.start()
          osc.stop(audioCtx.currentTime + 0.3)
        } catch (e) {
          // AudioContext might be blocked or unsupported
        }
      }
    }
    return () => clearInterval(interval)
  }, [isTimerRunning, timeLeft])

  const startTimer = (seconds, label = 'Rest Period') => {
    setTimerDuration(seconds)
    setTimeLeft(seconds)
    setActiveTimerLabel(label)
    setIsTimerRunning(true)
  }

  const toggleTimer = () => {
    setIsTimerRunning(!isTimerRunning)
  }

  const resetTimer = () => {
    setIsTimerRunning(false)
    setTimeLeft(timerDuration)
  }

  const toggleExerciseCheck = (dayIdx, exIdx) => {
    const key = `${dayIdx}-${exIdx}`
    setCompletedExercises((prev) => ({
      ...prev,
      [key]: !prev[key]
    }))
  }

  // Calculate total calories of active day
  const activeDay = workoutPlan[activeDayIdx]
  const totalDayCalories = activeDay?.exercises.reduce((sum, ex) => sum + ex.cal, 0) || 0

  return (
    <section id="workout" className="py-24 px-6 relative select-none">
      <div className="absolute top-1/3 left-10 w-[500px] h-[500px] bg-electricBlue/5 rounded-full blur-[120px] pointer-events-none -z-10" />

      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> Training Protocol
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            AI Workout Engine
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Generate micro-targeted workout structures optimized for athletic output, fat burning, and muscle building.
          </p>
        </div>

        {/* Selection Row */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-6 mb-12">
          {/* Workout Environment Toggle */}
          <div className="flex bg-[#121212] p-1 rounded-full border border-white/5">
            <button
              onClick={() => setWorkoutType('gym')}
              className={`flex items-center gap-2 px-6 py-2.5 rounded-full text-xs font-semibold tracking-wider font-outfit transition-all duration-300 cursor-pointer ${
                workoutType === 'gym'
                  ? 'bg-glow-gradient text-white shadow-[0_0_10px_rgba(0,210,255,0.2)]'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <Dumbbell size={14} /> Gym Protocol
            </button>
            <button
              onClick={() => setWorkoutType('home')}
              className={`flex items-center gap-2 px-6 py-2.5 rounded-full text-xs font-semibold tracking-wider font-outfit transition-all duration-300 cursor-pointer ${
                workoutType === 'home'
                  ? 'bg-glow-gradient text-white shadow-[0_0_10px_rgba(0,210,255,0.2)]'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <Home size={14} /> Home Protocol
            </button>
          </div>

          {/* Level Selector */}
          <div className="flex bg-[#121212] p-1 rounded-full border border-white/5">
            {['beginner', 'intermediate', 'advanced'].map((lvl) => (
              <button
                key={lvl}
                onClick={() => setLevel(lvl)}
                className={`px-5 py-2.5 rounded-full text-[10px] font-bold tracking-widest font-outfit uppercase transition-all duration-300 cursor-pointer ${
                  level === lvl
                    ? 'bg-white/10 text-white border border-white/10'
                    : 'text-gray-500 hover:text-gray-300'
                }`}
              >
                {lvl}
              </button>
            ))}
          </div>
        </div>

        {/* Main Workout Panel */}
        {activeDay && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
            
            {/* Day Selector Accordion/Sidebar */}
            <div className="flex flex-col gap-4">
              <span className="text-xs font-semibold uppercase tracking-wider text-gray-500 font-outfit px-2">
                Weekly Split Schedule
              </span>
              
              {workoutPlan.map((d, index) => {
                const isActive = activeDayIdx === index
                return (
                  <button
                    key={index}
                    onClick={() => setActiveDayIdx(index)}
                    className={`text-left p-5 rounded-2xl border transition-all duration-300 cursor-pointer ${
                      isActive
                        ? 'glass-panel border-[#00D2FF]/30 card-radial-blue shadow-[0_0_20px_rgba(0,210,255,0.05)]'
                        : 'bg-[#121212]/20 border-white/5 hover:border-white/15'
                    }`}
                  >
                    <div className="flex justify-between items-center mb-1">
                      <span className={`text-xs font-bold font-outfit uppercase ${isActive ? 'text-[#00D2FF]' : 'text-gray-400'}`}>
                        {d.day}
                      </span>
                      <span className="text-[10px] bg-white/5 border border-white/10 px-2 py-0.5 rounded text-gray-500">
                        {d.exercises.length} Exercises
                      </span>
                    </div>
                    <h4 className="text-sm font-bold text-white font-outfit leading-tight mt-1">
                      {d.focus}
                    </h4>
                  </button>
                )
              })}

              {/* Integrated Rest Timer Widget (Desktop size side widget) */}
              <div className="glass-panel p-6 rounded-3xl border border-white/5 mt-4 card-radial-purple text-center">
                <div className="flex items-center gap-2 justify-center mb-4">
                  <Timer size={16} className="text-[#9D00FF]" />
                  <span className="text-xs font-semibold uppercase tracking-wider text-gray-400 font-outfit">
                    {activeTimerLabel}
                  </span>
                </div>
                
                {/* Timer Clock */}
                <div className="text-4xl font-extrabold font-outfit text-white mb-4 tracking-wider">
                  {Math.floor(timeLeft / 60)}:{(timeLeft % 60).toString().padStart(2, '0')}
                </div>

                {/* Progress bar inside widget */}
                <div className="w-full h-1 bg-[#1F1F1F] rounded-full overflow-hidden mb-5">
                  <div 
                    className="h-full bg-gradient-to-r from-blue-400 to-[#9D00FF] transition-all duration-1000"
                    style={{ width: `${(timeLeft / timerDuration) * 100}%` }}
                  />
                </div>

                {/* Timer Controls */}
                <div className="flex justify-center gap-3">
                  <button
                    onClick={toggleTimer}
                    className="p-2.5 rounded-full bg-white/5 hover:bg-white/15 text-white transition-all cursor-pointer"
                  >
                    {isTimerRunning ? <Pause size={14} /> : <Play size={14} />}
                  </button>
                  <button
                    onClick={resetTimer}
                    className="p-2.5 rounded-full bg-white/5 hover:bg-white/15 text-gray-400 hover:text-white transition-all cursor-pointer"
                  >
                    <RotateCcw size={14} />
                  </button>
                </div>
              </div>
            </div>

            {/* Exercises Grid */}
            <div className="lg:col-span-2 flex flex-col gap-5">
              <div className="flex justify-between items-center px-2">
                <div>
                  <h3 className="text-2xl font-bold font-outfit text-white">
                    {activeDay.focus}
                  </h3>
                  <p className="text-xs text-gray-400 mt-1">
                    Complete your exercises and log your rest period.
                  </p>
                </div>

                {/* Day Summary calories */}
                <div className="text-right">
                  <span className="text-[10px] text-gray-500 font-bold uppercase block tracking-wider">Est. Burn</span>
                  <span className="text-lg font-extrabold font-outfit text-[#00F0FF] flex items-center gap-1">
                    <Zap size={14} className="fill-[#00F0FF]" /> {totalDayCalories} Kcal
                  </span>
                </div>
              </div>

              {/* Exercises Stack */}
              <div className="flex flex-col gap-4">
                {activeDay.exercises.map((ex, idx) => {
                  const isChecked = completedExercises[`${activeDayIdx}-${idx}`]
                  return (
                    <div
                      key={idx}
                      onClick={() => toggleExerciseCheck(activeDayIdx, idx)}
                      className={`glass-panel p-5 rounded-2xl glow-border flex items-center justify-between gap-4 hover:translate-x-1 transition-all duration-300 cursor-pointer ${
                        isChecked 
                          ? 'border-[#00D2FF]/20 bg-emerald-950/10' 
                          : 'card-radial-blue'
                      }`}
                    >
                      <div className="flex items-center gap-4">
                        {/* Custom emoji box */}
                        <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-lg">
                          {ex.icon}
                        </div>
                        <div>
                          <h4 className={`text-sm font-bold font-outfit transition-all ${isChecked ? 'text-gray-500 line-through' : 'text-white'}`}>
                            {ex.name}
                          </h4>
                          {/* Sets, reps details */}
                          <div className="flex items-center gap-3 mt-1.5 text-xs font-semibold text-gray-400">
                            <span>{ex.sets} Sets</span>
                            <span className="w-1.5 h-1.5 rounded-full bg-white/10" />
                            <span>{ex.reps} Reps</span>
                            {ex.rest > 0 && (
                              <>
                                <span className="w-1.5 h-1.5 rounded-full bg-white/10" />
                                <button
                                  onClick={(e) => {
                                    e.stopPropagation()
                                    startTimer(ex.rest, `Rest: ${ex.name}`)
                                  }}
                                  className="flex items-center gap-1 hover:text-[#00D2FF] text-[10px] bg-white/5 px-2 py-0.5 rounded border border-white/5 transition-all"
                                >
                                  <Timer size={10} /> {ex.rest}s rest
                                </button>
                              </>
                            )}
                          </div>
                        </div>
                      </div>

                      {/* Check-off status indicator */}
                      <div className="flex items-center gap-4">
                        <span className="text-xs font-outfit text-gray-500 font-bold hidden sm:inline">
                          +{ex.cal} Kcal
                        </span>
                        <div>
                          {isChecked ? (
                            <CheckCircle2 className="text-[#00F0FF]" size={22} />
                          ) : (
                            <div className="w-5.5 h-5.5 rounded-full border border-white/20 hover:border-[#00D2FF] transition-all" />
                          )}
                        </div>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>

          </div>
        )}
      </div>
    </section>
  )
}

export default WorkoutGenerator
