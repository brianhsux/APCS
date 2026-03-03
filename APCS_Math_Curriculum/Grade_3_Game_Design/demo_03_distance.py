# Grade 3 Demo 03: Manhattan Distance
# 觀念：不能走斜線時，距離 = |x1-x2| + |y1-y2|
# Run: pgzrun demo_03_distance.py

WIDTH = 600
HEIGHT = 400

# Theme: Dog finding Bone
dog = Actor('dog')
dog.pos = (80, 80)

bone = Actor('bone')
bone.pos = (500, 320)

SPEED = 5

def distance_manhattan(x1, y1, x2, y2):
    """Manhattan Distance: |x1-x2| + |y1-y2|"""
    return abs(x1 - x2) + abs(y1 - y2)

def draw():
    screen.fill("forestgreen")
    
    bone.draw()
    dog.draw()
    
    screen.draw.text("Help the Dog find the Bone!", (20, 370), color="white")
    
    # Display Distance
    d = distance_manhattan(dog.x, dog.y, bone.x, bone.y)
    screen.draw.text(f"Distance: {int(d)}", (20, 20), fontsize=28, color="white")
    
    if d < 50:
        screen.draw.text("Woof! So close!", (20, 50), fontsize=24, color="yellow")
    
    # Win Condition
    if d < 35:
        screen.draw.text("YUMMY!", (WIDTH//2 - 80, HEIGHT//2 - 20), fontsize=60, color="gold")

def update():
    if keyboard.right:  dog.x += SPEED
    if keyboard.left:   dog.x -= SPEED
    if keyboard.down:   dog.y += SPEED
    if keyboard.up:     dog.y -= SPEED
    
    dog.x = max(20, min(WIDTH - 20, dog.x))
    dog.y = max(20, min(HEIGHT - 20, dog.y))
