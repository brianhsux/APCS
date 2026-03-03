# Grade 6 Demo 04: Dijkstra's Algorithm (Shortest Path)
# 觀念：最短路徑 (Dijkstra) — 導航系統模擬，有權重的地圖 (塞車路段)
# Run: pgzrun demo_04_shortest_path_dijkstra.py

import heapq

WIDTH = 500
HEIGHT = 500
TILE = 50

# 0=Road(1), 1=Wall(inf), 2=Traffic(5)
grid = [
    [0,0,0,0,0,2,2,2,0,0],
    [0,1,1,1,0,2,1,2,0,0],
    [0,1,0,0,0,2,1,2,0,0],
    [0,1,0,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,2,0],
    [2,2,2,1,1,1,0,0,2,0],
    [0,0,0,0,0,1,0,0,2,0],
    [0,1,1,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

start = (0, 0)
end = (9, 9)
path = []
costs = {} # Store cost to reach each cell

def solve_dijkstra():
    global path, costs
    pq = [(0, start)] # (cost, (r, c))
    costs = {start: 0}
    parent = {}
    
    while pq:
        cost, curr = heapq.heappop(pq)
        
        if curr == end:
            # Reconstruct
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return
            
        if cost > costs.get(curr, float('inf')):
            continue
            
        r, c = curr
        neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        
        for nr, nc in neighbors:
            if 0 <= nr < 10 and 0 <= nc < 10 and grid[nr][nc] != 1:
                # Calculate weight
                weight = 1
                if grid[nr][nc] == 2: weight = 5 # Traffic jam
                
                new_cost = cost + weight
                
                if new_cost < costs.get((nr, nc), float('inf')):
                    costs[(nr, nc)] = new_cost
                    parent[(nr, nc)] = curr
                    heapq.heappush(pq, (new_cost, (nr, nc)))

solve_dijkstra()

def draw():
    screen.fill("black")
    
    for r in range(10):
        for c in range(10):
            color = "white" # Road
            if grid[r][c] == 1: color = "gray" # Wall
            elif grid[r][c] == 2: color = "orange" # Traffic
            
            if (r, c) in path: color = "cyan"
            if (r, c) == start: color = "lime"
            if (r, c) == end: color = "red"
            
            screen.draw.filled_rect(Rect(c*TILE, r*TILE, TILE-2, TILE-2), color)
            
            # Show cost
            if (r, c) in costs:
                screen.draw.text(str(costs[(r,c)]), (c*TILE+15, r*TILE+15), color="black")
                
    screen.draw.text("Dijkstra: Orange cells cost more (5)", (10, 460), color="white")
