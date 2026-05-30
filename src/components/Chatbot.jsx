import React, { useState, useRef, useEffect } from 'react'
import { 
  Sparkles, Send, User, Bot, Dumbbell, Apple, Trophy, RefreshCw, 
  Volume2, VolumeX, Award, Activity, Heart, ShieldAlert, Zap, Mic,
  TrendingUp
} from 'lucide-react'

// Word-by-word typewriter effect component
const TypewriterText = ({ text, onComplete, scrollRef, isAlreadyTyped }) => {
  const [displayedText, setDisplayedText] = useState('');
  
  useEffect(() => {
    if (isAlreadyTyped) {
      setDisplayedText(text);
      if (onComplete) onComplete();
      return;
    }
    
    const words = text.split(' ');
    let currentIdx = 0;
    let tempText = '';
    
    const interval = setInterval(() => {
      if (currentIdx >= words.length) {
        clearInterval(interval);
        if (onComplete) onComplete();
        return;
      }
      tempText += (currentIdx === 0 ? '' : ' ') + words[currentIdx];
      setDisplayedText(tempText);
      currentIdx++;
      
      // Auto-scroll-to-bottom on every word tick (localized to container)
      if (scrollRef && scrollRef.current) {
        scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
      }
    }, 25); // ~25ms per word
    
    return () => clearInterval(interval);
  }, [text, isAlreadyTyped]);
  
  return <span className="whitespace-pre-line font-medium font-sans">{displayedText}</span>;
};

// Interactive soundwave visualization component
const Soundwave = ({ isSpeaking, isTyping }) => {
  if (isSpeaking) {
    return (
      <div className="flex items-end gap-0.5 h-4 px-1.5">
        <div className="w-[2px] h-2 bg-[#00F0FF] rounded-full animate-bounce [animation-duration:0.6s]" />
        <div className="w-[2px] h-3.5 bg-[#9D00FF] rounded-full animate-bounce [animation-duration:0.4s] [animation-delay:0.1s]" />
        <div className="w-[2px] h-4 bg-[#00F0FF] rounded-full animate-bounce [animation-duration:0.5s] [animation-delay:0.2s]" />
        <div className="w-[2px] h-2.5 bg-[#9D00FF] rounded-full animate-bounce [animation-duration:0.7s] [animation-delay:0.05s]" />
        <div className="w-[2px] h-1 bg-[#00F0FF] rounded-full animate-bounce [animation-duration:0.3s] [animation-delay:0.15s]" />
      </div>
    );
  } else if (isTyping) {
    return (
      <div className="flex items-end gap-0.5 h-4 px-1.5">
        <div className="w-[2px] h-1.5 bg-[#00F0FF]/60 rounded-full animate-pulse [animation-duration:0.2s]" />
        <div className="w-[2px] h-2 bg-[#9D00FF]/60 rounded-full animate-pulse [animation-duration:0.15s] [animation-delay:0.05s]" />
        <div className="w-[2px] h-1.5 bg-[#00F0FF]/60 rounded-full animate-pulse [animation-duration:0.25s] [animation-delay:0.1s]" />
        <div className="w-[2px] h-2 bg-[#9D00FF]/60 rounded-full animate-pulse [animation-duration:0.18s] [animation-delay:0.02s]" />
        <div className="w-[2px] h-1 bg-[#00F0FF]/40 rounded-full animate-pulse [animation-duration:0.3s]" />
      </div>
    );
  } else {
    return (
      <div className="flex items-end gap-0.5 h-4 px-1.5 opacity-30">
        <div className="w-[2px] h-1 bg-gray-500 rounded-full" />
        <div className="w-[2px] h-1 bg-gray-500 rounded-full" />
        <div className="w-[2px] h-1 bg-gray-500 rounded-full" />
        <div className="w-[2px] h-1 bg-gray-500 rounded-full" />
        <div className="w-[2px] h-1 bg-gray-500 rounded-full" />
      </div>
    );
  }
};

// Biometric formulas
const calculateBiometrics = (profile) => {
  const w = parseFloat(profile.weight);
  const h = parseFloat(profile.height);
  const a = parseInt(profile.age);
  
  if (isNaN(w) || isNaN(h) || isNaN(a)) return null;

  // Mifflin-St Jeor Formula
  let bmr = 0;
  if (profile.gender.toLowerCase().includes('female')) {
    bmr = 10 * w + 6.25 * h - 5 * a - 161;
  } else {
    bmr = 10 * w + 6.25 * h - 5 * a + 5;
  }

  // Activity multiplier based on weekly workout schedule
  let multiplier = 1.2; // Sedentary baseline
  if (profile.schedule.includes('3')) multiplier = 1.375; // Lightly active
  else if (profile.schedule.includes('4') || profile.schedule.includes('5')) multiplier = 1.55; // Moderately active
  else if (profile.schedule.includes('6')) multiplier = 1.725; // Very active

  const tdee = Math.round(bmr * multiplier);

  // Calorie adjustments based on goals
  let targetCalories = tdee;
  if (profile.goal.includes('Fat Loss') || profile.goal.includes('Weight') || profile.goal.includes('Shred')) {
    targetCalories = Math.max(1200, tdee - 500); // 500 kcal deficit
  } else if (profile.goal.includes('Muscle') || profile.goal.includes('Size')) {
    targetCalories = tdee + 300; // 300 kcal surplus
  } else if (profile.goal.includes('Recomposition') || profile.goal.includes('Build') || profile.goal.includes('Recomp')) {
    targetCalories = tdee - 150; // Recomp slight deficit
  } else if (profile.goal.includes('Strength') || profile.goal.includes('Force')) {
    targetCalories = tdee + 150; // Strength lean surplus
  }

  // Protein targets (g/kg of bodyweight)
  let proteinMultiplier = 1.6;
  if (profile.goal.includes('Muscle') || profile.goal.includes('Strength') || profile.goal.includes('Size')) {
    proteinMultiplier = 2.0;
  } else if (profile.goal.includes('Fat Loss') || profile.goal.includes('Shred')) {
    proteinMultiplier = 2.2; // Higher protein to spare lean contractile mass
  } else if (profile.goal.includes('Performance') || profile.goal.includes('Speed') || profile.goal.includes('Athletic') || profile.goal.includes('Fitness')) {
    proteinMultiplier = 1.8;
  }
  const targetProtein = Math.round(w * proteinMultiplier);
  const targetCarbs = Math.round((targetCalories * 0.40) / 4);
  const targetFats = Math.round((targetCalories * 0.30) / 9);

  return {
    bmr: Math.round(bmr),
    tdee,
    targetCalories,
    targetProtein,
    targetCarbs,
    targetFats,
    weight: w,
    height: h,
    age: a,
    gender: profile.gender,
    multiplier,
    proteinMultiplier,
    offset: targetCalories - tdee
  };
}

// Onboarding steps definition
const onboardingFlow = [
  {
    key: 'start',
    question: "Welcome to your digital physical diagnostic, champion. I am Coach Nova, your precision fitness intelligence. Before we construct your physical training split and dietary macros, we need to analyze your biometrics and goals. Ready to begin your transformation?",
    options: ["Let's Begin", "Skip Setup", "More Info"]
  },
  {
    key: 'goal',
    question: "Step 1: What is your primary physical objective? Select one of the parameters below:",
    options: ["Fat Loss", "Muscle Gain", "Recomp", "Strength", "Fitness", "Athletic"]
  },
  {
    key: 'level',
    question: "Step 2: How many years of serious, consistent training experience do you have? This dictates your volume thresholds and progressive overload splits.",
    options: ["Beginner", "Intermediate", "Advanced"]
  },
  {
    key: 'location',
    question: "Step 3: Where will you be performing your training blocks? This determines our exercise selection (gym equipment vs bodyweight and bands).",
    options: ["Gym", "Home"]
  },
  {
    key: 'diet',
    question: "Step 4: Precision nutrition is 70% of the battle. Select your nutritional preference or diet style:",
    options: ["High Protein", "Vegetarian", "Vegan", "Keto", "Indian Diet", "Balanced"]
  },
  {
    key: 'injuries',
    question: "Step 5: Do you have any active injuries, joint issues, or physical limitations that we need to train around?",
    options: ["None", "Back Pain", "Knee Issues", "Shoulder Issues"]
  },
  {
    key: 'schedule',
    question: "Step 6: How many days per week can you dedicate to intense physical execution?",
    options: ["3 Days", "4 Days", "5 Days", "6 Days"]
  },
  {
    key: 'gender',
    question: "Step 7: Let's log your gender to accurately calculate your Basal Metabolic Rate (BMR):",
    options: ["Male", "Female"]
  },
  {
    key: 'age',
    question: "Step 8: What is your age? (Please type your age as a number, e.g. 25)",
    inputType: "number",
    placeholder: "Type your age in years (e.g. 25)..."
  },
  {
    key: 'weight',
    question: "Step 9: What is your current weight in kilograms? (Please type weight in kg, e.g. 78)",
    inputType: "number",
    placeholder: "Type your weight in kg (e.g. 78)..."
  },
  {
    key: 'height',
    question: "Step 10: What is your height in centimeters? (Please type height in cm, e.g. 175)",
    inputType: "number",
    placeholder: "Type your height in cm (e.g. 175)..."
  }
];

