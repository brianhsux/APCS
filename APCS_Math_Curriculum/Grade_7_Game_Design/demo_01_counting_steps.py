# Grade 7 Demo 01: Counting Steps (Time Complexity)
# 觀念：時間複雜度 — 比較 O(1)、O(n)、O(n^2) 的成長速度
# Run: pgzrun demo_01_counting_steps.py

WIDTH = 600
HEIGHT = 400

n = 10
steps_1 = 1
steps_n = n
steps_n2 = n * n

def draw():
    screen.fill("black")
    
    screen.draw.text(f"Input Size (N): {n}", (20, 20), fontsize=30, color="white")
    screen.draw.text("Press UP/DOWN to change N", (20, 50), color="gray")
    
    # Draw Bars
    # O(1)
    screen.draw.text("O(1)", (50, 350), color="lime")
    h1 = min(300, steps_1 * 2)
    screen.draw.filled_rect(Rect(50, 330 - h1, 40, h1), "lime")
    screen.draw.text(str(steps_1), (50, 330 - h1 - 20), color="lime")
    
    # O(n)
    screen.draw.text("O(n)", (150, 350), color="yellow")
    hn = min(300, steps_n * 2)
    screen.draw.filled_rect(Rect(150, 330 - hn, 40, hn), "yellow")
    screen.draw.text(str(steps_n), (150, 330 - hn - 20), color="yellow")
    
    # O(n^2)
    screen.draw.text("O(n^2)", (250, 350), color="red")
    hn2 = min(300, steps_n2 * 2)
    screen.draw.filled_rect(Rect(250, 330 - hn2, 40, hn2), "red")
    screen.draw.text(str(steps_n2), (250, 330 - hn2 - 20), color="red")
    
    if steps_n2 > 150:
        screen.draw.text("O(n^2) grows VERY fast!", (350, 200), color="red", fontsize=24)

def update():
    pass

def on_key_down(key):
    global n, steps_n, steps_n2
    if key == keys.UP:
        n += 1
    if key == keys.DOWN and n > 1:
        n -= 1
    
    # Update steps
    steps_n = n
    steps_n2 = n * n
