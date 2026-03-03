# Grade 3 Demo 02: Boundary Check (Logic: If/Else)
# 觀念：邏輯判斷 (if) — 讓角色不要跑出畫面外
# Run: pgzrun demo_02_boundaries.py

WIDTH = 600
HEIGHT = 400

# Theme: Penguin Ice Skating
player = Actor('penguin')
player.pos = (300, 200)
SPEED = 5
message = "Skating safely..."

def draw():
    screen.fill("aliceblue") # Icy color
    # Draw boundary box
    screen.draw.rect(Rect(50, 50, 500, 300), "blue")
    
    player.draw()
    
    screen.draw.text(f"({int(player.x)}, {int(player.y)})", (player.x-20, player.y-40), color="blue")
    screen.draw.text(message, (20, 20), fontsize=24, color="darkblue")

def update():
    global message
    
    # Try to move
    if keyboard.right: player.x += SPEED
    if keyboard.left:  player.x -= SPEED
    if keyboard.down:  player.y += SPEED
    if keyboard.up:    player.y -= SPEED
    
    # Boundary Logic
    # 如果 x 小於 50 (太左邊)，就讓 x 停在 50
    if player.x < 50:
        player.x = 50
        message = "Hit Left Wall! Ouch!"  # 撞到左牆
    elif player.x > 550:
        player.x = 550
        message = "Hit Right Wall! Ouch!" # 撞到右牆
    elif player.y < 50:
        player.y = 50
        message = "Hit Top Wall! Ouch!"   # 撞到上牆
    elif player.y > 350:
        player.y = 350
        message = "Hit Bottom Wall! Ouch!" # 撞到下牆
    else:
        message = "Skating safely..."
