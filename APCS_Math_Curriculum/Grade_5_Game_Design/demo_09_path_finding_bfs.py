# Grade 5 Demo 09: BFS Path Finding (Graph)
# 觀念：廣度優先搜尋 (BFS) — 像水波一樣擴散，找出迷宮最短路徑
# Run: pgzrun demo_09_path_finding_bfs.py

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
visited = []
queue = [start]
parent = {} # To reconstruct path
path = []
timer = 0

def draw():
    screen.fill("black")
    
    for r in range(10):
        for c in range(10):
            color = "black"
            if grid[r][c] == 1: color = "gray" # Wall
            elif (r, c) in path: color = "gold" # Path
            elif (r, c) in visited: color = "darkblue" # Visited
            
            if (r, c) == start: color = "lime"
            if (r, c) == end: color = "red"
            
            screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE-2, TILE-2), color)
            
    screen.draw.text("BFS: Expanding like a wave...", (10, 380), color="white")

def update():
    global timer, path
    
    if path: return # Done
    
    timer += 1
    if timer % 5 == 0 and queue:
        current = queue.pop(0)
        
        if current == end:
            # Reconstruct path
            curr = end
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return
            
        if current not in visited:
            visited.append(current)
            
            # Neighbors (Up, Down, Left, Right)
            r, c = current
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            
            for nr, nc in neighbors:
                if 0 <= nr < 10 and 0 <= nc < 10 and grid[nr][nc] == 0:
                    if (nr, nc) not in visited and (nr, nc) not in [q for q in queue]:
                        queue.append((nr, nc))
                        parent[(nr, nc)] = current
