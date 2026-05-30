import React, { useState, useEffect } from 'react'
import { Sparkles, Utensils, Apple, Flame, ChevronRight, Droplet } from 'lucide-react'

// Localized diet database that responds dynamically to targetCalories
const getDietPlan = (type, calories) => {
  const calFactor = calories / 2000 // scale food portions according to calories

  const diets = {
    vegetarian: {
      name: 'Futuristic Vegetarian',
      desc: 'Plant-based micro-nutrient rich protocol focusing on high fiber and balanced clean proteins.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Chia Seed Oatmeal with Almond Milk & Berries',
          cal: Math.round(380 * calFactor),
          protein: Math.round(14 * calFactor),
          carbs: Math.round(52 * calFactor),
          fat: Math.round(12 * calFactor),
          desc: 'Organic steel-cut oats, organic chia seeds, wild berries, unsweetened almond milk.'
        },
        {
          type: 'Lunch',
          name: 'Quinoa Buddha Bowl with Roasted Chickpeas',
          cal: Math.round(580 * calFactor),
          protein: Math.round(22 * calFactor),
          carbs: Math.round(78 * calFactor),
          fat: Math.round(18 * calFactor),
          desc: 'Red quinoa, roasted spiced chickpeas, raw spinach, avocado, tahini-lemon drizzle.'
        },
        {
          type: 'Dinner',
          name: 'Tofu Broccoli Stir-fry with Brown Rice',
          cal: Math.round(620 * calFactor),
          protein: Math.round(26 * calFactor),
          carbs: Math.round(82 * calFactor),
          fat: Math.round(20 * calFactor),
          desc: 'Seared firm tofu, organic broccoli, snap peas, sesame-ginger glaze, wild brown rice.'
        },
        {
          type: 'Snacks',
          name: 'Greek Yogurt with Walnuts & Honey',
          cal: Math.round(320 * calFactor),
          protein: Math.round(18 * calFactor),
          carbs: Math.round(24 * calFactor),
          fat: Math.round(15 * calFactor),
          desc: 'Non-fat plain Greek yogurt, raw English walnuts, a dash of organic raw honey.'
        }
      ],
      water: '3.5 Liters'
    },
    vegan: {
      name: 'Clean Vegan Protocol',
      desc: 'Zero animal-product diet packed with antioxidants, legumes, and natural plant fuels.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Spiced Tofu Scramble with Whole Wheat Toast',
          cal: Math.round(360 * calFactor),
          protein: Math.round(24 * calFactor),
          carbs: Math.round(38 * calFactor),
          fat: Math.round(12 * calFactor),
          desc: 'Crumbled tofu sauteed with turmeric, nutritional yeast, baby spinach, on Ezekiel toast.'
        },
        {
          type: 'Lunch',
          name: 'Lentil Vegetable Soup with Roasted Sweet Potatoes',
          cal: Math.round(550 * calFactor),
          protein: Math.round(22 * calFactor),
          carbs: Math.round(85 * calFactor),
          fat: Math.round(10 * calFactor),
          desc: 'Brown lentils, carrots, celery, fresh herbs, served with baked sweet potato cubes.'
        },
        {
          type: 'Dinner',
          name: 'Black Bean & Tempeh Tacos with Avocado Cream',
          cal: Math.round(640 * calFactor),
          protein: Math.round(30 * calFactor),
          carbs: Math.round(68 * calFactor),
          fat: Math.round(24 * calFactor),
          desc: 'Tempeh crumbles, organic black beans, fresh cilantro, salsa, homemade cashew-avocado cream.'
        },
        {
          type: 'Snacks',
          name: 'Mixed Seeds & Dried Goji Berries',
          cal: Math.round(280 * calFactor),
          protein: Math.round(10 * calFactor),
          carbs: Math.round(25 * calFactor),
          fat: Math.round(16 * calFactor),
          desc: 'Raw pumpkin seeds, sunflower seeds, organic dried goji berries.'
        }
      ],
      water: '3.8 Liters'
    },
    highprotein: {
      name: 'Hyper-Anabolic Muscle Build',
      desc: 'Protein-first diet engineered to optimize muscle tissue synthesis and speed up post-workout recovery.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Egg White Scramble with Lean Turkey Bacon & Avocado',
          cal: Math.round(420 * calFactor),
          protein: Math.round(38 * calFactor),
          carbs: Math.round(12 * calFactor),
          fat: Math.round(22 * calFactor),
          desc: '5 egg whites, 1 whole egg, 2 strips of lean turkey bacon, half avocado.'
        },
        {
          type: 'Lunch',
          name: 'Grilled Herb Chicken Breast with Sweet Potato & Asparagus',
          cal: Math.round(600 * calFactor),
          protein: Math.round(52 * calFactor),
          carbs: Math.round(48 * calFactor),
          fat: Math.round(14 * calFactor),
          desc: 'Free-range chicken breast grilled with rosemary, baked sweet potato, steamed asparagus spears.'
        },
        {
          type: 'Dinner',
          name: 'Seared Wild Salmon Fillet with Quinoa & Zucchini',
          cal: Math.round(680 * calFactor),
          protein: Math.round(48 * calFactor),
          carbs: Math.round(35 * calFactor),
          fat: Math.round(28 * calFactor),
          desc: 'Pan-seared Atlantic salmon in olive oil, organic tri-color quinoa, sauteed zucchini.'
        },
        {
          type: 'Snacks',
          name: 'Whey Isolate Shake with Almond Butter & Banana',
          cal: Math.round(350 * calFactor),
          protein: Math.round(32 * calFactor),
          carbs: Math.round(28 * calFactor),
          fat: Math.round(12 * calFactor),
          desc: '1 scoop grass-fed whey isolate protein, organic almond butter, half organic banana.'
        }
      ],
      water: '4.2 Liters'
    },
    keto: {
      name: 'Keto-Kinetics Burning Engine',
      desc: 'Ultra-low carb, high fat diet designed to induce ketosis and utilize fat deposits as prime fuel.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Smoked Salmon & Cream Cheese Omelette',
          cal: Math.round(460 * calFactor),
          protein: Math.round(28 * calFactor),
          carbs: Math.round(4 * calFactor),
          fat: Math.round(38 * calFactor),
          desc: '3 organic eggs, wild-caught smoked salmon, high-fat organic cream cheese, fresh dill.'
        },
        {
          type: 'Lunch',
          name: 'Avocado & Bacon Keto Bowl with Spinach',
          cal: Math.round(620 * calFactor),
          protein: Math.round(24 * calFactor),
          carbs: Math.round(7 * calFactor),
          fat: Math.round(56 * calFactor),
          desc: 'Crispy thick-cut bacon, full organic avocado, baby spinach, extra virgin olive oil vinaigrette.'
        },
        {
          type: 'Dinner',
          name: 'Ribeye Steak with Garlic Herb Grass-fed Butter',
          cal: Math.round(750 * calFactor),
          protein: Math.round(48 * calFactor),
          carbs: Math.round(2 * calFactor),
          fat: Math.round(62 * calFactor),
          desc: 'Grass-fed ribeye steak seared cast-iron style, topped with homemade garlic butter, roasted asparagus.'
        },
        {
          type: 'Snacks',
          name: 'Macadamia Nuts & Celery with Cream Cheese',
          cal: Math.round(300 * calFactor),
          protein: Math.round(6 * calFactor),
          carbs: Math.round(4 * calFactor),
          fat: Math.round(30 * calFactor),
          desc: 'Raw macadamia nuts, organic celery sticks with high-fat organic cream cheese.'
        }
      ],
      water: '4.0 Liters'
    },
    indian: {
      name: 'Precision Indian Macro Protocol',
      desc: 'Traditional flavors balanced with lean paneer, lentils, curd, and high-quality local grains.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Paneer Bhurji with Multi-Grain Roti & Curd',
          cal: Math.round(410 * calFactor),
          protein: Math.round(20 * calFactor),
          carbs: Math.round(42 * calFactor),
          fat: Math.round(18 * calFactor),
          desc: '150g fresh low-fat paneer cooked with onions, tomatoes, and Indian spices, 1 multi-grain roti, bowl of curd.'
        },
        {
          type: 'Lunch',
          name: 'Yellow Dal Tadka, Grilled Chicken/Tofu, and Basmati Rice',
          cal: Math.round(590 * calFactor),
          protein: Math.round(38 * calFactor),
          carbs: Math.round(72 * calFactor),
          fat: Math.round(15 * calFactor),
          desc: 'Moong & Masoor dal, 150g grilled chicken breast (or seared tofu), basmati rice, mixed vegetable salad.'
        },
        {
          type: 'Dinner',
          name: 'Soya Chunk Curry with Brown Rice & Cucumber Raita',
          cal: Math.round(520 * calFactor),
          protein: Math.round(32 * calFactor),
          carbs: Math.round(68 * calFactor),
          fat: Math.round(12 * calFactor),
          desc: 'High-protein soya chunks cooked in light home curry, wild brown rice, cooling cucumber yogurt raita.'
        },
        {
          type: 'Snacks',
          name: 'Roasted Chana (Chickpeas) & Double Toned Milk',
          cal: Math.round(260 * calFactor),
          protein: Math.round(16 * calFactor),
          carbs: Math.round(30 * calFactor),
          fat: Math.round(6 * calFactor),
          desc: '1 cup dry roasted chickpeas, 1 glass of hot double-toned skimmed milk.'
        }
      ],
      water: '3.6 Liters'
    },
    budget: {
      name: 'Sovereign Budget Clean Protocol',
      desc: 'Optimized calorie sourcing focusing on highly affordable, clean, whole food nutrient dense essentials.',
      meals: [
        {
          type: 'Breakfast',
          name: 'Whole Eggs Scramble with Banana & Peanut Butter Toast',
          cal: Math.round(430 * calFactor),
          protein: Math.round(22 * calFactor),
          carbs: Math.round(45 * calFactor),
          fat: Math.round(18 * calFactor),
          desc: '3 whole eggs, 1 banana, 1 slice of brown bread spread with 1 tbsp peanut butter.'
        },
        {
          type: 'Lunch',
          name: 'White Chickpea Curry (Chole) with Steamed White Rice',
          cal: Math.round(560 * calFactor),
          protein: Math.round(18 * calFactor),
          carbs: Math.round(85 * calFactor),
          fat: Math.round(12 * calFactor),
          desc: 'Chickpeas boiled and simmered in budget tomato gravy, served with white basmati rice, raw onions.'
        },
        {
          type: 'Dinner',
          name: 'Egg Curry with Brown Rice & Cabbage Salad',
          cal: Math.round(510 * calFactor),
          protein: Math.round(24 * calFactor),
          carbs: Math.round(65 * calFactor),
          fat: Math.round(16 * calFactor),
          desc: '3 boiled eggs cooked in curry sauce, wild brown rice, shredded green cabbage salad.'
        },
        {
          type: 'Snacks',
          name: 'Roasted Peanuts & Bananas',
          cal: Math.round(300 * calFactor),
          protein: Math.round(10 * calFactor),
          carbs: Math.round(36 * calFactor),
          fat: Math.round(14 * calFactor),
          desc: 'Handful of roasted salted peanuts, 1 fresh banana.'
        }
      ],
      water: '3.5 Liters'
    }
  }

  return diets[type] || diets['vegetarian']
}

