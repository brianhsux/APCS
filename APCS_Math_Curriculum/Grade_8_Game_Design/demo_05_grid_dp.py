# Grade 8 Demo 05: Grid Paths (2D DP)
# 觀念：二維動態規劃 — 只能向右或向下，計算路徑數
# Run: pgzrun demo_05_grid_dp.py

WIDTH = 500
HEIGHT = 500
ROWS, COLS = 5, 5
TILE = 80

dp = [[0]*COLS for _ in range(ROWS)]
# Init
for r in range(ROWS): dp[r][0] = 1
for c in range(COLS): dp[0][c] = 1

curr_r, curr_c = 1, 1
timer = 0

def draw():
    screen.fill("black")
    
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c*TILE + 50, r*TILE + 50
            screen.draw.rect(Rect(x, y, TILE, TILE), "white")
            
            val = dp[r][c]
            if val > 0:
                screen.draw.text(str(val), (x+30, y+30), fontsize=30, color="yellow")
                
    screen.draw.text("DP[r][c] = DP[r-1][c] + DP[r][c-1]", (50, 20), color="cyan")

def update():
    global curr_r, curr_c, timer
    timer += 1
    if timer % 10 == 0:
        if curr_r < ROWS:
            dp[curr_r][curr_c] = dp[curr_r-1][curr_c] + dp[curr_r][curr_c-1]
            
            curr_c += 1
            if curr_c >= COLS:
                curr_c = 1
                curr_r += 1
