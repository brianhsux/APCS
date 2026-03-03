# Grade 8 Demo 10: Mini Project (Routing)
# 觀念：綜合應用 — 簡單的節點移動與路徑規劃
# Run: pgzrun demo_10_mini_project.py

WIDTH = 600
HEIGHT = 400

nodes = {
    "Home": (50, 50),
    "School": (300, 50),
    "Park": (50, 300),
    "Shop": (300, 300),
    "Cinema": (500, 200)
}
edges = [
    ("Home", "School"), ("Home", "Park"),
    ("School", "Shop"), ("Park", "Shop"),
    ("School", "Cinema"), ("Shop", "Cinema")
]

player_pos = "Home"
target = "Cinema"
path = ["Home", "School", "Cinema"] # Hardcoded shortest path for demo
step = 0
moving = False
anim_x, anim_y = nodes["Home"]

def draw():
    screen.fill("black")
    
    # Edges
    for u, v in edges:
        screen.draw.line(nodes[u], nodes[v], "gray")
        
    # Nodes
    for name, pos in nodes.items():
        color = "white"
        if name == player_pos: color = "lime"
        if name == target: color = "red"
        screen.draw.filled_circle(pos, 20, color)
        screen.draw.text(name, (pos[0]-20, pos[1]-40), color="white")
        
    # Player
    screen.draw.filled_circle((anim_x, anim_y), 10, "yellow")
    
    screen.draw.text("Press [SPACE] to Travel to Cinema", (200, 370), color="cyan")

def update():
    global step, moving, anim_x, anim_y, player_pos
    
    if moving:
        dest_name = path[step]
        dest_pos = nodes[dest_name]
        
        # Move logic
        dx = dest_pos[0] - anim_x
        dy = dest_pos[1] - anim_y
        dist = (dx**2 + dy**2)**0.5
        
        if dist < 5:
            player_pos = dest_name
            if step < len(path) - 1:
                step += 1
            else:
                moving = False
        else:
            anim_x += dx * 0.05
            anim_y += dy * 0.05

def on_key_down(key):
    global moving
    if key == keys.SPACE:
        moving = True