// Compile final custom coaching layout
const compileBlueprint = (profile) => {
  const { goal, level, location, diet, injuries, schedule, gender, age, weight, height } = profile;
  const calcs = calculateBiometrics(profile);
  
  if (!calcs) return "Biometric analysis failed. Please verify your weight and height values.";

  let dietAdvice = "";
  if (diet.includes("High Protein")) {
    dietAdvice = `Prioritize lean animal proteins (chicken breast, egg whites, lean beef, fish) alongside complex carbohydrates (sweet potatoes, oats, brown rice) and healthy fats. Focus on meeting your protein goal of ${calcs.targetProtein}g daily to maximize muscle protein synthesis and optimize recovery.`;
  } else if (diet.includes("Vegetarian")) {
    dietAdvice = `Incorporate dense vegetarian protein sources like low-fat paneer, Greek yogurt, tempeh, organic tofu, lentils, and double scoop whey isolate. Keep fat intake moderate to accommodate carbohydrate targets and hit your target of ${calcs.targetProtein}g.`;
  } else if (diet.includes("Vegan")) {
    dietAdvice = `Rely on clean plant proteins: tempeh, organic tofu, seitan, lentils, edamame, and pea/rice protein blends. Supplement with Vitamin B12 and Omega-3 (algae-based) to cover gaps and hit your target of ${calcs.targetProtein}g.`;
  } else if (diet.includes("Keto")) {
    dietAdvice = `Focus on healthy fats (avocados, extra virgin olive oil, nuts, grass-fed butter) and moderate protein. Keep total net carbohydrates strictly under 25-30g daily to induce and maintain metabolic ketosis, while keeping protein at ${calcs.targetProtein}g.`;
  } else if (diet.includes("Indian")) {
    dietAdvice = `Focus on a balanced Indian macro profile. Incorporate paneer bhurji, soya chunks, daal with curd, and sprouts, alongside a high-quality whey isolate. Replace refined carbs (maida) with fiber-rich carbs (oats, brown rice, whole wheat roti) to hit ${calcs.targetProtein}g protein without spilling over on fats.`;
  } else {
    dietAdvice = `Follow a balanced 40% carb, 30% protein, 30% fat macro split. Prioritize whole foods, fiber (30g+ daily), and micronutrient-dense leafy greens. Ensure you consume ${calcs.targetProtein}g protein.`;
  }

  let mealTiming = "";
  if (goal.includes("Muscle") || goal.includes("Strength") || goal.includes("Size")) {
    mealTiming = "Distribute protein intake evenly across 4-5 meals (30-40g each) every 3-4 hours. Consume a fast-digesting carb + protein source 90 minutes pre-workout, and a recovery meal within 60 minutes post-workout.";
  } else {
    mealTiming = "Aim for 3 main meals and 1 high-protein snack. Utilize a 12-to-14-hour overnight fasting window to improve insulin sensitivity and accelerate metabolic flexibility.";
  }

  let workoutPlan = "";
  if (location.includes("Gym")) {
    if (level.includes("Beginner")) {
      workoutPlan = "3-Day Full Body Compound Routine. Focus on mastering the big 3 compound lifts:\n- Day 1: Barbell Squats (3x8), Bench Press (3x8), Lat Pulldowns (3x10)\n- Day 2: Romanian Deadlifts (3x10), Overhead Dumbbell Press (3x8), Seated Rows (3x10)\n- Day 3: Goblet Squats (3x10), Incline Dumbbell Press (3x10), Facepulls (3x15)";
    } else if (level.includes("Intermediate")) {
      workoutPlan = "4-Day Upper/Lower Strength-Hypertrophy Split:\n- Mon (Upper A): Bench Press (4x6), Barbell Rows (4x8), DB Incline Press (3x10), Lat Pulldown (3x10)\n- Tue (Lower A): Back Squats (4x6), Romanian Deadlifts (3x8), Leg Press (3x12), Calf Raises (4x15)\n- Thu (Upper B): Overhead Press (4x6), Pull-ups (4xMax), Incline DB Flyes (3x12), Bicep/Tricep superset (3x12)\n- Fri (Lower B): Deadlifts (1x5 / 3x5 pull), Bulgarian Split Squats (3x10/leg), Leg Curls (3x12), Abs (3x15)";
    } else {
      workoutPlan = "5-Day Push/Pull/Legs (PPL) + Upper/Lower Hypertrophy Split:\n- Day 1 (Push): Incline Barbell Press (4x6-8), Flat DB Press (3x8-10), Lateral Raises (4x12), Overhead Tricep Extensions (3x10)\n- Day 2 (Pull): Conventional Deadlifts or Rack Pulls (3x5), Weighted Pull-ups (3x6-8), Chest-Supported Rows (3x10), Hammer Curls (3x12)\n- Day 3 (Legs): Barbell Back Squats (4x6-8), Romanian Deadlifts (4x8-10), Bulgarian Split Squats (3x10/leg), Seated Calf Raises (4x15)\n- Day 4 (Upper): Incline DB Press (3x8-10), Cable Rows (3x10), Lateral Raises (4x15), Incline Bicep Curls (3x12)\n- Day 5 (Lower): Leg Press (4x10-12), Lying Leg Curls (3x12), Leg Extensions (3x15), Standing Calf Raises (4x20)";
    }
  } else {
    if (level.includes("Beginner")) {
      workoutPlan = "3-Day Full Body Bodyweight Circuit. 3 rounds of:\n- Bodyweight Squats (15 reps)\n- Incline Pushups (using couch or table, 10-12 reps)\n- Doorframe Rows or Towel Pulls (12 reps)\n- Glute Bridges (15 reps)\n- Plank Hold (30-45 seconds)\n- 60s Rest between rounds.";
    } else if (level.includes("Intermediate")) {
      workoutPlan = "4-Day Home Resistance Split:\n- Day 1/3 (Upper): Pushups (4x15), Incline Pushups (3x12), Backpack Rows (fill pack with books, 4x12), Resistance Band Facepulls (3x15), Diamond Pushups (3x10)\n- Day 2/4 (Lower): Bulgarian Split Squats (4x12/leg), Walking Lunges (3x20 steps), Glute Bridges (3x15), Single-Leg Calf Raises (4x15/leg), Plank Walks (3x45s)";
    } else {
      workoutPlan = "5-Day Advanced Calisthenics Split:\n- Day 1 (Push): Decline Pushups (4x20), Archer Pushups (3x10/side), Handstand Pushups (against wall, 3x6-8), Dips (on chairs, 3x12)\n- Day 2 (Pull): Pull-ups (if bar available, 4x8-10) or Single-Arm Backpack Rows (4x12), Doorframe Pulls (3x15), Inverted Rows (3x10), Towel Hammer Curls (3x15)\n- Day 3 (Legs): Pistol Squats (3x6/leg), Weighted Bulgarian Split Squats (Backpack, 4x10/leg), Jump Squats (3x15), Single-Leg Romanian Deadlifts (3x12/leg)\n- Day 4 (Core/HIIT): Burpees (4x45s), Plank (3x60s), Russian Twists (3x30/side), Mountain Climbers (3x45s)\n- Day 5 (Upper Pump): Pushup to failure (3 sets), Incline Pushup to failure (3 sets), Bodyweight Rows to failure (3 sets), Band Lateral Raises (4x20)";
    }
  }

  let injuryNotes = "";
  if (injuries.toLowerCase().includes("knee")) {
    injuryNotes = "KNEE SENSITIVITY FLAGGED. Avoid heavy patellar shear stress. Swap deep weighted squats for Box Squats (sitting back completely) or Glute Bridges. Limit leg extensions and focus on hip-hinge movements (Romanian Deadlifts, Glute Bridges) to load the posterior chain and protect the patella.";
  } else if (injuries.toLowerCase().includes("back")) {
    injuryNotes = "LUMBAR SPINE DISCOMFORT FLAGGED. Zero axial loading. Swap conventional deadlifts and barbell back squats for Chest-Supported Dumbbell Rows, Goblet Squats (keeping torso upright), and split squats. Keep your core braced using Valsalva maneuver at all times.";
  } else if (injuries.toLowerCase().includes("shoulder")) {
    injuryNotes = "SHOULDER IMPINGEMENT FLAGGED. Avoid overhead presses and wide-grip barbell bench press. Perform Neutral-Grip Dumbbell Press (palms facing in), Floor Press (limits shoulder extension), and focus heavily on rear delts/rotator cuffs (facepulls, band pull-aparts) to stabilize the shoulder joint.";
  } else {
    injuryNotes = "No joint restrictions flagged. Maintain clean lifting form, ensure full range of motion, and track progression safely.";
  }

  return `**DIAGNOSTIC COMPLETE. CONFIGURING SYSTEM ARCHITECTURE...**

*Welcome to the Fit Nova Elite tier, champion. I have calibrated your bio-telemetry. Here is your battle-tested, custom-calibrated physiological blueprint. Let's make every single rep count.*

**1. METABOLIC BASES**
* **Basal Metabolic Rate (BMR):** ${calcs.bmr} kcal
* **Total Daily Energy Expenditure (TDEE):** ${calcs.tdee} kcal
* **Target Daily Intake:** **${calcs.targetCalories} kcal** (adapted for ${goal})
* **Daily Protein Target:** **${calcs.targetProtein}g** (essential for muscle retention & repair)
* **Macronutrient Split:** ${calcs.targetCarbs}g Carbs | ${calcs.targetProtein}g Protein | ${calcs.targetFats}g Fats

**2. NUTRITIONAL STRATEGY (${diet})**
* ${dietAdvice}
* **Meal Timing:** ${mealTiming}

**3. TRAINING SYSTEM (${location} - ${level})**
* **Split Structure:** ${schedule}
* **Core Exercises:**
${workoutPlan}
* **Injury Adaptation:** ${injuryNotes}

**4. RECOVERY PROTOCOL**
* **Sleep Target:** 7.5 to 8.5 hours of deep sleep (vital for CNS and muscular recovery)
* **Water Target:** 3.5L to 4.5L daily (crucial for intracellular hydration and transport)
* **Mobility focus:** 10 mins dynamic lower/upper mobility pre-workout, 5 mins static stretching post-workout.

*Let's execute this program with absolute discipline. Ask me any follow-up questions about this protocol (e.g., 'What should my first meal be?', 'What exercises can I do at home?', 'How do I progress?').*`;
};

