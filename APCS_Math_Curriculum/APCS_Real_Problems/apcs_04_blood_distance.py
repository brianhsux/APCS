# APCS 真題 04: 血緣關係 (Blood Distance)
# 來源：2016-03-05 實作題 Q4 (經典難題)
# 題目：給定家族樹，計算兩個人之間的「血緣距離」
# 距離 = A到最近共同祖先的步數 + B到最近共同祖先的步數
#
# Run: pgzrun apcs_04_blood_distance.py

WIDTH = 600
HEIGHT = 400

# Tree Structure: Parent -> Children
tree = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [], 4: [], 5: []
}
# Positions for visualization
pos = {
    0: (300, 50),
    1: (200, 150), 2: (400, 150),
    3: (150, 250), 4: (250, 250), 5: (450, 250)
}

# Query: Distance between 3 and 5
target_a = 3
target_b = 5
lca = 0 # Lowest Common Ancestor (0 is root for 3 and 5)
path_a = [3, 1, 0] # Path from 3 to 0
path_b = [5, 2, 0] # Path from 5 to 0

def draw():
    screen.fill("black")
    screen.draw.text(f"Distance between {target_a} and {target_b}", (20, 20), fontsize=30, color="white")
    
    # Draw Edges
    for p in tree:
        for c in tree[p]:
            start = pos[p]
            end = pos[c]
            color = "gray"
            
            # Highlight path
            if (c in path_a and p in path_a) or (c in path_b and p in path_b):
                color = "yellow"
                
            screen.draw.line(start, end, color)
            
    # Draw Nodes
    for n, p in pos.items():
        color = "white"
        if n == target_a or n == target_b: color = "cyan"
        if n == lca: color = "lime" # LCA
        
        screen.draw.filled_circle(p, 20, color)
        screen.draw.text(str(n), (p[0]-5, p[1]-5), color="black")
        
    # Info
    dist = (len(path_a)-1) + (len(path_b)-1)
    screen.draw.text(f"LCA (Common Ancestor): {lca}", (20, 320), color="lime")
    screen.draw.text(f"Distance: {dist}", (20, 350), fontsize=40, color="yellow")
    screen.draw.text("(3 -> 1 -> 0) + (0 <- 2 <- 5)", (250, 360), color="gray")

def update():
    pass
