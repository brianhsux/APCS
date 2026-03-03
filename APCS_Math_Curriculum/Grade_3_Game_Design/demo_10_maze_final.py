# Grade 3 Demo 10: Maze Runner (Final Project)
# 觀念：座標、曼哈頓距離、體力（每步扣 1）、矩陣地圖
# Run: pgzrun demo_10_maze_final.py

WIDTH = 420
HEIGHT = 460

# Theme: Hero in Dungeon
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

# Actors
hero = Actor('hero')
chest = Actor('chest')
wall_img = Actor('wall') # We'll use this to draw walls

# Start & End Indices
start_r, start_c = 1, 1
end_r, end_c = 5, 5

# Set initial positions
hero.pos = (start_c * TILE + TILE//2, start_r * TILE + TILE//2)
chest.pos = (end_c * TILE + TILE//2, end_r * TILE + TILE//2)

# Logic State
pr, pc = start_r, start_c
energy = 30
game_over = None

def draw():
    screen.fill("black")
    for r in range(ROWS):
        for c in range(COLS):
            x = c * TILE + TILE // 2
            y = r * TILE + TILE // 2
            
            if MAZE[r][c] == 1:
                wall_img.pos = (x, y)
                wall_img.draw()
            else:
                # Draw floor (just dark rect)
                screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE, TILE), (20, 20, 20))
    
    chest.draw()
    hero.draw()
    
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
    # Update Graphic Position
    hero.x = pc * TILE + TILE // 2
    hero.y = pr * TILE + TILE // 2
    
    energy -= 1
    
    if pr == end_r and pc == end_c:
        game_over = "win"
    elif energy <= 0:
        game_over = "lose"
