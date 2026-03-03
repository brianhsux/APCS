# Grade 7 Demo 05: Insertion Sort Visualization
# 觀念：插入排序 — 像整理撲克牌一樣，把這張牌插到前面正確的位置
# Run: pgzrun demo_05_insertion_sort.py

import random

WIDTH = 600
HEIGHT = 400

bars = [random.randint(20, 200) for _ in range(15)]
curr_i = 1
curr_j = 1
sorting = False

def draw():
    screen.fill("black")
    
    w = 30
    for idx, h in enumerate(bars):
        x = 50 + idx * 35
        y = 300 - h
        color = "white"
        
        if idx == curr_i: color = "yellow" # Current element to insert
        if idx == curr_j: color = "red"    # Comparing with
        
        screen.draw.filled_rect(Rect(x, y, w, h), color)
        screen.draw.text(str(h), (x+5, y-20), fontsize=18)
        
    screen.draw.text("Insertion Sort", (20, 20), fontsize=30, color="white")
    screen.draw.text("Press [SPACE] to Step", (20, 350), color="gray")

def on_key_down(key):
    global curr_i, curr_j, sorting, bars
    
    if key == keys.SPACE:
        if curr_i < len(bars):
            # Logic: Move bars[curr_j] backwards if smaller
            if curr_j > 0 and bars[curr_j] < bars[curr_j-1]:
                # Swap
                bars[curr_j], bars[curr_j-1] = bars[curr_j-1], bars[curr_j]
                curr_j -= 1
            else:
                # Placed correctly, move to next i
                curr_i += 1
                curr_j = curr_i
