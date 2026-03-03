# Grade 8 Demo 09: Frequency Map (Hash)
# 觀念：雜湊表 (Dictionary) — 快速統計每個字母出現的次數
# Run: pgzrun demo_09_frequency_map.py

WIDTH = 600
HEIGHT = 400

text = "HELLO WORLD"
freq = {}
processed_idx = 0
timer = 0

def draw():
    screen.fill("midnightblue")
    
    # Draw Text
    for i, char in enumerate(text):
        color = "white"
        if i == processed_idx: color = "yellow"
        screen.draw.text(char, (50 + i*30, 50), fontsize=40, color=color)
        
    # Draw Histogram
    keys = sorted(freq.keys())
    for i, k in enumerate(keys):
        count = freq[k]
        x = 50 + i * 50
        h = count * 50
        y = 350
        
        screen.draw.filled_rect(Rect(x, y-h, 40, h), "cyan")
        screen.draw.text(k, (x+10, y+10), fontsize=30)
        screen.draw.text(str(count), (x+10, y-h-25), color="yellow")

def update():
    global processed_idx, timer
    if processed_idx >= len(text): return
    
    timer += 1
    if timer % 30 == 0:
        char = text[processed_idx]
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
        processed_idx += 1
