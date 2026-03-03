# Grade 3 Demo 09: Coin Collector (List)
# 觀念：列表 (List) — 用一個變數存好多個金幣的位置
# Run: pgzrun demo_09_coins.py

import random

WIDTH = 600
HEIGHT = 400

player_x, player_y = 300, 200
# Create 5 coins, each is [x, y]
coins = []
for i in range(5):
    c_x = random.randint(50, 550)
    c_y = random.randint(50, 350)
    coins.append([c_x, c_y])

score = 0

def draw():
    screen.fill("darkgreen")
    screen.draw.filled_circle((player_x, player_y), 15, "white")
    
    # Draw all coins (Iterate List)
    for coin in coins:
        screen.draw.filled_circle((coin[0], coin[1]), 10, "gold")
        
    screen.draw.text(f"Coins: {score}", (10, 10), fontsize=30, color="white")
    if not coins:
        screen.draw.text("YOU WIN!", (200, 180), fontsize=60, color="yellow")

def update():
    global player_x, player_y, score
    
    if keyboard.left: player_x -= 3
    if keyboard.right: player_x += 3
    if keyboard.up: player_y -= 3
    if keyboard.down: player_y += 3
    
    # Check Coin Collection
    # Iterate backwards to safely remove items
    for coin in coins[:]:
        dist = abs(player_x - coin[0]) + abs(player_y - coin[1])
        if dist < 25:
            coins.remove(coin)
            score += 1
