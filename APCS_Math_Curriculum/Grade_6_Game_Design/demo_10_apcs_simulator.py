# Grade 6 Demo 10: APCS Simulator (Robot Path)
# 觀念：綜合模擬 (APCS) — 模擬 APCS 考題：機器人路徑規劃與資源收集
# Run: pgzrun demo_10_apcs_simulator.py

WIDTH = 500
HEIGHT = 500
TILE = 50

# 10x10 Grid
# 0=Empty, 1=Resource, 2=Obstacle
grid = [[0]*10 for _ in range(10)]

# Setup Level
import random
for _ in range(15):
    grid[random.randint(0,9)][random.randint(0,9)] = 1 # Resource
for _ in range(10):
    grid[random.randint(0,9)][random.randint(0,9)] = 2 # Obstacle

# Robot
rx, ry = 0, 0
score = 0
program = [] # Stored commands
executing = False
cmd_idx = 0
timer = 0

def draw():
    screen.fill("black")
    
    # Draw Grid
    for r in range(10):
        for c in range(10):
            x, y = c*TILE, r*TILE
            screen.draw.rect(Rect(x, y, TILE, TILE), "dimgray")
            
            if grid[r][c] == 1:
                screen.draw.filled_circle((x+25, y+25), 10, "gold")
            elif grid[r][c] == 2:
                screen.draw.filled_rect(Rect(x+5, y+5, 40, 40), "red")
                
    # Draw Robot
    screen.draw.filled_circle((rx*TILE+25, ry*TILE+25), 20, "cyan")
    
    # UI
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    
    cmd_str = " ".join(program)
    screen.draw.text(f"Program: {cmd_str}", (10, 460), color="yellow", fontsize=20)
    screen.draw.text("Arrows to Plan, [ENTER] to Run", (10, 480), color="gray")

def update():
    global rx, ry, cmd_idx, executing, timer, score
    
    if executing:
        timer += 1
        if timer > 30: # Execute every 0.5s
            timer = 0
            if cmd_idx < len(program):
                cmd = program[cmd_idx]
                dx, dy = 0, 0
                if cmd == "U": dy = -1
                elif cmd == "D": dy = 1
                elif cmd == "L": dx = -1
                elif cmd == "R": dx = 1
                
                nx, ny = rx + dx, ry + dy
                
                # Boundary & Obstacle Check
                if 0 <= nx < 10 and 0 <= ny < 10 and grid[ny][nx] != 2:
                    rx, ry = nx, ny
                    # Collect
                    if grid[ry][rx] == 1:
                        score += 10
                        grid[ry][rx] = 0
                        
                cmd_idx += 1
            else:
                executing = False
                program.clear() # Reset

def on_key_down(key):
    if executing: return
    
    if key == keys.UP: program.append("U")
    if key == keys.DOWN: program.append("D")
    if key == keys.LEFT: program.append("L")
    if key == keys.RIGHT: program.append("R")
    
    if key == keys.RETURN:
        executing = True
        cmd_idx = 0
