# Grade 6 Demo 02: Circle Collision (Geometry)
# 觀念：幾何距離 (Geometry) — 圓形碰撞檢測 (距離公式 < 半徑和)
# Run: pgzrun demo_02_collision_circle.py

import math
import random

WIDTH = 600
HEIGHT = 400

# Player
p_pos = [300, 200]
p_radius = 20

# Enemies
enemies = []
for _ in range(5):
    enemies.append({
        "pos": [random.randint(0, WIDTH), random.randint(0, HEIGHT)],
        "radius": random.randint(15, 40),
        "vel": [random.uniform(-1, 1), random.uniform(-1, 1)],
        "color": "red"
    })

def draw():
    screen.fill("black")
    
    # Player
    screen.draw.filled_circle(p_pos, p_radius, "lime")
    
    # Enemies
    for e in enemies:
        screen.draw.filled_circle(e["pos"], e["radius"], e["color"])
        # Draw Radius Line
        screen.draw.circle(e["pos"], e["radius"], "white")
        
    screen.draw.text("Move with Mouse", (10, 10), color="white")

def update():
    global p_pos
    
    # Mouse Follow
    # (In Pygame Zero update(), we don't get mouse pos directly easily without event, 
    # so we'll use a simple approach or just keyboard)
    if keyboard.left: p_pos[0] -= 3
    if keyboard.right: p_pos[0] += 3
    if keyboard.up: p_pos[1] -= 3
    if keyboard.down: p_pos[1] += 3
    
    for e in enemies:
        # Move Enemy
        e["pos"][0] += e["vel"][0]
        e["pos"][1] += e["vel"][1]
        
        # Bounce off walls
        if e["pos"][0] < 0 or e["pos"][0] > WIDTH: e["vel"][0] *= -1
        if e["pos"][1] < 0 or e["pos"][1] > HEIGHT: e["vel"][1] *= -1
        
        # Collision Detection
        # Dist < r1 + r2
        dx = p_pos[0] - e["pos"][0]
        dy = p_pos[1] - e["pos"][1]
        dist = math.sqrt(dx*dx + dy*dy)
        
        if dist < p_radius + e["radius"]:
            e["color"] = "yellow" # Hit!
        else:
            e["color"] = "red"
