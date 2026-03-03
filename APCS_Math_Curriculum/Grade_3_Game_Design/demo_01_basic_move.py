# Grade 3 Demo 01: Basic Movement (Coordinates)
# 觀念：螢幕就是 (x, y) 方格紙，移動 = 加減法
# Run: pgzrun demo_01_basic_move.py

WIDTH = 600
HEIGHT = 400

# Theme: Cat Walk
# Player: Cat
player = Actor('cat')
player.pos = (100, 200)
SPEED = 4

def draw():
    screen.fill("midnightblue")
    
    player.draw()
    
    # Display coordinates
    # 顯示座標：讓學生看到數字和位置的關係
    screen.draw.text(f"Position: (x={int(player.x)}, y={int(player.y)})", (20, 20), fontsize=24, color="white")
    screen.draw.text("Use Arrow Keys to Move the Cat", (20, 50), fontsize=18, color="lightgray")

def update():
    if keyboard.right:
        player.x += SPEED
    if keyboard.left:
        player.x -= SPEED
    if keyboard.down:
        player.y += SPEED
    if keyboard.up:
        player.y -= SPEED
    
    # Prevent going out of screen (Optional: Boundary Check)
    # 簡單的邊界檢查
    player.x = max(20, min(WIDTH - 20, player.x))
    player.y = max(20, min(HEIGHT - 20, player.y))
