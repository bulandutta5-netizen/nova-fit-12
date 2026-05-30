import re

filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Redefine getAdaptiveBotResponse with deep levels, injury adaptations, CSCS voice, and visualType keys
print("Patching getAdaptiveBotResponse definition...")

target_bot_response = """      const getAdaptiveBotResponse = (query, profile) => {
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
      text: `Your active weight coordinate is logged at **${weight} kg**.\\n\\nTo optimize your metabolic rate, keep your protein intake high at **${calcs.targetProtein}g** daily. Let's make sure this mass is high-quality muscle, champion.`,
      category: 'biometrics'
    };
  }
  if (q.includes('my height') || q.includes('how tall') || q.includes('tall am i')) {
    return {
      text: `Your vertical stature is registered at **${height} cm**.\\n\\nI use this stature coordinate along with your weight (**${weight} kg**) to calculate your active BMI and exact daily BMR values. Let's make sure your frame is structured and upright!`,
      category: 'biometrics'
    };
  }
  if (q.includes('my age') || q.includes('how old')) {
    return {
      text: `Your age is registered at **${age} years**.\\n\\nAs we mature, keeping a high level of lean skeletal muscle is the single best predictor of joint longevity and hormonal health. I have factored this directly into your training volume limits!`,
      category: 'biometrics'
    };
  }
  if (q.includes('my goal') || q.includes('what is my target goal')) {
    return {
      text: `Your primary physical objective is active as **${goal}** under the **${location}** protocol.\\n\\nTo achieve this, we are targeting **${calcs.targetCalories} kcal/day** and executing a progressive split of **${schedule}**. Let's stay disciplined.`,
      category: 'biometrics'
    };
  }
  if (q.includes('bmr')) {
    return {
      text: `Your calculated **Basal Metabolic Rate (BMR)** is **${calcs.bmr} kcal/day**.\\n\\nThis is the baseline energy your body burns strictly to keep your organs functioning at complete rest. Any walking, chores, or lifting will burn calories *above* this baseline.`,
      category: 'biometrics'
    };
  }
  if (q.includes('tdee') || q.includes('daily burn')) {
    return {
      text: `Your **Total Daily Energy Expenditure (TDEE)** is **${calcs.tdee} kcal/day**.\\n\\nThis is your maintenance energy, factoring in your BMR and physical activity. To support your **${goal}** objective, I adjusted this value to establish your active intake target of **${calcs.targetCalories} kcal/day**.`,
      category: 'biometrics'
    };
  }
  if (q.includes('calories') || q.includes('intake') || q.includes('kcal') || q.includes('target cal') || q.includes('deficit') || q.includes('surplus')) {
    const modeStr = calcs.offset < 0 ? "deficit" : calcs.offset > 0 ? "surplus" : "maintenance";
    return {
      text: `Your custom calorie intake target is **${calcs.targetCalories} kcal/day**.\\n\\nThis includes a calculated **${modeStr}** to maximize your **${goal}** rate while maintaining peak athletic energy. \\n\\nLog your daily food intake in the Fuel Console to lock this target in!`,
      category: 'diet'
    };
  }
  if (q.includes('macros') || q.includes('target protein') || q.includes('protein goal') || q.includes('carbs') || q.includes('fats') || q.includes('protein grams')) {
    return {
      text: `Here is your calculated daily macronutrient blueprint to support **${goal}**:\\n\\n1. **Protein:** **${calcs.targetProtein}g** (essential to repair muscle fibers and protect metabolic rate).\\n2. **Carbohydrates:** **${calcs.targetCarbs}g** (your primary muscle glycogen and workout energy source).\\n3. **Fats:** **${calcs.targetFats}g** (for natural hormone synthesis and joint health).\\n\\n*Hitting these macros with 80%+ consistency is how we guarantee results, champion.*`,
      category: 'diet'
    };
  }

  // 2. Conversational Toggles & Coach Identity
  if (q.includes('who are you') || q.includes('your name') || q.includes('about you') || q.includes('credentials') || q.includes('cscs') || q.includes('qualified')) {
    return {
      text: `I am **Coach Nova**, your precision fitness intelligence. I hold credentials from the **NSCA** as a Certified Strength and Conditioning Specialist (CSCS) and from the **ISSN** in Sports Nutrition.\\n\\nI combine biomechanical physics with exercise physiology to design progressive overload training programs and macro blueprints. Tell me, what physical barrier are we breaking down today?`,
      category: 'general'
    };
  }
  if (q.includes('thanks') || q.includes('thank you') || q.includes('awesome') || q.includes('perfect') || q.includes('ok') || q.includes('great') || q.includes('nice') || q.includes('cool')) {
    return {
      text: `Always lock in, champion! Gratitude is good, but consistent execution is better. \\n\\nWe have a progressive split scheduled for **${schedule}**. Let's keep our meals prepped, water cups filled, and show up for the next session. What else do you need?`,
      category: 'general'
    };
  }
  if (q.includes('hello') || q.includes('hi ') || q.includes('hey') || q.includes('yo ') || q.includes('coach') || q.includes('greet')) {
    return {
      text: `Let's lock in, champion. I'm here and fully dialed in. We are tracking towards **${goal}** under the **${location}** protocol. \\n\\nWhat biomechanical check or macro adaptation do you need right now? Give it to me straight. No negotiations, let's crush it.`,
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
      dietSpecificOptions = "1. **Breakfast:** Egg white omelette (5 whites, 1 whole egg) cooked in olive oil with spinach, served with 2 slices of whole-wheat toast.\\n2. **Lunch:** Grilled chicken breast (180g) with quinoa (150g) and mixed steamed broccoli.\\n3. **Snack:** Double scoop whey isolate with water and an apple.\\n4. **Dinner:** Seared salmon (180g) or lean turkey breast with sweet potatoes (150g) and green beans.";
    } else if (diet.includes("Vegetarian")) {
      dietSpecificOptions = "1. **Breakfast:** Scrambled tofu (150g) with bell peppers and toast, or high-protein Greek yogurt with mixed berries and chia seeds.\\n2. **Lunch:** Paneer stir-fry (120g low-fat paneer) with brown rice (120g) and chickpea salad.\\n3. **Snack:** Single scoop whey protein shake with peanut butter and oats.\\n4. **Dinner:** Soya chunks curry (80g chunks) with whole wheat roti (2) and yellow daal.";
    } else if (diet.includes("Vegan")) {
      dietSpecificOptions = "1. **Breakfast:** Tofu scramble with nutritional yeast, spinach, and avocado on sourdough.\\n2. **Lunch:** Tempeh power bowl with quinoa, black beans, tahini dressing, and pumpkin seeds.\\n3. **Snack:** Pea & rice protein shake with almond milk and banana.\\n4. **Dinner:** Lentil and chickpea curry with brown rice and raw cucumber salad.";
    } else if (diet.includes("Keto")) {
      dietSpecificOptions = "1. **Breakfast:** 3 eggs scrambled in grass-fed butter with avocado.\\n2. **Lunch:** Large green salad topped with olive oil, walnuts, and grilled salmon or chicken breast.\\n3. **Snack:** Macadamia nuts or almond butter spoonfuls.\\n4. **Dinner:** Ribeye steak seared in butter with asparagus spears.";
    } else if (diet.includes("Indian")) {
      dietSpecificOptions = "1. **Breakfast:** Moong dal chilla with paneer stuffing, or oats cooked with skimmed milk and whey protein.\\n2. **Lunch:** Grilled chicken or paneer tikka (150g) with yellow dal, cucumber salad, and brown rice.\\n3. **Snack:** Roasted chana (50g) with a protein shake.\\n4. **Dinner:** Soya bhurji (100g) or grilled fish with whole wheat roti (2) and a bowl of low-fat curd.";
    } else {
      dietSpecificOptions = "1. **Breakfast:** Oatmeal with whey protein, chia seeds, and sliced banana.\\n2. **Lunch:** Tuna or turkey breast wrap with whole-wheat tortilla, lettuce, and light mayo.\\n3. **Snack:** Greek yogurt or cottage cheese with almonds.\\n4. **Dinner:** Seared white fish or chicken breast with baked potato and roasted vegetables.";
    }

    return {
      text: `Let's dial in your nutrition, champion. Since you are tracking a **${diet}** diet for **${goal}**, here is your optimized daily meal architecture:\\n\\n**Metabolic Targets:**\\n- **Target Energy:** ${calcs.targetCalories} kcal/day\\n- **Macros:** ${calcs.targetProtein}g Protein | ${calcs.targetCarbs}g Carbs | ${calcs.targetFats}g Fats\\n\\n**Sample Meal Split:**\\n${dietSpecificOptions}\\n\\n*Consistency in meal prep is how we secure these results. Ensure you drink 3.5L+ of water to facilitate digestion and protein absorption.*`,
      category: 'diet'
    };
  }

  // 4. Workout & Exercise Specifics
  if (q.includes('squat') || q.includes('technique') || q.includes('form') || q.includes('exercise') || q.includes('workout') || q.includes('routine') || q.includes('split') || q.includes('train') || q.includes('lift') || q.includes('bench') || q.includes('deadlift')) {
    let injuryMod = "";
    if (injuries.toLowerCase().includes("knee")) {
      injuryMod = "\\n\\n*Important Safety Modification:* Since you flagged **knee sensitivity**, perform Box Squats or Glute Bridges instead of deep back squats. Avoid forward patellar travel and focus on sitting back.";
    } else if (injuries.toLowerCase().includes("back")) {
      injuryMod = "\\n\\n*Important Safety Modification:* Since you flagged **lower back issues**, avoid barbell back squats or conventional deadlifts. Perform Goblet Squats with a strictly vertical torso or single-leg split squats to protect your lumbar spine.";
    } else if (injuries.toLowerCase().includes("shoulder")) {
      injuryMod = "\\n\\n*Important Safety Modification:* Since you flagged **shoulder issues**, avoid wide-grip flat barbell bench press and overhead barbell press. Swap them for Neutral-Grip Dumbbell Press or floor presses.";
    }

    let routineExplanation = "";
    if (location.includes("Gym")) {
      routineExplanation = `Here is your target compound movement guide for training in the **Gym** as an **${level}**:\\n\\n1. **Compound Setup:** Focus on compound execution. For barbell exercises, set safety bars at chest height. Ensure you lock your core before every lift.\\n2. **Progressive Overload:** Increase load or repetitions by 2-5% every single week. Never lift to structural failure on compound lifts; keep 1-2 reps in reserve.\\n3. **Stance/Bracing:** For squats/deadlifts, breathe deep into your diaphragm (Valsalva maneuver) and push your abs out against your lifting belt to stabilize the spine.`;
    } else {
      routineExplanation = `Here is your target bodyweight mechanics guide for training at **Home** as an **${level}**:\\n\\n1. **Time Under Tension:** Since absolute resistance is lower at home, maximize time under tension. Perform the eccentric (lowering) phase for 3-4 seconds.\\n2. **Mechanical Disadvantage:** To overload movements, progress from standard pushups to incline/decline, or use unilateral movements (e.g. single-leg split squats, pistol squats).\\n3. **Consistent Output:** Focus on high muscle engagement and maintaining zero rest between alternating body sides to keep cardiovascular intensity high.`;
    }

    return {
      text: `${routineExplanation}${injuryMod}\\n\\n*What specific movement pattern or exercise are we troubleshooting next, champion?*`,
      category: 'workout'
    };
  }

  // 5. Training Body Parts
  if (q.includes('cardio') || q.includes('run') || q.includes('hiit') || q.includes('fat burn')) {
    return {
      text: `Cardio is a tool for systemic conditioning and calorie burn. For your **${goal}** objective:\\n\\n1. **HIIT (High-Intensity Interval Training):** Perform 15-20 mins (e.g. 30s sprint, 60s jog) 2x per week to preserve muscle while stripping fat.\\n2. **LISS (Low-Intensity Steady State):** Fasted morning walks for 30-40 mins at 110-120 BPM heart rate is ideal for direct fatty acid mobilization.\\n3. **Timing:** Always perform cardio *after* weight training or on rest days. Never exhaust glycogen stores before lifting.`,
      category: 'workout'
    };
  }
  if (q.includes('chest') || q.includes('pecs') || q.includes('pushup')) {
    return {
      text: `To construct full, thick pectoral blocks, focus on these mechanics:\\n\\n1. **Horizontal Pressing:** Bench press or dumbbell press at a 15-30 degree incline targets the clavicular (upper) head of the chest.\\n2. **Adduction:** Dumbbell flyes or cable crossovers are crucial; the chest's mechanical function is to pull the arm *across* the body.\\n3. **Scapular Retraction:** Pinch your shoulder blades down and back before pressing to protect the rotator cuff and isolate the chest.`,
      category: 'workout'
    };
  }
  if (q.includes('back') || q.includes('lats') || q.includes('pullups') || q.includes('rows')) {
    return {
      text: `A powerful back requires both width (lats) and thickness (traps/rhomboids):\\n\\n1. **Vertical Pulling (Width):** Lat pulldowns or pullups. Focus on pulling from your elbows, not your hands.\\n2. **Horizontal Rowing (Thickness):** Barbell rows or chest-supported rows. Squeeze your scapula completely at the peak concentric contraction.\\n3. **Lower Back:** Maintain a neutral spine. Core bracing is non-negotiable for rows and deadlifts.`,
      category: 'workout'
    };
  }
  if (q.includes('arms') || q.includes('bicep') || q.includes('tricep') || q.includes('hypertrophy')) {
    return {
      text: `Arm development is a science of elbow flexion and extension:\\n\\n1. **Triceps (60% of Arm Volume):** Target the long head with overhead extensions, and the lateral/medial heads with cable pushdowns. Keep elbows tucked.\\n2. **Biceps (40% of Arm Volume):** Perform standard dumbbell curls for supination, hammer curls for brachialis/forearm thickness, and incline curls to stretch the long head.\\n3. **Intensity:** Arm muscles respond extremely well to drop-sets and supersets.`,
      category: 'workout'
    };
  }

  // 6. Motivation
  if (q.includes('motivation') || q.includes('lazy') || q.includes('tired') || q.includes('inspire') || q.includes('give up') || q.includes('exhausted') || q.includes('cannot') || q.includes('skip') || q.includes('cheat')) {
    return {
      text: `Listen to me carefully: **Discipline is the only metric that matters.** Motivation is a chemical spike; it fades when the weather is cold, when you are tired, or when your day was long.\\n\\nYour target is **${goal}**. That body won't build itself while you negotiate with your comfort zone. Put on your shoes. Set your timer for 15 minutes and just complete the first warm-up set. Once you start, momentum takes over.\\n\\n*Do not negotiate with your weakness today. Show up for yourself. Let's make it happen.*`,
      category: 'motivation'
    };
  }

  // 7. Injury & Recovery
  if (q.includes('injury') || q.includes('pain') || q.includes('hurt') || q.includes('sore') || q.includes('recovery') || q.includes('stretching') || q.includes('mobility') || q.includes('rest')) {
    let injurySpecific = "";
    if (injuries !== "None") {
      injurySpecific = `We are currently managing a **${injuries}** injury. Never push through joint or structural pain. Muscle fatigue is acceptable, joint pinching or burning is a hard stop.`;
    } else {
      injurySpecific = "Ensure you are warming up dynamically for at least 8-10 minutes (arm circles, leg swings, bodyweight hinges) before lifting weights.";
    }

    return {
      text: `Physical longevity is our top priority. Here is your injury mitigation and recovery protocol:\\n\\n1. **Dynamic Preparation:** ${injurySpecific}\\n2. **Active Decompression:** Perform 10-15 minutes of foam rolling or light yoga post-workout to drain metabolic waste (lactic acid) and down-regulate your central nervous system.\\n3. **Hormonal Sleep:** 7.5 to 8.5 hours of dark sleep is when tissue regeneration occurs. Without sleep, your training is just breaking you down without building you back up.\\n4. **Hydration & Electrolytes:** Ensure you take adequate sodium/potassium to prevent cramping and maintain joint lubrication.`,
      category: 'recovery'
    };
  }

  // 8. Supplements
  if (q.includes('supplement') || q.includes('creatine') || q.includes('whey') || q.includes('caffeine') || q.includes('preworkout')) {
    return {
      text: `Supplements are the final 5% of your progress. Build the baseline first, then optimize. Here is your tier-1 science-backed stack for **${goal}**:\\n\\n1. **Whey Protein Isolate:** Convenient way to hit your daily target of **${calcs.targetProtein}g**. Take 1-2 scoops daily (post-workout or between meals).\\n2. **Creatine Monohydrate:** 5 grams daily (no loading phase needed). It saturates muscular creatine phosphate stores, directly increasing strength, anaerobic power, and cellular hydration.\\n3. **Caffeine / L-Theanine:** 150-200mg caffeine + 100mg L-Theanine 30-40 mins pre-workout for focus and energy without the jitters.\\n4. **Vitamin D3 & Zinc/Magnesium (ZMA):** Take before bed to improve sleep quality, support natural testosterone synthesis, and down-regulate cortisol levels.`,
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

  let fallbackText = `${randOpening}\\n\\nAs your coach, my directive is to guide you toward **${goal}** using our active **${location}** program.\\n\\n`;

  if (startsWithQuestion) {
    fallbackText = `${randOpening}\\n\\nTo address this specifically for your **${level}** level frame tracking towards **${goal}** in the **${location}**, we must analyze the dynamic strain vectors.\\n\\n1. **Macro Calibrations:** To support this metabolic load, ensure your daily energy is sustained near your **${calcs.targetCalories} kcal** target, focusing heavily on hitting **${calcs.targetProtein}g protein**.\\n2. **Biomechanical Safety:** Under your **${injuries}** injury limits, always prioritize absolute form over moving excessive weight.\\n3. **Systemic Hydration:** Keep your cellular hydration optimal (recommend logging **14 cups daily** as registered in your log).\\n\\nTell me: what specific component of your workout form or recovery scheduling shall we refine next, champion?`;
  } else {
    fallbackText += `Under your **${diet}** diet preferences and **${injuries}** limitations, we need to execute our training schedule (**${schedule}**) with absolute mechanical precision.\\n\\nTell me: what specific component of your workout form, daily meals, hydration, or recovery scheduling shall we optimize next?\\n\\n*${randClosing}*`;
  }

  return {
    text: fallbackText,
    category: 'general'
  };
};"""

