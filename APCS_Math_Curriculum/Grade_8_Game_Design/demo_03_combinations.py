# Grade 8 Demo 03: Combinations (Subsets)
# 觀念：組合 — 從 N 個選 K 個，或列出所有子集合
# Run: pgzrun demo_03_combinations.py

WIDTH = 600
HEIGHT = 400

items = ["Apple", "Banana", "Cherry", "Date"]
selected = [False] * 4

def draw():
    screen.fill("midnightblue")
    screen.draw.text("Click items to form a Subset", (20, 20), fontsize=30, color="white")
    
    # Draw Items
    for i, item in enumerate(items):
        x = 50 + i * 130
        y = 100
        color = "lime" if selected[i] else "gray"
        screen.draw.filled_circle((x, y), 40, color)
        screen.draw.text(item, (x-20, y-5), color="black")
        
    # Show Current Combination
    combo = [items[i] for i in range(4) if selected[i]]
    screen.draw.text(f"Selected: {combo}", (50, 250), fontsize=30, color="yellow")
    screen.draw.text(f"Count: {len(combo)}", (50, 300), fontsize=30, color="white")

def on_mouse_down(pos):
    for i in range(4):
        x = 50 + i * 130
        y = 100
        if (pos[0]-x)**2 + (pos[1]-y)**2 < 1600:
            selected[i] = not selected[i]
