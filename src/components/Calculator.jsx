import React, { useState } from 'react'
import { Sparkles, Calculator as CalcIcon } from 'lucide-react'

const Calculator = ({ onCalculate }) => {
  const [formData, setFormData] = useState({
    age: '25',
    gender: 'male',
    weight: '75',
    height: '180',
    activity: '1.55', // Moderately Active
    goal: 'maintain', // Maintain, lose, gain
  })

  const [results, setResults] = useState(null)

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const calculateMetabolism = (e) => {
    e.preventDefault()
    const age = parseFloat(formData.age)
    const weight = parseFloat(formData.weight)
    const height = parseFloat(formData.height)
    const activity = parseFloat(formData.activity)
    const gender = formData.gender
    const goal = formData.goal

    // Basic Validation
    if (!age || !weight || !height) return

    // 1. BMI Calculation
    const heightM = height / 100
    const bmi = (weight / (heightM * heightM)).toFixed(1)
    let bmiCategory = 'Healthy Weight'
    if (bmi < 18.5) bmiCategory = 'Underweight'
    else if (bmi >= 25 && bmi < 30) bmiCategory = 'Overweight'
    else if (bmi >= 30) bmiCategory = 'Obese'

    // 2. BMR (Mifflin-St Jeor)
    let bmr = 0
    if (gender === 'male') {
      bmr = 10 * weight + 6.25 * height - 5 * age + 5
    } else {
      bmr = 10 * weight + 6.25 * height - 5 * age - 161
    }

    // 3. TDEE
    const tdee = Math.round(bmr * activity)

    // 4. Target Calories based on Goal
    let targetCalories = tdee
    if (goal === 'lose') targetCalories = tdee - 500
    else if (goal === 'gain') targetCalories = tdee + 400

    // 5. Macros Split (Protein, Carbs, Fat)
    // Lose: P: 35%, C: 35%, F: 30%
    // Gain: P: 30%, C: 45%, F: 25%
    // Maintain: P: 25%, C: 45%, F: 30%
    let pPct = 0.25, cPct = 0.45, fPct = 0.30
    if (goal === 'lose') {
      pPct = 0.35; cPct = 0.35; fPct = 0.30
    } else if (goal === 'gain') {
      pPct = 0.30; cPct = 0.45; fPct = 0.25
    }

    const proteinGrams = Math.round((targetCalories * pPct) / 4)
    const carbsGrams = Math.round((targetCalories * cPct) / 4)
    const fatGrams = Math.round((targetCalories * fPct) / 9)

    const calcResults = {
      bmi,
      bmiCategory,
      targetCalories,
      protein: { pct: Math.round(pPct * 100), grams: proteinGrams },
      carbs: { pct: Math.round(cPct * 100), grams: carbsGrams },
      fat: { pct: Math.round(fPct * 100), grams: fatGrams },
    }

    setResults(calcResults)
    if (onCalculate) {
      onCalculate({
        ...formData,
        ...calcResults
      })
    }
  }

  // Pre-calculate on load if not calculated
  React.useEffect(() => {
    // Generate initial calculations on mount
    const triggerBtn = document.getElementById('calculate-btn')
    if (triggerBtn) {
      triggerBtn.click()
    }
  }, [])

  return (
    <section id="nutrition" className="py-24 px-6 relative select-none">
      <div className="absolute top-10 left-10 w-96 h-96 bg-electricBlue/5 rounded-full blur-[100px] pointer-events-none -z-10" />
      
      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> Metabolic Engine
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            Precision Caloric Analysis
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Input your biometric data to initialize our predictive metabolic model for personalized diet and workout calculations.
          </p>
        </div>

        {/* Content Box */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
          {/* Calculator Input Form */}
          <div className="glass-panel p-8 rounded-3xl glow-border flex flex-col justify-between card-radial-blue">
            <div>
              <div className="flex items-center gap-2 mb-6">
                <div className="p-2 bg-electricBlue/20 rounded-xl text-electricBlue">
                  <CalcIcon size={20} />
                </div>
                <h3 className="text-xl font-bold text-white font-outfit">Biometric Input</h3>
              </div>

              <form onSubmit={calculateMetabolism} className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Age</label>
                  <input
                    type="number"
                    name="age"
                    value={formData.age}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all"
                    placeholder="e.g. 25"
                    min="10"
                    max="100"
                    required
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Gender</label>
                  <select
                    name="gender"
                    value={formData.gender}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all appearance-none cursor-pointer"
                  >
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Weight (kg)</label>
                  <input
                    type="number"
                    name="weight"
                    value={formData.weight}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all"
                    placeholder="e.g. 70"
                    min="30"
                    max="200"
                    required
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Height (cm)</label>
                  <input
                    type="number"
                    name="height"
                    value={formData.height}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all"
                    placeholder="e.g. 175"
                    min="100"
                    max="250"
                    required
                  />
                </div>

                <div className="sm:col-span-2">
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Activity Level</label>
                  <select
                    name="activity"
                    value={formData.activity}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all appearance-none cursor-pointer"
                  >
                    <option value="1.2">Sedentary (Little to no exercise)</option>
                    <option value="1.375">Lightly Active (Light exercise 1-3 days/wk)</option>
                    <option value="1.55">Moderately Active (Moderate exercise 3-5 days/wk)</option>
                    <option value="1.725">Very Active (Hard exercise 6-7 days/wk)</option>
                    <option value="1.9">Extra Active (Very intense physical job/training)</option>
                  </select>
                </div>

                <div className="sm:col-span-2">
                  <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Target Goal</label>
                  <select
                    name="goal"
                    value={formData.goal}
                    onChange={handleInputChange}
                    className="w-full bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-sm outline-none transition-all appearance-none cursor-pointer"
                  >
                    <option value="lose">Weight Loss (Caloric Deficit)</option>
                    <option value="maintain">Maintain Weight (Caloric Balance)</option>
                    <option value="gain">Muscle Gain (Caloric Surplus)</option>
                  </select>
                </div>

                <button
                  type="submit"
                  id="calculate-btn"
                  className="sm:col-span-2 mt-4 py-4 rounded-xl bg-glow-gradient hover:shadow-[0_0_20px_rgba(0,210,255,0.3)] text-white font-semibold text-sm transition-all duration-300 transform active:scale-95 cursor-pointer"
                >
                  CALCULATE PROTOCOL
                </button>
              </form>
            </div>
          </div>

          {/* Calorie Calculator Results */}
          <div className="glass-panel p-8 rounded-3xl glow-border flex flex-col justify-center items-center card-radial-purple relative overflow-hidden">
            {results ? (
              <div className="w-full flex flex-col items-center">
                {/* BMI and Calorie row */}
                <div className="flex flex-col sm:flex-row items-center gap-10 w-full justify-around mb-8">
                  {/* Radial Progress Ring */}
                  <div className="relative w-44 h-44 flex items-center justify-center">
                    <svg className="w-full h-full transform -rotate-90">
                      {/* Inner circle track */}
                      <circle
                        cx="88"
                        cy="88"
                        r="76"
                        className="stroke-[#2D2D2D]"
                        strokeWidth="10"
                        fill="transparent"
                      />
                      {/* Glowing colored ring */}
                      <circle
                        cx="88"
                        cy="88"
                        r="76"
                        className="stroke-[url(#gradient-ring)]"
                        strokeWidth="10"
                        fill="transparent"
                        strokeDasharray={2 * Math.PI * 76}
                        strokeDashoffset={2 * Math.PI * 76 * 0.15} // just styling, offset slightly for design feel
                        strokeLinecap="round"
                      />
                      <defs>
                        <linearGradient id="gradient-ring" x1="0%" y1="0%" x2="100%" y2="100%">
                          <stop offset="0%" stopColor="#00D2FF" />
                          <stop offset="100%" stopColor="#9D00FF" />
                        </linearGradient>
                      </defs>
                    </svg>

                    <div className="absolute text-center flex flex-col items-center">
                      <span className="text-3xl font-extrabold font-outfit text-white leading-none">
                        {results.targetCalories.toLocaleString()}
                      </span>
                      <span className="text-[10px] font-semibold text-gray-400 mt-1 uppercase tracking-wider">
                        Kcal / Day
                      </span>
                    </div>
                  </div>

                  {/* Metabolic Stats */}
                  <div className="text-center sm:text-left flex flex-col gap-4">
                    <div>
                      <span className="text-xs text-gray-500 font-semibold uppercase tracking-wider block">Metabolic Rating (BMI)</span>
                      <div className="flex items-baseline gap-2 mt-1 justify-center sm:justify-start">
                        <span className="text-4xl font-extrabold font-outfit text-white">{results.bmi}</span>
                        <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-[#00F0FF]/15 text-[#00F0FF]">
                          {results.bmiCategory}
                        </span>
                      </div>
                    </div>
                    <div>
                      <span className="text-xs text-gray-500 font-semibold uppercase tracking-wider block">Recommended Goal Strategy</span>
                      <span className="text-sm font-semibold text-gray-300 mt-1 block">
                        {formData.goal === 'lose' ? '500 kcal Deficit (High Fat Burn)' : formData.goal === 'gain' ? '400 kcal Surplus (Anabolic Growth)' : 'Caloric Maintenance (Recomp)'}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Macro Progress Bars */}
                <div className="w-full flex flex-col gap-5 mt-4">
                  {/* Protein */}
                  <div>
                    <div className="flex justify-between items-center text-xs font-semibold tracking-wider mb-2">
                      <span className="text-gray-400 uppercase">Protein ({results.protein.pct}%)</span>
                      <span className="text-[#00D2FF] font-outfit font-bold">{results.protein.grams}g</span>
                    </div>
                    <div className="w-full h-2.5 bg-[#1F1F1F] rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-blue-400 to-[#00D2FF] rounded-full transition-all duration-1000"
                        style={{ width: `${results.protein.pct}%` }}
                      />
                    </div>
                  </div>

                  {/* Carbs */}
                  <div>
                    <div className="flex justify-between items-center text-xs font-semibold tracking-wider mb-2">
                      <span className="text-gray-400 uppercase">Carbohydrates ({results.carbs.pct}%)</span>
                      <span className="text-[#9D00FF] font-outfit font-bold">{results.carbs.grams}g</span>
                    </div>
                    <div className="w-full h-2.5 bg-[#1F1F1F] rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-[#9D00FF] to-pink-500 rounded-full transition-all duration-1000"
                        style={{ width: `${results.carbs.pct}%` }}
                      />
                    </div>
                  </div>

                  {/* Fat */}
                  <div>
                    <div className="flex justify-between items-center text-xs font-semibold tracking-wider mb-2">
                      <span className="text-gray-400 uppercase">Fats ({results.fat.pct}%)</span>
                      <span className="text-yellow-400 font-outfit font-bold">{results.fat.grams}g</span>
                    </div>
                    <div className="w-full h-2.5 bg-[#1F1F1F] rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-yellow-500 to-amber-300 rounded-full transition-all duration-1000"
                        style={{ width: `${results.fat.pct}%` }}
                      />
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center text-gray-500 p-8 flex flex-col items-center">
                <CalcIcon size={48} className="text-gray-600 mb-4 animate-bounce" />
                <p>Initializing metabolic diagnostics...</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  )
}

export default Calculator
