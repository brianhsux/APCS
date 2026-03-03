# Grade 9 Demo 05: 2D Traversal (Spiral)
# 觀念：二維陣列走訪 — 螺旋矩陣 (模擬方向轉折)
# Run: pgzrun demo_05_2d_traversal.py

WIDTH = 500
HEIGHT = 500
TILE = 80
ROWS, COLS = 5, 5

grid = [[0]*COLS for _ in range(ROWS)]
visited = [[False]*COLS for _ in range(ROWS)]

r, c = 0, 0
dr, dc = 0, 1 # Right
timer = 0
counter = 1

def draw():
    screen.fill("black")
    
    for i in range(ROWS):
        for j in range(COLS):
            val = grid[i][j]
            if val > 0:
                screen.draw.filled_rect(Rect(j*TILE, i*TILE, TILE-2, TILE-2), "blue")
                screen.draw.text(str(val), (j*TILE+30, i*TILE+30), fontsize=30)
            else:
                screen.draw.rect(Rect(j*TILE, i*TILE, TILE-2, TILE-2), "gray")

def update():
    global r, c, dr, dc, counter, timer
    if counter > ROWS * COLS: return
    
    timer += 1
    if timer % 20 == 0:
        grid[r][c] = counter
        visited[r][c] = True
        counter += 1
        
        # Check next step
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]):
            # Turn Right: (0,1)->(1,0)->(0,-1)->(-1,0)
            dr, dc = dc, -dr
            nr, nc = r + dr, c + dc
            
        r, c = nr, nc
