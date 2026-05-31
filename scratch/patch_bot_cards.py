filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Patch widget message renderer (around line 3946)
print("Patching widget message map renderer...")

target_widget_map = """                        {typedMessageIds.includes(msg.id) || msg.sender === 'user' || msg.isAlreadyTyped ? (
                          <span>{msg.text}</span>
                        ) : (
                          <TypewriterText text={msg.text} onComplete={() => setTypedMessageIds(prev => [...prev, msg.id])} scrollRef={messagesEndRef} />
                        )}
                        
                        {/* Options choices */}"""

replacement_widget_map = """                        {typedMessageIds.includes(msg.id) || msg.sender === 'user' || msg.isAlreadyTyped ? (
                          <span>{msg.text}</span>
                        ) : (
                          <TypewriterText text={msg.text} onComplete={() => setTypedMessageIds(prev => [...prev, msg.id])} scrollRef={messagesEndRef} />
                        )}

                        {isBot && msg.visualType === 'workout' && (
                          <InteractiveWorkoutCard profile={profile} />
                        )}
                        {isBot && msg.visualType === 'diet' && (
                          <InteractiveDietCard profile={profile} />
                        )}
                        {isBot && msg.visualType === 'roadmap' && (
                          <InteractiveRoadmapCard profile={profile} />
                        )}
                        
                        {/* Options choices */}"""

if target_widget_map in code:
    code = code.replace(target_widget_map, replacement_widget_map)
    print("Widget renderer successfully updated with interactive visual card hooks.")
else:
    print("ERROR: target_widget_map not found.")

# 2. Patch full message renderer (around line 4225)
print("Patching full message map renderer...")

target_full_map = """                                <div className="whitespace-pre-line font-medium font-sans">
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
                                
                                <div className="flex items-center justify-between gap-4 mt-2">"""

replacement_full_map = """                                <div className="whitespace-pre-line font-medium font-sans">
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

                                {isBot && msg.visualType === 'workout' && (
                                  <InteractiveWorkoutCard profile={profile} />
                                )}
                                {isBot && msg.visualType === 'diet' && (
                                  <InteractiveDietCard profile={profile} />
                                )}
                                {isBot && msg.visualType === 'roadmap' && (
                                  <InteractiveRoadmapCard profile={profile} />
                                )}
                                
                                <div className="flex items-center justify-between gap-4 mt-2">"""

if target_full_map in code:
    code = code.replace(target_full_map, replacement_full_map)
    print("Full chat renderer successfully updated with interactive visual card hooks.")
else:
    print("ERROR: target_full_map not found.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(code)

print("Visual card injection complete.")