// Adaptive bot response lookup for normal conversation after onboarding
const getAdaptiveBotResponse = (query, profile) => {
  const q = query.toLowerCase().trim();
  const goal = profile.goal || "Fitness Optimization";
  const level = profile.level || "Intermediate";
  const location = profile.location || "Gym";
  const diet = profile.diet || "Balanced";
  const injuries = profile.injuries || "None";
  const schedule = profile.schedule || "4 Days/Week";
  const age = profile.age || "25";
  const weight = profile.weight || "75";
  const height = profile.height || "175";
  const calcs = profile.calculations || { targetCalories: 2200, targetProtein: 140, targetCarbs: 220, targetFats: 73, bmr: 1650, tdee: 2450 };

  // 1. Specific Biometric Queries
  if (q.includes('my weight') || q.includes('how heavy') || q.includes('weigh')) {
    return {
      text: `Your active weight coordinate is logged at **${weight} kg**.\n\nTo optimize your metabolic rate, keep your protein intake high at **${calcs.targetProtein}g** daily. Let's make sure this mass is high-quality muscle, champion.`,
      category: 'biometrics'
    };
  }
  if (q.includes('my height') || q.includes('how tall') || q.includes('tall am i')) {
    return {
      text: `Your vertical stature is registered at **${height} cm**.\n\nI use this stature coordinate along with your weight (**${weight} kg**) to calculate your active BMI and exact daily BMR values. Let's make sure your frame is structured and upright!`,
      category: 'biometrics'
    };
  }
  if (q.includes('my age') || q.includes('how old')) {
    return {
      text: `Your age is registered at **${age} years**.\n\nAs we mature, keeping a high level of lean skeletal muscle is the single best predictor of joint longevity and hormonal health. I have factored this directly into your training volume limits!`,
      category: 'biometrics'
    };
  }
  if (q.includes('my goal') || q.includes('what is my target goal')) {
    return {
      text: `Your primary physical objective is active as **${goal}** under the **${location}** protocol.\n\nTo achieve this, we are targeting **${calcs.targetCalories} kcal/day** and executing a progressive split of **${schedule}**. Let's stay disciplined.`,
      category: 'biometrics'
    };
  }
  if (q.includes('bmr')) {
    return {
      text: `Your calculated **Basal Metabolic Rate (BMR)** is **${calcs.bmr} kcal/day**.\n\nThis is the baseline energy your body burns strictly to keep your organs functioning at complete rest. Any walking, chores, or lifting will burn calories *above* this baseline.`,
      category: 'biometrics'
    };
  }
  if (q.includes('tdee') || q.includes('daily burn')) {
    return {
      text: `Your **Total Daily Energy Expenditure (TDEE)** is **${calcs.tdee} kcal/day**.\n\nThis is your maintenance energy, factoring in your BMR and physical activity. To support your **${goal}** objective, I adjusted this value to establish your active intake target of **${calcs.targetCalories} kcal/day**.`,
      category: 'biometrics'
    };
  }
  if (q.includes('calories') || q.includes('intake') || q.includes('kcal') || q.includes('target cal') || q.includes('deficit') || q.includes('surplus')) {
    const modeStr = calcs.offset < 0 ? "deficit" : calcs.offset > 0 ? "surplus" : "maintenance";
    return {
      text: `Your custom calorie intake target is **${calcs.targetCalories} kcal/day**.\n\nThis includes a calculated **${modeStr}** to maximize your **${goal}** rate while maintaining peak athletic energy. \n\nLog your daily food intake in the Fuel Console to lock this target in!`,
      category: 'diet'
    };
  }
  if (q.includes('macros') || q.includes('target protein') || q.includes('protein goal') || q.includes('carbs') || q.includes('fats') || q.includes('protein grams')) {
    return {
      text: `Here is your calculated daily macronutrient blueprint to support **${goal}**:\n\n1. **Protein:** **${calcs.targetProtein}g** (essential to repair muscle fibers and protect metabolic rate).\n2. **Carbohydrates:** **${calcs.targetCarbs}g** (your primary muscle glycogen and workout energy source).\n3. **Fats:** **${calcs.targetFats}g** (for natural hormone synthesis and joint health).\n\n*Hitting these macros with 80%+ consistency is how we guarantee results, champion.*`,
      category: 'diet'
    };
  }

  // 2. Conversational Toggles & Coach Identity
  if (q.includes('who are you') || q.includes('your name') || q.includes('about you') || q.includes('credentials') || q.includes('cscs') || q.includes('qualified')) {
    return {
      text: `I am **Coach Nova**, your precision fitness intelligence. I hold credentials from the **NSCA** as a Certified Strength and Conditioning Specialist (CSCS) and from the **ISSN** in Sports Nutrition.\n\nI combine biomechanical physics with exercise physiology to design progressive overload training programs and macro blueprints. Tell me, what physical barrier are we breaking down today?`,
      category: 'general'
    };
  }
  if (q.includes('thanks') || q.includes('thank you') || q.includes('awesome') || q.includes('perfect') || q.includes('ok') || q.includes('great') || q.includes('nice') || q.includes('cool')) {
    return {
      text: `Always lock in, champion! Gratitude is good, but consistent execution is better. \n\nWe have a progressive split scheduled for **${schedule}**. Let's keep our meals prepped, water cups filled, and show up for the next session. What else do you need?`,
      category: 'general'
    };
  }
  if (q.includes('hello') || q.includes('hi ') || q.includes('hey') || q.includes('yo ') || q.includes('coach') || q.includes('greet')) {
    return {
      text: `Let's lock in, champion. I'm here and fully dialed in. We are tracking towards **${goal}** under the **${location}** protocol. \n\nWhat biomechanical check or macro adaptation do you need right now? Give it to me straight. No negotiations, let's crush it.`,
      category: 'general'
    };
  }
  if (q.includes('bye') || q.includes('goodbye') || q.includes('see ya') || q.includes('exit')) {
    return {
      text: `Discipline never sleeps. Rest up, prepare your meals for tomorrow, and make sure to hit your target sleep hours. I'll be here in the console when you're ready to execute. Let's conquer it.`,
      category: 'general'
    };
  }

  // 3. Nutrition & Diet (specific prompts)
  if (q.includes('protein source') || q.includes('dinner') || q.includes('food') || q.includes('eat') || q.includes('diet') || q.includes('breakfast') || q.includes('lunch') || q.includes('meal') || q.includes('recipe')) {
    let dietSpecificOptions = "";
    if (diet.includes("High Protein")) {
      dietSpecificOptions = "1. **Breakfast:** Egg white omelette (5 whites, 1 whole egg) cooked in olive oil with spinach, served with 2 slices of whole-wheat toast.\n2. **Lunch:** Grilled chicken breast (180g) with quinoa (150g) and mixed steamed broccoli.\n3. **Snack:** Double scoop whey isolate with water and an apple.\n4. **Dinner:** Seared salmon (180g) or lean turkey breast with sweet potatoes (150g) and green beans.";
    } else if (diet.includes("Vegetarian")) {
      dietSpecificOptions = "1. **Breakfast:** Scrambled tofu (150g) with bell peppers and toast, or high-protein Greek yogurt with mixed berries and chia seeds.\n2. **Lunch:** Paneer stir-fry (120g low-fat paneer) with brown rice (120g) and chickpea salad.\n3. **Snack:** Single scoop whey protein shake with peanut butter and oats.\n4. **Dinner:** Soya chunks curry (80g chunks) with whole wheat roti (2) and yellow daal.";
    } else if (diet.includes("Vegan")) {
      dietSpecificOptions = "1. **Breakfast:** Tofu scramble with nutritional yeast, spinach, and avocado on sourdough.\n2. **Lunch:** Tempeh power bowl with quinoa, black beans, tahini dressing, and pumpkin seeds.\n3. **Snack:** Pea & rice protein shake with almond milk and banana.\n4. **Dinner:** Lentil and chickpea curry with brown rice and raw cucumber salad.";
    } else if (diet.includes("Keto")) {
      dietSpecificOptions = "1. **Breakfast:** 3 eggs scrambled in grass-fed butter with bacon and avocado.\n2. **Lunch:** Large green salad topped with olive oil, walnuts, and grilled salmon or chicken breast.\n3. **Snack:** Macadamia nuts or almond butter spoonfuls.\n4. **Dinner:** Ribeye steak or chicken thighs cooked in coconut oil with asparagus spears.";
    } else if (diet.includes("Indian")) {
      dietSpecificOptions = "1. **Breakfast:** Moong dal chilla with paneer stuffing, or oats cooked with skimmed milk and whey protein.\n2. **Lunch:** Grilled chicken or paneer tikka (150g) with yellow dal, cucumber salad, and brown rice.\n3. **Snack:** Roasted chana (50g) with a protein shake.\n4. **Dinner:** Soya bhurji (100g) or grilled fish with whole wheat roti (2) and a bowl of low-fat curd.";
    } else {
      dietSpecificOptions = "1. **Breakfast:** Oatmeal with whey protein, chia seeds, and sliced banana.\n2. **Lunch:** Tuna or turkey breast wrap with whole-wheat tortilla, lettuce, and light mayo.\n3. **Snack:** Greek yogurt or cottage cheese with almonds.\n4. **Dinner:** Seared white fish or chicken breast with baked potato and roasted vegetables.";
    }

    return {
      text: `Let's dial in your nutrition, champion. Since you are tracking a **${diet}** diet for **${goal}**, here is your optimized daily meal architecture:\n\n**Metabolic Targets:**\n- **Target Energy:** ${calcs.targetCalories} kcal/day\n- **Macros:** ${calcs.targetProtein}g Protein | ${calcs.targetCarbs}g Carbs | ${calcs.targetFats}g Fats\n\n**Sample Meal Split:**\n${dietSpecificOptions}\n\n*Consistency in meal prep is how we secure these results. Ensure you drink 3.5L+ of water to facilitate digestion and protein absorption.*`,
      category: 'diet'
    };
  }

  // 4. Workout & Exercise Specifics
  if (q.includes('squat') || q.includes('technique') || q.includes('form') || q.includes('exercise') || q.includes('workout') || q.includes('routine') || q.includes('split') || q.includes('train') || q.includes('lift') || q.includes('bench') || q.includes('deadlift')) {
    let injuryMod = "";
    if (injuries.toLowerCase().includes("knee")) {
      injuryMod = "\n\n*Important Safety Modification:* Since you flagged **knee sensitivity**, perform Box Squats or Glute Bridges instead of deep back squats. Avoid forward patellar travel and focus on sitting back.";
    } else if (injuries.toLowerCase().includes("back")) {
      injuryMod = "\n\n*Important Safety Modification:* Since you flagged **lower back issues**, avoid barbell back squats or conventional deadlifts. Perform Goblet Squats with a strictly vertical torso or single-leg split squats to protect your lumbar spine.";
    } else if (injuries.toLowerCase().includes("shoulder")) {
      injuryMod = "\n\n*Important Safety Modification:* Since you flagged **shoulder issues**, avoid wide-grip flat barbell bench press and overhead barbell press. Swap them for Neutral-Grip Dumbbell Press or floor presses.";
    }

    let routineExplanation = "";
    if (location.includes("Gym")) {
      routineExplanation = `Here is your target compound movement guide for training in the **Gym** as an **${level}**:\n\n1. **Compound Setup:** Focus on compound execution. For barbell exercises, set safety bars at chest height. Ensure you lock your core before every lift.\n2. **Progressive Overload:** Increase load or repetitions by 2-5% every single week. Never lift to structural failure on compound lifts; keep 1-2 reps in reserve.\n3. **Stance/Bracing:** For squats/deadlifts, breathe deep into your diaphragm (Valsalva maneuver) and push your abs out against your lifting belt to stabilize the spine.`;
    } else {
      routineExplanation = `Here is your target bodyweight mechanics guide for training at **Home** as an **${level}**:\n\n1. **Time Under Tension:** Since absolute resistance is lower at home, maximize time under tension. Perform the eccentric (lowering) phase for 3-4 seconds.\n2. **Mechanical Disadvantage:** To overload movements, progress from standard pushups to incline/decline, or use unilateral movements (e.g. single-leg split squats, pistol squats).\n3. **Consistent Output:** Focus on high muscle engagement and maintaining zero rest between alternating body sides to keep cardiovascular intensity high.`;
    }

    return {
      text: `${routineExplanation}${injuryMod}\n\n*What specific movement pattern or exercise are we troubleshooting next, champion?*`,
      category: 'workout'
    };
  }

  // 5. Training Body Parts
  if (q.includes('cardio') || q.includes('run') || q.includes('hiit') || q.includes('fat burn')) {
    return {
      text: `Cardio is a tool for systemic conditioning and calorie burn. For your **${goal}** objective:\n\n1. **HIIT (High-Intensity Interval Training):** Perform 15-20 mins (e.g. 30s sprint, 60s jog) 2x per week to preserve muscle while stripping fat.\n2. **LISS (Low-Intensity Steady State):** Fasted morning walks for 30-40 mins at 110-120 BPM heart rate is ideal for direct fatty acid mobilization.\n3. **Timing:** Always perform cardio *after* weight training or on rest days. Never exhaust glycogen stores before lifting.`,
      category: 'workout'
    };
  }
  if (q.includes('chest') || q.includes('pecs') || q.includes('pushup')) {
    return {
      text: `To construct full, thick pectoral blocks, focus on these mechanics:\n\n1. **Horizontal Pressing:** Bench press or dumbbell press at a 15-30 degree incline targets the clavicular (upper) head of the chest.\n2. **Adduction:** Dumbbell flyes or cable crossovers are crucial; the chest's mechanical function is to pull the arm *across* the body.\n3. **Scapular Retraction:** Pinch your shoulder blades down and back before pressing to protect the rotator cuff and isolate the chest.`,
      category: 'workout'
    };
  }
  if (q.includes('back') || q.includes('lats') || q.includes('pullups') || q.includes('rows')) {
    return {
      text: `A powerful back requires both width (lats) and thickness (traps/rhomboids):\n\n1. **Vertical Pulling (Width):** Lat pulldowns or pullups. Focus on pulling from your elbows, not your hands.\n2. **Horizontal Rowing (Thickness):** Barbell rows or chest-supported rows. Squeeze your scapula completely at the peak concentric contraction.\n3. **Lower Back:** Maintain a neutral spine. Core bracing is non-negotiable for rows and deadlifts.`,
      category: 'workout'
    };
  }
  if (q.includes('arms') || q.includes('bicep') || q.includes('tricep') || q.includes('hypertrophy')) {
    return {
      text: `Arm development is a science of elbow flexion and extension:\n\n1. **Triceps (60% of Arm Volume):** Target the long head with overhead extensions, and the lateral/medial heads with cable pushdowns. Keep elbows tucked.\n2. **Biceps (40% of Arm Volume):** Perform standard dumbbell curls for supination, hammer curls for brachialis/forearm thickness, and incline curls to stretch the long head.\n3. **Intensity:** Arm muscles respond extremely well to drop-sets and supersets.`,
      category: 'workout'
    };
  }

  // 6. Motivation
  if (q.includes('motivation') || q.includes('lazy') || q.includes('tired') || q.includes('inspire') || q.includes('give up') || q.includes('exhausted') || q.includes('cannot') || q.includes('skip') || q.includes('cheat')) {
    return {
      text: `Listen to me carefully: **Discipline is the only metric that matters.** Motivation is a chemical spike; it fades when the weather is cold, when you are tired, or when your day was long.\n\nYour target is **${goal}**. That body won't build itself while you negotiate with your comfort zone. Put on your shoes. Set your timer for 15 minutes and just complete the first warm-up set. Once you start, momentum takes over.\n\n*Do not negotiate with your weakness today. Show up for yourself. Let's make it happen.*`,
      category: 'motivation'
    };
  }

  // 7. Advanced Muscle Physiology & Hypertrophy Mechanics
  if (q.includes('muscle growth') || q.includes('hypertrophy') || q.includes('build muscle') || q.includes('mechanical tension') || q.includes('rpe') || q.includes('rir') || q.includes('reps in reserve') || q.includes('plateau') || q.includes('progressive overload') || q.includes('periodization')) {
    return {
      text: `Let's break down the exact biophysics of skeletal muscle hypertrophy, champion. Muscle growth is not a random occurrence; it is an adaptive response to structured biophysical load. Here are the three pillars:

1. **Mechanical Tension (The Primary Driver):** This occurs when a muscle fiber contracts under a heavy load through a full range of motion. The mechanoreceptors in your muscle cells detect this tension and trigger the **mTOR pathway**, which initiates muscle protein synthesis (MPS). Always prioritize the stretched position of an exercise (e.g., deep chest stretch in DB bench press) as tension is highest there.
2. **RPE (Rate of Perceived Exertion) & RIR (Reps in Reserve):** To trigger growth, your working sets must be within **1 to 3 RIR** (meaning you stop 1 to 3 reps before complete muscular failure). Working sets with an RPE of less than 7 do not recruit the high-threshold motor units responsible for real growth.
3. **Progressive Overload & Periodization:** You must systematically increase the total volume (Sets × Reps × Load) over time. If you lift the same weights for the same reps every week, your body has no physiological reason to build new muscle. Use a linear or block periodization structure to cycle your volume and intensity.
4. **Myo-Reps & Rest-Pause:** For advanced hypertrophy, incorporate myo-reps on lateral raises or biceps curls: perform a set to failure, rest for 10-15 seconds (5 deep breaths), and perform 3-5 mini-sets of 3 reps to keep your motor units fully recruited.`,
      category: 'workout'
    };
  }

  // 8. Sleep & Circadian Recovery Science
  if (q.includes('sleep') || q.includes('insomnia') || q.includes('circadian') || q.includes('cortisol') || q.includes('rem') || q.includes('deep sleep') || q.includes('bedtime') || q.includes('night')) {
    return {
      text: `Sleep is your absolute biological superpower for muscle building and fat loss, champion. You do not grow in the gym; the gym is where you create the micro-tears. You grow and recover strictly during deep sleep. Here is the science of recovery:

1. **Anabolic Hormone Release:** During slow-wave (deep) sleep, your pituitary gland releases the highest natural spike of **Human Growth Hormone (HGH)** and testosterone. These hormones are critical for tissue recovery, nitrogen retention, and cellular repair.
2. **Cortisol & Insulin Sensitivity:** Chronic sleep deprivation (less than 7 hours) triggers a massive spike in baseline **cortisol** (your primary catabolic stress hormone). High cortisol actively breaks down skeletal muscle tissue, decreases your BMR, increases visceral fat accumulation, and blocks thyroid activity. It also compromises your insulin sensitivity, making your body more likely to store carbohydrates as fat instead of storing them as muscle glycogen.
3. **Circadian Hygiene & REM Sleep:** To optimize sleep quality, maintain a strict circadian schedule. Sleep in a pitch-black, cool room (18-20°C). Avoid blue-spectrum light for 90 minutes before bed, as blue light suppresses **melatonin** synthesis. REM sleep is where psychological stress is metabolized and neural pathways are cleared, restoring your motor coordination and strength potential.
4. **Active Sleep Protocol:** Aim for **5 complete sleep cycles** (roughly 7.5 to 8.5 hours). Supplementing with elemental Magnesium Glycinate 30-40 minutes before bed directly calms the nervous system and increases deep sleep duration.`,
      category: 'recovery'
    };
  }

  // 9. Hydration & Electrolytes Mechanics
  if (q.includes('hydration') || q.includes('water') || q.includes('electrolyte') || q.includes('cramp') || q.includes('salt') || q.includes('sodium') || q.includes('potassium') || q.includes('dehydration')) {
    return {
      text: `Let's look at the cellular mechanics of hydration, champion. Water alone is not enough; hydration is a delicate balance of fluid and critical minerals (electrolytes) inside your muscles. Here is the physiological breakdown:

1. **The Sodium-Potassium Pump:** Your muscle cells rely on the sodium-potassium ATPase pump to generate action potentials. This electrical signal is what allows a muscle fiber to contract with high force. Even a **2% drop in cellular hydration** can cause a **10% drop in strength and peak power output**.
2. **Muscular Cell Volumization:** Water is pulled into the muscle cells via glycogen and sodium. Well-hydrated muscles appear fuller, have superior leverage, and experience increased nutrient delivery. Dehydrated muscle tissue is highly susceptible to painful cramping, micro-tears, and tendon irritation.
3. **Electrolyte Intake Strategy:** For intense lifting, especially in warm climates, drinking water without replacing electrolytes will dilute your blood stream, causing hyponatremia. Ensure you consume adequate sodium (about 2000-3000mg/day) and potassium (3500-4700mg/day from whole foods like avocados and bananas). Add a small pinch of pink Himalayan salt to your pre-workout water to dramatically increase your muscle pump.
4. **Hydration Target:** Your target is **14 cups (3.5 Liters)** daily. Track this directly in the calendar page stats panel to maintain optimal systemic cellular volume!`,
      category: 'recovery'
    };
  }

  // 10. Alcohol & Physiological Fitness Mechanics
  if (q.includes('alcohol') || q.includes('beer') || q.includes('wine') || q.includes('whiskey') || q.includes('drinking') || q.includes('party') || q.includes('hangover')) {
    return {
      text: `Let's discuss the metabolic reality of alcohol on your physical coordinates, champion. If you are serious about **${goal}**, you need to understand how alcohol acts as a direct biological disruptor:

1. **Blocks Muscle Protein Synthesis (MPS):** Alcohol directly suppresses the **mTOR (mammalian target of rapamycin) signaling pathway**, which is the master regulator of muscle building. Consuming alcohol after a workout blocks your body's ability to repair and grow damaged muscle tissue by up to **30%**, regardless of how much protein you eat.
2. **Hormonal Degradation (Testosterone & Cortisol):** Alcohol is a direct testicular toxin. It inhibits the Leydig cells in your testes, causing a significant drop in free testosterone levels for up to 36 hours. At the same time, it elevates **cortisol** (the catabolic stress hormone) and decreases growth hormone (HGH) secretion by up to 70%.
3. **Dehydration & Glycogen Depletion:** Alcohol is a powerful diuretic. It blocks the release of vasopressin (anti-diuretic hormone), forcing your kidneys to excrete water. This dehydrates your muscle cells, drains your muscle glycogen stores, and destroys your strength and aerobic performance for your next session.
4. **Metabolic Inhibition & Fat Accumulation:** Alcohol cannot be stored by your body; it must be burned immediately. When you drink, your liver prioritizes clearing the toxic acetaldehyde, completely **blocking fat oxidation (fat burning) by up to 70%** and halting gluconeogenesis. The empty calories (7 kcal/gram) are highly likely to be stored as visceral abdominal fat.
5. **Mitigation Strategy:** If you choose to drink, limit it to 1-2 standard drinks, consume a massive amount of water containing electrolytes before bed, and ensure you consume at least 30-40g of high-quality protein beforehand to help offset the muscle breakdown.`,
      category: 'diet'
    };
  }

  // 11. Gut Health, Digestion & Nutrient Absorption
  if (q.includes('digestion') || q.includes('bloat') || q.includes('gut') || q.includes('fiber') || q.includes('constipation') || q.includes('stomach') || q.includes('gas') || q.includes('absorb')) {
    return {
      text: `You are not what you eat, champion; **you are what you digest and absorb.** You can track all the macros you want, but if your gut microbiome is compromised, those nutrients will pass right through you without repairing a single muscle fiber. Here is the science of gut health:

1. **The Gut Microbiome & Inflammation:** Your colon is home to trillions of bacteria that regulate systemic inflammation, neurotransmitters (90% of your serotonin is made in the gut), and immune function. A compromised gut barrier (leaky gut) triggers systemic inflammation, which spikes cortisol and directly hinders muscle recovery.
2. **Fiber Quotas (Soluble vs Insoluble):** Aim for at least **30 to 40 grams of dietary fiber** daily. Soluble fiber (found in oats, apples, beans) forms a gel-like substance that slows digestion, improves nutrient absorption, and feeds beneficial gut bacteria (generating short-chain fatty acids like butyrate). Insoluble fiber (found in whole grains, green vegetables) provides bulk to prevent constipation.
3. **Bloating & Lactose Swaps:** Chronic bloating is a sign of food intolerances or poor enzyme activity. If you experience bloating after taking standard whey concentrate, swap it immediately for **Whey Protein Isolate** or a high-purity **Plant-based blend** (pea/rice). Reduce high-FODMAP foods if gas persists.
4. **Digestive Optimization Protocol:** 
   - Integrate prebiotic foods (garlic, onions, bananas) and probiotics (curd, kefir, kimchi).
   - Chew your food to liquid form; digestion begins in the mouth with salivary amylase.
   - Avoid drinking massive amounts of ice-cold water *during* large meals, as it dilutes your stomach acid (hydrochloric acid) and pancreatic enzymes, leading to incomplete protein breakdown.`,
      category: 'diet'
    };
  }

  // 12. Stretching, Mobility & Joint Biomechanics
  if (q.includes('stretching') || q.includes('stretch') || q.includes('mobility') || q.includes('warmup') || q.includes('warm-up') || q.includes('foam roll') || q.includes('flexibility') || q.includes('stiff') || q.includes('tight') || q.includes('warm up')) {
    return {
      text: `Mobility is the mechanical foundation of raw strength, champion. If your joints lack the range of motion to execute a movement, your body will compensate by placing stress on tendons and secondary muscles, inevitably leading to injury. Here is the science of movement prep and recovery:

1. **Dynamic Warm-Up (Pre-Workout):** Never perform static stretching *before* lifting. Static stretching temporarily desensitizes muscle spindles and reduces peak force output by up to 10%. Instead, execute an **8-10 minute dynamic warm-up** to increase core temperature, lubricate joints with synovial fluid, and activate the central nervous system:
   - **Lower Body:** Hip openers, leg swings, bodyweight deep squats, and glute bridges.
   - **Upper Body:** Arm circles, band pull-aparts, and shoulder dislocations with a resistance band.
2. **Static Stretching (Post-Workout):** The ideal window for static stretching is immediately after lifting when your tissues are warm and hyperemic. Hold passive stretches for **30-40 seconds** to lengthen muscle fibers, down-regulate your sympathetic nervous system, and trigger myofibrillar relaxation.
3. **Myofascial Release (Foam Rolling):** Foam rolling acts as autogenic inhibition. By applying targeted pressure to muscle trigger points, you stimulate the **Golgi Tendon Organs (GTO)**, which forces the hyperactive muscle fibers to release tension. Focus on your lats, thoracic spine, glutes, and IT bands for 2-3 minutes.
4. **Targeted Mobility Exercises:** 
   - **Ankle Mobility:** wall ankle drives.
   - **Thoracic Spine Mobility:** foam roller extensions.
   - **Hip Mobility:** 90/90 hip transitions.`,
      category: 'recovery'
    };
  }

  // 13. Injury & Recovery Protocol (CSCS Guidelines)
  if (q.includes('injury') || q.includes('pain') || q.includes('hurt') || q.includes('sore') || q.includes('recovery') || q.includes('rest') || q.includes('joint pain') || q.includes('knee pain') || q.includes('back pain') || q.includes('shoulder pain') || q.includes('tendonitis')) {
    let injurySpecific = "";
    if (injuries !== "None") {
      injurySpecific = `We are currently managing a **${injuries}** injury. Never push through joint or structural pain. Muscle fatigue is acceptable, joint pinching or burning is a hard stop.`;
    } else {
      injurySpecific = "Ensure you are warming up dynamically for at least 8-10 minutes (arm circles, leg swings, bodyweight hinges) before lifting weights.";
    }

    return {
      text: `Physical longevity is our top priority. Here is your injury mitigation and recovery protocol, certified under CSCS guidelines:

1. **Dynamic Preparation & Joint Lubrication:** ${injurySpecific}
2. **M.E.T.H. over R.I.C.E.:** Modern sports medicine is moving away from R.I.C.E. (Rest, Ice, Compression, Elevation) because ice constricts blood vessels and actively delays tissue healing. Instead, follow **M.E.T.H. (Movement, Elevation, Traction, Heat)**. Low-intensity, pain-free active movement increases blood flow to the damaged area, delivering essential amino acids and oxygen to rebuild tendons and myofibrils.
3. **Tendonitis & Overuse Recovery:** Tendons are poorly vascularized and take up to 10x longer to heal than muscle tissue. If you are experiencing tendonitis (patellar, bicep, or elbow), perform **isometric holds** (e.g., holding a squat or leg extension at a 45-degree angle for 30-45 seconds) which acts as a powerful local analgesic and stimulates collagen synthesis.
4. **Muscle Soreness (DOMS):** Delayed Onset Muscle Soreness is not a badge of honor; it is a sign of eccentric micro-tears and localized inflammation. Do not perform high-intensity workouts on severely sore muscles. Instead, execute light cardio or dynamic stretching to flush blood and waste products through the muscle tissue.`,
      category: 'recovery'
    };
  }

  // 14. Supplements Stack (ISSN Science-Backed Stack)
  if (q.includes('supplement') || q.includes('creatine') || q.includes('whey') || q.includes('caffeine') || q.includes('preworkout') || q.includes('beta-alanine') || q.includes('bcaa') || q.includes('glutamine') || q.includes('vitamins')) {
    return {
      text: `Supplements are the final 5% of your progress. Build the foundation first, then optimize. Here is your tier-1 science-backed stack for **${goal}**:

1. **Whey Protein Isolate:** Take 1-2 scoops daily (post-workout or between meals) to hit your daily target of **${calcs.targetProtein}g**. Isolate undergoes cross-flow microfiltration, removing lactose and fats, resulting in a 90%+ pure protein yield containing high **Leucine** content (the critical trigger for muscle protein synthesis).
2. **Creatine Monohydrate (The King of Supplements):** Take 5 grams daily (no loading phase needed, timing is less important than consistency). It saturates muscular creatine phosphate stores, directly increasing cellular ATP resynthesis during short-burst, anaerobic lifting. It also pulls water inside the muscle cells (osmotic hydration), promoting cellular volume and mechanical leverage.
3. **Caffeine (Adenosine Receptor Antagonism):** Take 150-250mg of caffeine 30-40 minutes pre-workout. Caffeine binds to your brain's adenosine receptors, blocking fatigue signals, increasing motor unit recruitment, and lowering your Rating of Perceived Exertion (RPE).
4. **Beta-Alanine (Lactic Buffer):** Take 3.2 to 4.8 grams daily. It synthesizes with histidine in your body to form **Carnosine**, which acts as an intracellular buffer to neutralize hydrogen ions (lactic acid) in your muscles, delaying fatigue in the 8-15 rep range. (Note: harmless skin tingling, called paresthesia, is normal!).
5. **Vitamin D3 & ZMA:** Take before bed. Vitamin D3 acts as a powerful steroid hormone precursor, supporting bone density and natural testosterone production. Zinc and Magnesium (ZMA) directly down-regulate central nervous system activity, promote deep sleep, and support muscle fiber repair.`,
      category: 'general'
    };
  }

  // 9. Intelligent Contextual Dynamic Fallback
  const startsWithQuestion = q.startsWith('how') || q.startsWith('what') || q.startsWith('why') || q.startsWith('when') || q.startsWith('can') || q.startsWith('should') || q.includes('?');

  const openings = [
    "Let's analyze the biomechanical physics here, champion.",
    "Excellent metabolic inquiry. Let's look at the physiological data.",
    "To optimize this for your physical frame, we need to break down the biomechanics.",
    "Always a crucial check. Let's structure the answer scientifically.",
    "Biophysical execution is key. Let's align this with your coordinates."
  ];

  const closings = [
    "No negotiations with comfort. Let's lock in and execute.",
    "Discipline is the only currency of results. Let's make it happen.",
    "Keep showing up for yourself. The physical rebuild is compounding daily.",
    "Track your metrics, prep your meals, and crush the next block.",
    "Form first, intensity second, consistency always. Let's conquer it."
  ];

  const randOpening = openings[Math.floor(Math.random() * openings.length)];
  const randClosing = closings[Math.floor(Math.random() * closings.length)];

  let fallbackText = `${randOpening}\n\nAs your coach, my directive is to guide you toward **${goal}** using our active **${location}** program.\n\n`;

  if (startsWithQuestion) {
    fallbackText = `${randOpening}\n\nTo address this specifically for your **${level}** level frame tracking towards **${goal}** in the **${location}**, we must analyze the dynamic strain vectors.\n\n1. **Macro Calibrations:** To support this metabolic load, ensure your daily energy is sustained near your **${calcs.targetCalories} kcal** target, focusing heavily on hitting **${calcs.targetProtein}g protein**.\n2. **Biomechanical Safety:** Under your **${injuries}** injury limits, always prioritize absolute form over moving excessive weight.\n3. **Systemic Hydration:** Keep your cellular hydration optimal (recommend logging **14 cups daily** as registered in your log).\n\nTell me: what specific component of your workout form or recovery scheduling shall we refine next, champion?`;
  } else {
    fallbackText += `Under your **${diet}** diet preferences and **${injuries}** limitations, we need to execute our training schedule (**${schedule}**) with absolute mechanical precision.\n\nTell me: what specific component of your workout form, daily meals, hydration, or recovery scheduling shall we optimize next?\n\n*${randClosing}*`;
  }

  return {
    text: fallbackText,
    category: 'general'
  };
};

