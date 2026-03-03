# Grade 6 Demo 01: Vector Movement (Physics)
# 觀念：向量運算 (Vector) — 模擬太空船慣性漂移與重力吸引
# Run: pgzrun demo_01_vector_movement.py

import math

WIDTH = 600
HEIGHT = 400

# Position, Velocity, Acceleration
pos = [300, 200]
vel = [0, 0]
acc = [0, 0]

# Planet (Gravity Source)
planet_pos = [300, 200]
planet_mass = 500

def draw():
    screen.fill("black")
    
    # Planet
    screen.draw.filled_circle(planet_pos, 30, "blue")
    
    # Ship
    screen.draw.filled_circle(pos, 10, "white")
    # Draw Velocity Vector
    screen.draw.line(pos, (pos[0] + vel[0]*10, pos[1] + vel[1]*10), "red")
    
    screen.draw.text(f"Vel: ({vel[0]:.2f}, {vel[1]:.2f})", (10, 10), color="white")
    screen.draw.text("Arrow Keys to Thrust", (10, 30), color="gray")

def update():
    global vel, pos
    
    # Gravity (F = G * m1 * m2 / r^2)
    dx = planet_pos[0] - pos[0]
    dy = planet_pos[1] - pos[1]
    dist = math.sqrt(dx*dx + dy*dy)
    
    if dist > 30: # Don't pull if too close (crash)
        force = planet_mass / (dist * dist)
        angle = math.atan2(dy, dx)
        acc[0] = math.cos(angle) * force
        acc[1] = math.sin(angle) * force
    else:
        acc[0] = 0
        acc[1] = 0
        
    # Thrust (Player Input)
    if keyboard.left: acc[0] -= 0.1
    if keyboard.right: acc[0] += 0.1
    if keyboard.up: acc[1] -= 0.1
    if keyboard.down: acc[1] += 0.1
    
    # Physics Update
    vel[0] += acc[0]
    vel[1] += acc[1]
    pos[0] += vel[0]
    pos[1] += vel[1]
    
    # Wrap around screen
    pos[0] %= WIDTH
    pos[1] %= HEIGHT
