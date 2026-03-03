# Grade 7 Demo 03: Prefix Sum (Range Query)
# 觀念：前綴和 — 預先算好累積加總，讓區間查詢變超快
# Run: pgzrun demo_03_prefix_sum.py

import random

WIDTH = 600
HEIGHT = 400

data = [random.randint(1, 9) for _ in range(10)]
prefix = [0] * 11
for i in range(10):
    prefix[i+1] = prefix[i] + data[i]

# Query Range [L, R]
L = 2
R = 6

def draw():
    screen.fill("black")
    
    # Draw Data Array
    screen.draw.text("Data Array:", (20, 50), color="white")
    for i, val in enumerate(data):
        x = 50 + i * 50
        y = 80
        color = "white"
        if L <= i <= R: color = "yellow" # Highlight range
        
        screen.draw.filled_rect(Rect(x, y, 40, 40), "dimgray")
        screen.draw.text(str(val), (x+15, y+10), color=color, fontsize=24)
        screen.draw.text(str(i), (x+15, y-20), color="gray", fontsize=14)
        
    # Draw Prefix Sum Array
    screen.draw.text("Prefix Sum Array (Accumulated):", (20, 200), color="cyan")
    for i, val in enumerate(prefix):
        x = 50 + (i-1) * 50 + 25 # Shift to align
        y = 230
        if i == 0: x = 20 # 0th element
        
        color = "cyan"
        if i == L: color = "red" # Subtract this
        if i == R+1: color = "lime" # Add this
        
        screen.draw.filled_rect(Rect(x, y, 40, 40), "darkblue")
        screen.draw.text(str(val), (x+10, y+10), color=color, fontsize=20)
        
    # Calculation
    screen.draw.text(f"Query Range [{L}, {R}]", (20, 320), fontsize=30, color="yellow")
    
    sum_val = prefix[R+1] - prefix[L]
    screen.draw.text(f"Sum = Prefix[{R+1}] - Prefix[{L}]", (250, 320), fontsize=24, color="white")
    screen.draw.text(f"    = {prefix[R+1]} - {prefix[L]} = {sum_val}", (250, 350), fontsize=30, color="lime")
    
    screen.draw.text("Use Arrows to change Range", (20, 370), color="gray")

def on_key_down(key):
    global L, R
    if key == keys.LEFT and L > 0: L -= 1
    if key == keys.RIGHT and L < R: L += 1
    if key == keys.UP and R < 9: R += 1
    if key == keys.DOWN and R > L: R -= 1
