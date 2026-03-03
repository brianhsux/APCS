# Grade 8 Demo 06: Graph Traversal (BFS/DFS)
# 觀念：圖的走訪 — 廣度優先 (排隊) vs 深度優先 (鑽到底)
# Run: pgzrun demo_06_graph_bfs_dfs.py

WIDTH = 600
HEIGHT = 400

# Adjacency List
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}
positions = {
    0: (300, 50),
    1: (200, 150),
    2: (400, 150),
    3: (100, 250),
    4: (300, 250),
    5: (500, 250)
}

visited = []
queue = [] # For BFS
stack = [] # For DFS
mode = None # "BFS" or "DFS"
timer = 0

def draw():
    screen.fill("black")
    
    # Draw Edges
    for u in graph:
        for v in graph[u]:
            screen.draw.line(positions[u], positions[v], "gray")
            
    # Draw Nodes
    for node, pos in positions.items():
        color = "white"
        if node in visited: color = "blue"
        screen.draw.filled_circle(pos, 20, color)
        screen.draw.text(str(node), (pos[0]-5, pos[1]-5), color="black")
        
    screen.draw.text("Press [B] for BFS, [D] for DFS", (20, 360), color="white")
    if mode:
        screen.draw.text(f"Mode: {mode}", (20, 20), color="yellow", fontsize=30)

def update():
    global timer
    if not mode: return
    
    timer += 1
    if timer % 30 == 0:
        if mode == "BFS" and queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.append(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        
        elif mode == "DFS" and stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)
                for neighbor in reversed(graph[curr]): # Reverse to visit left first visually
                    if neighbor not in visited:
                        stack.append(neighbor)

def on_key_down(key):
    global mode, visited, queue, stack
    if key == keys.B:
        mode = "BFS"
        visited = []
        queue = [0]
    if key == keys.D:
        mode = "DFS"
        visited = []
        stack = [0]
