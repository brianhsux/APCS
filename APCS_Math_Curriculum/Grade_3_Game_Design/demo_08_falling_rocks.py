# Grade 3 Demo 08: Falling Rocks (Random)
# 觀念：亂數 (Random) — 每次石頭掉下來的位置都不一樣
# Run: pgzrun demo_08_falling_rocks.py

import random

WIDTH = 400
HEIGHT = 600

# Theme: Chick dodging Rain Drops
chick = Actor('chick')
chick.pos = (200, 550)

drop = Actor('drop')
drop.pos = (random.randint(20, 380), -50)

score = 0
game_over = False

def draw():
    screen.fill("black")
    if game_over:
        screen.draw.text("GAME OVER", (100, 250), fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}", (120, 320), fontsize=40, color="white")
        return

    chick.draw()
    drop.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

def update():
    global score, game_over
    
    if game_over: return

    # Player Movement
    if keyboard.left: chick.x -= 5
    if keyboard.right: chick.x += 5
    
    # Drop Falling (y increases)
    drop.y += 5
    
    # Reset Drop
    if drop.y > HEIGHT:
        drop.y = -50
        drop.x = random.randint(20, 380) # Random X
        score += 1
        
    # Collision Check
    if chick.colliderect(drop):
        game_over = True
