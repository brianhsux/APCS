# Grade 3 Demo 07: Shooting Star (Vector)
# 觀念：子彈一旦發射，就會依照固定的速度 (vx, vy) 一直飛，直到飛出螢幕
# Run: pgzrun demo_07_shooting.py

WIDTH = 600
HEIGHT = 400

# Theme: Rocket shooting Meteors
rocket = Actor('rocket')
rocket.pos = (50, 200)
rocket.angle = -90 # Point right

meteor = Actor('meteor')
meteor.pos = (-100, -100) # Off screen
meteor_active = False
SPEED = 8

def draw():
    screen.fill("midnightblue")
    
    rocket.draw()
    
    if meteor_active:
        meteor.draw()
        
    screen.draw.text("Press SPACE to Shoot Meteor", (10, 370), color="white")

def update():
    global meteor_active
    
    # Player Movement (Up/Down)
    if keyboard.up: rocket.y -= 5
    if keyboard.down: rocket.y += 5
    
    # Shooting Logic
    if keyboard.space and not meteor_active:
        meteor_active = True
        meteor.pos = rocket.pos
        
    # Meteor Flight (Vector: x keeps increasing)
    if meteor_active:
        meteor.x += SPEED
        meteor.angle += 5 # Spin!
        # Reset if out of screen
        if meteor.x > WIDTH:
            meteor_active = False
