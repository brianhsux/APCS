# Grade 3 Demo 02: Boundary Check (Logic: If/Else)
# 觀念：邏輯判斷 (if) — 讓角色不要跑出畫面外
# Run: pgzrun demo_02_boundaries.py

WIDTH = 600
HEIGHT = 400

px, py = 300, 200
SPEED = 5
message = "Moving safely..."

def draw():
    screen.fill("indigo")
    # Draw boundary box
    screen.draw.rect(Rect(50, 50, 500, 300), "white")
    
    screen.draw.filled_circle((px, py), 20, "cyan")
    screen.draw.text(f"({px}, {py})", (px-20, py-40), color="white")
    screen.draw.text(message, (20, 20), fontsize=24, color="yellow")

def update():
    global px, py, message
    
    # Try to move
    if keyboard.right: px += SPEED
    if keyboard.left:  px -= SPEED
    if keyboard.down:  py += SPEED
    if keyboard.up:    py -= SPEED
    
    # Boundary Logic
    # 如果 x 小於 50 (太左邊)，就讓 x 停在 50
    if px < 50:
        px = 50
        message = "Hit Left Wall!"  # 撞到左牆
    elif px > 550:
        px = 550
        message = "Hit Right Wall!" # 撞到右牆
    elif py < 50:
        py = 50
        message = "Hit Top Wall!"   # 撞到上牆
    elif py > 350:
        py = 350
        message = "Hit Bottom Wall!" # 撞到下牆
    else:
        message = "Moving safely..."