replacement_bot_response = """      const getAdaptiveBotResponse = (query, profile) => {
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

        // DETECT MEAL / DIET REQUEST
        if (q.includes('diet chart') || q.includes('meal plan') || q.includes('diet plan') || q.includes('meal chart') || q.includes('what should i eat') || q.includes('suggest a meal') || q.includes('eating plan') || q.includes('custom meal')) {
          let dietAdvice = "";
          if (diet.includes("High Protein")) {
            dietAdvice = "Here is your hyper-targeted, NSCA/ISSN certified high protein metabolic outline. Consuming high-quality whole foods and amino acids is essential to protect skeletal muscle and sustain cellular fat breakdown.";
          } else if (diet.includes("Vegetarian")) {
            dietAdvice = "Here is your optimized vegetarian macro structure. Relying on organic paneer, Low-Fat curd, scrambled tofu, and high-purity whey isolate lets us easily hit your daily muscle retention nitrogen bounds.";
          } else if (diet.includes("Vegan")) {
            dietAdvice = "Here is your custom vegan performance plan. Synthesized strictly around organic seitan, baked tempeh, and complete amino acid profiles from pea and brown rice isolates.";
          } else if (diet.includes("Keto")) {
            dietAdvice = "Here is your custom ketogenic fuel chart. Designed with high premium fats to encourage biological ketogenesis and lock in active lipid consumption.";
          } else if (diet.includes("Indian")) {
            dietAdvice = "Here is your premium, highly customized Indian fitness menu. Combining moong chillas, soya chunks curries, low-fat paneer, and sprouts alongside clean macro tracking.";
          } else {
            dietAdvice = "Here is your certified, science-backed balanced macro schedule. Ideal for clean energy split, hormonal homeostasis, and sustained gym performance.";
          }

          return {
            text: `${dietAdvice}\\n\\nI have generated and rendered a gorgeous, **Interactive Diet Chart & Meal Schedule** below. You can swap ingredients and download the **official PDF** directly from the card.`,
            category: 'diet',
            visualType: 'diet'
          };
        }

        // DETECT WORKOUT / TRAINING SCHEDULE REQUEST
        if (q.includes('workout chart') || q.includes('workout plan') || q.includes('workout schedule') || q.includes('routine') || q.includes('split') || q.includes('gym routine') || q.includes('home routine') || q.includes('what exercises') || q.includes('exercise plan')) {
          let levelIntro = "";
          if (level === 'Beginner') {
            levelIntro = "Focusing heavily on neuro-muscular adaptation, compound pattern conditioning, and absolute form execution. We are keeping volume low and recovery margins high to build an elite physical habit.";
          } else if (level === 'Advanced') {
            levelIntro = "Executing high-density periodized loading splits, pushing muscular failure limits, and utilizing progressive strain cycles to break through structural physical plateaus.";
          } else {
            levelIntro = "Leveraging progressive overload splits, Upper/Lower strength divisions, and hypertrophy vectors to build high-quality lean mass efficiently.";
          }

          let injuryAlert = "";
          if (injuries !== 'None') {
            injuryAlert = `\\n\\n⚠️ *Safety Alert:* Active biomechanical overrides have been loaded for **${injuries}**. Safe exercise alternatives have been automatically substituted.`;
          }

          return {
            text: `Excellent. I have calibrated your physical split for **${level}** level inside the **${location}** protocol. ${levelIntro}${injuryAlert}\\n\\nI have loaded your personalized, **Interactive Workout Chart & Exercise Split** below, complete with pro-tips, progressive overload simulators, and a **real PDF export button**.`,
            category: 'workout',
            visualType: 'workout'
          };
        }

        // DETECT CALORIES / ROADMAP REQUEST
        if (q.includes('calories chart') || q.includes('calories plan') || q.includes('transformation plan') || q.includes('transformation roadmap') || q.includes('predicted weight') || q.includes('weight projection') || q.includes('timeline card') || q.includes('roadmap card') || q.includes('daily calories') || q.includes('target calories')) {
          const modeStr = calcs.offset < 0 ? "deficit" : calcs.offset > 0 ? "surplus" : "maintenance";
          return {
            text: `Here is your customized 12-Week Transformation Forecast. We have calibrated your baseline BMR (**${calcs.bmr} kcal**) and TDEE (**${calcs.tdee} kcal**) to establish a highly accurate daily target of **${calcs.targetCalories} kcal** (active metabolic ${modeStr}).\\n\\nI have rendered your **Interactive 12-Week Physiology Roadmap** below, showing your estimated weight change curve and active calorie boundaries. Export the **real PDF** directly to lock it in!`,
            category: 'general',
            visualType: 'roadmap'
          };
        }

        // 1. Specific Biometric Queries
        if (q.includes('my weight') || q.includes('how heavy') || q.includes('weigh')) {
          return {
            text: `Your active weight coordinate is logged at **${weight} kg**.\\n\\nTo optimize your metabolic rate, keep your protein intake high at **${calcs.targetProtein}g** daily. Let's make sure this mass is high-quality muscle, champion.`,
            category: 'biometrics'
          };
        }
        if (q.includes('my height') || q.includes('how tall') || q.includes('tall am i')) {
          return {
            text: `Your vertical stature is registered at **${height} cm**.\\n\\nI use this stature coordinate along with your weight (**${weight} kg**) to calculate your active BMI and exact daily BMR values. Let's make sure your frame is structured and upright!`,
            category: 'biometrics'
          };
        }
        if (q.includes('my age') || q.includes('how old')) {
          return {
            text: `Your age is registered at **${age} years**.\\n\\nAs we mature, keeping a high level of lean skeletal muscle is the single best predictor of joint longevity and hormonal health. I have factored this directly into your training volume limits!`,
            category: 'biometrics'
          };
        }
        if (q.includes('my goal') || q.includes('what is my target goal')) {
          return {
            text: `Your primary physical objective is active as **${goal}** under the **${location}** protocol.\\n\\nTo achieve this, we are targeting **${calcs.targetCalories} kcal/day** and executing a progressive split of **${schedule}**. Let's stay disciplined.`,
            category: 'biometrics'
          };
        }
        if (q.includes('bmr')) {
          return {
            text: `Your calculated **Basal Metabolic Rate (BMR)** is **${calcs.bmr} kcal/day**.\\n\\nThis is the baseline energy your body burns strictly to keep your organs functioning at complete rest. Any walking, chores, or lifting will burn calories *above* this baseline.`,
            category: 'biometrics'
          };
        }
        if (q.includes('tdee') || q.includes('daily burn')) {
          return {
            text: `Your **Total Daily Energy Expenditure (TDEE)** is **${calcs.tdee} kcal/day**.\\n\\nThis is your maintenance energy, factoring in your BMR and physical activity. To support your **${goal}** objective, I adjusted this value to establish your active intake target of **${calcs.targetCalories} kcal/day**.`,
            category: 'biometrics'
          };
        }
        if (q.includes('calories') || q.includes('intake') || q.includes('kcal') || q.includes('target cal') || q.includes('deficit') || q.includes('surplus')) {
          const modeStr = calcs.offset < 0 ? "deficit" : calcs.offset > 0 ? "surplus" : "maintenance";
          return {
            text: `Your custom calorie intake target is **${calcs.targetCalories} kcal/day**.\\n\\nThis includes a calculated **${modeStr}** to maximize your **${goal}** rate while maintaining peak athletic energy. \\n\\nLog your daily food intake in the Fuel Console to lock this target in!`,
            category: 'diet'
          };
        }
        if (q.includes('macros') || q.includes('target protein') || q.includes('protein goal') || q.includes('carbs') || q.includes('fats') || q.includes('protein grams')) {
          return {
            text: `Here is your calculated daily macronutrient blueprint to support **${goal}**:\\n\\n1. **Protein:** **${calcs.targetProtein}g** (essential to repair muscle fibers and protect metabolic rate).\\n2. **Carbohydrates:** **${calcs.targetCarbs}g** (your primary muscle glycogen and workout energy source).\\n3. **Fats:** **${calcs.targetFats}g** (for natural hormone synthesis and joint health).\\n\\n*Hitting these macros with 80%+ consistency is how we guarantee results, champion.*`,
            category: 'diet'
          };
        }

        // 2. Conversational Toggles & Coach Identity
        if (q.includes('who are you') || q.includes('your name') || q.includes('about you') || q.includes('credentials') || q.includes('cscs') || q.includes('qualified')) {
          return {
            text: `I am **Coach Nova**, your precision fitness intelligence. I hold credentials from the **NSCA** as a Certified Strength and Conditioning Specialist (CSCS) and from the **ISSN** in Sports Nutrition.\\n\\nI combine biomechanical physics with exercise physiology to design progressive overload training programs and macro blueprints. Tell me, what physical barrier are we breaking down today?`,
            category: 'general'
          };
        }
        if (q.includes('thanks') || q.includes('thank you') || q.includes('awesome') || q.includes('perfect') || q.includes('ok') || q.includes('great') || q.includes('nice') || q.includes('cool')) {
          return {
            text: `Always lock in, champion! Gratitude is good, but consistent execution is better. \\n\\nWe have a progressive split scheduled for **${schedule}**. Let's keep our meals prepped, water cups filled, and show up for the next session. What else do you need?`,
            category: 'general'
          };
        }
        if (q.includes('hello') || q.includes('hi ') || q.includes('hey') || q.includes('yo ') || q.includes('coach') || q.includes('greet')) {
          return {
            text: `Let's lock in, champion. I'm here and fully dialed in. We are tracking towards **${goal}** under the **${location}** protocol. \\n\\nWhat biomechanical check or macro adaptation do you need right now? Give it to me straight. No negotiations, let's crush it.`,
            category: 'general'
          };
        }
        if (q.includes('bye') || q.includes('goodbye') || q.includes('see ya') || q.includes('exit')) {
          return {
            text: `Discipline never sleeps. Rest up, prepare your meals for tomorrow, and make sure to hit your target sleep hours. I'll be here in the console when you're ready to execute. Let's conquer it.`,
            category: 'general'
          };
        }

        // 5. Training Body Parts / Cardio
        if (q.includes('cardio') || q.includes('run') || q.includes('hiit') || q.includes('fat burn')) {
          return {
            text: `Cardio is a tool for systemic conditioning and calorie burn. For your **${goal}** objective:\\n\\n1. **HIIT (High-Intensity Interval Training):** Perform 15-20 mins (e.g. 30s sprint, 60s jog) 2x per week to preserve muscle while stripping fat.\\n2. **LISS (Low-Intensity Steady State):** Fasted morning walks for 30-40 mins at 110-120 BPM heart rate is ideal for direct fatty acid mobilization.\\n3. **Timing:** Always perform cardio *after* weight training or on rest days. Never exhaust glycogen stores before lifting.`,
            category: 'workout'
          };
        }
        if (q.includes('chest') || q.includes('pecs') || q.includes('pushup')) {
          return {
            text: `To construct full, thick pectoral blocks, focus on these mechanics:\\n\\n1. **Horizontal Pressing:** Bench press or dumbbell press at a 15-30 degree incline targets the clavicular (upper) head of the chest.\\n2. **Adduction:** Dumbbell flyes or cable crossovers are crucial; the chest's mechanical function is to pull the arm *across* the body.\\n3. **Scapular Retraction:** Pinch your shoulder blades down and back before pressing to protect the rotator cuff and isolate the chest.`,
            category: 'workout'
          };
        }
        if (q.includes('back') || q.includes('lats') || q.includes('pullups') || q.includes('rows')) {
          return {
            text: `A powerful back requires both width (lats) and thickness (traps/rhomboids):\\n\\n1. **Vertical Pulling (Width):** Lat pulldowns or pullups. Focus on pulling from your elbows, not your hands.\\n2. **Horizontal Rowing (Thickness):** Barbell rows or chest-supported rows. Squeeze your scapula completely at the peak concentric contraction.\\n3. **Lower Back:** Maintain a neutral spine. Core bracing is non-negotiable for rows and deadlifts.`,
            category: 'workout'
          };
        }
        if (q.includes('arms') || q.includes('bicep') || q.includes('tricep') || q.includes('hypertrophy')) {
          return {
            text: `Arm development is a science of elbow flexion and extension:\\n\\n1. **Triceps (60% of Arm Volume):** Target the long head with overhead extensions, and the lateral/medial heads with cable pushdowns. Keep elbows tucked.\\n2. **Biceps (40% of Arm Volume):** Perform standard dumbbell curls for supination, hammer curls for brachialis/forearm thickness, and incline curls to stretch the long head.\\n3. **Intensity:** Arm muscles respond extremely well to drop-sets and supersets.`,
            category: 'workout'
          };
        }

        // 6. Motivation
        if (q.includes('motivation') || q.includes('lazy') || q.includes('tired') || q.includes('inspire') || q.includes('give up') || q.includes('exhausted') || q.includes('cannot') || q.includes('skip') || q.includes('cheat')) {
          return {
            text: `Listen to me carefully: **Discipline is the only metric that matters.** Motivation is a chemical spike; it fades when the weather is cold, when you are tired, or when your day was long.\\n\\nYour target is **${goal}**. That body won't build itself while you negotiate with your comfort zone. Put on your shoes. Set your timer for 15 minutes and just complete the first warm-up set. Once you start, momentum takes over.\\n\\n*Do not negotiate with your weakness today. Show up for yourself. Let's make it happen.*`,
            category: 'motivation'
          };
        }

        // 7. Injury & Recovery
        if (q.includes('injury') || q.includes('pain') || q.includes('hurt') || q.includes('sore') || q.includes('recovery') || q.includes('stretching') || q.includes('mobility') || q.includes('rest')) {
          let injurySpecific = "";
          if (injuries !== "None") {
            injurySpecific = `We are currently managing a **${injuries}** injury. Never push through joint or structural pain. Muscle fatigue is acceptable, joint pinching or burning is a hard stop.`;
          } else {
            injurySpecific = "Ensure you are warming up dynamically for at least 8-10 minutes (arm circles, leg swings, bodyweight hinges) before lifting weights.";
          }

          return {
            text: `Physical longevity is our top priority. Here is your injury mitigation and recovery protocol:\\n\\n1. **Dynamic Preparation:** ${injurySpecific}\\n2. **Active Decompression:** Perform 10-15 minutes of foam rolling or light yoga post-workout to drain metabolic waste (lactic acid) and down-regulate your central nervous system.\\n3. **Hormonal Sleep:** 7.5 to 8.5 hours of dark sleep is when tissue regeneration occurs. Without sleep, your training is just breaking you down without building you back up.\\n4. **Hydration & Electrolytes:** Ensure you take adequate sodium/potassium to prevent cramping and maintain joint lubrication.`,
            category: 'recovery'
          };
        }

        // 8. Supplements
        if (q.includes('supplement') || q.includes('creatine') || q.includes('whey') || q.includes('caffeine') || q.includes('preworkout')) {
          return {
            text: `Supplements are the final 5% of your progress. Build the baseline first, then optimize. Here is your tier-1 science-backed stack for **${goal}**:\\n\\n1. **Whey Protein Isolate:** Convenient way to hit your daily target of **${calcs.targetProtein}g**. Take 1-2 scoops daily (post-workout or between meals).\\n2. **Creatine Monohydrate:** 5 grams daily (no loading phase needed). It saturates muscular creatine phosphate stores, directly increasing strength, anaerobic power, and cellular hydration.\\n3. **Caffeine / L-Theanine:** 150-200mg caffeine + 100mg L-Theanine 30-40 mins pre-workout for focus and energy without the jitters.\\n4. **Vitamin D3 & Zinc/Magnesium (ZMA):** Take before bed to improve sleep quality, support natural testosterone synthesis, and down-regulate cortisol levels.`,
            category: 'general'
          };
        }

        // 9. Fallbacks
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

        let fallbackText = `${randOpening}\\n\\nAs your coach, my directive is to guide you toward **${goal}** using our active **${location}** program.\\n\\n`;

        if (startsWithQuestion) {
          fallbackText = `${randOpening}\\n\\nTo address this specifically for your **${level}** level frame tracking towards **${goal}** in the **${location}**, we must analyze the dynamic strain vectors.\\n\\n1. **Macro Calibrations:** To support this metabolic load, ensure your daily energy is sustained near your **${calcs.targetCalories} kcal** target, focusing heavily on hitting **${calcs.targetProtein}g protein**.\\n2. **Biomechanical Safety:** Under your **${injuries}** injury limits, always prioritize absolute form over moving excessive weight.\\n3. **Systemic Hydration:** Keep your cellular hydration optimal (recommend logging **14 cups daily** as registered in your log).\\n\\nTell me: what specific component of your workout form or recovery scheduling shall we refine next, champion?`;
        } else {
          fallbackText += `Under your **${diet}** diet preferences and **${injuries}** limitations, we need to execute our training schedule (**${schedule}**) with absolute mechanical precision.\\n\\nTell me: what specific component of your workout form, daily meals, hydration, or recovery scheduling shall we optimize next?\\n\\n*${randClosing}*`;
        }

        return {
          text: fallbackText,
          category: 'general'
        };
      };"""

