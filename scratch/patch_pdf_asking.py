filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Inject compilePdfContentText right after generateRealPDF definition
print("Injecting compilePdfContentText utility...")
target_generate_pdf_end = "};"

# We will locate the exact end of generateRealPDF
# In our previous insert, generateRealPDF ends with:
# doc.save(`FitNova_Premium_${type.toUpperCase()}_Protocol.pdf`);
# return true;
# } catch (err) { ... }
# };

target_marker = """          doc.save(`FitNova_Premium_${type.toUpperCase()}_Protocol.pdf`);
          return true;
        } catch (err) {
          console.error("PDF compilation error:", err);
          alert("Error generating PDF: " + err.message);
          return false;
        }
      };"""

replacement_marker = """          doc.save(`FitNova_Premium_${type.toUpperCase()}_Protocol.pdf`);
          return true;
        } catch (err) {
          console.error("PDF compilation error:", err);
          alert("Error generating PDF: " + err.message);
          return false;
        }
      };

      // Helper to compile customized PDF text content dynamically
      const compilePdfContentText = (type, profile) => {
        const level = profile.level || 'Intermediate';
        const location = profile.location || 'Gym';
        const injuries = profile.injuries || 'None';
        const diet = profile.diet || 'Balanced';
        const goal = profile.goal || 'recomp';
        const startW = parseFloat(profile.weight) || 75;
        const calcs = profile.calculations || { targetCalories: 2200, targetProtein: 140, targetCarbs: 220, targetFats: 73, bmr: 1650, tdee: 2450 };

        if (type === 'workout') {
          let routineTitle = location === 'Home' ? `${level} Progressive Home Calisthenics` : `${level} Compound Strength Engine`;
          let days = [];

          if (location === 'Home') {
            if (level === 'Beginner') {
              days = [
                { day: 'Day 1', focus: 'Full Body A', exercises: ['Bodyweight Squats (3 sets x 15 reps)', 'Incline Pushups (3 sets x 10 reps)', 'Doorframe Towel Pulls (3 sets x 12 reps)'] },
                { day: 'Day 2', focus: 'Recovery Focus', exercises: ['Dynamic Joint Mobility (1 set x 10 min)', 'Core Plank Hold (3 sets x 30s)'] },
                { day: 'Day 3', focus: 'Full Body B', exercises: ['Glute Bridges (3 sets x 15 reps)', 'Chair Dips (3 sets x 8 reps)', 'Backpack Rows (3 sets x 10 reps)'] }
              ];
            } else if (level === 'Advanced') {
              days = [
                { day: 'Day 1', focus: 'Push Focus', exercises: ['Decline Archer Pushups (4 sets x 12 reps)', 'Handstand Wall Press (4 sets x 8 reps)', 'Chair Dips (3 sets x 15 reps)'] },
                { day: 'Day 2', focus: 'Pull Focus', exercises: ['Pullups (4 sets x 10 reps)', 'Single-Arm Backpack Rows (4 sets x 12 reps)', 'Towel Bicep Curls (3 sets x 15 reps)'] },
                { day: 'Day 3', focus: 'Legs / Core', exercises: ['Pistol Squats (4 sets x 6 reps/side)', 'Bulgarian Split Squats (3 sets x 12 reps/side)', 'L-Sit Chair Holds (3 sets x 20s)'] }
              ];
            } else {
              days = [
                { day: 'Day 1', focus: 'Upper Body Split', exercises: ['Regular Pushups (4 sets x 15 reps)', 'Backpack Rows (4 sets x 12 reps)', 'Band Facepulls (3 sets x 15 reps)'] },
                { day: 'Day 2', focus: 'Lower Body / Abs', exercises: ['Bulgarian Split Squats (4 sets x 12 reps/side)', 'Single-Leg Calf Raises (4 sets x 15 reps/side)', 'Plank Knee-to-Elbows (3 sets x 45s)'] }
              ];
            }
          } else {
            if (level === 'Beginner') {
              days = [
                { day: 'Day 1', focus: 'Full Body Compounds', exercises: ['Barbell Squats (3 sets x 8 reps @ 40kg)', 'Barbell Bench Press (3 sets x 8 reps @ 30kg)', 'Lat Pulldowns (3 sets x 10 reps @ 35kg)'] },
                { day: 'Day 2', focus: 'Rest / Light Core', exercises: ['Hanging Leg Raises (3 sets x 12 reps)', 'Fasted LISS Cardio (1 set x 30 min)'] },
                { day: 'Day 3', focus: 'Posterior & Pulls', exercises: ['Romanian Deadlifts (3 sets x 10 reps @ 45kg)', 'Seated Cable Rows (3 sets x 10 reps @ 40kg)', 'Overhead DB Press (3 sets x 10 reps @ 10kg)'] }
              ];
            } else if (level === 'Advanced') {
              days = [
                { day: 'Day 1', focus: 'Push Hypertrophy', exercises: ['Incline Barbell Bench (4 sets x 8 reps @ 80kg)', 'Flat DB Chest Press (3 sets x 10 reps @ 34kg DBs)', 'Cable Overhead Triceps (4 sets x 12 reps @ 25kg)'] },
                { day: 'Day 2', focus: 'Pull Hypertrophy', exercises: ['Weighted Pullups (4 sets x 6 reps @ +15kg)', 'Barbell Bent Rows (4 sets x 8 reps @ 85kg)', 'Hammer DB Curls (3 sets x 12 reps @ 18kg DBs)'] },
                { day: 'Day 3', focus: 'Legs Performance', exercises: ['Barbell Back Squats (4 sets x 6 reps @ 110kg)', 'Romanian Deadlifts (4 sets x 8 reps @ 100kg)', 'Bulgarian Split Squats (3 sets x 10 reps/side @ 24kg DBs)'] }
              ];
            } else {
              days = [
                { day: 'Mon (Upper)', focus: 'Strength / Hypertrophy A', exercises: ['Barbell Bench Press (4 sets x 6 reps @ 60kg)', 'Barbell Bent Rows (4 sets x 8 reps @ 50kg)', 'Incline DB Flyes (3 sets x 12 reps @ 14kg DBs)'] },
                { day: 'Tue (Lower)', focus: 'Skeletal Strength A', exercises: ['Barbell Back Squats (4 sets x 6 reps @ 80kg)', 'Romanian Deadlifts (3 sets x 8 reps @ 70kg)', 'Seated Calf Raises (4 sets x 15 reps @ 30kg)'] },
                { day: 'Thu (Upper B)', focus: 'Hypertrophy B', exercises: ['Overhead Press (OHP) (4 sets x 6 reps @ 40kg)', 'Wide Grip Pullups (4 sets x 8 reps)', 'DB Hammer Curls (3 sets x 12 reps @ 14kg DBs)'] }
              ];
            }
          }

          let txt = `FITNOVA SYSTEM PROTOCOL: ${routineTitle.toUpperCase()}\\n`;
          txt += `ENVIRONMENT: ${location} | LEVEL: ${level} | INJURIES: ${injuries}\\n\\n`;
          
          days.forEach(d => {
            txt += `--- ${d.day.toUpperCase()}: ${d.focus.toUpperCase()} ---\\n`;
            d.exercises.forEach(ex => {
              let exName = ex;
              if (injuries.toLowerCase().includes('knee') && ex.includes('Back Squats')) {
                exName = "Box Squats (Knee-Safe - sitting back completely)";
              } else if (injuries.toLowerCase().includes('back') && (ex.includes('Deadlift') || ex.includes('Back Squats'))) {
                exName = ex.includes('Deadlift') ? "Chest-Supported DB Rows (Spine-Safe)" : "Goblet Squats (Spine-Safe - torso strictly upright)";
              } else if (injuries.toLowerCase().includes('shoulder') && (ex.includes('Bench Press') || ex.includes('OHP') || ex.includes('Overhead'))) {
                exName = "Neutral DB Press (Shoulder-Safe)";
              }
              txt += `  * ${exName}\\n`;
            });
            txt += `\\n`;
          });
          
          txt += `CORE INSTRUCTIONS:\\n`;
          txt += `1. Warmup dynamically for 8-10 minutes prior to physical strain vectors.\\n`;
          txt += `2. Focus heavily on eccentric tempo (3s lowering phase) to maximize tension limits.\\n`;
          if (injuries !== 'None') {
            txt += `3. CRITICAL: Injury safeguard is enabled for: ${injuries}. Never lift to mechanical form failure.\\n`;
          }
          return txt;
        } else if (type === 'diet') {
          let meals = [];
          if (diet.includes('High Protein')) {
            meals = [
              { label: 'Breakfast', base: '5 egg whites, 1 whole egg scrambled in olive oil with fresh spinach' },
              { label: 'Lunch', base: '180g lean chicken breast grilled with 150g quinoa & fresh steamed broccoli' },
              { label: 'Snack', base: '200g low fat unsweetened Greek yogurt topped with blueberries' },
              { label: 'Dinner', base: '180g grilled sea bass filet with 150g sweet potato & green asparagus' }
            ];
          } else if (diet.includes('Vegetarian')) {
            meals = [
              { label: 'Breakfast', base: 'Moong dal chillas (2) with low-fat paneer stuffing & fresh curd' },
              { label: 'Lunch', base: '120g low-fat paneer cooked in light tomato-spinach gravy + 120g brown rice' },
              { label: 'Snack', base: 'Whey protein isolate shake with 40g rolled oats & almond milk' },
              { label: 'Dinner', base: '1.5 cups yellow daal tadka with sautéed broccoli salad & 1 multigrain roti' }
            ];
          } else if (diet.includes('Vegan')) {
            meals = [
              { label: 'Breakfast', base: 'High-Density Tofu scramble (150g) with spinach, bell peppers & avocado' },
              { label: 'Lunch', base: 'Tempeh power bowl with 120g organic quinoa, black beans & organic tahini' },
              { label: 'Snack', base: 'Pea & rice vegan protein shake with a medium banana & raw pumpkin seeds' },
              { label: 'Dinner', base: 'Red lentil and chickpea curry with 120g brown rice & raw cucumber salad' }
            ];
          } else if (diet.includes('Keto')) {
            meals = [
              { label: 'Breakfast', base: '3 eggs scrambled in grass-fed butter with organic avocado slices' },
              { label: 'Lunch', base: '180g pan-seared salmon served over walnut green salad dressed in olive oil' },
              { label: 'Snack', base: '2 tbsp raw unsweetened almond butter or organic macadamia nuts' },
              { label: 'Dinner', base: '180g ribeye steak seared in butter served with buttered asparagus' }
            ];
          } else if (diet.includes('Indian')) {
            meals = [
              { label: 'Breakfast', base: 'Moong dal chilla with 100g low-fat paneer bhurji & skimmed curd bowl' },
              { label: 'Lunch', base: 'Grilled chicken tikka (150g) served with yellow tadka dal & brown rice' },
              { label: 'Snack', base: 'Double scoop whey isolate shake served with 50g roasted chana' },
              { label: 'Dinner', base: 'Soya granules curry (100g chunks) served with 2 whole wheat rotis & cucumber' }
            ];
          } else {
            meals = [
              { label: 'Breakfast', base: 'Oatmeal (50g) cooked in skimmed milk, mixed with 1 scoop whey isolate' },
              { label: 'Lunch', base: ' turkey wrap with whole-wheat tortilla, fresh lettuce & light mayonnaise' },
              { label: 'Snack', base: '200g Greek yogurt with 15g raw almonds and organic honey drizzle' },
              { label: 'Dinner', base: '150g baked salmon filet with sweet potato (120g) & roasted broccoli' }
            ];
          }

          let txt = `FITNOVA SYSTEM DIETARY PROTOCOL: ${diet.toUpperCase()}\\n`;
          txt += `METABOLIC TARGETS: ${calcs.targetCalories} KCALS | PROTEIN: ${calcs.targetProtein}G | DIET STYLE: ${diet}\\n\\n`;
          
          meals.forEach(m => {
            txt += `--- ${m.label.toUpperCase()} ---\\n`;
            txt += `  * Recipe: ${m.base}\\n\\n`;
          });
          txt += `CORE GUIDELINES FOR METABOLIC PHYSICAL ABSORPTION:\\n`;
          txt += `1. Drink exactly 350ml of room temperature water 30 minutes before major meals to optimize gastric enzymes.\\n`;
          txt += `2. Ensure all protein vectors are prepped in advance to maximize compliance.\\n`;
          return txt;
        } else {
          let phaseTitle1 = goal === 'shred' ? "Adaptive Glycogen Flush" : goal === 'bulk' ? "Myofibrillar Hypertrophy" : "Neural Re-composition";
          let phaseTitle2 = goal === 'shred' ? "Lipid Lipolysis Overdrive" : goal === 'bulk' ? "Glycogen Loading Spline" : "Intramuscular Re-alignment";
          let phaseTitle3 = goal === 'shred' ? "Subcutaneous Tightening" : goal === 'bulk' ? "Myonuclear Domain Expansion" : "Peak Anabolic Compression";

          let txt = `FITNOVA 12-WEEK PHYSIOLOGY ROADMAP\\n`;
          txt += `ATHLETE TARGET: ${goal.toUpperCase()} | BASAL WEIGHT: ${startW} KG | EXPERIENCE: ${level}\\n\\n`;
          txt += `--- TRANSFORMATION BLOCK ARCHITECTURE ---\\n`;
          txt += `* PHASE 1 (Weeks 1-4): ${phaseTitle1}\\n`;
          txt += `  Objective: Flush neural systems, reset metabolic adaptation parameters.\\n\\n`;
          txt += `* PHASE 2 (Weeks 5-8): ${phaseTitle2}\\n`;
          txt += `  Objective: Target localized adipose vectors or escalate myofibrillar loading.\\n\\n`;
          txt += `* PHASE 3 (Weeks 9-12): ${phaseTitle3}\\n`;
          txt += `  Objective: Tighten subcutaneous borders, establish peak muscular conditioning.\\n\\n`;
          return txt;
        }
      };"""

