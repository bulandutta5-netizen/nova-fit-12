filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Patch Viewport rendering block
print("Patching main viewport rendering block to include calendar...")

target_viewport = """                <div className={activeTab === 'pricing' ? "animate-bubble-appear" : "hidden"}>
                  <Pricing />
                </div>"""

replacement_viewport = """                <div className={activeTab === 'pricing' ? "animate-bubble-appear" : "hidden"}>
                  <Pricing />
                </div>

                <div className={activeTab === 'calendar' ? "animate-bubble-appear" : "hidden"}>
                  <WorkoutCalendar profile={profile} />
                </div>"""

if target_viewport in code:
    code = code.replace(target_viewport, replacement_viewport)
    print("Viewport rendering block successfully updated.")
else:
    print("ERROR: target_viewport not found.")

# 2. Patch mobile bottom navigation bar
print("Patching mobile bottom navigation bar...")

target_mobile_nav = """                <button onClick={() => setActiveTab('nutrition')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'nutrition' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-apple w-4.5 h-4.5"></i>
                  <span>Nutrition</span>
                </button>"""

replacement_mobile_nav = """                <button onClick={() => setActiveTab('nutrition')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'nutrition' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-apple w-4.5 h-4.5"></i>
                  <span>Nutrition</span>
                </button>
                <button onClick={() => setActiveTab('calendar')} className={`flex flex-col items-center gap-1 text-[9px] font-bold ${activeTab === 'calendar' ? 'text-[#00D2FF]' : ''}`}>
                  <i className="lucide-calendar w-4.5 h-4.5"></i>
                  <span>Calendar</span>
                </button>"""

if target_mobile_nav in code:
    code = code.replace(target_mobile_nav, replacement_mobile_nav)
    print("Mobile bottom navigation bar successfully updated.")
else:
    print("ERROR: target_mobile_nav not found.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Viewport and nav patches complete.")
