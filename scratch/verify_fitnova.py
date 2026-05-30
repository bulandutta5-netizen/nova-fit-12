import os

filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

checks = {
    "jsPDF CDN Import": "jspdf.umd.min.js",
    "generateRealPDF Core Utility": "const generateRealPDF = (type, content, profile) =>",
    "InteractiveWorkoutCard Sub-component": "const InteractiveWorkoutCard = ({ profile }) =>",
    "InteractiveDietCard Sub-component": "const InteractiveDietCard = ({ profile }) =>",
    "InteractiveRoadmapCard Sub-component": "const InteractiveRoadmapCard = ({ profile }) =>",
    "Widget Renderer Hook (Workout)": "msg.visualType === 'workout' && (",
    "Widget Renderer Hook (Diet)": "msg.visualType === 'diet' && (",
    "Widget Renderer Hook (Roadmap)": "msg.visualType === 'roadmap' && (",
    "Full Chat Renderer Hook (Workout)": "msg.visualType === 'workout' && (",
    "Full Chat Renderer Hook (Diet)": "msg.visualType === 'diet' && (",
    "Full Chat Renderer Hook (Roadmap)": "msg.visualType === 'roadmap' && (",
    "handleSendMessage activeVisualType Hook": "let activeVisualType = null;",
    "getAdaptiveBotResponse upgraded split routing": "visualType: 'workout'",
    "WorkoutCalendar Component": "const WorkoutCalendar = ({ profile }) =>",
    "WorkoutCalendar Viewport Container": "activeTab === 'calendar'",
    "WorkoutCalendar Mobile Nav Trigger": "setActiveTab('calendar')"
}

print("Running Automated Code Verification...")
has_errors = False

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

for label, query in checks.items():
    if query in content:
        print(f"  [PASS] {label}")
    else:
        print(f"  [FAIL] {label} (Could not find: '{query}')")
        has_errors = True

if not has_errors:
    print("\nSUCCESS: All automated validation checks passed successfully!")
else:
    print("\nWARNING: Some validation checks failed. Please inspect coordinates.")
