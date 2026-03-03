# Grade 3 Demo 03: Manhattan Distance
# 觀念：不能走斜線時，距離 = |x1-x2| + |y1-y2|
# Run: pgzrun demo_03_distance.py

WIDTH = 600
HEIGHT = 400

# Player
px, py = 80, 80
# Treasure position
treasure_x, treasure_y = 500, 320
SPEED = 5

def distance_manhattan(x1, y1, x2, y2):
    """Manhattan Distance: |x1-x2| + |y1-y2|"""
    return abs(x1 - x2) + abs(y1 - y2)

def draw():
    screen.fill("darkgreen")
    
    # Treasure (Square)
    screen.draw.filled_rect(Rect(treasure_x - 20, treasure_y - 15, 40, 30), "sienna")
    screen.draw.rect(Rect(treasure_x - 20, treasure_y - 15, 40, 30), "gold")
    screen.draw.text("?", (treasure_x - 8, treasure_y - 12), fontsize=24, color="gold")
    
    # Player (Circle)
    screen.draw.filled_circle((px, py), 12, "red")
    screen.draw.text("Me", (px - 8, py - 8), fontsize=14, color="white")
    
    # Display Distance
    d = distance_manhattan(px, py, treasure_x, treasure_y)
    screen.draw.text(f"Distance to Treasure: {d}", (20, 20), fontsize=22, color="white")
    
    if d < 40:
        screen.draw.text("Close enough! Touch to win!", (20, 50), fontsize=18, color="yellow")
    
    # Win Condition
    if d < 35:
        screen.draw.text("YOU WIN!", (WIDTH//2 - 80, HEIGHT//2 - 20), fontsize=48, color="gold")

def update():
    global px, py
    if keyboard.right:  px = px + SPEED
    if keyboard.left:   px = px - SPEED
    if keyboard.down:   py = py + SPEED
    if keyboard.up:     py = py - SPEED
    px = max(15, min(WIDTH - 15, px))
    py = max(15, min(HEIGHT - 15, py))
