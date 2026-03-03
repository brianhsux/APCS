# Grade 6 Demo 08: Sorting Race (Algo Comparison)
# 觀念：排序演算法比較 — 泡泡排序 vs 快速排序 (模擬)，看誰跑得快
# Run: pgzrun demo_08_sorting_race.py

import random

WIDTH = 600
HEIGHT = 400

# Two identical lists
list_a = [random.randint(10, 150) for _ in range(30)]
list_b = list_a.copy()

# Sort States
# Bubble Sort State
b_i, b_j = 0, 0
b_done = False

# Selection Sort State (Simpler than Quick for visual)
s_i = 0
s_min_idx = 0
s_j = 1
s_done = False

def draw():
    screen.fill("black")
    
    # Draw List A (Bubble Sort) - Top
    screen.draw.text("Bubble Sort (Slow)", (10, 10), color="red")
    for idx, h in enumerate(list_a):
        color = "white"
        if idx == b_j: color = "red"
        screen.draw.filled_rect(Rect(idx*18 + 10, 180 - h, 15, h), color)
        
    # Draw List B (Selection Sort) - Bottom
    screen.draw.text("Selection Sort (Faster)", (10, 210), color="cyan")
    for idx, h in enumerate(list_b):
        color = "white"
        if idx == s_j: color = "cyan"
        if idx == s_i: color = "blue" # Sorted part
        screen.draw.filled_rect(Rect(idx*18 + 10, 380 - h, 15, h), color)

def update():
    global b_i, b_j, b_done, list_a
    global s_i, s_j, s_min_idx, s_done, list_b
    
    # Bubble Sort Step
    if not b_done:
        if b_i < len(list_a):
            if b_j < len(list_a) - 1 - b_i:
                if list_a[b_j] > list_a[b_j+1]:
                    list_a[b_j], list_a[b_j+1] = list_a[b_j+1], list_a[b_j]
                b_j += 1
            else:
                b_j = 0
                b_i += 1
        else:
            b_done = True
            
    # Selection Sort Step
    if not s_done:
        if s_i < len(list_b):
            if s_j < len(list_b):
                if list_b[s_j] < list_b[s_min_idx]:
                    s_min_idx = s_j
                s_j += 1
            else:
                # Swap
                list_b[s_i], list_b[s_min_idx] = list_b[s_min_idx], list_b[s_i]
                s_i += 1
                s_min_idx = s_i
                s_j = s_i + 1
        else:
            s_done = True
