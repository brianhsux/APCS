# Grade 9 Demo 04: Max Sum Subarray (Kadane)
# 觀念：最大子陣列和 — Kadane's Algorithm 視覺化 (DP 技巧)
# Run: pgzrun demo_04_max_sum_subarray.py

WIDTH = 600
HEIGHT = 400

arr = [1, -3, 2, 1, -1, 3, -2, 3]
curr_sum = 0
max_sum = float('-inf')
idx = 0
timer = 0

def draw():
    screen.fill("black")
    
    for i, val in enumerate(arr):
        x = 50 + i * 60
        y = 200
        color = "white"
        if i == idx: color = "yellow"
        
        screen.draw.rect(Rect(x, y, 50, 50), "gray")
        screen.draw.text(str(val), (x+15, y+15), color=color, fontsize=24)
        
    screen.draw.text(f"Current Sum: {curr_sum}", (50, 300), color="yellow", fontsize=30)
    screen.draw.text(f"Max So Far: {max_sum}", (350, 300), color="lime", fontsize=30)

def update():
    global idx, curr_sum, max_sum, timer
    if idx >= len(arr): return
    
    timer += 1
    if timer % 60 == 0:
        val = arr[idx]
        curr_sum = max(val, curr_sum + val)
        max_sum = max(max_sum, curr_sum)
        idx += 1
