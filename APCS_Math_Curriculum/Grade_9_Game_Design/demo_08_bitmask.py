# Grade 9 Demo 08: Bitmask Subsets
# 觀念：位元運算 — 用二進位枚舉所有子集合 (000 ~ 111)
# Run: pgzrun demo_08_bitmask.py

WIDTH = 600
HEIGHT = 400

items = ["A", "B", "C"]
mask = 0
timer = 0

def draw():
    screen.fill("black")
    
    bin_str = format(mask, '03b')
    screen.draw.text(f"Mask: {bin_str} ({mask})", (200, 50), fontsize=40, color="cyan")
    
    # Draw Items
    for i in range(3):
        x = 150 + i * 100
        y = 200
        
        # Check bit i (from right)
        # item 0 corresponds to bit 0 (rightmost)
        is_on = (mask >> (2-i)) & 1
        
        color = "lime" if is_on else "gray"
        screen.draw.filled_circle((x, y), 40, color)
        screen.draw.text(items[i], (x-10, y-10), fontsize=40, color="black")
        
    subset = []
    if (mask >> 2) & 1: subset.append("A")
    if (mask >> 1) & 1: subset.append("B")
    if (mask >> 0) & 1: subset.append("C")
    
    screen.draw.text(f"Subset: {subset}", (150, 300), fontsize=30, color="yellow")

def update():
    global mask, timer
    timer += 1
    if timer % 60 == 0:
        mask = (mask + 1) % 8