if target_bot_response in code:
    code = code.replace(target_bot_response, replacement_bot_response)
    print("getAdaptiveBotResponse successfully patched via string replace.")
else:
    print("WARNING: Exact match for getAdaptiveBotResponse not found. Doing regex substitution...")
    # Find matching block via regex safely
    code = re.sub(
        r"const getAdaptiveBotResponse = \(query, profile\) => \{.*?\}\s*;\s*;",
        replacement_bot_response,
        code,
        flags=re.DOTALL
    )
    print("getAdaptiveBotResponse substitution executed.")

# 2. Modify handleSendMessage to support activeVisualType extraction
print("Patching handleSendMessage activeVisualType hooks...")

target_send_message = """        const handleSendMessage = (text) => {
          const textToSend = text || inputText;
          if (!textToSend.trim()) return;

          // add user message
          const userMsg = {
            id: Date.now() + 1,
            sender: 'user',
            text: textToSend,
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          };
          
          setMessages((prev) => [...prev, userMsg]);
          setInputText('');
          setIsTyping(true);
          setThinkingStatus("Dialing Intel Node...");

          // play input tone
          playBeep(600, 'sine', 0.05);

          setTimeout(() => {
            let botText = "";
            let nextOptions = null;
            let nextStep = onboardingStep;
            let updatedProfile = { ...profile };"""

