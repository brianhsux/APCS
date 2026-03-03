# Grade 9 Demo 07: Topological Sort (Course Schedule)
# 觀念：拓樸排序 — 解決先修課程問題 (DAG)
# Run: pgzrun demo_07_topological_sort.py

WIDTH = 600
HEIGHT = 400

# Graph (DAG)
graph = {
    "Math": ["Physics", "CS"],
    "Physics": ["Eng"],
    "CS": ["AI"],
    "Eng": [],
    "AI": []
}
positions = {
    "Math": (100, 200),
    "Physics": (250, 100),
    "CS": (250, 300),
    "Eng": (400, 100),
    "AI": (400, 300)
}

in_degree = {u: 0 for u in graph}
for u in graph:
    for v in graph[u]:
        in_degree[v] += 1

queue = [u for u in in_degree if in_degree[u] == 0]
result = []
timer = 0

def draw():
    screen.fill("black")
    
    for u in graph:
        for v in graph[u]:
            # Draw arrow (simple line)
            screen.draw.line(positions[u], positions[v], "white")
            
    for n, pos in positions.items():
        color = "gray"
        if n in result: color = "lime"
        elif in_degree[n] == 0: color = "yellow" # Ready
        
        screen.draw.filled_circle(pos, 30, color)
        screen.draw.text(n, (pos[0]-20, pos[1]-10), color="black")
        
    screen.draw.text(f"Order: {result}", (50, 350), fontsize=30, color="white")

def update():
    global timer
    timer += 1
    if timer % 60 == 0 and queue:
        u = queue.pop(0)
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
