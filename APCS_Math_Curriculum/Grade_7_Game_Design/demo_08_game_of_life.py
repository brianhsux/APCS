# Grade 7 Demo 08: Game of Life (Simulation)
# 觀念：模擬 (Simulation) — 細胞自動機，根據鄰居數量決定生死
# Run: pgzrun demo_08_game_of_life.py

import random

WIDTH = 500
HEIGHT = 500
TILE = 20
COLS = WIDTH // TILE
ROWS = HEIGHT // TILE

# 0=Dead, 1=Alive
grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
paused = False

def count_neighbors(r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0: continue
            nr, nc = (r + dr) % ROWS, (c + dc) % COLS # Wrap around
            count += grid[nr][nc]
    return count

def update_grid():
    global grid
    new_grid = [[0]*COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(r, c)
            if grid[r][c] == 1:
                if n < 2 or n > 3: new_grid[r][c] = 0 # Die
                else: new_grid[r][c] = 1 # Stay
            else:
                if n == 3: new_grid[r][c] = 1 # Born
    grid = new_grid

def update():
    if not paused:
        update_grid()

def draw():
    screen.fill("black")
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE-1, TILE-1), "lime")
                
    screen.draw.text("Space to Pause/Resume", (10, 10), color="white")

def on_key_down(key):
    global paused
    if key == keys.SPACE:
        paused = not paused