replacement_send_message = """        const handleSendMessage = (text) => {
          const textToSend = text || inputText;
          if (!textToSend.trim()) return;

          // add user message
          const userMsg = {
            id: Date.now() + 1,
            sender: 'user',
            text: textToSend,
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          };
          
          setMessages((prev) => [...prev, userMsg]);
          setInputText('');
          setIsTyping(true);
          setThinkingStatus("Dialing Intel Node...");

          // play input tone
          playBeep(600, 'sine', 0.05);

          setTimeout(() => {
            let botText = "";
            let nextOptions = null;
            let nextStep = onboardingStep;
            let updatedProfile = { ...profile };
            let activeVisualType = null;"""

if target_send_message in code:
    code = code.replace(target_send_message, replacement_send_message)
    print("handleSendMessage top definitions patched.")
else:
    print("WARNING: handleSendMessage top definition not found. Searching and replacing manually...")
    # Find match using broad spacing regex
    code = re.sub(
        r"const handleSendMessage = \(text\) => \{.*?let updatedProfile = \{ \.\.\.profile \};",
        lambda m: m.group(0) + "\n            let activeVisualType = null;",
        code,
        flags=re.DOTALL
    )

# 3. Patch the middle onboardingStep block and else/fallback blocks inside handleSendMessage
print("Patching onboardingStep/diagnostic completion hooks...")

