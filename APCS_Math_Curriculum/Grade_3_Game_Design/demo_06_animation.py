# Grade 3 Demo 06: Animation with Modulo
# 觀念：用 frame % 2 輪流顯示 圖片 → 走路動畫
# Run: pgzrun demo_06_animation.py

WIDTH = 500
HEIGHT = 350

# Theme: Rabbit Jumping
# Using 2 frames: rabbit (stand), rabbit_jump (jump)
rabbit = Actor('rabbit')
rabbit.pos = (250, 200)
SPEED = 3
frame_count = 0

def update(dt=0):
    global frame_count
    frame_count += 1
    
    if keyboard.right: rabbit.x += SPEED
    if keyboard.left:  rabbit.x -= SPEED
    if keyboard.down:  rabbit.y += SPEED
    if keyboard.up:    rabbit.y -= SPEED
    
    rabbit.x = max(20, min(WIDTH - 20, rabbit.x))
    rabbit.y = max(50, min(HEIGHT - 20, rabbit.y))
    
    # Animation Logic
    # Switch image every 10 frames
    anim_idx = (frame_count // 10) % 2
    if anim_idx == 0:
        rabbit.image = 'rabbit'
    else:
        rabbit.image = 'rabbit_jump'

def draw():
    screen.fill("cornflowerblue")
    
    # Draw Ground
    screen.draw.filled_rect(Rect(0, 300, 500, 50), "green")
    
    rabbit.draw()
        
    screen.draw.text(f"Frame % 2 = {(frame_count // 10) % 2}", (20, 20), fontsize=20, color="white")
    screen.draw.text("Use Arrow Keys to Hop", (20, 48), fontsize=16, color="lightgray")
