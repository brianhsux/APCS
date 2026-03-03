# Grade 8 Demo 07: Unweighted Shortest Path (BFS)
# 觀念：最短路徑 — 在無權重圖中，BFS 保證找到最短路徑
# Run: pgzrun demo_07_shortest_path_unweighted.py

WIDTH = 400
HEIGHT = 400
TILE = 40

grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,0,1,1,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,1,0,0,0,1,1,1,1,0],
    [0,1,1,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

start = (0, 0)
end = (9, 9)
queue = [(start, [])] # (pos, path)
final_path = []
visited = {start}
timer = 0

def draw():
    screen.fill("black")
    for r in range(10):
        for c in range(10):
            color = "black"
            if grid[r][c] == 1: color = "gray"
            elif (r, c) == start: color = "lime"
            elif (r, c) == end: color = "red"
            
            if (r, c) in visited: color = "darkblue"
            if (r, c) in final_path: color = "gold"
            
            screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE-2, TILE-2), color)

def update():
    global timer, final_path
    if final_path: return
    
    timer += 1
    if timer % 5 == 0 and queue:
        (r, c), path = queue.pop(0)
        
        if (r, c) == end:
            final_path = path + [(r, c)]
            return
            
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 10 and 0 <= nc < 10 and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(r, c)]))
