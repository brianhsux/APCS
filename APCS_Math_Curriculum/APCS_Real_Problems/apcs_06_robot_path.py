# APCS 真題 06: 機器人路徑 (Robot Path)
# 來源：2017-10-28 實作題 Q4 (簡化版)
# 題目：機器人在網格上移動，走到特定格子會有分數，不能走出邊界
#
# Run: pgzrun apcs_06_robot_path.py

WIDTH = 500
HEIGHT = 500
TILE = 50
ROWS = 10
COLS = 10

# 0=Empty, 1=Point
grid = [[0]*COLS for _ in range(ROWS)]
import random
# Random points
for _ in range(15):
    grid[random.randint(0,9)][random.randint(0,9)] = 1

robot_r, robot_c = 0, 0
score = 0
# Path history
path = [(0,0)]

def draw():
    screen.fill("black")
    
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c*TILE, r*TILE
            screen.draw.rect(Rect(x, y, TILE, TILE), "dimgray")
            
            if grid[r][c] == 1:
                screen.draw.filled_circle((x+25, y+25), 10, "gold")
                
            if (r, c) in path:
                screen.draw.filled_circle((x+25, y+25), 5, "blue")
                
    # Robot
    rx, ry = robot_c*TILE, robot_r*TILE
    screen.draw.filled_rect(Rect(rx+5, ry+5, 40, 40), "cyan")
    
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    screen.draw.text("Arrows to Move", (10, 470), color="gray")

def on_key_down(key):
    global robot_r, robot_c, score
    
    nr, nc = robot_r, robot_c
    if key == keys.UP: nr -= 1
    elif key == keys.DOWN: nr += 1
    elif key == keys.LEFT: nc -= 1
    elif key == keys.RIGHT: nc += 1
    
    # Boundary Check
    if 0 <= nr < ROWS and 0 <= nc < COLS:
        robot_r, robot_c = nr, nc
        path.append((nr, nc))
        
        # Collect Point
        if grid[nr][nc] == 1:
            score += 10
            grid[nr][nc] = 0