if target_marker in code:
    code = code.replace(target_marker, replacement_marker)
    print("compilePdfContentText helper successfully injected.")
else:
    print("ERROR: target_marker not found.")

# 2. Patch handleSendMessage to intercept "pdf" or "download" queries and trigger compilation immediately
print("Patching handleSendMessage text query PDF intercept triggers...")

target_pdf_trigger = """            } else {
              const response = getAdaptiveBotResponse(textToSend, profile);
              botText = response.text;
              activeVisualType = response.visualType || null;
            }"""

replacement_pdf_trigger = """            } else {
              const response = getAdaptiveBotResponse(textToSend, profile);
              botText = response.text;
              activeVisualType = response.visualType || null;
            }

            // AUTO-PDF DIRECT DOWNLOAD INTERCEPT
            const lowerQuery = textToSend.toLowerCase();
            if (lowerQuery.includes('pdf') || lowerQuery.includes('download')) {
              let triggerPdfType = null;
              if (lowerQuery.includes('workout') || lowerQuery.includes('training') || lowerQuery.includes('split') || lowerQuery.includes('exercise')) {
                triggerPdfType = 'workout';
              } else if (lowerQuery.includes('diet') || lowerQuery.includes('meal') || lowerQuery.includes('food') || lowerQuery.includes('nutrition')) {
                triggerPdfType = 'diet';
              } else if (lowerQuery.includes('recovery') || lowerQuery.includes('roadmap') || lowerQuery.includes('transformation') || lowerQuery.includes('calories') || lowerQuery.includes('recomp')) {
                triggerPdfType = 'roadmap';
              } else {
                // Default fallback to overall transformation roadmap
                triggerPdfType = 'roadmap';
              }

              if (triggerPdfType) {
                console.log("Direct PDF request intercepted. Compiling document for type: ", triggerPdfType);
                botText = `Understood, champion. I have successfully intercepted your direct file request. I am compiling your hyper-personalized **${triggerPdfType.toUpperCase()} PDF** report and initiating the download in your browser immediately!\\n\\nLet's keep executing with discipline, champion.`;
                activeVisualType = triggerPdfType;
                
                // Trigger client-side PDF document download
                setTimeout(() => {
                  try {
                    const generatedText = compilePdfContentText(triggerPdfType, profile);
                    generateRealPDF(triggerPdfType, generatedText, profile);
                    playBeep(1200, 'sine', 0.1);
                  } catch (e) {
                    console.error("Direct PDF compile failure:", e);
                  }
                }, 1000);
              }
            }"""

if target_pdf_trigger in code:
    code = code.replace(target_pdf_trigger, replacement_pdf_trigger)
    print("Auto-PDF download triggers successfully integrated.")
else:
    print("ERROR: target_pdf_trigger not found.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("PDF asking patch complete.")
