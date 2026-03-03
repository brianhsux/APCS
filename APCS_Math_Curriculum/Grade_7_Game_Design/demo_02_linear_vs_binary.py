# Grade 7 Demo 02: Linear vs Binary Search
# 觀念：搜尋演算法 — 線性搜尋 (慢慢找) vs 二分搜尋 (切一半)
# Run: pgzrun demo_02_linear_vs_binary.py

import random

WIDTH = 600
HEIGHT = 400

# Sorted Array
data = sorted([random.randint(1, 99) for _ in range(20)])
target = data[random.randint(0, 19)]

# State
linear_idx = -1
binary_low = 0
binary_high = len(data) - 1
binary_mid = -1
linear_done = False
binary_done = False
timer = 0

def draw():
    screen.fill("black")
    
    screen.draw.text(f"Target: {target}", (250, 20), fontsize=40, color="gold")
    
    # Draw Array
    for i, val in enumerate(data):
        x = 30 + i * 28
        y = 150
        color = "white"
        
        # Linear Visualization (Top markers)
        if not linear_done:
            if i == linear_idx:
                screen.draw.text("L", (x+5, y-30), color="red")
                color = "red"
        
        # Binary Visualization (Bottom markers)
        if not binary_done:
            if i == binary_mid:
                screen.draw.text("M", (x+5, y+30), color="cyan")
                color = "cyan"
            elif binary_low <= i <= binary_high:
                screen.draw.rect(Rect(x, y, 25, 25), "blue")
                
        screen.draw.rect(Rect(x, y, 25, 25), "gray")
        screen.draw.text(str(val), (x+5, y+5), color=color)
        
    screen.draw.text("Linear Search (Red)", (50, 300), color="red")
    screen.draw.text("Binary Search (Cyan)", (350, 300), color="cyan")
    
    if linear_done and binary_done:
        screen.draw.text("Press [SPACE] to Reset", (200, 350), color="white")

def update():
    global linear_idx, linear_done, binary_low, binary_high, binary_mid, binary_done, timer
    
    if linear_done and binary_done: return
    
    timer += 1
    if timer % 30 == 0:
        # Linear Step
        if not linear_done:
            linear_idx += 1
            if data[linear_idx] == target:
                linear_done = True
                
        # Binary Step
        if not binary_done:
            binary_mid = (binary_low + binary_high) // 2
            if data[binary_mid] == target:
                binary_done = True
            elif data[binary_mid] < target:
                binary_low = binary_mid + 1
            else:
                binary_high = binary_mid - 1

def on_key_down(key):
    if key == keys.SPACE:
        reset()

def reset():
    global data, target, linear_idx, binary_low, binary_high, binary_mid, linear_done, binary_done
    data = sorted([random.randint(1, 99) for _ in range(20)])
    target = data[random.randint(0, 19)]
    linear_idx = -1
    binary_low = 0
    binary_high = len(data) - 1
    binary_mid = -1
    linear_done = False
    binary_done = False
