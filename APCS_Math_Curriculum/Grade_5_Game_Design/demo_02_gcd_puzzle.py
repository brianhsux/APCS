# Grade 5 Demo 02: GCD Puzzle (Euclidean Algorithm)
# 觀念：最大公因數 (GCD) — 切蛋糕/拼地磚，找出最大正方形邊長
# Run: pgzrun demo_02_gcd_puzzle.py

import math

WIDTH = 600
HEIGHT = 400

rect_w = 300
rect_h = 180
tile_size = 10 # Current tile size guess
message = "Adjust Tile Size (Up/Down)"

def draw():
    screen.fill("black")
    
    # Draw Big Rectangle
    screen.draw.rect(Rect(50, 50, rect_w, rect_h), "white")
    screen.draw.text(f"Room: {rect_w} x {rect_h}", (50, 20), fontsize=24)
    
    # Draw Tiles
    cols = rect_w // tile_size
    rows = rect_h // tile_size
    
    for r in range(rows):
        for c in range(cols):
            screen.draw.rect(Rect(50 + c*tile_size, 50 + r*tile_size, tile_size, tile_size), "cyan")
            
    # Check if perfect fit
    rem_w = rect_w % tile_size
    rem_h = rect_h % tile_size
    
    screen.draw.text(f"Tile Size: {tile_size}", (50, 250), fontsize=24, color="yellow")
    
    if rem_w == 0 and rem_h == 0:
        screen.draw.text("PERFECT FIT!", (50, 300), fontsize=32, color="lime")
        if tile_size == math.gcd(rect_w, rect_h):
             screen.draw.text("(This is the GCD - Maximum Size)", (50, 340), color="lime")
    else:
        screen.draw.text(f"Gap: {rem_w}x{rem_h}", (50, 300), fontsize=24, color="red")

def on_key_down(key):
    global tile_size
    if key == keys.UP:
        tile_size += 1
    if key == keys.DOWN and tile_size > 1:
        tile_size -= 1
