# Grade 3 Demo 08: Falling Rocks (Random)
# 觀念：亂數 (Random) — 每次石頭掉下來的位置都不一樣
# Run: pgzrun demo_08_falling_rocks.py

import random

WIDTH = 400
HEIGHT = 600

player_x = 200
player_y = 550
# Rock
rock_x = random.randint(20, 380)
rock_y = -50
score = 0
game_over = False

def draw():
    screen.fill("black")
    if game_over:
        screen.draw.text("GAME OVER", (100, 250), fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}", (120, 320), fontsize=40, color="white")
        return

    screen.draw.filled_circle((player_x, player_y), 20, "lime")
    screen.draw.filled_circle((rock_x, rock_y), 25, "gray")
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

def update():
    global player_x, rock_x, rock_y, score, game_over
    
    if game_over: return

    # Player Movement
    if keyboard.left: player_x -= 5
    if keyboard.right: player_x += 5
    
    # Rock Falling (y increases)
    rock_y += 5
    
    # Reset Rock
    if rock_y > HEIGHT:
        rock_y = -50
        rock_x = random.randint(20, 380) # Random X
        score += 1
        
    # Collision Check
    if abs(player_x - rock_x) < 40 and abs(player_y - rock_y) < 40:
        game_over = True
