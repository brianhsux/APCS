# Grade 3 Demo 09: Coin Collector (List)
# 觀念：列表 (List) — 用一個變數存好多個金幣的位置
# Run: pgzrun demo_09_coins.py

import random

WIDTH = 600
HEIGHT = 400

# Theme: Frog eating Coins
frog = Actor('frog')
frog.pos = (300, 200)

# Create 5 coins (Actors)
coins = []
for i in range(5):
    c = Actor('coin')
    c.pos = (random.randint(50, 550), random.randint(50, 350))
    coins.append(c)

score = 0

def draw():
    screen.fill("darkgreen")
    
    frog.draw()
    
    # Draw all coins (Iterate List)
    for c in coins:
        c.draw()
        
    screen.draw.text(f"Coins: {score}", (10, 10), fontsize=30, color="white")
    if not coins:
        screen.draw.text("YUMMY!", (220, 180), fontsize=60, color="yellow")

def update():
    global score
    
    if keyboard.left: frog.x -= 3
    if keyboard.right: frog.x += 3
    if keyboard.up: frog.y -= 3
    if keyboard.down: frog.y += 3
    
    # Check Coin Collection
    # Iterate backwards to safely remove items
    for c in coins[:]:
        if frog.colliderect(c):
            coins.remove(c)
            score += 1
