# APCS 真題 01: 成績指標 (Grade Indicators)
# 來源：2016-03-05 實作題 Q1
# 題目：輸入 N 個學生的成績，輸出：
# 1. 所有成績 (由小到大排列)
# 2. 不及格 (<60) 的最高分 (Best of Bad)
# 3. 及格 (>=60) 的最低分 (Worst of Good)
#
# Run: pgzrun apcs_01_grade.py

import random

WIDTH = 600
HEIGHT = 400

# 模擬輸入資料
scores = [random.randint(10, 100) for _ in range(10)]
# 為了視覺化，我們先不排序，按步驟來
sorted_scores = []
step = 0 # 0:Show Raw, 1:Sorting, 2:Show Result
timer = 0

best_bad = -1
worst_good = -1

def solve():
    global sorted_scores, best_bad, worst_good
    sorted_scores = sorted(scores)
    
    # Logic
    for s in sorted_scores:
        if s < 60:
            best_bad = s # Keep updating, last one is max
        else:
            if worst_good == -1: # First one found is min
                worst_good = s
                
solve()

def draw():
    screen.fill("black")
    
    screen.draw.text("APCS Q1: Grade Indicators", (20, 20), fontsize=30, color="cyan")
    
    # Draw Threshold Line
    y_60 = 350 - 60 * 3
    screen.draw.line((50, y_60), (550, y_60), "white")
    screen.draw.text("60 (Pass)", (10, y_60 - 10), color="white")
    
    # Draw Bars
    data_to_draw = scores if step == 0 else sorted_scores
    
    for i, s in enumerate(data_to_draw):
        h = s * 3
        x = 60 + i * 50
        y = 350 - h
        
        color = "gray"
        if step == 2:
            if s == best_bad: color = "red"
            elif s == worst_good: color = "lime"
            elif s < 60: color = "darkred"
            else: color = "darkgreen"
            
        screen.draw.filled_rect(Rect(x, y, 40, h), color)
        screen.draw.text(str(s), (x+10, y-20), color="white")
        
    if step == 0:
        screen.draw.text("Raw Input", (250, 370), color="gray")
    elif step >= 1:
        screen.draw.text("Sorted Output", (250, 370), color="yellow")
        
    if step == 2:
        screen.draw.text(f"Best Fail: {best_bad if best_bad != -1 else 'N/A'}", (50, 80), color="red", fontsize=30)
        screen.draw.text(f"Worst Pass: {worst_good if worst_good != -1 else 'N/A'}", (350, 80), color="lime", fontsize=30)

def update():
    global step, timer
    timer += 1
    if timer % 120 == 0: # Every 2 seconds
        step = (step + 1) % 3
