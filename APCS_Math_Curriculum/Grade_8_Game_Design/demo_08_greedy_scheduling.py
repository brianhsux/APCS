# Grade 8 Demo 08: Greedy Interval Scheduling
# 觀念：貪心演算法 — 總是選擇最早結束的活動，可以參加最多場
# Run: pgzrun demo_08_greedy_scheduling.py

WIDTH = 600
HEIGHT = 400

# Intervals: (Start, End)
intervals = [(1, 3), (2, 4), (3, 6), (5, 7), (8, 9), (0, 2)]
# Sort by End Time for Greedy
intervals.sort(key=lambda x: x[1])

selected = []
last_end = -1
curr_idx = 0
timer = 0

def draw():
    screen.fill("black")
    
    screen.draw.text("Greedy Strategy: Pick Earliest Finish Time", (20, 20), color="white")
    
    for i, (s, e) in enumerate(intervals):
        y = 100 + i * 40
        w = (e - s) * 50
        x = 50 + s * 50
        
        color = "gray"
        if i in selected: color = "lime"
        elif i == curr_idx: color = "yellow"
        
        screen.draw.filled_rect(Rect(x, y, w, 30), color)
        screen.draw.text(f"{s}-{e}", (x+5, y+5), color="black")
        
    screen.draw.text(f"Selected Count: {len(selected)}", (20, 360), fontsize=30)

def update():
    global curr_idx, last_end, timer
    
    if curr_idx >= len(intervals): return
    
    timer += 1
    if timer % 60 == 0:
        s, e = intervals[curr_idx]
        if s >= last_end:
            selected.append(curr_idx)
            last_end = e
        curr_idx += 1
