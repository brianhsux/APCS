# Grade 7 Demo 04: String Matching (Sliding Window)
# 觀念：字串搜尋 — 像窗戶一樣滑動，比對是否符合
# Run: pgzrun demo_04_string_match.py

WIDTH = 600
HEIGHT = 300

text = "ABABCABCACBAB"
pattern = "ABC"
window_idx = 0
match_idx = -1
timer = 0

def draw():
    screen.fill("black")
    
    start_x = 50
    
    # Draw Text
    for i, char in enumerate(text):
        x = start_x + i * 40
        y = 100
        color = "white"
        
        # Highlight Window
        if window_idx <= i < window_idx + len(pattern):
            screen.draw.rect(Rect(x-2, y-2, 35, 45), "yellow")
            
        if match_idx != -1 and match_idx <= i < match_idx + len(pattern):
            color = "lime"
            
        screen.draw.text(char, (x, y), fontsize=40, color=color)
        
    # Draw Pattern below window
    for i, char in enumerate(pattern):
        x = start_x + (window_idx + i) * 40
        y = 160
        screen.draw.text(char, (x, y), fontsize=40, color="cyan")
        
    if match_idx != -1:
        screen.draw.text("MATCH FOUND!", (200, 250), fontsize=40, color="lime")
    else:
        screen.draw.text("Searching...", (200, 250), fontsize=30, color="gray")

def update():
    global window_idx, match_idx, timer
    
    if match_idx != -1: return
    
    timer += 1
    if timer % 30 == 0:
        # Check match
        if text[window_idx : window_idx + len(pattern)] == pattern:
            match_idx = window_idx
        else:
            window_idx += 1
            if window_idx > len(text) - len(pattern):
                window_idx = 0 # Loop
