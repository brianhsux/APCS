# Grade 4 Demo 08: Flood Fill (Recursion)
# 觀念：從一個點開始，把相連的顏色都換掉
# Run: pgzrun demo_08_flood_fill.py

import sys
sys.setrecursionlimit(2000)

WIDTH = 400
HEIGHT = 400
TILE = 40
ROWS = 10
COLS = 10

# 0=Black, 1=White
grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,1,1,0,0],
    [0,1,0,1,0,0,1,0,0,0],
    [0,1,1,1,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,0,0,0,0,0,1,0],
    [0,1,0,0,0,1,1,1,1,0],
    [0,1,0,0,0,1,0,0,0,0],
    [0,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def draw():
    screen.fill("black")
    for r in range(ROWS):
        for c in range(COLS):
            color = "white" if grid[r][c] == 1 else "black"
            if grid[r][c] == 2: color = "red" # Filled
            
            screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE-1, TILE-1), color)
            
    screen.draw.text("Click White Area to Fill Red", (10, 380), color="gray")

def flood_fill(r, c):
    # Boundary Check
    if r < 0 or r >= ROWS or c < 0 or c >= COLS: return
    # Color Check (Only fill White=1)
    if grid[r][c] != 1: return
    
    # Fill
    grid[r][c] = 2
    
    # Recurse 4 directions
    flood_fill(r+1, c)
    flood_fill(r-1, c)
    flood_fill(r, c+1)
    flood_fill(r, c-1)

def on_mouse_down(pos):
    c = pos[0] // TILE
    r = pos[1] // TILE
    flood_fill(r, c)
