import re

html_path = "preview.html"

# Read preview.html
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the new UMD-compatible Chatbot, TypewriterText, and Soundwave code block
new_code = """      // Word-by-word typewriter effect component
      const TypewriterText = ({ text, onComplete, scrollRef, isAlreadyTyped }) => {
        const [displayedText, setDisplayedText] = React.useState('');
        
        React.useEffect(() => {
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
            
            // Auto-scroll-to-bottom on every word tick
            if (scrollRef && scrollRef.current) {
              scrollRef.current.scrollIntoView({ behavior: 'auto' });
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

      const Chatbot = () => {
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
        const [isSpeechEnabled, setIsSpeechEnabled] = useState(false);
        const [isSpeaking, setIsSpeaking] = useState(false);
        const [typedMessageIds, setTypedMessageIds] = useState([]);
        
        // Mobile responsive views
        const [showCredsModal, setShowCredsModal] = useState(false);
        const [showTelemetryModal, setShowTelemetryModal] = useState(false);

        const messagesEndRef = useRef(null);

        const scrollToBottom = () => {
          messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
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

        // Re-trigger lucide icons creation whenever sub-components change dynamically
        useEffect(() => {
          if (window.lucide) {
            window.lucide.createIcons();
          }
        }, [messages, isTyping, onboardingStep, showCredsModal, showTelemetryModal]);

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
              playOscillator(1046.50, 'sine', 0.5, 0.15, 0.015);  // C6 harmony
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
            // AudioContext not supported
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
            let clean = text.replace(/[\\*\\#\\_]/g, ''); // strip markdown
            clean = clean.replace(/\\-\\s+/g, ''); // strip bullet symbols
            const utterance = new SpeechSynthesisUtterance(clean);
            const voices = window.speechSynthesis.getVoices();
            const englishVoice = voices.find(v => v.lang.startsWith('en'));
            if (englishVoice) utterance.voice = englishVoice;
            
            utterance.rate = 1.05;
            utterance.pitch = 0.95; // lower pitch for trainer profile
            
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
              let clean = text.replace(/[\\*\\#\\_]/g, '');
              clean = clean.replace(/\\-\\s+/g, '');
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

              botText = `Diagnostic bypassed, champion. I have calibrated your console with a default active biometric profile (28 yrs, 78kg, 175cm, Goal: Recomposition, 4 Days/Week Gym split). We are fully operational in direct coaching mode.

Ask me anything about training splits, custom macros, technique breakdowns, or recovery strategies. Let's get to work.`;
              
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
                if (textToSend.includes("begin") || textToSend.includes("Let's")) {
                  nextStep = 1;
                } else {
                  botText = "I am a world-class certified fitness expert with years of experience in bodybuilding, fat loss, muscle gain, strength training, nutrition, and lifestyle optimization. By establishing your biometrics, I will calculate your exact daily calorie and protein requirements, and generate a customized program tailored to your goals. Shall we begin?";
                  nextOptions = ["Let's begin!", "Skip Diagnostic & Chat", "Tell me more first"];
                  
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
          }, 1000 + Math.random() * 800); // 1.8s delay feels very real and high-end
        };

        const simulateSpeechInput = () => {
          playBeep(800, 'triangle', 0.2);
          alert("Holographic Mic Active. Speak clearly into your device.\\n\\n(Simulated: Speak your command now. Try typing instead if mic permissions are disabled.)");
        };

        const quickPrompts = onboardingStep === null ? [
          { text: "Suggest a custom meal plan", icon: "lucide-apple" },
          { text: "Troubleshoot squat form", icon: "lucide-dumbbell" },
          { text: "Give me intense motivation", icon: "lucide-trophy" },
          { text: "Optimize my supplements", icon: "lucide-sparkles" }
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
                  <i className="lucide-sparkles w-3 h-3"></i> Core Intelligence Node
                </span>
                <h2 className="text-3xl md:text-5xl font-bold font-outfit text-white">
                  Fit Nova Elite AI Coach
                </h2>
                <p className="text-gray-400 mt-4 max-w-xl mx-auto text-sm">
                  Consult Coach Nova, your CSCS certified AI Strength & Transformation mentor, for hyper-personalized macros and structural workout adaptation.
                </p>
              </div>

              {/* 3-Column Grid */}
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch h-[680px] max-w-6xl mx-auto">
                
                {/* Column 1: Profile (3 cols) */}
                <div className="hidden lg:flex lg:col-span-3 flex-col justify-between glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-transparent via-[#00F0FF]/5 to-transparent h-[200%] w-full pointer-events-none animate-hologram-scan" />
                  
                  <div className="z-10">
                    <span className="text-[9px] text-[#00F0FF] font-bold uppercase tracking-widest border border-[#00F0FF]/30 px-2 py-0.5 rounded bg-[#00F0FF]/5 font-outfit inline-block mb-4">
                      CERTIFIED MENTOR
                    </span>
                    
                    {/* Holographic Avatar */}
                    <div className="relative w-32 h-32 mx-auto mb-6 flex items-center justify-center">
                      <div className="absolute inset-0 border border-dashed border-[#9D00FF]/30 rounded-full animate-orbital-spin" />
                      <div className="absolute inset-1.5 border border-dashed border-[#00D2FF]/40 rounded-full animate-orbital-spin-reverse" />
                      
                      <div className={`w-24 h-24 rounded-full bg-black/60 flex items-center justify-center relative overflow-hidden transition-all duration-500 ${
                        isSpeaking 
                          ? 'border-2 border-[#9D00FF] shadow-[0_0_30px_rgba(157,0,255,0.6),inset_0_0_15px_rgba(157,0,255,0.3)] animate-pulse' 
                          : isTyping 
                            ? 'border-2 border-[#00F0FF] shadow-[0_0_20px_rgba(0,240,255,0.4),inset_0_0_10px_rgba(0,240,255,0.2)] animate-pulse' 
                            : 'border-2 border-[#00D2FF]/60 shadow-[0_0_15px_rgba(0,210,255,0.15),inset_0_0_5px_rgba(0,210,255,0.15)] hover:border-[#00D2FF] hover:shadow-[0_0_20px_rgba(0,210,255,0.3)]'
                      }`}>
                        <div className="absolute top-0 left-0 w-full h-1 bg-[#00F0FF]/30 blur-xs animate-hologram-scan" />
                        <div className={`w-8 h-8 rounded-lg bg-gradient-to-tr from-[#9D00FF] to-[#00D2FF] rotate-45 flex items-center justify-center animate-eye-shift shadow-[0_0_15px_rgba(0,240,255,0.6)] ${isSpeaking ? '[animation-duration:3s]' : ''}`}>
                          <div className="w-2 h-2 bg-white rounded-full animate-pulse shadow-[0_0_5px_#fff]" />
                        </div>
                        <div className="absolute inset-0 opacity-10 bg-[linear-gradient(rgba(255,255,255,0.1)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.1)_1px,transparent_1px)] bg-[size:10px_10px]" />
                      </div>
                      <div className="absolute -bottom-1 w-28 h-3 bg-[#00D2FF]/20 rounded-full blur-xs" />
                    </div>

                    <div className="text-center">
                      <h4 className="text-base font-bold font-outfit text-white">Coach Nova</h4>
                      <p className="text-[10px] text-gray-400 font-semibold tracking-wide mt-1">CSCS Strength & Transformation Coach</p>
                      
                      <div className="flex justify-center gap-2 mt-3">
                        <div className="text-[9px] font-bold tracking-wider px-2 py-0.5 rounded bg-[#00F0FF]/10 border border-[#00F0FF]/30 text-[#00F0FF] flex items-center gap-1">
                          <i className="lucide-shield-alert shrink-0 w-2.5 h-2.5"></i> NSCA-CSCS
                        </div>
                        <div className="text-[9px] font-bold tracking-wider px-2 py-0.5 rounded bg-[#9D00FF]/10 border border-[#9D00FF]/30 text-[#9D00FF] flex items-center gap-1">
                          <i className="lucide-award shrink-0 w-2.5 h-2.5"></i> ISSN-SNS
                        </div>
                      </div>

                      <div className="h-px bg-white/5 my-4" />
                      
                      <div className="flex flex-col gap-2.5 text-left text-xs font-semibold text-gray-300">
                        <div className="flex items-center gap-2">
                          <i className="lucide-award text-[#00F0FF] shrink-0 w-3.5 h-3.5"></i>
                          <span>12+ Years Coaching Experience</span>
                        </div>
                        <div className="flex items-center gap-2">
                          <i className="lucide-zap text-[#9D00FF] shrink-0 w-3.5 h-3.5"></i>
                          <span>Fat Loss & Hypertrophy Specialist</span>
                        </div>
                        <div className="flex items-center gap-2">
                          <i className="lucide-activity text-[#00F0FF] shrink-0 w-3.5 h-3.5"></i>
                          <span>5,240+ Verified Transformations</span>
                        </div>
                        <div className="flex items-center gap-2">
                          <i className="lucide-heart text-[#9D00FF] shrink-0 w-3.5 h-3.5"></i>
                          <span>99.4% Client Goal Success Rate</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="z-10 flex flex-col gap-3">
                    <div className="bg-white/5 border border-white/5 p-3 rounded-2xl">
                      <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block mb-1">LIVE COACH STATUS</span>
                      <div className="flex items-center gap-2">
                        <span className={`w-2 h-2 rounded-full bg-emerald-500 ${isSpeaking || isTyping ? 'animate-ping' : 'animate-pulse'}`} />
                        <span className="text-xs font-bold text-gray-200">
                          {isSpeaking ? 'Speaking guidance...' : isTyping ? 'AI Coach is thinking...' : 'Empathy & Focus Active'}
                        </span>
                      </div>
                    </div>
                    
                    <div className="bg-white/5 border border-white/5 p-3 rounded-2xl">
                      <span className="text-[9px] text-gray-500 font-bold uppercase tracking-wider block mb-1">CLIENT SUCCESS LOG</span>
                      <div className="flex flex-col gap-1.5 text-[10px] font-semibold text-gray-300">
                        <div className="flex items-center gap-1.5">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#00F0FF]" />
                          <span>Calculations verified under NSCA guidelines</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#9D00FF]" />
                          <span>Client #5242: -12kg Fat (Complete)</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#00F0FF]" />
                          <span>Client #5243: +6.5kg Muscle (Active)</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Column 2: Chat (6 cols) */}
                <div className="col-span-1 lg:col-span-6 flex flex-col justify-between glass-panel rounded-3xl glow-border card-radial-blue border-white/5 shadow-2xl relative">
                  
                  <div className="p-4 border-b border-white/5 flex items-center justify-between bg-black/30">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-full bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] p-0.5 flex items-center justify-center relative overflow-hidden shrink-0">
                        <div className="w-full h-full rounded-full bg-[#0B0B0B] flex items-center justify-center">
                          <i className="lucide-bot text-[#00F0FF] animate-pulse w-4.5 h-4.5"></i>
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

                    <div className="flex items-center gap-2">
                      <button
                        type="button"
                        onClick={handleSpeechToggle}
                        className={`p-2 rounded-full border transition-all cursor-pointer flex items-center justify-center ${
                          isSpeechEnabled 
                            ? 'bg-[#00F0FF]/15 border-[#00F0FF]/40 text-[#00F0FF] shadow-[0_0_10px_rgba(0,240,255,0.2)]' 
                            : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'
                        }`}
                        title={isSpeechEnabled ? "Speech guidance on" : "Speech guidance muted"}
                      >
                        {isSpeechEnabled ? <i className="lucide-volume-2 w-3.5 h-3.5"></i> : <i className="lucide-volume-x w-3.5 h-3.5"></i>}
                      </button>

                      <button
                        type="button"
                        onClick={() => setShowCredsModal(true)}
                        className="lg:hidden p-2 rounded-full bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center"
                        title="View Coach Credentials"
                      >
                        <i className="lucide-award w-3.5 h-3.5"></i>
                      </button>

                      <button
                        type="button"
                        onClick={() => setShowTelemetryModal(true)}
                        className="lg:hidden p-2 rounded-full bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center"
                        title="View Profile Telemetry"
                      >
                        <i className="lucide-activity w-3.5 h-3.5"></i>
                      </button>

                      {profile.calculations && (
                        <button
                          type="button"
                          onClick={resetDiagnostic}
                          className="flex items-center gap-1 text-[9px] font-bold text-[#00F0FF] hover:text-white bg-[#00F0FF]/10 hover:bg-[#00F0FF]/20 border border-[#00F0FF]/30 px-3 py-1.5 rounded-full transition-all cursor-pointer font-outfit"
                        >
                          <i className="lucide-refresh-cw w-2.5 h-2.5"></i> Recalibrate
                        </button>
                      )}
                    </div>
                  </div>

                  <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-4">
                    {messages.map((msg) => {
                      const isBot = msg.sender === 'bot';
                      return (
                        <div key={msg.id} className={`flex flex-col gap-1.5 max-w-[85%] animate-bubble-appear ${isBot ? 'self-start' : 'self-end items-end'}`}>
                          <div className={`flex gap-2.5 ${isBot ? '' : 'flex-row-reverse'}`}>
                            <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 border border-white/5 ${isBot ? 'bg-[#9D00FF]/15 text-[#9D00FF]' : 'bg-white/5 text-[#00D2FF]'}`}>
                              {isBot ? <i className="lucide-bot w-3.5 h-3.5"></i> : <i className="lucide-user w-3.5 h-3.5"></i>}
                            </div>

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
                                {isBot ? (
                                  <button
                                    type="button"
                                    onClick={() => speakMessageManually(msg.text)}
                                    className="text-gray-500 hover:text-[#00F0FF] p-0.5 rounded cursor-pointer transition-colors"
                                    title="Listen to this block"
                                  >
                                    <i className="lucide-volume-2 w-2.5 h-2.5"></i>
                                  </button>
                                ) : <div />}
                                <span className={`text-[8px] font-semibold block text-right ${isBot ? 'text-gray-500' : 'text-white/60'}`}>
                                  {msg.time}
                                </span>
                              </div>
                            </div>
                          </div>

                          {isBot && msg.options && onboardingStep !== null && messages[messages.length - 1].id === msg.id && (
                            <div className="flex flex-wrap gap-2 mt-1.5 ml-10">
                              {msg.options.map((opt, i) => (
                                <button
                                  key={i}
                                  type="button"
                                  onClick={() => handleSendMessage(opt)}
                                  className="glass-panel text-[10px] font-semibold text-gray-300 hover:text-white border border-white/5 hover:border-[#00D2FF]/40 hover:bg-[#00D2FF]/10 px-4 py-2 rounded-xl transition-all cursor-pointer shadow-sm hover:shadow-[0_0_10px_rgba(0,210,255,0.1)]"
                                >
                                  {opt}
                                </button>
                              ))}
                            </div>
                          )}
                        </div>
                      );
                    })}

                    {isTyping && (
                      <div className="flex gap-3 self-start max-w-[85%] animate-pulse">
                        <div className="w-8 h-8 rounded-full bg-[#9D00FF]/15 text-[#9D00FF] flex items-center justify-center border border-white/5">
                          <i className="lucide-bot w-3.5 h-3.5"></i>
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
                    
                    <div ref={messagesEndRef} />
                  </div>

                  {quickPrompts.length > 0 && (
                    <div className="px-6 py-2 flex flex-wrap gap-2 border-t border-white/5 bg-black/15">
                      {quickPrompts.map((p, index) => (
                        <button
                          key={index}
                          type="button"
                          onClick={() => handleSendMessage(p.text)}
                          className="flex items-center gap-1.5 text-[10px] font-semibold text-gray-400 hover:text-white bg-white/5 border border-white/5 hover:border-[#00D2FF]/30 hover:bg-white/10 px-3 py-1.5 rounded-full transition-all cursor-pointer"
                        >
                          <i className={`${p.icon} w-3 h-3`}></i> {p.text}
                        </button>
                      ))}
                    </div>
                  )}

                  <form
                    onSubmit={(e) => {
                      e.preventDefault();
                      handleSendMessage(inputText);
                    }}
                    className="p-4 border-t border-white/5 flex gap-3 bg-black/30"
                  >
                    <button
                      type="button"
                      onClick={simulateSpeechInput}
                      className="p-3 rounded-xl bg-white/5 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-colors cursor-pointer"
                      title="Voice Input"
                    >
                      <i className="lucide-mic w-4 h-4"></i>
                    </button>

                    <input
                      type={currentStepData && currentStepData.inputType === 'number' ? 'number' : 'text'}
                      value={inputText}
                      onChange={(e) => setInputText(e.target.value)}
                      placeholder={inputPlaceholder}
                      className="flex-1 bg-[#161616] border border-white/5 focus:border-[#00D2FF]/40 rounded-xl px-4 py-3 text-white text-xs outline-none transition-all font-medium font-sans"
                    />
                    
                    <button
                      type="submit"
                      className="p-3 rounded-xl bg-gradient-to-r from-[#00D2FF] to-[#9D00FF] text-white shadow-[0_0_10px_rgba(0,210,255,0.2)] hover:shadow-[0_0_15px_rgba(0,210,255,0.45)] transition-all cursor-pointer flex items-center justify-center shrink-0"
                    >
                      <i className="lucide-send w-3.5 h-3.5"></i>
                    </button>
                  </form>
                </div>

                {/* Column 3: Telemetry (3 cols) */}
                <div className="hidden lg:flex lg:col-span-3 flex-col justify-between glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 relative">
                  <div>
                    <span className="text-[9px] text-[#9D00FF] font-bold uppercase tracking-widest border border-[#9D00FF]/30 px-2 py-0.5 rounded bg-[#9D00FF]/5 font-outfit inline-block mb-5">
                      TELEMETRY CONSOLE
                    </span>
                    
                    <h4 className="text-xs font-bold text-white uppercase tracking-wider font-outfit mb-4">Saved Parameters</h4>
                    
                    <div className="flex flex-col gap-3">
                      {[
                        { label: 'Goal Coordinate', value: profile.goal },
                        { label: 'Intensity Split', value: profile.level },
                        { label: 'Location Node', value: profile.location },
                        { label: 'Diet Matrix', value: profile.diet },
                        { label: 'Injury Flag', value: profile.injuries },
                        { label: 'Weekly Frequency', value: profile.schedule },
                        { label: 'Gender Registry', value: profile.gender },
                        { label: 'Age Value', value: profile.age ? `${profile.age} yrs` : '' },
                        { label: 'Mass Index', value: profile.weight ? `${profile.weight} kg` : '' },
                        { label: 'Height Coordinate', value: profile.height ? `${profile.height} cm` : '' }
                      ].map((item, idx) => (
                        <div key={idx} className="flex justify-between items-center text-[10px] pb-2 border-b border-white/5">
                          <span className="text-gray-500 font-semibold">{item.label}</span>
                          <span className={`font-bold font-outfit ${item.value ? 'text-[#00F0FF]' : 'text-amber-500/60 animate-pulse'}`}>
                            {item.value || 'PENDING'}
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="bg-black/35 border border-white/5 p-4 rounded-2xl">
                    <span className="text-[9px] text-[#00F0FF] font-bold uppercase tracking-wider font-outfit block mb-3">METABOLIC MATHS CONSOLE</span>
                    {profile.calculations ? (
                      <div className="flex flex-col gap-3 text-[10px] font-mono leading-normal text-gray-300">
                        <div className="border-b border-white/5 pb-2">
                          <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">1. Basal Metabolic Rate (BMR)</span>
                          <span className="text-gray-400 block mt-0.5">Formula (Mifflin-St Jeor):</span>
                          <span className="text-[#00F0FF] block font-semibold text-[9px] break-all">
                            {profile.calculations.gender.toLowerCase().includes('female') 
                              ? `(10 * ${profile.calculations.weight}) + (6.25 * ${profile.calculations.height}) - (5 * ${profile.calculations.age}) - 161`
                              : `(10 * ${profile.calculations.weight}) + (6.25 * ${profile.calculations.height}) - (5 * ${profile.calculations.age}) + 5`
                            }
                          </span>
                          <div className="flex justify-between items-center mt-1">
                            <span className="text-gray-500">Output:</span>
                            <span className="text-white font-bold font-outfit">{profile.calculations.bmr} kcal/day</span>
                          </div>
                        </div>

                        <div className="border-b border-white/5 pb-2">
                          <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">2. Daily Energy Expenditure (TDEE)</span>
                          <span className="text-gray-400 block mt-0.5">Formula: BMR * Activity Multiplier</span>
                          <span className="text-[#00F0FF] block font-semibold text-[9px]">
                            {profile.calculations.bmr} * {profile.calculations.multiplier} (Workout Frequency)
                          </span>
                          <div className="flex justify-between items-center mt-1">
                            <span className="text-gray-500">Output:</span>
                            <span className="text-white font-bold font-outfit">{profile.calculations.tdee} kcal/day</span>
                          </div>
                        </div>

                        <div className="border-b border-white/5 pb-2">
                          <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">3. Calorie Intake Target</span>
                          <span className="text-gray-400 block mt-0.5">Adjustment: TDEE {profile.calculations.offset >= 0 ? '+' : '-'} {Math.abs(profile.calculations.offset)} kcal</span>
                          <span className="text-[#00F0FF] block font-semibold text-[9px]">
                            {profile.calculations.tdee} {profile.calculations.offset >= 0 ? '+' : '-'} {Math.abs(profile.calculations.offset)} (Goal Adjusted)
                          </span>
                          <div className="flex justify-between items-center mt-1">
                            <span className="text-gray-500">Output:</span>
                            <span className="text-[#00F0FF] font-bold font-outfit">{profile.calculations.targetCalories} kcal/day</span>
                          </div>
                        </div>

                        <div>
                          <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">4. Daily Macronutrient Splits</span>
                          <div className="flex flex-col gap-1.5 mt-1.5">
                            <div className="flex justify-between items-center">
                              <span className="text-gray-400">Protein: {profile.calculations.weight}kg * {profile.calculations.proteinMultiplier}g/kg</span>
                              <span className="text-[#9D00FF] font-bold font-outfit">{profile.calculations.targetProtein}g</span>
                            </div>
                            <div className="flex justify-between items-center">
                              <span className="text-gray-400">Carbs (40%): ({profile.calculations.targetCalories} * 0.4) / 4</span>
                              <span className="text-white font-bold font-outfit">{profile.calculations.targetCarbs}g</span>
                            </div>
                            <div className="flex justify-between items-center">
                              <span className="text-gray-400">Fat (30%): ({profile.calculations.targetCalories} * 0.3) / 9</span>
                              <span className="text-white font-bold font-outfit">{profile.calculations.targetFats}g</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    ) : (
                      <span className="text-[9px] text-gray-500 font-bold block italic text-center py-4 font-mono">
                        Awaiting biometric telemetry vectors...
                      </span>
                    )}
                  </div>
                </div>
              </div>

              {/* Mobile Modals */}
              {showCredsModal && (
                <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4">
                  <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 max-w-sm w-full relative">
                    <button 
                      type="button"
                      onClick={() => { playBeep(1000, 'sine', 0.05); setShowCredsModal(false); }}
                      className="absolute top-4 right-4 text-gray-400 hover:text-white font-bold"
                    >
                      ✕
                    </button>
                    <span className="text-[9px] text-[#00F0FF] font-bold uppercase tracking-widest border border-[#00F0FF]/30 px-2 py-0.5 rounded bg-[#00F0FF]/5 font-outfit inline-block mb-4">
                      CERTIFIED MENTOR
                    </span>
                    <div className="text-center mb-6">
                      <h4 className="text-base font-bold font-outfit text-white">Coach Nova</h4>
                      <p className="text-xs text-gray-400 mt-1">CSCS Strength & Transformation Coach</p>
                    </div>
                    <div className="flex flex-col gap-3 text-xs font-semibold text-gray-300">
                      <div className="flex items-center gap-2">
                        <i className="lucide-award text-[#00F0FF] w-3.5 h-3.5"></i>
                        <span>12+ Years Coaching Experience</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <i className="lucide-zap text-[#9D00FF] w-3.5 h-3.5"></i>
                        <span>Fat Loss & Muscle Building Specialist</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <i className="lucide-activity text-[#00F0FF] w-3.5 h-3.5"></i>
                        <span>5,240+ Verified Transformations</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <i className="lucide-heart text-[#9D00FF] w-3.5 h-3.5"></i>
                        <span>99.4% Goal Success Rate</span>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {showTelemetryModal && (
                <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4">
                  <div className="glass-panel p-6 rounded-3xl glow-border card-radial-purple border-white/5 max-w-sm w-full max-h-[90vh] overflow-y-auto relative">
                    <button 
                      type="button"
                      onClick={() => { playBeep(1000, 'sine', 0.05); setShowTelemetryModal(false); }}
                      className="absolute top-4 right-4 text-gray-400 hover:text-white font-bold"
                    >
                      ✕
                    </button>
                    <span className="text-[9px] text-[#9D00FF] font-bold uppercase tracking-widest border border-[#9D00FF]/30 px-2 py-0.5 rounded bg-[#9D00FF]/5 font-outfit inline-block mb-4">
                      TELEMETRY CONSOLE
                    </span>
                    <div className="flex flex-col gap-2.5 mb-6">
                      {[
                        { label: 'Goal Coordinate', value: profile.goal },
                        { label: 'Intensity Split', value: profile.level },
                        { label: 'Location Node', value: profile.location },
                        { label: 'Diet Matrix', value: profile.diet },
                        { label: 'Injury Flag', value: profile.injuries },
                        { label: 'Weekly Frequency', value: profile.schedule },
                        { label: 'Gender Registry', value: profile.gender },
                        { label: 'Age Value', value: profile.age ? `${profile.age} yrs` : '' },
                        { label: 'Mass Index', value: profile.weight ? `${profile.weight} kg` : '' },
                        { label: 'Height Coordinate', value: profile.height ? `${profile.height} cm` : '' }
                      ].map((item, idx) => (
                        <div key={idx} className="flex justify-between items-center text-[10px] pb-1.5 border-b border-white/5">
                          <span className="text-gray-500 font-semibold">{item.label}</span>
                          <span className={`font-bold font-outfit ${item.value ? 'text-[#00F0FF]' : 'text-amber-500/60 animate-pulse'}`}>
                            {item.value || 'PENDING'}
                          </span>
                        </div>
                      ))}
                    </div>
                    <div className="bg-black/35 border border-white/5 p-4 rounded-2xl">
                      <span className="text-[9px] text-[#00F0FF] font-bold uppercase tracking-wider font-outfit block mb-3">METABOLIC MATHS CONSOLE</span>
                      {profile.calculations ? (
                        <div className="flex flex-col gap-3 text-[10px] font-mono leading-normal text-gray-300">
                          <div className="border-b border-white/5 pb-2">
                            <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">1. Basal Metabolic Rate (BMR)</span>
                            <span className="text-gray-400 block mt-0.5">Formula (Mifflin-St Jeor):</span>
                            <span className="text-[#00F0FF] block font-semibold text-[9px] break-all">
                              {profile.calculations.gender.toLowerCase().includes('female') 
                                ? `(10 * ${profile.calculations.weight}) + (6.25 * ${profile.calculations.height}) - (5 * ${profile.calculations.age}) - 161`
                                : `(10 * ${profile.calculations.weight}) + (6.25 * ${profile.calculations.height}) - (5 * ${profile.calculations.age}) + 5`
                              }
                            </span>
                            <div className="flex justify-between items-center mt-1">
                              <span className="text-gray-500">Output:</span>
                              <span className="text-white font-bold font-outfit">{profile.calculations.bmr} kcal/day</span>
                            </div>
                          </div>

                          <div className="border-b border-white/5 pb-2">
                            <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">2. Daily Energy Expenditure (TDEE)</span>
                            <span className="text-gray-400 block mt-0.5">Formula: BMR * Activity Multiplier</span>
                            <span className="text-[#00F0FF] block font-semibold text-[9px]">
                              {profile.calculations.bmr} * {profile.calculations.multiplier} (Workout Frequency)
                            </span>
                            <div className="flex justify-between items-center mt-1">
                              <span className="text-gray-500">Output:</span>
                              <span className="text-white font-bold font-outfit">{profile.calculations.tdee} kcal/day</span>
                            </div>
                          </div>

                          <div className="border-b border-white/5 pb-2">
                            <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">3. Calorie Intake Target</span>
                            <span className="text-gray-400 block mt-0.5">Adjustment: TDEE {profile.calculations.offset >= 0 ? '+' : '-'} {Math.abs(profile.calculations.offset)} kcal</span>
                            <span className="text-[#00F0FF] block font-semibold text-[9px]">
                              {profile.calculations.tdee} {profile.calculations.offset >= 0 ? '+' : '-'} {Math.abs(profile.calculations.offset)} (Goal Adjusted)
                            </span>
                            <div className="flex justify-between items-center mt-1">
                              <span className="text-gray-500">Output:</span>
                              <span className="text-[#00F0FF] font-bold font-outfit">{profile.calculations.targetCalories} kcal/day</span>
                            </div>
                          </div>

                          <div>
                            <span className="text-[8px] text-gray-500 font-bold block uppercase tracking-wider">4. Daily Macronutrient Splits</span>
                            <div className="flex flex-col gap-1.5 mt-1.5">
                              <div className="flex justify-between items-center">
                                <span className="text-gray-400">Protein: {profile.calculations.weight}kg * {profile.calculations.proteinMultiplier}g/kg</span>
                                <span className="text-[#9D00FF] font-bold font-outfit">{profile.calculations.targetProtein}g</span>
                              </div>
                              <div className="flex justify-between items-center">
                                <span className="text-gray-400">Carbs (40%): ({profile.calculations.targetCalories} * 0.4) / 4</span>
                                <span className="text-white font-bold font-outfit">{profile.calculations.targetCarbs}g</span>
                              </div>
                              <div className="flex justify-between items-center">
                                <span className="text-gray-400">Fat (30%): ({profile.calculations.targetCalories} * 0.3) / 9</span>
                                <span className="text-white font-bold font-outfit">{profile.calculations.targetFats}g</span>
                              </div>
                            </div>
                          </div>
                        </div>
                      ) : (
                        <span className="text-[9px] text-gray-500 font-bold block italic text-center py-4 font-mono">
                          Awaiting biometric coordinates...
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              )}

            </div>
          </section>
        );
      };"""

# Build regex pattern to match:
# const Chatbot = () => { ... } up to (but not including) // 9. Testimonials Component
# Note: we need re.DOTALL to match across line breaks.
pattern = r"const Chatbot = \(\) => \{.*?\};(?=\s*// 9\. Testimonials Component)"

if re.search(pattern, content, re.DOTALL):
    updated_content = re.sub(pattern, lambda m: new_code, content, flags=re.DOTALL)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Success: Synchronized chatbot code in preview.html")
else:
    # Let's try matching with const Testimonials = () => { instead
    pattern_alt = r"const Chatbot = \(\) => \{.*?\};(?=\s*const Testimonials = \(\) => \{)"
    if re.search(pattern_alt, content, re.DOTALL):
        updated_content = re.sub(pattern_alt, lambda m: new_code, content, flags=re.DOTALL)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("Success: Synchronized chatbot code in preview.html (alt pattern)")
    else:
        print("Error: Could not locate Chatbot component pattern in preview.html")
