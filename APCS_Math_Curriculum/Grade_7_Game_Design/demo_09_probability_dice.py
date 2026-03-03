# Grade 7 Demo 09: Probability Dice (Monte Carlo)
# 觀念：機率與大數法則 — 丟越多骰子，分佈越接近理論值
# Run: pgzrun demo_09_probability_dice.py

import random

WIDTH = 600
HEIGHT = 400

counts = [0] * 7 # Index 1-6 used
total_rolls = 0

def draw():
    screen.fill("black")
    
    screen.draw.text(f"Total Rolls: {total_rolls}", (20, 20), fontsize=30)
    screen.draw.text("Hold [SPACE] to Roll Fast", (20, 50), color="gray")
    
    # Draw Histogram
    max_h = 300
    scale = 1
    if total_rolls > 0:
        max_count = max(counts)
        if max_count > 0:
            scale = 250 / max_count
            
    for i in range(1, 7):
        h = counts[i] * scale
        x = 50 + i * 80
        y = 350
        
        screen.draw.filled_rect(Rect(x, y-h, 50, h), "cyan")
        screen.draw.text(str(i), (x+20, y+10), fontsize=30)
        screen.draw.text(str(counts[i]), (x+10, y-h-20), fontsize=20, color="yellow")

def update():
    global total_rolls
    if keyboard.space:
        for _ in range(10): # Roll 10 times per frame
            roll = random.randint(1, 6)
            counts[roll] += 1
            total_rolls += 1