const isGeneralQuestion = (text, options) => {
  const q = text.toLowerCase().trim();
  
  if (options && options.some(opt => opt.toLowerCase() === q || q.includes(opt.toLowerCase()) || opt.toLowerCase().includes(q))) {
    return false;
  }
  
  const questionStarters = ['what', 'how', 'why', 'can', 'could', 'is', 'are', 'should', 'do', 'does', 'explain', 'tell', 'show', 'who', 'where', 'when', 'help'];
  const fitnessKeywords = ['squat', 'bench', 'deadlift', 'protein', 'creatine', 'diet', 'workout', 'exercise', 'training', 'fat', 'muscle', 'lose', 'gain', 'sore', 'pain', 'injury', 'supplement', 'whey', 'caffeine', 'preworkout', 'motivation', 'tired', 'lazy'];
  
  const hasQuestionMark = q.includes('?');
  const startsWithQuestion = questionStarters.some(word => q.startsWith(word + ' ') || q === word);
  const containsKeyword = fitnessKeywords.some(kw => q.includes(kw));
  
  return hasQuestionMark || startsWithQuestion || containsKeyword;
};

const Chatbot = ({ mode = 'full', user = null, userProfile = null }) => {
  const hasSynchronized = useRef(false);
  const [profile, setProfile] = useState({
    goal: '',
    level: '',
    location: '',
    diet: '',
    injuries: '',
    schedule: '',
    gender: '',
    age: '',
    weight: '',
    height: '',
    calculations: null
  });

  const [onboardingStep, setOnboardingStep] = useState(0);
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: "Fit Nova Diagnostic System online. I am Coach Nova, your precision fitness intelligence. Before we construct your physical training split and dietary macros, we need to analyze your biometrics and goals. Ready to begin your transformation?",
      options: ["Let's begin!", "Skip Diagnostic & Chat", "Tell me more first"],
      time: 'Just now'
    }
  ]);
  
  const [inputText, setInputText] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [thinkingStatus, setThinkingStatus] = useState('Analyzing biometric vectors...');

  // Load synced profile from parent context once to prevent resetting chat on subsequent parent updates
  useEffect(() => {
    if (userProfile && userProfile.goal) {
      const activeGoal = userProfile.goal === 'bulk' ? 'Muscle Gain (Bulk)' : userProfile.goal === 'shred' ? 'Fat Loss (Shred)' : userProfile.goal === 'recomp' ? 'Body Recomposition' : userProfile.goal;
      const w = parseFloat(userProfile.weight || 75);
      const h = parseFloat(userProfile.height || 180);
      const a = parseFloat(userProfile.age || 25);
      const g = userProfile.gender || 'male';
      const bmrVal = Math.round(10 * w + 6.25 * h - 5 * a + (g.toLowerCase() === 'female' ? -161 : 5));
      const tdeeVal = Math.round(bmrVal * 1.45);
      const targetCals = userProfile.targetCalories || (userProfile.goal === 'shred' ? tdeeVal - 500 : userProfile.goal === 'bulk' ? tdeeVal + 300 : tdeeVal);
      
      const newCalcs = {
        targetCalories: userProfile.calculations?.targetCalories || targetCals,
        targetProtein: userProfile.calculations?.targetProtein || Math.round(w * 2.2) || 160,
        targetCarbs: userProfile.calculations?.targetCarbs || Math.round(targetCals * 0.45 / 4) || 250,
        targetFats: userProfile.calculations?.targetFats || Math.round(targetCals * 0.25 / 9) || 64,
        bmr: userProfile.calculations?.bmr || bmrVal,
        tdee: userProfile.calculations?.tdee || tdeeVal,
        multiplier: userProfile.calculations?.multiplier || 1.45,
        proteinMultiplier: userProfile.calculations?.proteinMultiplier || 2.2,
        offset: userProfile.calculations?.offset !== undefined ? userProfile.calculations.offset : (targetCals - tdeeVal),
        gender: userProfile.calculations?.gender || g,
        weight: userProfile.calculations?.weight || w,
        height: userProfile.calculations?.height || h,
        age: userProfile.calculations?.age || a
      };

      setProfile(prev => ({
        ...prev,
        goal: activeGoal,
        level: userProfile.level || prev.level || 'Intermediate',
        location: userProfile.location || prev.location || 'Gym',
        diet: userProfile.diet || prev.diet || 'Balanced',
        injuries: userProfile.injuries || prev.injuries || 'None',
        schedule: userProfile.schedule || prev.schedule || '4 Days/Week',
        gender: g,
        age: a,
        weight: w,
        height: h,
        calculations: newCalcs
      }));

      // Only perform initial message greeting synchronization once
      if (!hasSynchronized.current) {
        hasSynchronized.current = true;
        setOnboardingStep(null);
        setMessages([
          {
            id: 1,
            sender: 'bot',
            text: `Fit Nova Telemetry synchronized. Welcome back, champion! I am Coach Nova, your CSCS certified fitness mentor. I have successfully loaded your biometric profile (${a} yrs, ${w}kg, Goal: ${activeGoal}).\n\nWe are fully operational. Ask me anything about your progressive lifting volume, customized macros, or technique mechanics. Let's conquer it!`,
            options: ["Suggest a custom meal plan", "Troubleshoot squat form", "Optimize my supplements"],
            time: 'Just now',
            isAlreadyTyped: true
          }
        ]);
      }
    }
  }, [userProfile]);

  const [isSpeechEnabled, setIsSpeechEnabled] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [typedMessageIds, setTypedMessageIds] = useState([]);
  
  // Mobile responsive views
  const [showCredsModal, setShowCredsModal] = useState(false);
  const [showTelemetryModal, setShowTelemetryModal] = useState(false);

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollTop = messagesEndRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  useEffect(() => {
    // Clean up voice synthesis if page unmounts
    return () => {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  // Play UI synthesized sound effects using Web Audio API
  const playUiSound = (type) => {
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      
      const playOscillator = (freq, waveType, duration, delay = 0, gainVal = 0.05) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        osc.type = waveType;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delay);
        
        gain.gain.setValueAtTime(0, audioCtx.currentTime + delay);
        gain.gain.linearRampToValueAtTime(gainVal, audioCtx.currentTime + delay + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + delay + duration);
        
        osc.start(audioCtx.currentTime + delay);
        osc.stop(audioCtx.currentTime + delay + duration);
      };

      if (type === 'tap') {
        playOscillator(1500, 'sine', 0.04, 0, 0.02);
      } else if (type === 'option') {
        playOscillator(1600, 'sine', 0.06, 0, 0.02);
        playOscillator(2000, 'sine', 0.08, 0.03, 0.02);
      } else if (type === 'chime') {
        playOscillator(523.25, 'sine', 0.4, 0, 0.03);      // C5
        playOscillator(659.25, 'sine', 0.4, 0.05, 0.03);    // E5
        playOscillator(783.99, 'sine', 0.4, 0.10, 0.03);    // G5
        playOscillator(1046.50, 'sine', 0.5, 0.15, 0.015);  // C6 high harmony
      } else if (type === 'reset') {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(600, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(150, audioCtx.currentTime + 0.35);
        gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.35);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.35);
      }
    } catch (e) {
      // AudioContext not permitted/supported
    }
  };

  // Backwards compatible wrapper for playBeep
  const playBeep = (freq = 800, type = 'sine', duration = 0.1) => {
    if (freq === 450) {
      playUiSound('reset');
    } else if (freq === 850 || freq === 900) {
      playUiSound('chime');
    } else if (freq === 800) {
      playUiSound('option');
    } else {
      playUiSound('tap');
    }
  };

  // Speak bot response using browser TTS with speaking state hooks
  const speakText = (text) => {
    if (!isSpeechEnabled || !('speechSynthesis' in window)) {
      setIsSpeaking(false);
      return;
    }
    try {
      window.speechSynthesis.cancel();
      let clean = text.replace(/[\*\#\_]/g, ''); // strip markdown
      clean = clean.replace(/\-\s+/g, ''); // strip bullet symbols
      const utterance = new SpeechSynthesisUtterance(clean);
      const voices = window.speechSynthesis.getVoices();
      const englishVoice = voices.find(v => v.lang.startsWith('en'));
      if (englishVoice) utterance.voice = englishVoice;
      
      utterance.rate = 1.05;
      utterance.pitch = 0.95; // slightly lower pitch for confident masculine trainer profile
      
      utterance.onstart = () => setIsSpeaking(true);
      utterance.onend = () => setIsSpeaking(false);
      utterance.onerror = () => setIsSpeaking(false);
      
      window.speechSynthesis.speak(utterance);
    } catch (err) {
      console.warn("Speech synthesis error:", err);
      setIsSpeaking(false);
    }
  };

  const handleSpeechToggle = () => {
    const prev = isSpeechEnabled;
    setIsSpeechEnabled(!prev);
    if (!prev) {
      playUiSound('option');
      setTimeout(() => {
        speakText("Voice Guidance Activated. Ready to crush this transformation.");
      }, 100);
    } else {
      playUiSound('tap');
      setIsSpeaking(false);
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    }
  };

  const speakMessageManually = (text) => {
    playUiSound('tap');
    try {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        let clean = text.replace(/[\*\#\_]/g, '');
        clean = clean.replace(/\-\s+/g, '');
        const utterance = new SpeechSynthesisUtterance(clean);
        const voices = window.speechSynthesis.getVoices();
        const englishVoice = voices.find(v => v.lang.startsWith('en'));
        if (englishVoice) utterance.voice = englishVoice;
        utterance.rate = 1.05;
        utterance.pitch = 0.95;
        
        utterance.onstart = () => setIsSpeaking(true);
        utterance.onend = () => setIsSpeaking(false);
        utterance.onerror = () => setIsSpeaking(false);
        
        window.speechSynthesis.speak(utterance);
      }
    } catch (err) {
      console.warn(err);
      setIsSpeaking(false);
    }
  };

  const resetDiagnostic = () => {
    playUiSound('reset');
    setIsSpeaking(false);
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    setOnboardingStep(0);
    setTypedMessageIds([]);
    setProfile({
      goal: '',
      level: '',
      location: '',
      diet: '',
      injuries: '',
      schedule: '',
      gender: '',
      age: '',
      weight: '',
      height: '',
      calculations: null
    });
    setMessages([
      {
        id: Date.now(),
        sender: 'bot',
        text: "Fit Nova Diagnostic System reset. I am Coach Nova. Let's establish your fitness coordinates. Ready to begin?",
        options: ["Let's begin!", "Skip Diagnostic & Chat", "Tell me more first"],
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
  };

  const handleSendMessage = (textToSend) => {
    if (!textToSend.trim()) return;

    // play input beep
    playBeep(650, 'triangle', 0.1);

    const newMsg = {
      id: Date.now(),
      sender: 'user',
      text: textToSend,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, newMsg]);
    setInputText('');
    setIsTyping(true);

    // Dynamic thinking telemetry rotations
    const thinkingStates = [
      "Analyzing biometric vectors...",
      "Calibrating macro energy matrices...",
      "Correlating skeletal safety nodes...",
      "Modeling progressive load volumes...",
      "Synthesizing metabolic targets..."
    ];
    let stateIdx = 0;
    setThinkingStatus(thinkingStates[0]);
    const stateInterval = setInterval(() => {
      stateIdx = (stateIdx + 1) % thinkingStates.length;
      setThinkingStatus(thinkingStates[stateIdx]);
    }, 800);

    // Simulated human coaching delay
    setTimeout(() => {
      clearInterval(stateInterval);
      let botText = "";
      let nextStep = onboardingStep;
      let nextOptions = null;
      let updatedProfile = { ...profile };

      const lowerText = textToSend.toLowerCase();

      // Check if user requested to skip/bypass diagnostic
      if (lowerText.includes("skip") || lowerText.includes("bypass") || lowerText.includes("chat directly")) {
        const defaultProfile = {
          goal: 'Body Recomposition (Lose Fat, Build Muscle)',
          level: 'Intermediate (1-3 years training)',
          location: 'Gym (Full Barbell & Machine access)',
          diet: 'Balanced / General',
          injuries: 'None - Fully Operational',
          schedule: '4 Days / Week (Upper / Lower Split)',
          gender: 'Male',
          age: '28',
          weight: '78',
          height: '175'
        };
        const calcs = calculateBiometrics(defaultProfile);
        const bypassedProfile = { ...defaultProfile, calculations: calcs };
        
        setProfile(bypassedProfile);
        setOnboardingStep(null);

        botText = "Diagnostic bypassed, champion. I have calibrated your console with a default active biometric profile (28 yrs, 78kg, 175cm, Goal: Recomposition, 4 Days/Week Gym split). We are fully operational in direct coaching mode.\n\nAsk me anything about training splits, custom macros, technique breakdowns, or recovery strategies. Let's get to work.";
        
        const botMsg = {
          id: Date.now() + 2,
          sender: 'bot',
          text: botText,
          options: null,
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };
        setMessages((prev) => [...prev, botMsg]);
        setIsTyping(false);
        playBeep(900, 'sine', 0.08);
        speakText(botText);
        return;
      }

      if (onboardingStep !== null && onboardingStep !== undefined && onboardingStep >= 0 && onboardingStep < onboardingFlow.length) {
        const currentFlowStep = onboardingFlow[onboardingStep];
        const key = currentFlowStep.key;

        // Check if user is asking a general question during onboarding
        if (isGeneralQuestion(textToSend, currentFlowStep.options)) {
          const response = getAdaptiveBotResponse(textToSend, profile);
          botText = `${response.text}\n\n💡 *Resuming Onboarding:* Let's get your personalized profile set up to customize these recommendations.\n\n${currentFlowStep.question}`;
          nextOptions = currentFlowStep.options || null;

          const botMsg = {
            id: Date.now() + 2,
            sender: 'bot',
            text: botText,
            options: nextOptions,
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          };
          setMessages((prev) => [...prev, botMsg]);
          setIsTyping(false);
          playBeep(900, 'sine', 0.08);
          speakText(response.text); // speak only the answer
          return;
        }

        if (key === 'start') {
          if (textToSend.toLowerCase().includes("begin") || textToSend.includes("Let's") || textToSend.toLowerCase().includes("start")) {
            nextStep = 1;
          } else {
            botText = "I am a world-class certified fitness expert with years of experience in bodybuilding, fat loss, muscle gain, strength training, nutrition, and lifestyle optimization. By establishing your biometrics, I will calculate your exact daily calorie and protein requirements, and generate a customized program tailored to your goals. Shall we begin?";
            nextOptions = ["Let's Begin", "Skip Setup", "More Info"];
            
            const botMsg = {
              id: Date.now() + 1,
              sender: 'bot',
              text: botText,
              options: nextOptions,
              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            };
            setMessages((prev) => [...prev, botMsg]);
            setIsTyping(false);
            playBeep(850, 'sine', 0.08);
            speakText(botText);
            return;
          }
        } else if (key === 'age' || key === 'weight' || key === 'height') {
          const val = parseFloat(textToSend);
          if (isNaN(val) || val <= 0) {
            botText = `Invalid entry. Please enter a positive number representing your ${key === 'age' ? 'age' : key === 'weight' ? 'weight (kg)' : 'height (cm)'}:`;
            
            const botMsg = {
              id: Date.now() + 1,
              sender: 'bot',
              text: botText,
              options: null,
              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            };
            setMessages((prev) => [...prev, botMsg]);
            setIsTyping(false);
            playBeep(850, 'sine', 0.08);
            speakText(botText);
            return;
          }
          updatedProfile[key] = val;
          nextStep = onboardingStep + 1;
        } else {
          updatedProfile[key] = textToSend;
          nextStep = onboardingStep + 1;
        }

        setOnboardingStep(nextStep);
        setProfile(updatedProfile);

        if (nextStep < onboardingFlow.length) {
          const nextFlowStep = onboardingFlow[nextStep];
          botText = nextFlowStep.question;
          nextOptions = nextFlowStep.options || null;
        } else {
          setOnboardingStep(null);
          const calcs = calculateBiometrics(updatedProfile);
          updatedProfile.calculations = calcs;
          setProfile(updatedProfile);
          botText = compileBlueprint(updatedProfile);
          nextOptions = null;
        }
      } else {
        const response = getAdaptiveBotResponse(textToSend, profile);
        botText = response.text;
      }

      const botMsg = {
        id: Date.now() + 2,
        sender: 'bot',
        text: botText,
        options: nextOptions,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      
      setMessages((prev) => [...prev, botMsg]);
      setIsTyping(false);
      
      // play output beep & voice synthesis
      playBeep(900, 'sine', 0.08);
      speakText(botText);
    }, 1800); // 1.8s delay feels very real and high-end
  };

  const simulateSpeechInput = () => {
    playBeep(800, 'triangle', 0.2);
    alert("Holographic Mic Active. Speak clearly into your device.\n\n(Simulated: Speak your command now. Try typing instead if mic permissions are disabled.)");
  };

  const quickPrompts = onboardingStep === null ? [
    { text: "Suggest a custom meal plan", icon: <Apple size={12} /> },
    { text: "Troubleshoot squat form", icon: <Dumbbell size={12} /> },
    { text: "Give me intense motivation", icon: <Trophy size={12} /> },
    { text: "Optimize my supplements", icon: <Sparkles size={12} /> }
  ] : [];

  const currentStepData = onboardingStep !== null && onboardingStep >= 0 && onboardingStep < onboardingFlow.length
    ? onboardingFlow[onboardingStep]
    : null;

  const inputPlaceholder = currentStepData && currentStepData.placeholder
    ? currentStepData.placeholder
    : "Ask Coach Nova (e.g., 'What is my protein goal?' or 'Need workout tips')...";

  return (
    <section id="chatbot" className="py-24 px-6 relative select-none">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-electricBlue/5 rounded-full blur-[130px] pointer-events-none -z-10" />

      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-widest text-[#00F0FF] uppercase flex items-center justify-center gap-1.5 mb-3 font-outfit">
            <Sparkles size={12} /> Core Intelligence Node
          </span>
          <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
            Fit Nova Elite AI Coach
          </h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
            Consult Coach Nova, your CSCS certified AI Strength & Transformation mentor, for hyper-personalized macros and structural workout adaptation.
          </p>
        </div>

        {/* 3-Column Luxury Workspace Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch h-[680px] max-w-6xl mx-auto">
                  {/* Column 1: Coach Profile info (3 cols) */}
          <div className="hidden lg:flex lg:col-span-3 h-full min-h-0 flex-col justify-start gap-4 glass-panel p-5 rounded-3xl glow-border card-radial-purple border-white/5 relative overflow-hidden">
            {/* hologram scanline overlay */}
            <div className="absolute inset-0 bg-gradient-to-b from-transparent via-[#00F0FF]/5 to-transparent h-[200%] w-full pointer-events-none animate-hologram-scan" />
            
            <div className="z-10 text-center">
              <span className="text-[8px] text-[#00F0FF] font-bold uppercase tracking-widest border border-[#00F0FF]/30 px-2 py-0.5 rounded bg-[#00F0FF]/5 font-outfit inline-block mb-3">
                AI INTEL NODE
              </span>
              
              {/* Holographic Interactive Avatar Sphere */}
              <div className="relative w-24 h-24 mx-auto mb-4 flex items-center justify-center">
                {/* Orbital Rotating Rings */}
                <div className="absolute inset-0 border border-dashed border-[#9D00FF]/30 rounded-full animate-orbital-spin" />
                <div className="absolute inset-1.5 border border-dashed border-[#00D2FF]/40 rounded-full animate-orbital-spin-reverse" />
                
                {/* Breathing Core Globe */}
                <div className="w-20 h-20 rounded-full bg-black/60 flex items-center justify-center relative overflow-hidden border border-[#00D2FF]/40 shadow-[0_0_15px_rgba(0,210,255,0.15)]">
                  {/* Internal scan beam */}
                  <div className="absolute top-0 left-0 w-full h-1 bg-[#00F0FF]/30 blur-xs animate-hologram-scan" />
                  {/* Eye-Shifting Core */}
                  <div className="w-6 h-6 rounded-lg bg-gradient-to-tr from-[#9D00FF] to-[#00D2FF] rotate-45 flex items-center justify-center animate-eye-shift shadow-[0_0_15px_rgba(0,240,255,0.6)]">
                    <div className="w-1.5 h-1.5 bg-white rounded-full animate-pulse shadow-[0_0_5px_#fff]" />
                  </div>
                  {/* Matrix mesh background */}
                  <div className="absolute inset-0 opacity-10 bg-[linear-gradient(rgba(255,255,255,0.1)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.1)_1px,transparent_1px)] bg-[size:10px_10px]" />
                </div>
                {/* Floor glow base */}
                <div className="absolute -bottom-1 w-24 h-2.5 bg-[#00D2FF]/20 rounded-full blur-xs" />
              </div>

              {/* Credentials & Bio */}
              <div className="text-center">
                <h4 className="text-sm font-bold font-outfit text-white">Coach Nova</h4>
                <p className="text-[9px] text-gray-500 font-semibold tracking-wide mt-0.5">CSCS Strength & Hypertrophy Coach</p>
                
                {/* Badge Badges */}
                <div className="flex justify-center gap-1.5 mt-2.5">
                  <div className="text-[8px] font-bold tracking-wider px-1.5 py-0.5 rounded bg-[#00F0FF]/10 border border-[#00F0FF]/20 text-[#00F0FF]">
                    NSCA-CSCS
                  </div>
                  <div className="text-[8px] font-bold tracking-wider px-1.5 py-0.5 rounded bg-[#9D00FF]/10 border border-[#9D00FF]/20 text-[#9D00FF]">
                    ISSN-SNS
                  </div>
                </div>

                <div className="h-px bg-white/5 my-3" />
                
                {/* Compact Specs Grid */}
                <div className="grid grid-cols-2 gap-2 text-left text-[10px] font-semibold text-gray-400 font-mono">
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                    <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Experience</span>
                    <span className="text-white font-bold font-outfit">12+ Years</span>
                  </div>
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                    <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Protocol</span>
                    <span className="text-[#00F0FF] font-bold font-outfit">Hypertrophy</span>
                  </div>
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl col-span-2 flex justify-between items-center">
                    <div>
                      <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Success Rate</span>
                      <span className="text-white font-bold font-outfit">99.4% Goal Met</span>
                    </div>
                    <TrendingUp className="text-emerald-500 w-3.5 h-3.5 mr-1 shrink-0" />
                  </div>
                </div>
              </div>
            </div>

            {/* Compact Status Beacon */}
            <div className="z-10 mt-auto">
              <div className="bg-gradient-to-br from-black/40 to-black/20 border border-white/5 p-3 rounded-xl flex items-center justify-between">
                <span className="text-[8px] text-gray-500 font-bold uppercase tracking-widest font-mono">STATUS</span>
                <div className="flex items-center gap-1.5">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                  <span className="text-[9px] font-bold text-gray-300 font-outfit uppercase tracking-wide">
                    {isSpeaking ? 'Speaking' : isTyping ? 'Thinking' : 'Online'}
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Column 2: Active Chat Interface (6 cols) */}
          <div className="col-span-1 lg:col-span-6 flex flex-col justify-between glass-panel rounded-3xl glow-border card-radial-blue border-white/5 shadow-2xl relative">
            
            {/* Chat header */}
            <div className="p-4 border-b border-white/5 flex items-center justify-between bg-black/30">
              <div className="flex items-center gap-3">
                {/* Miniature animated avatar circle */}
                <div className="w-10 h-10 rounded-full bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] p-0.5 flex items-center justify-center relative overflow-hidden shrink-0">
                  <div className="w-full h-full rounded-full bg-[#0B0B0B] flex items-center justify-center">
                    <Bot size={18} className="text-[#00F0FF] animate-pulse" />
                  </div>
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white font-outfit flex items-center gap-1.5">
                    Coach Nova <span className="w-1.5 h-1.5 rounded-full bg-[#00F0FF] animate-ping" />
                  </h4>
                  <div className="flex items-center gap-2 mt-0.5">
                    <span className="text-[10px] text-gray-500 font-semibold uppercase tracking-wider block">CSCS Advisor Active</span>
                    <Soundwave isSpeaking={isSpeaking} isTyping={isTyping} />
                  </div>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex items-center gap-2">
                {/* Voice mode toggle */}
                <button
                  onClick={handleSpeechToggle}
                  className={`p-2 rounded-full border transition-all cursor-pointer flex items-center justify-center ${
                    isSpeechEnabled 
                      ? 'bg-[#00F0FF]/15 border-[#00F0FF]/40 text-[#00F0FF] shadow-[0_0_10px_rgba(0,240,255,0.2)]' 
                      : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'
                  }`}
                  title={isSpeechEnabled ? "Speech guidance on" : "Speech guidance muted"}
                >
                  {isSpeechEnabled ? <Volume2 size={13} /> : <VolumeX size={13} />}
                </button>

                {/* Mobile view action buttons */}
                <button
                  onClick={() => setShowCredsModal(true)}
                  className="lg:hidden p-2 rounded-full bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center"
                  title="View Coach Credentials"
                >
                  <Award size={13} />
                </button>

                <button
                  onClick={() => setShowTelemetryModal(true)}
                  className="lg:hidden p-2 rounded-full bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center"
                  title="View Profile Telemetry"
                >
                  <Activity size={13} />
                </button>

                {/* Reset button */}
                {profile.calculations && (
                  <button
                    onClick={resetDiagnostic}
                    className="flex items-center gap-1 text-[9px] font-bold text-[#00F0FF] hover:text-white bg-[#00F0FF]/10 hover:bg-[#00F0FF]/20 border border-[#00F0FF]/30 px-3 py-1.5 rounded-full transition-all cursor-pointer font-outfit"
                  >
                    <RefreshCw size={9} /> Recalibrate
                  </button>
                )}
              </div>
            </div>

            {/* Chat message space */}
            <div ref={messagesEndRef} className="flex-1 overflow-y-auto p-6 flex flex-col gap-4">
              {messages.map((msg) => {
                const isBot = msg.sender === 'bot';
                return (
                  <div key={msg.id} className={`flex flex-col gap-1.5 max-w-[85%] animate-bubble-appear ${isBot ? 'self-start' : 'self-end items-end'}`}>
                    <div className={`flex gap-2.5 ${isBot ? '' : 'flex-row-reverse'}`}>
                      {/* Avatar icon */}
                      <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 border border-white/5 ${isBot ? 'bg-[#9D00FF]/15 text-[#9D00FF]' : 'bg-white/5 text-[#00D2FF]'}`}>
                        {isBot ? <Bot size={13} /> : <User size={13} />}
                      </div>

                      {/* Chat Bubble */}
                      <div className={`p-4 rounded-2xl text-xs leading-relaxed relative ${
                        isBot 
                          ? 'bg-[#121212]/80 border border-white/5 text-gray-200 hover:border-[#00D2FF]/20 transition-all' 
                          : 'bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white shadow-[0_0_15px_rgba(0,210,255,0.12)]'
                      }`}>
                        <div className="whitespace-pre-line font-medium font-sans">
                          {isBot ? (
                            <TypewriterText 
                              text={msg.text} 
                              scrollRef={messagesEndRef}
                              isAlreadyTyped={typedMessageIds.includes(msg.id)}
                              onComplete={() => {
                                if (!typedMessageIds.includes(msg.id)) {
                                  setTypedMessageIds(prev => [...prev, msg.id]);
                                }
                              }}
                            />
                          ) : (
                            msg.text
                          )}
                        </div>
                        
                        <div className="flex items-center justify-between gap-4 mt-2">
                          {/* Speak button for this individual bubble */}
                          {isBot ? (
                            <button
                              onClick={() => speakMessageManually(msg.text)}
                              className="text-gray-500 hover:text-[#00F0FF] p-0.5 rounded cursor-pointer transition-colors"
                              title="Listen to this block"
                            >
                              <Volume2 size={10} />
                            </button>
                          ) : <div />}
                          <span className={`text-[8px] font-semibold block text-right ${isBot ? 'text-gray-500' : 'text-white/60'}`}>
                            {msg.time}
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* Quick Select Options inside chat timeline */}
                    {isBot && msg.options && onboardingStep !== null && messages[messages.length - 1].id === msg.id && (
                      <div className="flex flex-wrap gap-2 mt-1.5 ml-10">
                        {msg.options.map((opt, i) => (
                          <button
                            key={i}
                            onClick={() => handleSendMessage(opt)}
                            className="glass-panel text-[10px] sm:text-xs font-semibold text-gray-300 hover:text-white border border-white/5 hover:border-[#00D2FF]/40 hover:bg-[#00D2FF]/10 px-2.5 py-1.5 sm:px-4 sm:py-2.5 rounded-xl transition-all cursor-pointer shadow-sm hover:shadow-[0_0_10px_rgba(0,210,255,0.1)]"
                          >
                            {opt}
                          </button>
                        ))}
                      </div>
                    )}
                  </div>
                );
              })}

              {/* Thinking/Analyzing state */}
              {isTyping && (
                <div className="flex gap-3 self-start max-w-[85%] animate-pulse">
                  <div className="w-8 h-8 rounded-full bg-[#9D00FF]/15 text-[#9D00FF] flex items-center justify-center border border-white/5">
                    <Bot size={13} />
                  </div>
                  <div className="p-4 rounded-2xl bg-[#121212]/80 border border-white/5 flex flex-col gap-1.5">
                    <span className="text-[9px] text-[#00F0FF] font-bold uppercase tracking-widest font-outfit animate-pulse">
                      {thinkingStatus}
                    </span>
                    <div className="flex items-center gap-1.5">
                      <span className="w-1.5 h-1.5 bg-[#00F0FF] rounded-full animate-bounce" />
                      <span className="w-1.5 h-1.5 bg-[#00F0FF] rounded-full animate-bounce [animation-delay:0.2s]" />
                      <span className="w-1.5 h-1.5 bg-[#00F0FF] rounded-full animate-bounce [animation-delay:0.4s]" />
                    </div>
                  </div>
                </div>
              )}
              <div />
            </div>

            {/* Quick Prompts list */}
            {quickPrompts.length > 0 && (
              <div className="px-6 py-2 flex flex-wrap gap-2 border-t border-white/5 bg-black/15">
                {quickPrompts.map((p, index) => (
                  <button
                    key={index}
                    onClick={() => handleSendMessage(p.text)}
                    className="flex items-center gap-1.5 text-[10px] font-semibold text-gray-400 hover:text-white bg-white/5 border border-white/5 hover:border-[#00D2FF]/30 hover:bg-white/10 px-3 py-1.5 rounded-full transition-all cursor-pointer"
                  >
                    {p.icon} {p.text}
                  </button>
                ))}
              </div>
            )}

            {/* Form Input controls */}
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSendMessage(inputText);
              }}
              className="p-2.5 sm:p-4 border-t border-white/5 flex gap-2 sm:gap-3 bg-black/30"
            >
              {/* Mic audio stimulation */}
              <button
                type="button"
                onClick={simulateSpeechInput}
                className="p-2 sm:p-3 rounded-lg sm:rounded-xl bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-colors cursor-pointer"
                title="Voice Input"
              >
                <Mic className="w-3.5 h-3.5 sm:w-[15px] sm:h-[15px]" />
              </button>

              <input
                type={currentStepData && currentStepData.inputType === 'number' ? 'number' : 'text'}
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder={inputPlaceholder}
                className="flex-1 bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-lg sm:rounded-xl px-2.5 py-2 sm:px-4 sm:py-3 text-white text-[11px] sm:text-xs outline-none transition-all font-medium font-sans"
              />
              
              <button
                type="submit"
                className="p-2 sm:p-3 rounded-lg sm:rounded-xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white shadow-[0_0_10px_rgba(0,210,255,0.2)] hover:shadow-[0_0_15px_rgba(0,210,255,0.45)] transition-all cursor-pointer flex items-center justify-center shrink-0"
              >
                <Send className="w-3.5 h-3.5 sm:w-[15px] sm:h-[15px]" />
              </button>
            </form>
          </div>

          {/* Column 3: Telemetry Profile monitor (3 cols) */}
          <div className="hidden lg:flex lg:col-span-3 h-full min-h-0 flex-col justify-start gap-4 glass-panel p-5 rounded-3xl glow-border card-radial-purple border-white/5 relative overflow-hidden">
            <div className="absolute inset-0 bg-gradient-to-b from-transparent via-[#9D00FF]/5 to-transparent h-[200%] w-full pointer-events-none animate-hologram-scan" />
            
            <div className="z-10">
              <span className="text-[8px] text-[#9D00FF] font-bold uppercase tracking-widest border border-[#9D00FF]/30 px-2 py-0.5 rounded bg-[#9D00FF]/5 font-outfit inline-block mb-3">
                METABOLICS
              </span>
              
              <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit mb-2 flex items-center gap-1">
                <Activity className="text-[#00F0FF] w-3.5 h-3.5 shrink-0" /> Vitals Telemetry
              </h4>
              
              <div className="grid grid-cols-2 gap-2">
                {[
                  { label: 'Active Goal', value: profile.goal === 'bulk' ? 'Muscle Gain' : profile.goal === 'shred' ? 'Fat Loss' : profile.goal === 'recomp' ? 'Body Recomp' : (profile.goal || 'PENDING') },
                  { label: 'Diet Matrix', value: profile.diet || 'PENDING' },
                  { label: 'Stature Height', value: profile.height ? `${profile.height} cm` : 'PENDING' },
                  { label: 'Active Weight', value: profile.weight ? `${profile.weight} kg` : 'PENDING' }
                ].map((item, idx) => (
                  <div key={idx} className="bg-white/[0.01] border border-white/5 p-2 rounded-xl flex flex-col justify-between min-h-[42px] hover:border-[#00F0FF]/20 transition-all duration-300 font-mono">
                    <span className="text-[7px] text-gray-500 font-bold uppercase tracking-wider">{item.label}</span>
                    <span className={`text-[9px] font-bold font-outfit mt-0.5 truncate ${item.value === 'PENDING' ? 'text-amber-500/60 animate-pulse' : 'text-[#00F0FF]'}`}>
                      {item.value}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-gradient-to-br from-black/40 to-[#121215]/20 border border-white/5 p-3 rounded-2xl z-10 mt-auto">
              <span className="text-[8px] text-gray-500 font-bold uppercase tracking-widest font-mono block mb-2">METABOLIC PROFILE</span>
              {profile.calculations ? (
                <div className="flex flex-col gap-2.5 text-[9px] font-mono leading-normal text-gray-300">
                  
                  {/* Compact Rows */}
                  <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                    <span className="text-gray-500">Basal Metabolic (BMR)</span>
                    <span className="text-white font-bold font-outfit text-[10px]">{profile.calculations.bmr} kcal</span>
                  </div>

                  <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                    <span className="text-gray-500">Total Expenditure (TDEE)</span>
                    <span className="text-white font-bold font-outfit text-[10px]">{profile.calculations.tdee} kcal</span>
                  </div>

                  <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                    <span className="text-gray-500">Calorie Target</span>
                    <span className="text-[#00F0FF] font-bold font-outfit text-[10px]">{profile.calculations.targetCalories} kcal</span>
                  </div>

                  {/* Tiny Macros Row */}
                  <div className="flex items-center justify-between mt-1">
                    <span className="text-gray-500">Macros</span>
                    <div className="flex gap-1.5">
                      <span className="bg-[#9D00FF]/15 border border-[#9D00FF]/30 px-1.5 py-0.5 rounded text-[8px] text-[#9D00FF] font-bold">P: {profile.calculations.targetProtein}g</span>
                      <span className="bg-white/5 border border-white/10 px-1.5 py-0.5 rounded text-[8px] text-white font-bold">C: {profile.calculations.targetCarbs}g</span>
                      <span className="bg-white/5 border border-white/10 px-1.5 py-0.5 rounded text-[8px] text-white font-bold">F: {profile.calculations.targetFats}g</span>
                    </div>
                  </div>

                </div>
              ) : (
                <span className="text-[9px] text-gray-500 font-bold block italic text-center py-2 font-mono">
                  Awaiting telemetry vectors...
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Mobile Modal for Coach Credentials */}
        {showCredsModal && (
          <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4">
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 max-w-sm w-full relative">
              <button 
                onClick={() => { playBeep && playBeep(1000, 'sine', 0.05); setShowCredsModal(false); }}
                className="absolute top-4 right-4 text-gray-400 hover:text-white font-bold animate-pulse"
              >
                ✕
              </button>
              <div className="text-center">
                <span className="text-[8px] text-[#00F0FF] font-bold uppercase tracking-widest border border-[#00F0FF]/30 px-2 py-0.5 rounded bg-[#00F0FF]/5 font-outfit inline-block mb-3">
                  AI INTEL NODE
                </span>
                
                <h4 className="text-sm font-bold font-outfit text-white">Coach Nova</h4>
                <p className="text-[9px] text-gray-500 font-semibold tracking-wide mt-0.5">CSCS Strength & Hypertrophy Coach</p>
                
                <div className="flex justify-center gap-1.5 mt-2.5">
                  <div className="text-[8px] font-bold tracking-wider px-1.5 py-0.5 rounded bg-[#00F0FF]/10 border border-[#00F0FF]/20 text-[#00F0FF]">
                    NSCA-CSCS
                  </div>
                  <div className="text-[8px] font-bold tracking-wider px-1.5 py-0.5 rounded bg-[#9D00FF]/10 border border-[#9D00FF]/20 text-[#9D00FF]">
                    ISSN-SNS
                  </div>
                </div>

                <div className="h-px bg-white/5 my-4" />
                
                {/* Compact Specs Grid */}
                <div className="grid grid-cols-2 gap-2 text-left text-[10px] font-semibold text-gray-400 font-mono">
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                    <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Experience</span>
                    <span className="text-white font-bold font-outfit">12+ Years</span>
                  </div>
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl">
                    <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Protocol</span>
                    <span className="text-[#00F0FF] font-bold font-outfit">Hypertrophy</span>
                  </div>
                  <div className="bg-white/[0.01] border border-white/5 p-2 rounded-xl col-span-2 flex justify-between items-center">
                    <div>
                      <span className="text-[7px] text-gray-500 font-bold block uppercase tracking-wider">Success Rate</span>
                      <span className="text-white font-bold font-outfit">99.4% Goal Met</span>
                    </div>
                    <TrendingUp className="text-emerald-500 w-3.5 h-3.5 mr-1 shrink-0" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Mobile Modal for Telemetry Dashboard */}
        {showTelemetryModal && (
          <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4">
            <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 max-w-sm w-full max-h-[90vh] overflow-y-auto relative">
              <button 
                onClick={() => { playBeep && playBeep(1000, 'sine', 0.05); setShowTelemetryModal(false); }}
                className="absolute top-4 right-4 text-gray-400 hover:text-white font-bold animate-pulse"
              >
                ✕
              </button>
              <span className="text-[9px] text-[#9D00FF] font-bold uppercase tracking-widest border border-[#9D00FF]/30 px-2 py-0.5 rounded bg-[#9D00FF]/5 font-outfit inline-block mb-4">
                TELEMETRY CONSOLE
              </span>
              <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit mb-3 flex items-center gap-1.5">
                <Activity className="text-[#00F0FF] w-3.5 h-3.5 shrink-0" /> Vitals Telemetry
              </h4>
              
              <div className="grid grid-cols-2 gap-2 mb-4">
                {[
                  { label: 'Active Goal', value: profile.goal === 'bulk' ? 'Muscle Gain' : profile.goal === 'shred' ? 'Fat Loss' : profile.goal === 'recomp' ? 'Body Recomp' : (profile.goal || 'PENDING') },
                  { label: 'Diet Matrix', value: profile.diet || 'PENDING' },
                  { label: 'Stature Height', value: profile.height ? `${profile.height} cm` : 'PENDING' },
                  { label: 'Active Weight', value: profile.weight ? `${profile.weight} kg` : 'PENDING' }
                ].map((item, idx) => (
                  <div key={idx} className="bg-white/[0.01] border border-white/5 p-2 rounded-xl flex flex-col justify-between min-h-[42px] font-mono">
                    <span className="text-[7px] text-gray-500 font-bold uppercase tracking-wider">{item.label}</span>
                    <span className={`text-[9px] font-bold font-outfit mt-0.5 truncate ${item.value === 'PENDING' ? 'text-amber-500/60 animate-pulse' : 'text-[#00F0FF]'}`}>
                      {item.value}
                    </span>
                  </div>
                ))}
              </div>

              <div className="bg-gradient-to-br from-black/40 to-[#121215]/20 border border-white/5 p-3 rounded-2xl">
                <span className="text-[8px] text-gray-500 font-bold uppercase tracking-widest font-mono block mb-2">METABOLIC PROFILE</span>
                {profile.calculations ? (
                  <div className="flex flex-col gap-2.5 text-[9px] font-mono leading-normal text-gray-300">
                    
                    <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                      <span className="text-gray-500">Basal Metabolic (BMR)</span>
                      <span className="text-white font-bold font-outfit text-[10px]">{profile.calculations.bmr} kcal</span>
                    </div>

                    <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                      <span className="text-gray-500">Total Expenditure (TDEE)</span>
                      <span className="text-white font-bold font-outfit text-[10px]">{profile.calculations.tdee} kcal</span>
                    </div>

                    <div className="flex justify-between items-center pb-1.5 border-b border-white/5">
                      <span className="text-gray-500">Calorie Target</span>
                      <span className="text-[#00F0FF] font-bold font-outfit text-[10px]">{profile.calculations.targetCalories} kcal</span>
                    </div>

                    <div className="flex items-center justify-between mt-1">
                      <span className="text-gray-500">Macros</span>
                      <div className="flex gap-1.5">
                        <span className="bg-[#9D00FF]/15 border border-[#9D00FF]/30 px-1.5 py-0.5 rounded text-[8px] text-[#9D00FF] font-bold">P: {profile.calculations.targetProtein}g</span>
                        <span className="bg-white/5 border border-white/10 px-1.5 py-0.5 rounded text-[8px] text-white font-bold">C: {profile.calculations.targetCarbs}g</span>
                        <span className="bg-white/5 border border-white/10 px-1.5 py-0.5 rounded text-[8px] text-white font-bold">F: {profile.calculations.targetFats}g</span>
                      </div>
                    </div>

                  </div>
                ) : (
                  <span className="text-[9px] text-gray-500 font-bold block italic text-center py-2 font-mono">
                    Awaiting telemetry vectors...
                  </span>
                )}
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
};

export default Chatbot;