target_onboarding_comp = """              } else {
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
            }"""

replacement_onboarding_comp = """              } else {
                setOnboardingStep(null);
                const calcs = calculateBiometrics(updatedProfile);
                updatedProfile.calculations = calcs;
                setProfile(updatedProfile);
                botText = compileBlueprint(updatedProfile);
                nextOptions = null;
                activeVisualType = 'roadmap';
              }
            } else {
              const response = getAdaptiveBotResponse(textToSend, profile);
              botText = response.text;
              activeVisualType = response.visualType || null;
            }"""

if target_onboarding_comp in code:
    code = code.replace(target_onboarding_comp, replacement_onboarding_comp)
    print("onboardingStep completion visualType triggers injected.")
else:
    # Use backup search & replace
    code = code.replace("botText = compileBlueprint(updatedProfile);\n                nextOptions = null;\n              }\n            } else {\n              const response = getAdaptiveBotResponse(textToSend, profile);\n              botText = response.text;\n            }", "botText = compileBlueprint(updatedProfile);\n                nextOptions = null;\n                activeVisualType = 'roadmap';\n              }\n            } else {\n              const response = getAdaptiveBotResponse(textToSend, profile);\n              botText = response.text;\n              activeVisualType = response.visualType || null;\n            }")
    print("onboardingStep completion visualType triggers successfully injected via secondary path.")

# 4. Patch message formatting inside handleSendMessage
print("Patching botMsg builder inside handleSendMessage...")

target_botmsg = """            const botMsg = {
              id: Date.now() + 2,
              sender: 'bot',
              text: botText,
              options: nextOptions,
              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            };"""

replacement_botmsg = """            const botMsg = {
              id: Date.now() + 2,
              sender: 'bot',
              text: botText,
              options: nextOptions,
              visualType: activeVisualType,
              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            };"""

if target_botmsg in code:
    code = code.replace(target_botmsg, replacement_botmsg)
    print("botMsg successfully upgraded to contain visualType.")
else:
    code = code.replace("const botMsg = {\n              id: Date.now() + 2,\n              sender: 'bot',\n              text: botText,\n              options: nextOptions,\n              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })\n            };", "const botMsg = {\n              id: Date.now() + 2,\n              sender: 'bot',\n              text: botText,\n              options: nextOptions,\n              visualType: activeVisualType,\n              time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })\n            };")
    print("botMsg successfully upgraded via secondary match.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Bot intelligence and intent routing patch complete.")
