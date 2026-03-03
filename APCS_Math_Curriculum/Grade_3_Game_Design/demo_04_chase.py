# Grade 3 Demo 04: Chase AI (Coordinate Comparison)
# 觀念：比較大小 — 如果鬼的 x 比我小，鬼就往右走 (x變大) 來抓我
# Run: pgzrun demo_04_chase.py

WIDTH = 600
HEIGHT = 400

player_x, player_y = 100, 100
enemy_x, enemy_y = 500, 300
PLAYER_SPEED = 4
ENEMY_SPEED = 2  # Ghost is slower
game_over = False

def draw():
    screen.fill("black")
    if game_over:
        screen.draw.text("CAUGHT!", (200, 180), fontsize=60, color="red")
        return

    # Player
    screen.draw.filled_circle((player_x, player_y), 15, "lime")
    screen.draw.text("Me", (player_x-8, player_y-8), color="black")
    
    # Enemy (Ghost)
    screen.draw.filled_circle((enemy_x, enemy_y), 15, "red")
    screen.draw.text("Ghost", (enemy_x-20, enemy_y-8), color="white")
    
    screen.draw.text("Run! The Ghost is chasing you!", (10, 10), color="gray")

def update():
    global player_x, player_y, enemy_x, enemy_y, game_over
    
    if game_over: return

    # Player Movement
    if keyboard.right: player_x += PLAYER_SPEED
    if keyboard.left:  player_x -= PLAYER_SPEED
    if keyboard.down:  player_y += PLAYER_SPEED
    if keyboard.up:    player_y -= PLAYER_SPEED
    
    # AI Logic (Chase)
    # 如果鬼在玩家左邊 (enemy_x < player_x)，鬼就要往右走 (+speed)
    if enemy_x < player_x:
        enemy_x += ENEMY_SPEED
    elif enemy_x > player_x:
        enemy_x -= ENEMY_SPEED
        
    if enemy_y < player_y:
        enemy_y += ENEMY_SPEED
    elif enemy_y > player_y:
        enemy_y -= ENEMY_SPEED
        
    # Collision Check (Distance < 30)
    dist = abs(player_x - enemy_x) + abs(player_y - enemy_y)
    if dist < 30:
        game_over = True
