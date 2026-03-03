# Grade 3 Demo 10: Maze Runner (Final Project)
# 觀念：座標、曼哈頓距離、體力（每步扣 1）、矩陣地圖
# Run: pgzrun demo_10_maze_final.py

WIDTH = 420
HEIGHT = 460

# Map: 0=Road, 1=Wall
MAZE = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
ROWS, COLS = 7, 7
TILE = 58
# Start & End
start_r, start_c = 1, 1
end_r, end_c = 5, 5
# Player State
pr, pc = start_r, start_c
energy = 30  # Energy, -1 per step
game_over = None  # None / "win" / "lose"

def draw():
    screen.fill("black")
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * TILE, r * TILE
            if MAZE[r][c] == 1:
                screen.draw.filled_rect(Rect(x, y, TILE - 2, TILE - 2), "gray")
            else:
                screen.draw.filled_rect(Rect(x, y, TILE - 2, TILE - 2), "darkgreen")
    
    # Goal (Treasure)
    screen.draw.filled_rect(Rect(end_c * TILE + 10, end_r * TILE + 10, 36, 36), "gold")
    screen.draw.text("*", (end_c * TILE + 22, end_r * TILE + 14), fontsize=28, color="sienna")
    
    # Player
    cx = pc * TILE + TILE // 2
    cy = pr * TILE + TILE // 2
    screen.draw.filled_circle((cx, cy), 18, "red")
    screen.draw.text("Me", (cx - 8, cy - 10), fontsize=16, color="white")
    
    # Info Bar
    dist = abs(pr - end_r) + abs(pc - end_c)
    screen.draw.text(f"Energy: {energy}  Dist: {dist}", (10, 412), fontsize=20, color="white")
    
    if game_over == "win":
        screen.draw.text("YOU WIN!", (WIDTH // 2 - 60, 180), fontsize=40, color="gold")
    elif game_over == "lose":
        screen.draw.text("Out of Energy!", (WIDTH // 2 - 70, 180), fontsize=28, color="red")

def on_key_down(key):
    global pr, pc, energy, game_over
    if game_over:
        return
    dr, dc = 0, 0
    if key == keys.UP:    dr = -1
    elif key == keys.DOWN:  dr = 1
    elif key == keys.LEFT:  dc = -1
    elif key == keys.RIGHT: dc = 1
    
    nr, nc = pr + dr, pc + dc
    
    # Wall Collision
    if MAZE[nr][nc] == 1:
        return
        
    pr, pc = nr, nc
    energy -= 1
    
    if pr == end_r and pc == end_c:
        game_over = "win"
    elif energy <= 0:
        game_over = "lose"
