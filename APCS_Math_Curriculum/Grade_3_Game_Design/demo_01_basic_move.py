# Grade 3 Demo 01: Basic Movement (Coordinates)
# 觀念：螢幕就是 (x, y) 方格紙，移動 = 加減法
# Run: pgzrun demo_01_basic_move.py

WIDTH = 600
HEIGHT = 400

# Player position (px, py)
px = 100
py = 200
SPEED = 4

def draw():
    screen.fill("midnightblue")
    # Draw player (Circle)
    screen.draw.filled_circle((px, py), 15, "gold")
    screen.draw.circle((px, py), 15, "white")
    
    # Display coordinates
    # 顯示座標：讓學生看到數字和位置的關係
    screen.draw.text(f"Position: (x={px}, y={py})", (20, 20), fontsize=24, color="white")
    screen.draw.text("Use Arrow Keys to Move", (20, 50), fontsize=18, color="lightgray")

def update():
    global px, py
    if keyboard.right:
        px = px + SPEED
    if keyboard.left:
        px = px - SPEED
    if keyboard.down:
        py = py + SPEED
    if keyboard.up:
        py = py - SPEED
    
    # Prevent going out of screen (Optional: Boundary Check)
    # 簡單的邊界檢查
    px = max(15, min(WIDTH - 15, px))
    py = max(15, min(HEIGHT - 15, py))
