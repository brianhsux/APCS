# Grade 6 Demo 06: Tree Traversal (DFS)
# 觀念：樹的走訪 (DFS/BFS) — 檔案總管模擬，遍歷所有子資料夾
# Run: pgzrun demo_06_tree_traversal.py

WIDTH = 600
HEIGHT = 400

# Simple Tree Structure
# Node: [Name, x, y, [Children]]
tree = ["Root", 300, 50, [
    ["Folder A", 150, 150, [
        ["File A1", 80, 250, []],
        ["File A2", 220, 250, []]
    ]],
    ["Folder B", 450, 150, [
        ["File B1", 380, 250, []],
        ["Sub B2", 520, 250, [
            ["File B2-1", 520, 350, []]
        ]]
    ]]
]]

visited_order = []
timer = 0

def dfs(node):
    global visited_order
    name, x, y, children = node
    visited_order.append(name)
    for child in children:
        dfs(child)

dfs(tree) # Pre-calculate order

def draw():
    screen.fill("black")
    
    # Draw Connections first
    draw_lines(tree)
    
    # Draw Nodes
    draw_nodes(tree)
    
    # Animation
    current_idx = (timer // 60) % len(visited_order)
    current_name = visited_order[current_idx]
    
    screen.draw.text(f"Visiting: {current_name}", (20, 20), fontsize=30, color="yellow")
    screen.draw.text("DFS: Depth First Search", (20, 370), color="gray")

def draw_lines(node):
    name, x, y, children = node
    for child in children:
        cx, cy = child[1], child[2]
        screen.draw.line((x, y), (cx, cy), "white")
        draw_lines(child)

def draw_nodes(node):
    name, x, y, children = node
    
    # Highlight if currently visiting
    current_idx = (timer // 60) % len(visited_order)
    is_current = (name == visited_order[current_idx])
    
    color = "lime" if is_current else "blue"
    screen.draw.filled_circle((x, y), 20, color)
    screen.draw.text(name, (x-20, y-35), color="white")
    
    for child in children:
        draw_nodes(child)

def update():
    global timer
    timer += 1
