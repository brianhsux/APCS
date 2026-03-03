# Grade 3 Demo 04: Chase AI (Coordinate Comparison)
# 觀念：比較大小 — 如果鬼的 x 比我小，鬼就往右走 (x變大) 來抓我
# Run: pgzrun demo_04_chase.py

WIDTH = 600
HEIGHT = 400

# Theme: Mouse vs Cat
mouse = Actor('mouse')
mouse.pos = (100, 100)

cat = Actor('cat_face')
cat.pos = (500, 300)

PLAYER_SPEED = 4
ENEMY_SPEED = 2  # Cat is slower
game_over = False

def draw():
    screen.fill("black")
    if game_over:
        screen.draw.text("CAUGHT!", (200, 180), fontsize=60, color="red")
        return

    mouse.draw()
    cat.draw()
    
    screen.draw.text("Run Mouse! The Cat is chasing you!", (10, 10), color="gray")

def update():
    global game_over
    
    if game_over: return

    # Player Movement
    if keyboard.right: mouse.x += PLAYER_SPEED
    if keyboard.left:  mouse.x -= PLAYER_SPEED
    if keyboard.down:  mouse.y += PLAYER_SPEED
    if keyboard.up:    mouse.y -= PLAYER_SPEED
    
    # AI Logic (Chase)
    # 如果貓在老鼠左邊 (cat.x < mouse.x)，貓就要往右走
    if cat.x < mouse.x:
        cat.x += ENEMY_SPEED
    elif cat.x > mouse.x:
        cat.x -= ENEMY_SPEED
        
    if cat.y < mouse.y:
        cat.y += ENEMY_SPEED
    elif cat.y > mouse.y:
        cat.y -= ENEMY_SPEED
        
    # Collision Check
    dist = abs(mouse.x - cat.x) + abs(mouse.y - cat.y)
    if dist < 30:
        game_over = True
