filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Inject global playBeep helper at the very beginning of React script scope
print("Injecting global playBeep helper...")
target_react_start = "const { useState, useEffect, useRef } = React;"

global_audio_helper = """const { useState, useEffect, useRef } = React;

      // ======================================================
      // FITNOVA AI — CORE GLOBAL AUDIO SYNTHESIZER UTILITY
      // ======================================================
      const playBeep = (freq = 800, type = 'sine', dur = 0.1) => {
        try {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (!AudioContext) return;
          const audioCtx = new AudioContext();
          const oscillator = audioCtx.createOscillator();
          const gainNode = audioCtx.createGain();
          
          oscillator.type = type;
          oscillator.frequency.value = freq;
          
          // Clean exponential sound gain envelope to protect speakers
          gainNode.gain.setValueAtTime(0.001, audioCtx.currentTime);
          gainNode.gain.exponentialRampToValueAtTime(0.08, audioCtx.currentTime + 0.02);
          gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
          
          oscillator.connect(gainNode);
          gainNode.connect(audioCtx.destination);
          
          oscillator.start();
          oscillator.stop(audioCtx.currentTime + dur);
        } catch (e) {
          console.warn("Audio Context synth warning: ", e);
        }
      };"""

if target_react_start in code:
    code = code.replace(target_react_start, global_audio_helper)
    print("global playBeep helper successfully injected.")
else:
    print("ERROR: target_react_start not found in code.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Global audio helper patch complete.")