const DietPlanner = ({ userProfile }) => {
  const targetCalories = userProfile?.targetCalories || 2000
  const [selectedDiet, setSelectedDiet] = useState('vegetarian')
  const [dietPlan, setDietPlan] = useState(null)

  useEffect(() => {
    setDietPlan(getDietPlan(selectedDiet, targetCalories))
  }, [selectedDiet, targetCalories])

  const dietOptions = [
    { id: 'vegetarian', name: 'Vegetarian' },
    { id: 'vegan', name: 'Vegan' },
    { id: 'highprotein', name: 'High Protein' },
    { id: 'keto', name: 'Keto Diet' },
    { id: 'indian', name: 'Indian Diet' },
    { id: 'budget', name: 'Budget Diet' }
  ]

  return (
    <section className="py-24 px-6 relative select-none">
      <div className="absolute bottom-20 right-10 w-[450px] h-[450px] bg-neonPurple/5 rounded-full blur-[120px] pointer-events-none -z-10" />
      
      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#9D00FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> Nutrition Protocol
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            AI Diet Optimization
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Generate custom culinary protocols tailored for your metabolic engine. Change diets to re-calculate macros.
          </p>
        </div>

        {/* Tab Selection */}
        <div className="flex flex-wrap justify-center gap-3 mb-12">
          {dietOptions.map((opt) => (
            <button
              key={opt.id}
              onClick={() => setSelectedDiet(opt.id)}
              className={`px-5 py-2.5 rounded-full text-xs font-semibold tracking-wider font-outfit transition-all duration-300 border cursor-pointer ${
                selectedDiet === opt.id
                  ? 'bg-glow-gradient text-white border-transparent shadow-[0_0_15px_rgba(0,210,255,0.25)]'
                  : 'bg-[#121212]/40 text-gray-400 border-white/5 hover:border-white/20 hover:text-white'
              }`}
            >
              {opt.name}
            </button>
          ))}
        </div>

        {/* Diet Plan Body */}
        {dietPlan && (
          <div className="flex flex-col gap-8">
            {/* Meta Row */}
            <div className="glass-panel p-6 rounded-3xl glow-border flex flex-col md:flex-row items-center justify-between gap-6 card-radial-purple">
              <div>
                <h3 className="text-xl font-bold font-outfit text-white flex items-center gap-2">
                  <Utensils size={18} className="text-[#9D00FF]" /> {dietPlan.name}
                </h3>
                <p className="text-xs text-gray-400 mt-1 max-w-xl">{dietPlan.desc}</p>
              </div>

              {/* Targets Summary */}
              <div className="flex items-center gap-6 divide-x divide-white/10">
                <div className="text-center">
                  <span className="text-[10px] text-gray-500 font-semibold block uppercase">Calorie Target</span>
                  <span className="text-lg font-bold font-outfit text-white flex items-center gap-1 justify-center mt-1">
                    <Flame size={14} className="text-[#00F0FF]" /> {targetCalories.toLocaleString()}
                  </span>
                </div>
                <div className="text-center pl-6">
                  <span className="text-[10px] text-gray-500 font-semibold block uppercase">Hydration Limit</span>
                  <span className="text-lg font-bold font-outfit text-[#00D2FF] flex items-center gap-1 justify-center mt-1">
                    <Droplet size={14} className="fill-[#00D2FF]" /> {dietPlan.water}
                  </span>
                </div>
              </div>
            </div>

            {/* Meal Cards Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
              {dietPlan.meals.map((meal, index) => (
                <div
                  key={index}
                  className="glass-panel p-6 rounded-3xl glow-border flex flex-col justify-between hover:translate-y-[-5px] transition-transform duration-300 card-radial-blue group cursor-pointer"
                >
                  <div>
                    {/* Header */}
                    <div className="flex justify-between items-center mb-4">
                      <span className="text-[10px] font-bold tracking-widest text-[#00F0FF] uppercase font-outfit">
                        {meal.type}
                      </span>
                      <Apple size={16} className="text-gray-500 group-hover:text-white transition-colors" />
                    </div>

                    {/* Meal Name */}
                    <h4 className="text-sm font-bold font-outfit text-white mb-2 leading-snug line-clamp-2">
                      {meal.name}
                    </h4>

                    {/* Description */}
                    <p className="text-xs text-gray-400 mb-4 line-clamp-3 leading-relaxed">
                      {meal.desc}
                    </p>
                  </div>

                  {/* Macros and Calories details */}
                  <div className="border-t border-white/5 pt-4">
                    <div className="flex justify-between items-center mb-3">
                      <span className="text-xs text-gray-500">Calories</span>
                      <span className="text-sm font-bold font-outfit text-white">{meal.cal} kcal</span>
                    </div>
                    {/* Macro pill summary */}
                    <div className="grid grid-cols-3 gap-1 bg-[#161616] p-1.5 rounded-xl text-center text-[10px] font-semibold">
                      <div>
                        <span className="text-[#00D2FF] block">{meal.protein}g</span>
                        <span className="text-[8px] text-gray-500 font-bold block uppercase">PRO</span>
                      </div>
                      <div>
                        <span className="text-[#9D00FF] block">{meal.carbs}g</span>
                        <span className="text-[8px] text-gray-500 font-bold block uppercase">CAR</span>
                      </div>
                      <div>
                        <span className="text-yellow-400 block">{meal.fat}g</span>
                        <span className="text-[8px] text-gray-500 font-bold block uppercase">FAT</span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  )
}

export default DietPlanner
