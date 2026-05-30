import re

filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Inject jsPDF CDN import
print("Patching jsPDF CDN import...")
target_cdn = '<script src="https://unpkg.com/lucide@latest" crossorigin></script>'
replacement_cdn = '''<script src="https://unpkg.com/lucide@latest" crossorigin></script>
    <!-- jsPDF UMD CDN for real client-side PDF generation -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>'''

if target_cdn in code:
    code = code.replace(target_cdn, replacement_cdn)
    print("jsPDF CDN successfully injected.")
else:
    print("ERROR: target_cdn not found in code.")

# 2. Inject React visual card components and generateRealPDF core
print("Injecting custom React Visual Card components and PDF generator...")
target_react_start = 'const { useState, useEffect, useRef } = React;'

custom_components = '''const { useState, useEffect, useRef } = React;

      // ==========================================
      // FITNOVA AI — CORE REAL PDF GENERATOR UTILITY
      // ==========================================
      const generateRealPDF = (type, content, profile) => {
        try {
          const { jsPDF } = window.jspdf;
          const doc = new jsPDF({
            orientation: 'portrait',
            unit: 'mm',
            format: 'a4'
          });

          const primaryColor = [0, 210, 255]; // Electric Blue
          const secondaryColor = [157, 0, 255]; // Neon Purple
          const darkBg = [18, 18, 18]; // Charcoal Accent
          const textColor = [55, 65, 81]; // Gray Slate Text
          const lightGray = [244, 245, 247]; // Off-White Panel

          // --- Elegant Header Banner ---
          doc.setFillColor(...darkBg);
          doc.rect(0, 0, 210, 36, 'F');

          // Gradient accents below header
          doc.setFillColor(...primaryColor);
          doc.rect(0, 36, 105, 1.5, 'F');
          doc.setFillColor(...secondaryColor);
          doc.rect(105, 36, 105, 1.5, 'F');

          // Header branding
          doc.setTextColor(255, 255, 255);
          doc.setFont("helvetica", "bold");
          doc.setFontSize(22);
          doc.text("FITNOVA AI", 15, 18);

          doc.setFontSize(8.5);
          doc.setFont("helvetica", "normal");
          doc.setTextColor(160, 160, 160);
          doc.text("HYPER-PERSONALIZED HUMAN METABOLIC & PHYSIOLOGY SYSTEM", 15, 26);

          doc.setFontSize(9.5);
          doc.setFont("helvetica", "bold");
          doc.setTextColor(...primaryColor);
          doc.text("COACH NOVA (NSCA-CSCS)", 136, 18);
          doc.setFontSize(7.5);
          doc.setTextColor(140, 140, 140);
          doc.setFont("helvetica", "normal");
          doc.text("SPORTS NUTRITION & EXERCISE PHYSIOLOGY CERTIFIED", 136, 24);
          doc.text(`SYSTEM PROTOCOL ID: FN-${Math.floor(100000 + Math.random() * 900000)}`, 136, 29);

          // --- Athlete Bio-Telemetry Matrix ---
          doc.setFillColor(...lightGray);
          doc.roundedRect(15, 43, 180, 36, 3, 3, 'F');

          doc.setFont("helvetica", "bold");
          doc.setFontSize(10);
          doc.setTextColor(...darkBg);
          doc.text("ATHLETE BIO-COORDINATES", 20, 49);

          doc.setFontSize(8.5);
          doc.setFont("helvetica", "normal");
          doc.setTextColor(80, 80, 80);

          const goalStr = profile.goal === 'bulk' ? 'Muscle Gain' : profile.goal === 'shred' ? 'Fat Loss' : profile.goal === 'recomp' ? 'Body Recomp' : (profile.goal || 'Fitness Optimization');
          const levelStr = profile.level || 'Intermediate';
          const dietStr = profile.diet || 'Balanced';
          const injuryStr = profile.injuries || 'None';

          // Grid coordinates
          doc.text(`Athlete: ${profile.name || 'Champion'}`, 20, 56);
          doc.text(`Primary Goal: ${goalStr}`, 20, 62);
          doc.text(`Training Level: ${levelStr}`, 20, 68);

          doc.text(`Dietary Protocol: ${dietStr}`, 85, 56);
          doc.text(`Active Injuries: ${injuryStr}`, 85, 62);
          doc.text(`Environment: ${profile.location || 'Gym'}`, 85, 68);

          const calcs = profile.calculations || { targetCalories: 2200, targetProtein: 140, targetCarbs: 220, targetFats: 73, bmr: 1650, tdee: 2450 };
          doc.text(`Calorie Target: ${calcs.targetCalories} kcal/day`, 142, 56);
          doc.text(`Protein Target: ${calcs.targetProtein}g/day`, 142, 62);
          doc.text(`Active Split: ${profile.schedule || '4 Days/Week'}`, 142, 68);

          // Divider Line
          doc.setDrawColor(210, 214, 220);
          doc.setLineWidth(0.3);
          doc.line(15, 84, 195, 84);

          // --- Main Content Assembly ---
          let yPos = 92;
          
          doc.setFont("helvetica", "bold");
          doc.setFontSize(11.5);
          doc.setTextColor(...darkBg);
          
          if (type === 'workout') {
            doc.text("WEEKLY OVERLOAD STRENGTH & HYPERTROPHY PROTOCOL", 15, yPos);
          } else if (type === 'diet') {
            doc.text("HYPER-TARGETED MACRO & DIET COMPOSITION PLAN", 15, yPos);
          } else {
            doc.text("METABOLIC TRANSFORMATIONAL ROADMAP & RECOVERY GUIDELINE", 15, yPos);
          }
          yPos += 8;

          doc.setFont("helvetica", "normal");
          doc.setFontSize(8.5);
          doc.setTextColor(...textColor);

          const lines = content.split('\\n');
          lines.forEach(line => {
            if (line.trim()) {
              const cleanedLine = line.replace(/\\*\\*/g, "").replace(/\\*/g, "").trim();
              
              // Formatting rules based on headers
              if (line.includes('Day ') || line.includes('Mon ') || line.includes('Tue ') || line.includes('Wed ') || line.includes('Thu ') || line.includes('Fri ') || line.includes('Sat ') || line.includes('Sun ') || line.startsWith('**') || line.startsWith('-') || line.includes('Meal ') || line.startsWith('1.') || line.startsWith('2.') || line.startsWith('3.') || line.startsWith('4.')) {
                doc.setFont("helvetica", "bold");
                doc.setTextColor(type === 'diet' ? secondaryColor[0] : primaryColor[0], type === 'diet' ? secondaryColor[1] : primaryColor[1], type === 'diet' ? secondaryColor[2] : primaryColor[2]);
                yPos += 2.5;
              } else {
                doc.setFont("helvetica", "normal");
                doc.setTextColor(...textColor);
              }

              const splitText = doc.splitTextToSize(cleanedLine, 180);
              splitText.forEach(t => {
                if (yPos > 272) {
                  doc.addPage();
                  // Redraw dark header elements inside new pages
                  doc.setFillColor(...darkBg);
                  doc.rect(0, 0, 210, 16, 'F');
                  doc.setTextColor(255, 255, 255);
                  doc.setFont("helvetica", "bold");
                  doc.setFontSize(10);
                  doc.text("FITNOVA AI — CORE ADAPTIVE Blueprints", 15, 10);
                  yPos = 24;
                }
                doc.text(t, 15, yPos);
                yPos += 5.5;
              });
            }
          });

          // --- Premium Footer ---
          if (yPos > 260) {
            doc.addPage();
            doc.setFillColor(...darkBg);
            doc.rect(0, 0, 210, 16, 'F');
            doc.setTextColor(255, 255, 255);
            doc.setFont("helvetica", "bold");
            doc.setFontSize(10);
            doc.text("FITNOVA AI — CORE ADAPTIVE Blueprints", 15, 10);
            yPos = 24;
          }

          doc.setDrawColor(210, 214, 220);
          doc.line(15, 274, 195, 274);

          doc.setFontSize(7.5);
          doc.setFont("helvetica", "bold");
          doc.setTextColor(...primaryColor);
          doc.text("DISCIPLINE IS THE ONLY CURRENCY OF RESULTS.", 15, 281);
          doc.setFont("helvetica", "normal");
          doc.setTextColor(140, 140, 140);
          doc.text("FORM FIRST. INTENSITY SECOND. CONSISTENCY ALWAYS.", 15, 285);
          doc.text("SECURE SYSTEM GENERATED ENCRYPTED PROTOCOL PDF.", 120, 285);

          doc.save(`FitNova_Premium_${type.toUpperCase()}_Protocol.pdf`);
          return true;
        } catch (err) {
          console.error("PDF compilation error:", err);
          alert("Error generating PDF: " + err.message);
          return false;
        }
      };

      // ==========================================
      // SUB-COMPONENT: INTERACTIVE WORKOUT CARD
      // ==========================================
      const InteractiveWorkoutCard = ({ profile }) => {
        const [overload, setOverload] = useState(0);
        const [showProTips, setShowProTips] = useState(false);
        const [pdfStatus, setPdfStatus] = useState('idle'); // 'idle', 'generating', 'success'

        const level = profile.level || 'Intermediate';
        const location = profile.location || 'Gym';
        const injuries = profile.injuries || 'None';

        // Generate tailored workout matrix based on user profile
        let routineTitle = "";
        let days = [];

        if (location === 'Home') {
          routineTitle = `${level} Progressive Home Calisthenics`;
          if (level === 'Beginner') {
            days = [
              { day: 'Day 1', focus: 'Full Body A', exercises: [{ name: 'Bodyweight Squats', reps: '15 reps', sets: 3, load: 'Bodyweight' }, { name: 'Incline Pushups (Couch)', reps: '10 reps', sets: 3, load: 'Bodyweight' }, { name: 'Doorframe Towel Pulls', reps: '12 reps', sets: 3, load: 'Bodyweight' }] },
              { day: 'Day 2', focus: 'Recovery Focus', exercises: [{ name: 'Dynamic Joint Mobility', reps: '10 min', sets: 1, load: 'Mobility' }, { name: 'Core Plank Hold', reps: '30s hold', sets: 3, load: 'Statics' }] },
              { day: 'Day 3', focus: 'Full Body B', exercises: [{ name: 'Glute Bridges', reps: '15 reps', sets: 3, load: 'Bodyweight' }, { name: 'Chair Dips (Modified)', reps: '8 reps', sets: 3, load: 'Bodyweight' }, { name: 'Backpack Rows (Light)', reps: '10 reps', sets: 3, load: '5kg' }] }
            ];
          } else if (level === 'Advanced') {
            days = [
              { day: 'Day 1', focus: 'Push Focus', exercises: [{ name: 'Decline Archer Pushups', reps: '12 reps', sets: 4, load: 'Bodyweight' }, { name: 'Handstand Wall Press', reps: '8 reps', sets: 4, load: 'Bodyweight' }, { name: 'Chair Dips (Weighted)', reps: '15 reps', sets: 3, load: '+10kg pack' }] },
              { day: 'Day 2', focus: 'Pull Focus', exercises: [{ name: 'Pullups (Strict)', reps: '10 reps', sets: 4, load: 'Bodyweight' }, { name: 'Single-Arm Backpack Rows', reps: '12 reps', sets: 4, load: '20kg' }, { name: 'Towel Bicep Hammer Curls', reps: '15 reps', sets: 3, load: 'Tension' }] },
              { day: 'Day 3', focus: 'Legs / Core', exercises: [{ name: 'Pistol Squats (Strict)', reps: '6 reps/side', sets: 4, load: 'Bodyweight' }, { name: 'Bulgarian Split Squats', reps: '12 reps/side', sets: 3, load: '20kg Pack' }, { name: 'L-Sit Chair Holds', reps: '20s hold', sets: 3, load: 'Core' }] }
            ];
          } else {
            // Intermediate
            days = [
              { day: 'Day 1', focus: 'Upper Body Split', exercises: [{ name: 'Regular Pushups', reps: '15 reps', sets: 4, load: 'Bodyweight' }, { name: 'Backpack Rows (Medium)', reps: '12 reps', sets: 4, load: '12kg' }, { name: 'Band/Towel Facepulls', reps: '15 reps', sets: 3, load: 'Tension' }] },
              { day: 'Day 2', focus: 'Lower Body / Abs', exercises: [{ name: 'Bulgarian Split Squats', reps: '12 reps/side', sets: 4, load: 'Bodyweight' }, { name: 'Single-Leg Calf Raises', reps: '15 reps', sets: 3, load: 'Bodyweight' }, { name: 'Plank Knee-to-Elbows', reps: '45s hold', sets: 3, load: 'Core' }] }
            ];
          }
        } else {
          // Gym
          routineTitle = `${level} Compound Strength Engine`;
          if (level === 'Beginner') {
            days = [
              { day: 'Day 1', focus: 'Full Body Compounds', exercises: [{ name: 'Barbell Squats', reps: '8 reps', sets: 3, load: '40kg' }, { name: 'Barbell Bench Press', reps: '8 reps', sets: 3, load: '30kg' }, { name: 'Lat Pulldowns', reps: '10 reps', sets: 3, load: '35kg' }] },
              { day: 'Day 2', focus: 'Rest / Light Core', exercises: [{ name: 'Hanging Leg Raises', reps: '12 reps', sets: 3, load: 'Bodyweight' }, { name: 'Fasted LISS Cardio', reps: '30 min walk', sets: 1, load: 'Cardio' }] },
              { day: 'Day 3', focus: 'Posterior & Pulls', exercises: [{ name: 'Romanian Deadlifts', reps: '10 reps', sets: 3, load: '45kg' }, { name: 'Seated Cable Rows', reps: '10 reps', sets: 3, load: '40kg' }, { name: 'Overhead DB Press', reps: '10 reps', sets: 3, load: '10kg DBs' }] }
            ];
          } else if (level === 'Advanced') {
            days = [
              { day: 'Day 1', focus: 'Push Hypertrophy', exercises: [{ name: 'Incline Barbell Bench', reps: '8 reps', sets: 4, load: '80kg' }, { name: 'Flat DB Chest Press', reps: '10 reps', sets: 3, load: '34kg DBs' }, { name: 'Cable Overhead Triceps', reps: '12 reps', sets: 3, load: '25kg' }] },
              { day: 'Day 2', focus: 'Pull Hypertrophy', exercises: [{ name: 'Weighted Pullups', reps: '6 reps', sets: 4, load: '+15kg' }, { name: 'Barbell Bent-Over Rows', reps: '8 reps', sets: 4, load: '85kg' }, { name: 'Hammer Dumbbell Curls', reps: '12 reps', sets: 3, load: '18kg DBs' }] },
              { day: 'Day 3', focus: 'Legs Performance', exercises: [{ name: 'Barbell Back Squats', reps: '6 reps', sets: 4, load: '110kg' }, { name: 'Romanian Deadlifts', reps: '8 reps', sets: 4, load: '100kg' }, { name: 'Bulgarian Split Squats', reps: '10 reps/side', sets: 3, load: '24kg DBs' }] }
            ];
          } else {
            // Intermediate
            days = [
              { day: 'Mon (Upper)', focus: 'Strength / Hypertrophy A', exercises: [{ name: 'Barbell Bench Press', reps: '6 reps', sets: 4, load: '60kg' }, { name: 'Barbell Bent Rows', reps: '8 reps', sets: 4, load: '50kg' }, { name: 'Incline Dumbbell Flyes', reps: '12 reps', sets: 3, load: '14kg DBs' }] },
              { day: 'Tue (Lower)', focus: 'Skeletal Strength A', exercises: [{ name: 'Barbell Back Squats', reps: '6 reps', sets: 4, load: '80kg' }, { name: 'Romanian Deadlifts', reps: '8 reps', sets: 3, load: '70kg' }, { name: 'Seated Calf Raises', reps: '15 reps', sets: 4, load: '30kg' }] },
              { day: 'Thu (Upper B)', focus: 'Hypertrophy B', exercises: [{ name: 'Overhead Press (OHP)', reps: '6 reps', sets: 4, load: '40kg' }, { name: 'Wide Grip Pullups', reps: '8 reps', sets: 4, load: 'Bodyweight' }, { name: 'Dumbbell Hammer Curls', reps: '12 reps', sets: 3, load: '14kg DBs' }] }
            ];
          }
        }

        // Apply injury overrides to exercises in workout card dynamically
        const processedDays = days.map(d => {
          return {
            ...d,
            exercises: d.exercises.map(ex => {
              let name = ex.name;
              let load = ex.load;
              let isOverriden = false;

              if (injuries.toLowerCase().includes('knee') && name.includes('Back Squats')) {
                name = "Box Squats (Knee-Safe)";
                load = "Light " + load;
                isOverriden = true;
              } else if (injuries.toLowerCase().includes('back') && (name.includes('Deadlift') || name.includes('Back Squats'))) {
                name = name.includes('Deadlift') ? "Chest-Supported DB Rows" : "Goblet Squats (Spine-Safe)";
                load = "Lightweight";
                isOverriden = true;
              } else if (injuries.toLowerCase().includes('shoulder') && (name.includes('Bench Press') || name.includes('OHP') || name.includes('Overhead'))) {
                name = "Neutral DB Press (Shoulder-Safe)";
                load = "DBs (10-15% lower)";
                isOverriden = true;
              }

              // Calculate overload multiplier
              let finalLoad = load;
              if (overload > 0 && !load.includes('Bodyweight') && !load.includes('Tension') && !load.includes('Cardio')) {
                const matchNum = load.match(/\\d+/);
                if (matchNum) {
                  const val = parseFloat(matchNum[0]);
                  const newVal = Math.round(val * (1 + overload / 100));
                  finalLoad = load.replace(matchNum[0], newVal.toString());
                }
              }

              return { ...ex, name, load: finalLoad, isOverriden };
            })
          };
        });

        // Trigger real PDF compile
        const handlePdfDownload = () => {
          setPdfStatus('generating');
          
          let pdfContent = `FITNOVA SYSTEM PROTOCOL: ${routineTitle.toUpperCase()}\\n`;
          pdfContent += `ENVIRONMENT: ${location} | LEVEL: ${level} | INJURIES: ${injuries}\\n\\n`;
          
          processedDays.forEach(d => {
            pdfContent += `--- ${d.day.toUpperCase()}: ${d.focus.toUpperCase()} ---\\n`;
            d.exercises.forEach(ex => {
              const ov = ex.isOverriden ? " [INJURY LIMIT SAFETY OVERRIDE ACTIVE]" : "";
              pdfContent += `  * ${ex.name} - ${ex.sets} sets x ${ex.reps} @ ${ex.load}${ov}\\n`;
            });
            pdfContent += `\\n`;
          });

          pdfContent += `CORE INSTRUCTIONS:\\n`;
          pdfContent += `1. Warmup dynamically for 8-10 minutes prior to physical strain vectors.\\n`;
          pdfContent += `2. Focus heavily on eccentric tempo (3s lowering phase) to maximize tension limits.\\n`;
          if (injuries !== 'None') {
            pdfContent += `3. CRITICAL: Injury safeguard is enabled for: ${injuries}. Never lift to mechanical form failure.\\n`;
          }

          setTimeout(() => {
            const success = generateRealPDF('workout', pdfContent, profile);
            if (success) {
              setPdfStatus('success');
              // Play a quick beep
              try { playBeep(1200, 'sine', 0.1); } catch (e) {}
              setTimeout(() => setPdfStatus('idle'), 2500);
            } else {
              setPdfStatus('idle');
            }
          }, 1200);
        };

        return (
          <div className="mt-3 p-4 bg-[#121215]/80 border border-white/5 rounded-2xl relative overflow-hidden select-none hover:border-[#00D2FF]/20 transition-all font-sans text-left">
            <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold tracking-wider text-[#00F0FF] bg-[#00F0FF]/10 border-b border-l border-white/5 uppercase rounded-bl font-mono">
              DYNAMIC SCHEDULE
            </div>

            <div className="flex items-center gap-2 mb-3">
              <i className="lucide-calendar text-[#00D2FF] w-4 h-4"></i>
              <div>
                <h4 className="text-[12px] font-bold text-white font-outfit">{routineTitle}</h4>
                <p className="text-[9px] text-gray-500 font-semibold uppercase font-mono mt-0.5">calibrated to {level} level</p>
              </div>
            </div>

            <div className="flex flex-col gap-3.5 mb-4">
              {processedDays.map((d, dIdx) => (
                <div key={dIdx} className="bg-white/[0.01] border border-white/5 p-2.5 rounded-xl">
                  <div className="flex items-center justify-between mb-1.5 border-b border-white/5 pb-1">
                    <span className="text-[9px] font-bold text-[#00D2FF] uppercase font-mono">{d.day}</span>
                    <span className="text-[9px] font-bold text-white font-outfit">{d.focus}</span>
                  </div>
                  <div className="flex flex-col gap-1">
                    {d.exercises.map((ex, eIdx) => (
                      <div key={eIdx} className="flex justify-between items-center text-[10px] py-0.5 font-mono">
                        <span className="text-gray-300 flex items-center gap-1">
                          {ex.name}
                          {ex.isOverriden && (
                            <span className="text-[7px] bg-amber-500/10 text-amber-500 border border-amber-500/20 px-1 rounded uppercase font-sans font-bold">Safe</span>
                          )}
                        </span>
                        <span className="text-gray-400 font-bold shrink-0">
                          {ex.sets}x{ex.reps} @ <span className="text-[#9D00FF] font-black">{ex.load}</span>
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>

            {showProTips && (
              <div className="bg-white/5 border border-white/5 p-2.5 rounded-xl mb-4 text-[9px] text-gray-400 leading-normal animate-bubble-appear font-sans">
                <span className="text-[#00F0FF] font-bold uppercase tracking-wider block mb-1">PRO COACHING DIRECTIVES</span>
                * RPE Target: 8-9 (Keep 1-2 reps in reserve, never train to structural mechanical failure).<br />
                * Eccentric Phase: Take exactly 3 seconds to lower the weight. Explode upwards.<br />
                * Intra-set recovery: Rest for exactly 90-120 seconds between compound movements.
              </div>
            )}

            <div className="flex flex-wrap items-center justify-between gap-2.5 pt-2.5 border-t border-white/5">
              <div className="flex gap-2">
                <button
                  type="button"
                  onClick={() => {
                    setOverload(prev => (prev === 0 ? 5 : prev === 5 ? 10 : 0));
                    try { playBeep(800, 'sine', 0.05); } catch(e) {}
                  }}
                  className={`text-[9px] font-bold uppercase tracking-wider px-2.5 py-1.5 rounded-lg border transition-all cursor-pointer ${
                    overload > 0 
                      ? 'bg-[#9D00FF]/25 border-[#9D00FF]/40 text-white shadow-[0_0_10px_rgba(157,0,255,0.25)]' 
                      : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'
                  }`}
                >
                  <i className="lucide-trending-up w-2.5 h-2.5 inline-block mr-1"></i>
                  {overload > 0 ? `Overload +${overload}%` : "Apply Overload"}
                </button>

                <button
                  type="button"
                  onClick={() => {
                    setShowProTips(prev => !prev);
                    try { playBeep(800, 'sine', 0.05); } catch(e) {}
                  }}
                  className={`text-[9px] font-bold uppercase tracking-wider px-2.5 py-1.5 rounded-lg border transition-all cursor-pointer ${
                    showProTips ? 'bg-[#00F0FF]/10 border-[#00F0FF]/30 text-[#00F0FF]' : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'
                  }`}
                >
                  <i className="lucide-sparkles w-2.5 h-2.5 inline-block mr-1"></i>
                  Tips
                </button>
              </div>

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

      // ==========================================
      // SUB-COMPONENT: INTERACTIVE DIET CARD
      // ==========================================
      const InteractiveDietCard = ({ profile }) => {
        const [activeMealTab, setActiveMealTab] = useState(0);
        const [alternativeSwap, setAlternativeSwap] = useState(false);
        const [pdfStatus, setPdfStatus] = useState('idle');

        const diet = profile.diet || 'Balanced';
        const calcs = profile.calculations || { targetCalories: 2200, targetProtein: 140, targetCarbs: 220, targetFats: 73 };

        // Tailor meals based on diet style
        let meals = [];
        if (diet.includes('High Protein')) {
          meals = [
            { label: 'Breakfast', name: 'Egg White Scramble', base: '5 egg whites, 1 whole egg, spinach, cooking olive oil', alt: 'Double Scoop Whey Protein Shake + 40g oats with water', macros: { p: 32, c: 5, f: 6, cal: 200 } },
            { label: 'Lunch', name: 'Seared Chicken Breast', base: '180g lean chicken breast with 150g quinoa & broccoli', alt: '180g Extra Lean Beef Patty with 150g brown rice & mixed greens', macros: { p: 48, c: 35, f: 8, cal: 400 } },
            { label: 'Snack', name: 'Greek Yogurt Combo', base: '200g low fat unsweetened Greek yogurt with blueberries', alt: '1 Can of light tuna in water on 2 multigrain crispbreads', macros: { p: 20, c: 12, f: 2, cal: 150 } },
            { label: 'Dinner', name: 'Grilled Sea Bass Filet', base: '180g sea bass with 150g baked sweet potato & asparagus', alt: '180g Turkey breast mince cooked in coconut oil with baby spinach', macros: { p: 38, c: 32, f: 9, cal: 360 } }
          ];
        } else if (diet.includes('Vegetarian')) {
          meals = [
            { label: 'Breakfast', name: 'Moong Dal Chilla', base: '2 chillas with 100g low-fat paneer stuffing & green chutney', alt: '150g scrambled Tofu cooked with bell peppers, mushrooms & toast', macros: { p: 24, c: 30, f: 9, cal: 300 } },
            { label: 'Lunch', name: 'High-Protein Paneer Curry', base: '120g low-fat paneer cooked in light gravy + 120g brown rice', alt: 'Soya bhurji curry (120g soya chunks) with 2 whole wheat rotis', macros: { p: 32, c: 45, f: 12, cal: 420 } },
            { label: 'Snack', name: 'Whey Oats Shake', base: '1 scoop gold standard whey with 40g dry oats & almond milk', alt: '200g Roasted chickpeas (Chana) seasoned with light pink salt', macros: { p: 28, c: 26, f: 5, cal: 260 } },
            { label: 'Dinner', name: 'High-Fiber Lentil Bowl', base: '1.5 cups yellow daal tadka with broccoli salad & 1 roti', alt: '1.5 cups thick black bean chilli cooked with 100g grilled tofu', macros: { p: 22, c: 38, f: 6, cal: 290 } }
          ];
        } else if (diet.includes('Vegan')) {
          meals = [
            { label: 'Breakfast', name: 'High-Density Tofu Scramble', base: '150g firm organic tofu crumbled with nutritional yeast & spinach', alt: 'Pea & Rice vegan protein shake with a medium banana & flaxseeds', macros: { p: 22, c: 10, f: 8, cal: 200 } },
            { label: 'Lunch', name: 'Tempeh Power Bowl', base: '130g baked tempeh cubes with 120g quinoa and tahini dressing', alt: 'Spiced organic edamame bean salad (200g edamame) with bell peppers', macros: { p: 30, c: 40, f: 10, cal: 370 } },
            { label: 'Snack', name: 'Soya Chunks Stir Fry', base: '80g soya chunks boiled & pan seared with light soy sauce & broccoli', alt: '1 scoop plant protein isolate with a handful of raw pumpkin seeds', macros: { p: 32, c: 15, f: 4, cal: 220 } },
            { label: 'Dinner', name: 'Lentil & Chickpea Medley', base: '1.5 cups red lentil curry with 120g brown rice & raw cucumber', alt: 'Seitan stir fry (100g seitan strips) with snap peas and brown rice', macros: { p: 26, c: 50, f: 5, cal: 350 } }
          ];
        } else if (diet.includes('Keto')) {
          meals = [
            { label: 'Breakfast', name: 'Classic Butter Eggs', base: '3 eggs scrambled in grass-fed butter with avocado slices', alt: '3 slices sugar-free bacon with 2 poached eggs and sautéed mushrooms', macros: { p: 21, c: 3, f: 26, cal: 330 } },
            { label: 'Lunch', name: 'Salmon Walnut Greens', base: '180g pan-seared salmon over mixed greens, olive oil & walnuts', alt: '180g grilled chicken thighs with skin on, sautéed in garlic avocado oil', macros: { p: 38, c: 4, f: 28, cal: 420 } },
            { label: 'Snack', name: 'Almond Butter Spoonfuls', base: '2 tbsp raw unsweetened almond butter or organic macadamia nuts', alt: '1 scoop whey protein isolate mixed with 2 tbsp heavy double cream', macros: { p: 8, c: 5, f: 18, cal: 210 } },
            { label: 'Dinner', name: 'Ribeye Steak Broccoli', base: '180g Ribeye steak seared in coconut oil with buttered asparagus', alt: '180g seared pork chops with cauliflower mash (made with heavy cream)', macros: { p: 42, c: 5, f: 32, cal: 480 } }
          ];
        } else if (diet.includes('Indian')) {
          meals = [
            { label: 'Breakfast', name: 'Paneer Stuffed Chilla', base: 'Moong dal chilla with 100g paneer bhurji & curd bowl', alt: '3 egg whites, 1 whole egg scrambled with onions, served with a roti', macros: { p: 25, c: 28, f: 10, cal: 300 } },
            { label: 'Lunch', name: 'Chicken Tikka & Daal', base: '150g grilled chicken tikka with yellow tadka daal & cucumber salad', alt: '120g low-fat paneer tikka stir fry with a cup of yellow dal & sprouts', macros: { p: 38, c: 22, f: 7, cal: 300 } },
            { label: 'Snack', name: 'Double Scoop Isolate', base: 'Double scoop whey isolate mixed with water + 40g roasted chana', alt: 'Boiled egg bhurji (4 egg whites, 1 whole egg) with onion & tomato', macros: { p: 34, c: 14, f: 4, cal: 230 } },
            { label: 'Dinner', name: 'Soya Bhurji Curry', base: '100g soya granules curry with 2 whole wheat rotis & salad bowl', alt: '180g seared fish tikka with steamed cauliflower & 1 whole wheat roti', macros: { p: 35, c: 40, f: 8, cal: 370 } }
          ];
        } else {
          // Balanced
          meals = [
            { label: 'Breakfast', name: 'Protein Oatmeal', base: 'Oats (50g dry) cooked in water, mixed with 1 scoop whey isolate', alt: '3 egg whites, 1 whole egg omelette on 2 slices of whole wheat toast', macros: { p: 28, c: 35, f: 5, cal: 300 } },
            { label: 'Lunch', name: 'Turkey Breast Wrap', base: '150g roasted turkey breast in whole wheat tortilla with light mayonnaise', alt: '150g seared chicken breast with 150g white jasmine rice & salad', macros: { p: 32, c: 30, f: 6, cal: 300 } },
            { label: 'Snack', name: 'Greek Yogurt Crunch', base: '200g Greek yogurt with 15g raw almonds and organic honey drizzle', alt: '1 scoop whey protein isolate with a handful of raw pumpkin seeds', macros: { p: 22, c: 18, f: 7, cal: 220 } },
            { label: 'Dinner', name: 'Baked Salmon Filet', base: '150g baked salmon filet with sweet potato (120g) & broccoli spears', alt: '150g lean chicken breast cooked in olive oil with sweet potato mash', macros: { p: 34, c: 28, f: 11, cal: 350 } }
          ];
        }

        // Handle dynamically recalculated macro states
        const activeMeal = meals[activeMealTab];
        const displayFood = alternativeSwap ? activeMeal.alt : activeMeal.base;

        const totalMacros = meals.reduce((acc, m) => {
          return { p: acc.p + m.macros.p, c: acc.c + m.macros.c, f: acc.f + m.macros.f, cal: acc.cal + m.macros.cal };
        }, { p: 0, c: 0, f: 0, cal: 0 });

        const handlePdfDownload = () => {
          setPdfStatus('generating');
          
          let pdfContent = `FITNOVA SYSTEM DIETARY PROTOCOL: ${diet.toUpperCase()}\\n`;
          pdfContent += `METABOLIC TARGETS: ${calcs.targetCalories} KCALS | PROTEIN: ${calcs.targetProtein}G | DIET STYLE: ${diet}\\n\\n`;
          
          meals.forEach(m => {
            pdfContent += `--- ${m.label.toUpperCase()} (${m.macros.cal} kcal) ---\\n`;
            pdfContent += `  * Primary Recipe: ${m.base}\\n`;
            pdfContent += `  * Alternative Option: ${m.alt}\\n`;
            pdfContent += `  * Meal Macros: P: ${m.macros.p}g | C: ${m.macros.c}g | F: ${m.macros.f}g\\n\\n`;
          });

          pdfContent += `CORE GUIDELINES FOR METABOLIC ABSORPTION:\\n`;
          pdfContent += `1. Drink exactly 350ml of room temperature water 30 minutes before major meals to optimize gastric enzymes.\\n`;
          pdfContent += `2. Ensure all poultry, seafood, or paneer vectors are prepped 24 hours in advance to maximize dietary compliance.\\n`;
          pdfContent += `3. Track exact calories in the Fuel Console to ensure metabolic targets are fully registered.\\n`;

          setTimeout(() => {
            const success = generateRealPDF('diet', pdfContent, profile);
            if (success) {
              setPdfStatus('success');
              try { playBeep(1200, 'sine', 0.1); } catch (e) {}
              setTimeout(() => setPdfStatus('idle'), 2500);
            } else {
              setPdfStatus('idle');
            }
          }, 1200);
        };

        return (
          <div className="mt-3 p-4 bg-[#121215]/80 border border-white/5 rounded-2xl relative overflow-hidden select-none hover:border-[#9D00FF]/20 transition-all font-sans text-left">
            <div className="absolute top-0 right-0 p-1 px-2 text-[7px] font-bold tracking-wider text-[#9D00FF] bg-[#9D00FF]/10 border-b border-l border-white/5 uppercase rounded-bl font-mono">
              FUEL ARCHITECTURE
            </div>

            <div className="flex items-center gap-2 mb-3.5">
              <i className="lucide-apple text-[#9D00FF] w-4 h-4"></i>
              <div>
                <h4 className="text-[12px] font-bold text-white font-outfit">{diet} Meal Blueprint</h4>
                <p className="text-[9px] text-gray-500 font-semibold uppercase font-mono mt-0.5">calibrated to {calcs.targetCalories} kcal</p>
              </div>
            </div>

            {/* Meal Tabs */}
            <div className="flex bg-white/5 p-0.5 rounded-lg border border-white/5 gap-0.5 mb-3.5">
              {meals.map((m, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => {
                    setActiveMealTab(idx);
                    try { playBeep(900, 'sine', 0.04); } catch(e) {}
                  }}
                  className={`flex-1 text-center py-1 rounded text-[9px] uppercase font-bold tracking-wider transition-all cursor-pointer ${
                    activeMealTab === idx 
                      ? 'bg-gradient-to-r from-[#9D00FF] to-[#00D2FF] text-white shadow-sm' 
                      : 'text-gray-400 hover:text-white'
                  }`}
                >
                  {m.label}
                </button>
              ))}
            </div>

            {/* Selected Meal Panel */}
            <div className="bg-white/[0.01] border border-white/5 p-3 rounded-xl mb-4">
              <div className="flex justify-between items-center mb-1.5 border-b border-white/5 pb-1">
                <span className="text-[10px] font-bold text-white font-outfit">
                  {activeMeal.name}
                  {alternativeSwap && <span className="text-[7px] bg-[#9D00FF]/15 text-[#9D00FF] border border-[#9D00FF]/30 px-1 ml-1.5 rounded uppercase font-bold font-sans">Swapped</span>}
                </span>
                <span className="text-[9px] font-bold text-[#9D00FF] font-mono">{activeMeal.macros.cal} KCALS</span>
              </div>
              <p className="text-[11px] text-gray-300 leading-normal font-sans">{displayFood}</p>

              {/* Individual Meal Macros progress bars */}
              <div className="grid grid-cols-3 gap-2 mt-3.5 pt-2.5 border-t border-white/5 text-[8px] font-mono">
                <div>
                  <div className="flex justify-between mb-0.5 text-gray-500 font-bold">
                    <span>PRO</span>
                    <span className="text-white">{activeMeal.macros.p}g</span>
                  </div>
                  <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                    <div className="h-full bg-[#9D00FF] rounded-full" style={{ width: `${Math.min(100, (activeMeal.macros.p / 45) * 100)}%` }} />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between mb-0.5 text-gray-500 font-bold">
                    <span>CAR</span>
                    <span className="text-white">{activeMeal.macros.c}g</span>
                  </div>
                  <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                    <div className="h-full bg-white/40 rounded-full" style={{ width: `${Math.min(100, (activeMeal.macros.c / 60) * 100)}%` }} />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between mb-0.5 text-gray-500 font-bold">
                    <span>FAT</span>
                    <span className="text-white">{activeMeal.macros.f}g</span>
                  </div>
                  <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                    <div className="h-full bg-[#00D2FF] rounded-full" style={{ width: `${Math.min(100, (activeMeal.macros.f / 20) * 100)}%` }} />
                  </div>
                </div>
              </div>
            </div>

            {/* Footer triggers */}
            <div className="flex flex-wrap items-center justify-between gap-2.5 pt-2.5 border-t border-white/5">
              <button
                type="button"
                onClick={() => {
                  setAlternativeSwap(prev => !prev);
                  try { playBeep(800, 'sine', 0.05); } catch(e) {}
                }}
                className={`text-[9px] font-bold uppercase tracking-wider px-2.5 py-1.5 rounded-lg border transition-all cursor-pointer ${
                  alternativeSwap 
                    ? 'bg-[#9D00FF]/25 border-[#9D00FF]/40 text-white shadow-[0_0_10px_rgba(157,0,255,0.25)]' 
                    : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'
                }`}
              >
                <i className="lucide-shuffle w-2.5 h-2.5 inline-block mr-1"></i>
                Swap Ingredients
              </button>

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

      // ==========================================
      // SUB-COMPONENT: INTERACTIVE ROADMAP CARD
      // ==========================================
      const InteractiveRoadmapCard = ({ profile }) => {
        const [progressWeek, setProgressWeek] = useState(1);
        const [pdfStatus, setPdfStatus] = useState('idle');

        const goal = profile.goal || 'recomp';
        const startW = parseFloat(profile.weight) || 75;
        const level = profile.level || 'Intermediate';

        // Custom prediction coordinates based on goal
        let weightData = [];
        let phaseTitle1 = "Adapting CNS";
        let phaseTitle2 = "Metabolic Push";
        let phaseTitle3 = "Peak Compression";

        if (goal === 'shred' || goal.toLowerCase().includes('loss')) {
          phaseTitle1 = "Adaptive Glycogen Flush";
          phaseTitle2 = "Lipid Lipolysis Overdrive";
          phaseTitle3 = "Subcutaneous Tightening";
          weightData = [
            { week: 1, w: startW },
            { week: 2, w: startW - 0.8 },
            { week: 4, w: startW - 1.8 },
            { week: 6, w: startW - 2.8 },
            { week: 8, w: startW - 3.8 },
            { week: 10, w: startW - 4.9 },
            { week: 12, w: startW - 6.0 }
          ];
        } else if (goal === 'bulk' || goal.toLowerCase().includes('gain')) {
          phaseTitle1 = "Myofibrillar Hypertrophy Activation";
          phaseTitle2 = "Glycogen Loading Spline";
          phaseTitle3 = "Myonuclear Domain Expansion";
          weightData = [
            { week: 1, w: startW },
            { week: 2, w: startW + 0.3 },
            { week: 4, w: startW + 0.9 },
            { week: 6, w: startW + 1.5 },
            { week: 8, w: startW + 2.0 },
            { week: 10, w: startW + 2.6 },
            { week: 12, w: startW + 3.2 }
          ];
        } else {
          // Recomp
          phaseTitle1 = "Neural Re-composition";
          phaseTitle2 = "Intramuscular Re-alignment";
          phaseTitle3 = "Peak Anabolic Compression";
          weightData = [
            { week: 1, w: startW },
            { week: 2, w: startW - 0.2 },
            { week: 4, w: startW - 0.4 },
            { week: 6, w: startW - 0.5 },
            { week: 8, w: startW - 0.7 },
            { week: 10, w: startW - 0.9 },
            { week: 12, w: startW - 1.0 }
          ];
        }

        const currentEstW = weightData.find(d => d.week >= progressWeek)?.w.toFixed(1) || startW.toFixed(1);

        const handlePdfDownload = () => {
          setPdfStatus('generating');
          
          let pdfContent = `FITNOVA 12-WEEK PHYSIOLOGY ROADMAP\\n`;
          pdfContent += `ATHLETE TARGET: ${goal.toUpperCase()} | BASAL WEIGHT: ${startW} KG | EXPERIENCE: ${level}\\n\\n`;
          
          pdfContent += `--- TRANSFORMATION BLOCK ARCHITECTURE ---\\n`;
          pdfContent += `* PHASE 1 (Weeks 1-4): ${phaseTitle1}\\n`;
          pdfContent += `  Objective: Flush neural systems, reset metabolic adaptation parameters.\\n\\n`;
          pdfContent += `* PHASE 2 (Weeks 5-8): ${phaseTitle2}\\n`;
          pdfContent += `  Objective: Target localized adipose vectors or escalate myofibrillar loading.\\n\\n`;
          pdfContent += `* PHASE 3 (Weeks 9-12): ${phaseTitle3}\\n`;
          pdfContent += `  Objective: Tighten subcutaneous borders, establish peak muscular conditioning.\\n\\n`;

          pdfContent += `--- WEIGHT CALIBRATION GRAPH (12 WEEKS) ---\\n`;
          weightData.forEach(d => {
            pdfContent += `  * Week ${d.week}: Estimated Target ${d.w.toFixed(1)} kg\\n`;
          });

          pdfContent += `\\nINSTRUCTIONAL DISCIPLINE DIRECTIVES:\\n`;
          pdfContent += `1. Weigh yourself daily at 07:00 immediately post waking, dry, pre-meals.\\n`;
          pdfContent += `2. Never reduce calorie allocations by more than 150 kcal below target limits without consulting Coach Nova.\\n`;

          setTimeout(() => {
            const success = generateRealPDF('roadmap', pdfContent, profile);
            if (success) {
              setPdfStatus('success');
              try { playBeep(1200, 'sine', 0.1); } catch (e) {}
              setTimeout(() => setPdfStatus('idle'), 2500);
            } else {
              setPdfStatus('idle');
            }
          }, 1200);
        };

        return (
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
      };
'''

if target_react_start in code:
    code = code.replace(target_react_start, custom_components)
    print("React visual card components successfully injected.")
else:
    print("ERROR: target_react_start not found in code.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Patch complete.")
