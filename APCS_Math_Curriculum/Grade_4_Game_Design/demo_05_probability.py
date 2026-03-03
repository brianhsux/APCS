# Grade 4 Demo 05: Probability Box (Random Range)
# 觀念：隨機數 1~100，用「區間」決定獎勵（1-5 金, 6-30 藍, 31-100 白）
# Run: pgzrun demo_05_probability.py

import random

WIDTH = 480
HEIGHT = 320

result_text = "Press [SPACE] to Open!"
result_color = "white"
last_roll = 0

def draw():
    screen.fill("midnightblue")
    
    # Chest
    screen.draw.filled_rect(Rect(180, 120, 120, 100), "sienna")
    screen.draw.rect(Rect(180, 120, 120, 100), "gold")
    screen.draw.text("Chest", (210, 155), fontsize=28, color="gold")
    
    # Info
    screen.draw.text("Roll 1~100: 1-5=Gold, 6-30=Blue, 31-100=White", (20, 30), fontsize=18, color="lightgray")
    screen.draw.text(result_text, (80, 260), fontsize=24, color=result_color)
    
    if last_roll > 0:
        screen.draw.text(f"Rolled: {last_roll}", (200, 235), fontsize=20, color="yellow")

def on_key_down(key):
    global result_text, result_color, last_roll
    if key != keys.SPACE:
        return
        
    roll = random.randint(1, 100)
    last_roll = roll
    
    # Probability Logic
    if 1 <= roll <= 5:
        result_text = "LEGENDARY! (Gold 5%)"
        result_color = "gold"
    elif 6 <= roll <= 30:
        result_text = "RARE! (Blue 25%)"
        result_color = "deepskyblue"
    else:
        result_text = "Common Item (White 70%)"
        result_color = "white"
