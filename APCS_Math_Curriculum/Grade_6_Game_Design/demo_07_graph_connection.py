# Grade 6 Demo 07: Graph Connection (Union-Find Concept)
# 觀念：圖論連通性 (Graph) — 電力公司：檢查所有城市是否都有電 (連通圖)
# Run: pgzrun demo_07_graph_connection.py

import random

WIDTH = 600
HEIGHT = 400

# Cities
cities = []
for i in range(6):
    cities.append({
        "id": i,
        "pos": (random.randint(50, 550), random.randint(50, 350)),
        "connected": False
    })

# Connections (Edges)
edges = []

def is_connected():
    # Simple BFS to check if City 0 can reach all others
    if not edges: return False
    
    visited = {0}
    queue = [0]
    
    while queue:
        curr = queue.pop(0)
        for u, v in edges:
            neighbor = None
            if u == curr: neighbor = v
            elif v == curr: neighbor = u
            
            if neighbor is not None and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return len(visited) == len(cities)

def draw():
    screen.fill("black")
    
    connected_status = is_connected()
    bg_color = "darkgreen" if connected_status else "darkred"
    screen.draw.text(f"Power Grid Status: {'ONLINE' if connected_status else 'OFFLINE'}", (20, 20), fontsize=30, color=bg_color)
    
    # Draw Edges
    for u, v in edges:
        p1 = cities[u]["pos"]
        p2 = cities[v]["pos"]
        screen.draw.line(p1, p2, "yellow")
        
    # Draw Cities
    for c in cities:
        color = "cyan"
        screen.draw.filled_circle(c["pos"], 15, color)
        screen.draw.text(str(c["id"]), (c["pos"][0]-5, c["pos"][1]-5), color="black")
        
    screen.draw.text("Click 2 cities to connect them", (20, 370), color="white")

# Interaction
selected_city = None

def on_mouse_down(pos):
    global selected_city
    
    # Find clicked city
    clicked = None
    for c in cities:
        dx = pos[0] - c["pos"][0]
        dy = pos[1] - c["pos"][1]
        if dx*dx + dy*dy < 225: # radius 15^2
            clicked = c["id"]
            break
            
    if clicked is not None:
        if selected_city is None:
            selected_city = clicked
        else:
            if selected_city != clicked:
                edges.append((selected_city, clicked))
            selected_city = None
