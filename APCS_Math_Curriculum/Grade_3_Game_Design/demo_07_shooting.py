# Grade 3 Demo 07: Shooting Star (Vector)
# 觀念：子彈一旦發射，就會依照固定的速度 (vx, vy) 一直飛，直到飛出螢幕
# Run: pgzrun demo_07_shooting.py

WIDTH = 600
HEIGHT = 400

player_x, player_y = 50, 200
# Star Bullet (x, y, active)
star_x = -100
star_y = -100
star_active = False
SPEED = 8

def draw():
    screen.fill("midnightblue")
    # Player
    screen.draw.filled_circle((player_x, player_y), 20, "blue")
    screen.draw.text("Press SPACE to Shoot", (10, 370), color="white")
    
    # Star
    if star_active:
        screen.draw.filled_star((star_x, star_y), 4, 10, 15, "yellow")

def update():
    global player_x, player_y, star_x, star_y, star_active
    
    # Player Movement (Up/Down)
    if keyboard.up: player_y -= 5
    if keyboard.down: player_y += 5
    
    # Shooting Logic
    if keyboard.space and not star_active:
        star_active = True
        star_x = player_x + 20
        star_y = player_y
        
    # Star Flight (Vector: x keeps increasing)
    if star_active:
        star_x += SPEED
        # Reset if out of screen
        if star_x > WIDTH:
            star_active = False
