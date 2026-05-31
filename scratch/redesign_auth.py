import re

filePath = r"C:\Users\Bikranta Dutta\AppData\Local\Temp"
# We will use the correct path in the workspace
filePath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\login.html"

with open(filePath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Stylesheets upgrade: Locate the closing </style> tag and insert new onboarding styles right before it
styles_to_add = """
    /* ============================================================
       ONBOARDING WIZARD STYLES
    ============================================================ */
    .onboarding-progress-container {
      width: 100%;
    }
    .onboarding-progress-track {
      width: 100%;
      height: 4px;
      background: rgba(255,255,255,0.03);
      border-radius: 4px;
      overflow: hidden;
    }
    .onboarding-progress-bar {
      height: 100%;
      background: linear-gradient(90deg, var(--blue), var(--purple));
      border-radius: 4px;
      transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 0 10px rgba(0,210,255,0.3);
    }

    .step-slide {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: opacity 0.3s ease, transform 0.3s ease;
    }
    .step-slide.hidden {
      display: none;
      opacity: 0;
      transform: translateX(12px);
    }
    .step-slide.active {
      display: flex;
      opacity: 1;
      transform: translateX(0);
      animation: slideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes slideIn {
      from { opacity: 0; transform: translateX(12px); }
      to { opacity: 1; transform: translateX(0); }
    }

    .btn-secondary {
      flex: 1;
      padding: 13px 20px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.02);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: rgba(255, 255, 255, 0.5);
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      transition: all 0.25s;
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.15);
      color: #fff;
    }

    .toggle-pills {
      display: flex;
      gap: 8px;
      width: 100%;
      flex-wrap: wrap;
    }
    .pill-btn {
      flex: 1;
      min-width: 100px;
      padding: 12px 10px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.02);
      font-size: 11px;
      font-weight: 700;
      color: rgba(255,255,255,0.4);
      cursor: pointer;
      transition: all 0.2s;
      text-align: center;
      font-family: 'Inter', sans-serif;
    }
    .pill-btn:hover { border-color: rgba(0,210,255,0.25); color: rgba(255,255,255,0.8); }
    .pill-btn.selected {
      border-color: rgba(0,210,255,0.5);
      background: rgba(0,210,255,0.08);
      color: #fff;
      box-shadow: 0 0 12px rgba(0,210,255,0.12);
    }

    /* Telemetry Terminal on Left Side */
    .telemetry-terminal {
      width: 100%;
      max-width: 320px;
      background: rgba(10, 10, 12, 0.5);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      font-family: 'Fira Code', monospace;
      font-size: 11px;
      color: #E5E7EB;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.03), 0 10px 30px rgba(0,0,0,0.5);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      text-align: left;
    }
    .terminal-hdr {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      padding-bottom: 8px;
      margin-bottom: 10px;
      color: var(--blue);
      font-weight: 700;
      letter-spacing: 0.05em;
    }
    .terminal-pulse {
      width: 6px; height: 6px;
      border-radius: 50%;
      background: var(--blue);
      box-shadow: 0 0 8px var(--blue);
      animation: pulseBlink 1.5s infinite;
    }
    @keyframes pulseBlink { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
    .terminal-body {
      min-height: 80px;
      line-height: 1.6;
      color: rgba(255,255,255,0.85);
    }
    .terminal-cursor {
      display: inline-block;
      width: 6px; height: 12px;
      background: var(--cyan);
      margin-left: 2px;
      animation: cursorBlink 1s infinite;
      vertical-align: middle;
    }
    @keyframes cursorBlink { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }
"""

content = content.replace("  </style>", styles_to_add + "\n  </style>")

# 2. Left Panel Redesign: Replace Stats & Quote with Stats + Telemetry Terminal
left_panel_old = """          <!-- Stats -->
          <div class="stats-row">
            <div class="stat-card">
              <span class="stat-num">47K+</span>
              <span class="stat-label">Athletes</span>
            </div>
            <div class="stat-card">
              <span class="stat-num">98%</span>
              <span class="stat-label">Results</span>
            </div>
            <div class="stat-card">
              <span class="stat-num">4.9★</span>
              <span class="stat-label">Rated</span>
            </div>
          </div>

          <!-- Quote -->
          <div class="left-quote">
            <p>"Real progress doesn't come from perfect workouts — it comes from showing up every single day."</p>
            <span>— Built by trainers. Proven by results.</span>
          </div>"""

left_panel_new = """          <!-- Stats -->
          <div class="stats-row">
            <div class="stat-card">
              <span class="stat-num">47K+</span>
              <span class="stat-label">Athletes</span>
            </div>
            <div class="stat-card">
              <span class="stat-num">98%</span>
              <span class="stat-label">Results</span>
            </div>
            <div class="stat-card">
              <span class="stat-num">4.9★</span>
              <span class="stat-label">Rated</span>
            </div>
          </div>

          <!-- Telemetry Terminal -->
          <div class="telemetry-terminal">
            <div class="terminal-hdr">
              <span class="flex items-center gap-2">● NOVA CORE v2.8</span>
              <span class="terminal-pulse"></span>
            </div>
            <div class="terminal-body" id="telemetry-log">Initializing diagnostic system link...</div>
          </div>"""

content = content.replace(left_panel_old, left_panel_new)

# 3. Right Panel: Replace Register form with 6-step slide onboarding
signup_form_old_pattern = r'<!-- ========================\s*SIGN UP FORM\s*======================== -->.*?<form class="auth-form hidden" id="signup-form" novalidate>.*?</form>'

signup_form_new = """<!-- ========================
             SIGN UP FORM (Cinematic Onboarding Wizard)
        ======================== -->
        <form class="auth-form hidden" id="signup-form" novalidate>
          
          <!-- Onboarding Progress Header -->
          <div class="onboarding-progress-container">
            <div class="onboarding-progress-track">
              <div class="onboarding-progress-bar" id="signup-progress-bar" style="width: 16.66%;"></div>
            </div>
            <div class="flex justify-between items-center text-[10px] text-gray-500 font-bold uppercase mt-2 tracking-wider font-outfit" style="display: flex; justify-content: space-between;">
              <span>Calibration Step <span id="signup-step-num" style="color: var(--blue)">1</span> of 6</span>
              <span id="signup-step-name" style="color: #fff">Credentials Setup</span>
            </div>
          </div>

          <!-- Slide 1: Account Setup -->
          <div class="step-slide active" id="step-1">
            <div class="field-group">
              <label class="field-label" for="signup-name">Full Name</label>
              <div class="field-wrap">
                <svg class="field-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                <input type="text" id="signup-name" class="field-input" placeholder="e.g. Rohan Mehta" required autocomplete="name" />
              </div>
            </div>

            <div class="field-group">
              <label class="field-label" for="signup-email">Email Address</label>
              <div class="field-wrap">
                <svg class="field-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <input type="email" id="signup-email" class="field-input" placeholder="you@example.com" required autocomplete="email" />
              </div>
            </div>

            <div class="field-group">
              <label class="field-label" for="signup-password">Create Password</label>
              <div class="field-wrap">
                <svg class="field-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <input type="password" id="signup-password" class="field-input" placeholder="Minimum 6 characters" required autocomplete="new-password" />
              </div>
            </div>

            <button type="button" class="btn-primary mt-2" onclick="nextStep(2)">
              Begin Calibration
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </button>
            <div class="divider">or quick connect</div>
            <button type="button" class="btn-google" onclick="handleGoogleAuth()">
              <svg class="google-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
              </svg>
              Continue with Google
            </button>
          </div>

          <!-- Slide 2: Primary Goal Selection -->
          <div class="step-slide hidden" id="step-2">
            <div class="field-group">
              <label class="field-label">What is your primary fitness goal?</label>
              <div class="goal-grid select-none" id="goal-grid">
                <button type="button" class="goal-btn" data-goal="Fat Loss" onclick="selectGoal(this)">🔥 Fat Loss</button>
                <button type="button" class="goal-btn selected" data-goal="Muscle Gain" onclick="selectGoal(this)">💪 Muscle Gain</button>
                <button type="button" class="goal-btn" data-goal="Recomp" onclick="selectGoal(this)">⚡ Recomp</button>
                <button type="button" class="goal-btn" data-goal="Athletic" onclick="selectGoal(this)">🏃 Athlete</button>
                <button type="button" class="goal-btn" data-goal="Mobility" onclick="selectGoal(this)">🧘 Mobility</button>
                <button type="button" class="goal-btn" data-goal="General" onclick="selectGoal(this)">✨ General</button>
              </div>
              <input type="hidden" id="signup-goal" value="Muscle Gain" />
            </div>

            <div class="flex gap-4 mt-6" style="display: flex; gap: 12px;">
              <button type="button" class="btn-secondary" onclick="prevStep(1)">Back</button>
              <button type="button" class="btn-primary" onclick="nextStep(3)">Next Step</button>
            </div>
          </div>

          <!-- Slide 3: Environment & Experience -->
          <div class="step-slide hidden" id="step-3">
            <div class="field-group">
              <label class="field-label">Training Location</label>
              <div class="toggle-pills" id="location-grid" style="display: flex; gap: 8px;">
                <button type="button" class="pill-btn selected" data-value="Gym" onclick="selectPill('location', this)">🏋️ Gym (Full Equipment)</button>
                <button type="button" class="pill-btn" data-value="Home" onclick="selectPill('location', this)">🏡 Home (Bodyweight/Bands)</button>
              </div>
              <input type="hidden" id="signup-location" value="Gym" />
            </div>

            <div class="field-group mt-2">
              <label class="field-label">Training Experience</label>
              <div class="toggle-pills" id="level-grid" style="display: flex; gap: 8px;">
                <button type="button" class="pill-btn" data-value="Beginner" onclick="selectPill('level', this)">🔰 Beginner</button>
                <button type="button" class="pill-btn selected" data-value="Intermediate" onclick="selectPill('level', this)">⚙️ Intermediate</button>
                <button type="button" class="pill-btn" data-value="Advanced" onclick="selectPill('level', this)">🏆 Advanced</button>
              </div>
              <input type="hidden" id="signup-level" value="Intermediate" />
            </div>

            <div class="flex gap-4 mt-6" style="display: flex; gap: 12px;">
              <button type="button" class="btn-secondary" onclick="prevStep(2)">Back</button>
              <button type="button" class="btn-primary" onclick="nextStep(4)">Next Step</button>
            </div>
          </div>

          <!-- Slide 4: Commitment & Nutrition Habits -->
          <div class="step-slide hidden" id="step-4">
            <div class="field-group">
              <label class="field-label">Weekly Training Commitment</label>
              <div class="toggle-pills" id="schedule-grid" style="display: flex; gap: 8px;">
                <button type="button" class="pill-btn" data-value="3 Days" onclick="selectPill('schedule', this)">3 Days</button>
                <button type="button" class="pill-btn selected" data-value="4 Days" onclick="selectPill('schedule', this)">4 Days</button>
                <button type="button" class="pill-btn" data-value="5 Days" onclick="selectPill('schedule', this)">5 Days</button>
                <button type="button" class="pill-btn" data-value="6 Days" onclick="selectPill('schedule', this)">6 Days</button>
              </div>
              <input type="hidden" id="signup-schedule" value="4 Days" />
            </div>

            <div class="field-group mt-2">
              <label class="field-label">Diet & Nutritional Preference</label>
              <div class="goal-grid select-none" id="diet-grid">
                <button type="button" class="goal-btn selected" data-value="High Protein" onclick="selectDiet(this)">🍗 High Protein</button>
                <button type="button" class="goal-btn" data-value="Vegetarian" onclick="selectDiet(this)">🥗 Vegetarian</button>
                <button type="button" class="goal-btn" data-value="Vegan" onclick="selectDiet(this)">🌱 Vegan</button>
                <button type="button" class="goal-btn" data-value="Keto" onclick="selectDiet(this)">🥩 Keto</button>
                <button type="button" class="goal-btn" data-value="Indian Diet" onclick="selectDiet(this)">🍛 Indian Diet</button>
                <button type="button" class="goal-btn" data-value="Balanced" onclick="selectDiet(this)">🍳 Balanced</button>
              </div>
              <input type="hidden" id="signup-diet" value="High Protein" />
            </div>

            <div class="flex gap-4 mt-6" style="display: flex; gap: 12px;">
              <button type="button" class="btn-secondary" onclick="prevStep(3)">Back</button>
              <button type="button" class="btn-primary" onclick="nextStep(5)">Next Step</button>
            </div>
          </div>

          <!-- Slide 5: Vitals Calibration -->
          <div class="step-slide hidden" id="step-5">
            <div class="field-group">
              <label class="field-label">Gender (For Metabolic Calculations)</label>
              <div class="toggle-pills" id="gender-grid" style="display: flex; gap: 8px;">
                <button type="button" class="pill-btn selected" data-value="Male" onclick="selectPill('gender', this)">👨 Male</button>
                <button type="button" class="pill-btn" data-value="Female" onclick="selectPill('gender', this)">👩 Female</button>
              </div>
              <input type="hidden" id="signup-gender" value="Male" />
            </div>

            <div class="field-group mt-2">
              <div class="flex justify-between items-center text-xs font-bold text-gray-400 font-outfit mb-2 uppercase" style="display: flex; justify-content: space-between;">
                <span>Age</span>
                <span class="text-white font-black" id="age-val" style="color: #fff">28 Years</span>
              </div>
              <input type="range" min="15" max="75" step="1" value="28" id="signup-age" oninput="updateAge(this.value)" class="w-full accent-electricBlue bg-white/5 rounded-lg appearance-none h-1.5" style="width: 100%;" />
            </div>

            <div class="grid grid-cols-2 gap-4 mt-2" style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="field-group">
                <label class="field-label" for="signup-height">Height (cm)</label>
                <div class="field-wrap">
                  <input type="number" id="signup-height" class="field-input text-center" placeholder="175" value="175" required style="padding-left: 16px; text-align: center;" />
                </div>
              </div>
              <div class="field-group">
                <label class="field-label" for="signup-weight">Weight (kg)</label>
                <div class="field-wrap">
                  <input type="number" id="signup-weight" class="field-input text-center" placeholder="78" value="78" required style="padding-left: 16px; text-align: center;" />
                </div>
              </div>
            </div>

            <div class="flex gap-4 mt-6" style="display: flex; gap: 12px;">
              <button type="button" class="btn-secondary" onclick="prevStep(4)">Back</button>
              <button type="button" class="btn-primary" onclick="nextStep(6)">Next Step</button>
            </div>
          </div>

          <!-- Slide 6: Target & Safety Screening -->
          <div class="step-slide hidden" id="step-6">
            <div class="field-group">
              <label class="field-label" for="signup-target-weight">Target Weight Goal (kg)</label>
              <div class="field-wrap">
                <input type="number" id="signup-target-weight" class="field-input text-center" placeholder="74" value="74" required style="padding-left: 16px; text-align: center;" />
              </div>
            </div>

            <div class="field-group mt-2">
              <label class="field-label">Safety Injury Screening</label>
              <div class="toggle-pills" id="injuries-grid" style="display: flex; gap: 8px; flex-wrap: wrap;">
                <button type="button" class="pill-btn selected" data-value="None" onclick="selectInjury(this)">🟢 None</button>
                <button type="button" class="pill-btn" data-value="Back Pain" onclick="selectInjury(this)">🔴 Back Pain</button>
                <button type="button" class="pill-btn" data-value="Knee Issues" onclick="selectInjury(this)">Knee Issues</button>
                <button type="button" class="pill-btn" data-value="Shoulder Issues" onclick="selectInjury(this)">Shoulder Issues</button>
              </div>
              <input type="hidden" id="signup-injuries" value="None" />
            </div>

            <label class="agreement-label mt-4 mb-2" style="display: flex; align-items: center; gap: 8px;">
              <input type="checkbox" id="agree-terms" required checked style="margin-top: 0;" />
              <span>I authorize biometrics scan under <a href="#">Terms & Privacy</a></span>
            </label>

            <div class="flex gap-4 mt-4" style="display: flex; gap: 12px;">
              <button type="button" class="btn-secondary" onclick="prevStep(5)">Back</button>
              <button type="submit" class="btn-primary">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                Calibrate Vitals & Complete
              </button>
            </div>
          </div>
        </form>"""

content = re.sub(signup_form_old_pattern, signup_form_new, content, flags=re.DOTALL)

# 4. JavaScript functions for slides & Terminal: Add to modular scripts in login.html
# We will find the switchTab definition in login.html and insert our onboarding handlers there.
onboarding_js_to_add = """    // ── Onboarding Wizard Logic ───────────────────────────────
    let currentStep = 1;
    const totalSteps = 6;
    const stepNames = [
      "Credentials Setup",
      "Goal Calibration",
      "Location & Level",
      "Frequency & Diet",
      "Physical Vitals",
      "Injury & Complete"
    ];

    window.nextStep = function(step) {
      // Basic validation for step 1
      if (step === 2) {
        const name = document.getElementById('signup-name').value.trim();
        const email = document.getElementById('signup-email').value.trim();
        const password = document.getElementById('signup-password').value;
        if (!name || !email || !password) {
          showError('Please fill out all credentials to begin onboarding.');
          playBeep(330, 0.35, 'sawtooth');
          return;
        }
        if (password.length < 6) {
          showError('Password must be at least 6 characters.');
          playBeep(330, 0.35, 'sawtooth');
          return;
        }
      }

      clearError();
      document.getElementById(`step-${currentStep}`).classList.replace('active', 'hidden');
      document.getElementById(`step-${step}`).classList.replace('hidden', 'active');
      currentStep = step;

      // Update progress bar
      const progressPercent = (currentStep / totalSteps) * 100;
      document.getElementById('signup-progress-bar').style.width = `${progressPercent}%`;
      document.getElementById('signup-step-num').textContent = currentStep;
      document.getElementById('signup-step-name').textContent = stepNames[currentStep - 1];

      playBeep(500 + step * 80, 'sine', 0.08);
    };

    window.prevStep = function(step) {
      clearError();
      document.getElementById(`step-${currentStep}`).classList.replace('active', 'hidden');
      document.getElementById(`step-${step}`).classList.replace('hidden', 'active');
      currentStep = step;

      // Update progress bar
      const progressPercent = (currentStep / totalSteps) * 100;
      document.getElementById('signup-progress-bar').style.width = `${progressPercent}%`;
      document.getElementById('signup-step-num').textContent = currentStep;
      document.getElementById('signup-step-name').textContent = stepNames[currentStep - 1];

      playBeep(450 + step * 80, 'sine', 0.08);
    };

    window.selectPill = function(type, btn) {
      const container = btn.parentElement;
      container.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      document.getElementById(`signup-${type}`).value = btn.dataset.value;
      playBeep(700, 'triangle', 0.06);
    };

    window.selectDiet = function(btn) {
      const container = document.getElementById('diet-grid');
      container.querySelectorAll('.goal-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      document.getElementById('signup-diet').value = btn.dataset.value;
      playBeep(750, 'triangle', 0.06);
    };

    window.selectInjury = function(btn) {
      const container = document.getElementById('injuries-grid');
      container.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      document.getElementById('signup-injuries').value = btn.dataset.value;
      playBeep(720, 'triangle', 0.06);
    };

    window.updateAge = function(val) {
      document.getElementById('age-val').textContent = `${val} Years`;
    };

    // ── Telemetry Terminal Cycler ──────────────────────────────
    const telemetryLogs = [
      { user: "Rohan Mehta (Tech Lead)", action: "Analyzing body composition...", detail: "Surplus active. Target: 2,100 Kcal. Protein: 172g. Progress: Fat Loss -12% | Muscle +3.5kg." },
      { user: "Pooja Krishnan (Working Mom)", action: "Recalibrating mobility protocol...", detail: "Joint health priority. Spine support enabled. Target: 1,600 Kcal. Progress: Fat -7% | Strength +20%." },
      { user: "Karan Malhotra (Powerlifter)", action: "Syncing compound strength templates...", detail: "Advanced hypertrophy active. Target: 3,100 Kcal. Progress: Squat +35kg | Bench +20kg." }
    ];
    let activeLogIdx = 0;
    let charIdx = 0;
    let activeText = "";
    let isDeleting = false;
    const logElement = document.getElementById('telemetry-log');

    function typeTelemetry() {
      const log = telemetryLogs[activeLogIdx];
      const fullText = `USER: ${log.user}\\nACTION: ${log.action}\\nSTATUS: ${log.detail}`;
      
      if (!isDeleting) {
        activeText = fullText.substring(0, charIdx + 1);
        charIdx++;
        if (charIdx === fullText.length) {
          isDeleting = true;
          setTimeout(typeTelemetry, 4500); // Hold for 4.5 seconds
          return;
        }
      } else {
        activeText = fullText.substring(0, charIdx - 1);
        charIdx--;
        if (charIdx === 0) {
          isDeleting = false;
          activeLogIdx = (activeLogIdx + 1) % telemetryLogs.length;
          setTimeout(typeTelemetry, 500);
          return;
        }
      }

      if (logElement) {
        logElement.innerHTML = activeText.replace(/\\n/g, '<br/>') + '<span class="terminal-cursor"></span>';
      }
      setTimeout(typeTelemetry, isDeleting ? 15 : 30);
    }
    
    // Trigger typing cycle on load
    setTimeout(typeTelemetry, 1000);
"""

content = content.replace("    window.switchTab = function(tab) {", onboarding_js_to_add + "\n    window.switchTab = function(tab) {")

# 5. Connect multi-step parameters to signup form logic
# Let's inspect the signupForm submit listener in login.html.
# It reads:
#     signupForm.addEventListener('submit', async (e) => {
#       e.preventDefault();
#       clearError();
#       const name     = document.getElementById('signup-name').value.trim();
#       const email    = document.getElementById('signup-email').value.trim();
#       const password = document.getElementById('signup-password').value;
#       const goal     = document.getElementById('signup-goal').value;
#       const agreed   = document.getElementById('agree-terms').checked;
#
# Let's update it to read all variables:
#       const name     = document.getElementById('signup-name').value.trim();
#       const email    = document.getElementById('signup-email').value.trim();
#       const password = document.getElementById('signup-password').value;
#       const goal     = document.getElementById('signup-goal').value;
#       const location = document.getElementById('signup-location').value;
#       const level    = document.getElementById('signup-level').value;
#       const schedule = document.getElementById('signup-schedule').value;
#       const diet     = document.getElementById('signup-diet').value;
#       const gender   = document.getElementById('signup-gender').value;
#       const age      = document.getElementById('signup-age').value;
#       const height   = document.getElementById('signup-height').value;
#       const weight   = document.getElementById('signup-weight').value;
#       const targetWeight = document.getElementById('signup-target-weight').value;
#       const injuries = document.getElementById('signup-injuries').value;

signup_vars_old = """      const name     = document.getElementById('signup-name').value.trim();
      const email    = document.getElementById('signup-email').value.trim();
      const password = document.getElementById('signup-password').value;
      const goal     = document.getElementById('signup-goal').value;
      const agreed   = document.getElementById('agree-terms').checked;"""

signup_vars_new = """      const name     = document.getElementById('signup-name').value.trim();
      const email    = document.getElementById('signup-email').value.trim();
      const password = document.getElementById('signup-password').value;
      const goal     = document.getElementById('signup-goal').value;
      const location = document.getElementById('signup-location').value;
      const level    = document.getElementById('signup-level').value;
      const schedule = document.getElementById('signup-schedule').value;
      const diet     = document.getElementById('signup-diet').value;
      const gender   = document.getElementById('signup-gender').value;
      const age      = document.getElementById('signup-age').value;
      const height   = document.getElementById('signup-height').value;
      const weight   = document.getElementById('signup-weight').value;
      const targetWeight = document.getElementById('signup-target-weight').value;
      const injuries = document.getElementById('signup-injuries').value;
      const agreed   = document.getElementById('agree-terms').checked;"""

content = content.replace(signup_vars_old, signup_vars_new)

# Update saveUser logic in signup form to save all these values
save_user_old = """        saveUser(result.user, { goal });
        overlaySuccess('You\\\'re in! Let\\\'s get to work. 🔥', `Hey ${name}, your ${goal} journey starts NOW.`);"""

# We can run BMR calculations right here to save calculated targetCalories, targetProtein, targetCarbs, targetFats, etc.!
# This is incredibly realistic, giving the dashboard perfect synced values on first load!
save_user_new = """        // Run biometrics Mifflin-St Jeor engine
        const w = parseFloat(weight);
        const h = parseFloat(height);
        const a = parseInt(age);
        let bmr = 0;
        if (gender === 'Female') bmr = 10 * w + 6.25 * h - 5 * a - 161;
        else bmr = 10 * w + 6.25 * h - 5 * a + 5;
        
        let multiplier = 1.2;
        if (schedule.includes('3')) multiplier = 1.375;
        else if (schedule.includes('4') || schedule.includes('5')) multiplier = 1.55;
        else if (schedule.includes('6')) multiplier = 1.725;
        const tdee = Math.round(bmr * multiplier);
        
        let targetCalories = tdee;
        if (goal.includes('Fat Loss')) targetCalories = Math.max(1200, tdee - 500);
        else if (goal.includes('Muscle')) targetCalories = tdee + 300;
        else if (goal.includes('Recomp')) targetCalories = tdee - 150;
        
        let proteinMultiplier = 1.6;
        if (goal.includes('Muscle')) proteinMultiplier = 2.0;
        else if (goal.includes('Fat Loss')) proteinMultiplier = 2.2;
        else if (goal.includes('Athletic')) proteinMultiplier = 1.8;
        const targetProtein = Math.round(w * proteinMultiplier);
        
        const biometrics = {
          goal, location, level, schedule, diet, gender, age, height, weight, targetWeight, injuries,
          bmr: Math.round(bmr), tdee, targetCalories, targetProtein,
          waterGoal: 14 // default
        };
        
        saveUser(result.user, biometrics);
        overlaySuccess('Calibration Successful! 🧬', `Vitals mapped. Hey ${name}, let's build your ${goal} body!`);"""

content = content.replace(save_user_old, save_user_new)

with open(filePath, "w", encoding="utf-8") as f:
    f.write(content)

print("Redesign applied successfully to login.html")
