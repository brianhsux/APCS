# Grade 4 Demo 09: Bubble Sort Visualization
# 觀念：兩兩比較，大的往右邊交換
# Run: pgzrun demo_09_bubble_sort.py

import random

WIDTH = 600
HEIGHT = 400

# Generate 20 random bars
bars = []
for i in range(20):
    bars.append(random.randint(50, 300))

# Sort State
i = 0 # Pass number
j = 0 # Current index
sorting = False

def draw():
    screen.fill("black")
    
    bar_width = 25
    for idx, h in enumerate(bars):
        color = "white"
        if idx == j or idx == j+1:
            color = "red" # Comparing
        if idx >= len(bars) - i:
            color = "green" # Sorted
            
        screen.draw.filled_rect(Rect(idx*30 + 10, HEIGHT-h, bar_width, h), color)
        
    screen.draw.text("Press [SPACE] to Start/Pause Sort", (10, 10), fontsize=24, color="white")

def update():
    global i, j, sorting
    if not sorting: return
    
    # Bubble Sort Logic
    if i < len(bars):
        if j < len(bars) - 1 - i:
            # Compare j and j+1
            if bars[j] > bars[j+1]:
                # Swap
                temp = bars[j]
                bars[j] = bars[j+1]
                bars[j+1] = temp
            j += 1
        else:
            # End of pass
            j = 0
            i += 1
    else:
        sorting = False # Done

def on_key_down(key):
    global sorting
    if key == keys.SPACE:
        sorting = not sorting
