# Grade 9 Demo 06: Dijkstra Visualization
# 觀念：最短路徑 (有權重) — Dijkstra 演算法視覺化
# Run: pgzrun demo_06_dijkstra_visual.py

import heapq

WIDTH = 600
HEIGHT = 400

# Graph: Adjacency List (Node -> [(Neighbor, Cost)])
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('E', 3)],
    'D': [('F', 1)],
    'E': [('D', 2), ('F', 5)],
    'F': []
}
positions = {
    'A': (50, 200), 'B': (200, 100), 'C': (200, 300),
    'D': (400, 100), 'E': (400, 300), 'F': (550, 200)
}

pq = [(0, 'A')]
dists = {node: float('inf') for node in graph}
dists['A'] = 0
visited = set()
timer = 0

def draw():
    screen.fill("black")
    
    # Edges
    for u in graph:
        for v, w in graph[u]:
            screen.draw.line(positions[u], positions[v], "gray")
            # Draw weight roughly mid
            mx = (positions[u][0] + positions[v][0]) / 2
            my = (positions[u][1] + positions[v][1]) / 2
            screen.draw.text(str(w), (mx, my), color="yellow")
            
    # Nodes
    for n, pos in positions.items():
        color = "blue"
        if n in visited: color = "lime"
        screen.draw.filled_circle(pos, 25, color)
        screen.draw.text(f"{n}\n{dists[n]}", (pos[0]-10, pos[1]-10), color="white")

def update():
    global timer
    timer += 1
    if timer % 60 == 0 and pq:
        d, u = heapq.heappop(pq)
        
        if u in visited: return
        visited.add(u)
        
        for v, w in graph[u]:
            if dists[u] + w < dists[v]:
                dists[v] = dists[u] + w
                heapq.heappush(pq, (dists[v], v))
