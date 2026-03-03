# Grade 5 Demo 10: Dungeon Generator (ProcGen)
# 觀念：隨機地圖生成 — 結合亂數與遞迴，自動產生不重複的地牢
# Run: pgzrun demo_10_dungeon_gen.py

import random

WIDTH = 500
HEIGHT = 500
TILE = 10
ROWS, COLS = 50, 50

# 1=Wall, 0=Floor
dungeon = [[1 for _ in range(COLS)] for _ in range(ROWS)]

def generate_room(x, y, w, h):
    for r in range(y, y+h):
        for c in range(x, x+w):
            if 0 < r < ROWS-1 and 0 < c < COLS-1:
                dungeon[r][c] = 0

def generate_dungeon():
    # Reset
    for r in range(ROWS):
        for c in range(COLS):
            dungeon[r][c] = 1
            
    # Simple algorithm: Random Rooms + Corridors
    rooms = []
    for _ in range(10):
        w = random.randint(5, 10)
        h = random.randint(5, 10)
        x = random.randint(1, COLS - w - 1)
        y = random.randint(1, ROWS - h - 1)
        
        generate_room(x, y, w, h)
        
        # Connect to previous room
        if rooms:
            prev_x, prev_y = rooms[-1]
            # Horizontal Tunnel
            for c in range(min(x, prev_x), max(x, prev_x) + 1):
                dungeon[prev_y][c] = 0
            # Vertical Tunnel
            for r in range(min(y, prev_y), max(y, prev_y) + 1):
                dungeon[r][x] = 0
                
        rooms.append((x + w//2, y + h//2))

generate_dungeon()

def draw():
    screen.fill("black")
    
    for r in range(ROWS):
        for c in range(COLS):
            if dungeon[r][c] == 0:
                screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE, TILE), "white")
                
    screen.draw.text("Press [SPACE] to Regenerate", (10, 480), color="red", fontsize=20)

def on_key_down(key):
    if key == keys.SPACE:
        generate_dungeon()
