# Grade 5 Demo 04: Fractal Tree (Recursion)
# 觀念：遞迴 (Recursion) — 畫出一棵碎形樹，自己呼叫自己
# Run: pgzrun demo_04_recursion_tree.py

import math

WIDTH = 600
HEIGHT = 500

angle_change = 20
length_scale = 0.7

def draw():
    screen.fill("black")
    screen.draw.text(f"Angle: {angle_change}", (20, 20), color="white")
    screen.draw.text("Left/Right to change angle", (20, 40), color="gray")
    
    # Start recursion from bottom center
    draw_branch(300, 500, 100, -90)

def draw_branch(x, y, length, angle):
    if length < 5: return # Base case: stop if too small
    
    # Calculate end point
    rad = math.radians(angle)
    end_x = x + length * math.cos(rad)
    end_y = y + length * math.sin(rad)
    
    # Draw line
    color = "brown" if length > 20 else "green"
    screen.draw.line((x, y), (end_x, end_y), color)
    
    # Recursive calls (Left and Right branches)
    draw_branch(end_x, end_y, length * length_scale, angle - angle_change)
    draw_branch(end_x, end_y, length * length_scale, angle + angle_change)

def on_key_down(key):
    global angle_change
    if key == keys.RIGHT: angle_change += 5
    if key == keys.LEFT: angle_change -= 5
