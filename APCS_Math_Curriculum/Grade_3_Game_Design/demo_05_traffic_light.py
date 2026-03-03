# Grade 3 Demo 05: Modulo & Traffic Light
# 觀念：用「除以 3 的餘數」決定現在是紅 / 黃 / 綠燈（0, 1, 2 循環）
# Run: pgzrun demo_05_traffic_light.py

WIDTH = 400
HEIGHT = 300

# Theme: Car waiting for lights
car = Actor('car')
car.pos = (50, 250)

# Light Actors
light_red = Actor('light_red')
light_yellow = Actor('light_yellow')
light_green = Actor('light_green')
light_off = Actor('light_off') # Gray light for off state

# Positions
light_red.pos = (200, 90)
light_yellow.pos = (200, 160)
light_green.pos = (200, 230)

# Use frame count as time
LIGHT_DURATION = 60  # Change light every 60 frames
frame_count = 0

def update(dt=0):
    global frame_count
    frame_count += 1
    
    # Move car only on Green (Phase 2)
    phase = (frame_count // LIGHT_DURATION) % 3
    if phase == 2:
        car.x += 2
        if car.x > WIDTH + 50: car.x = -50

def draw():
    screen.fill("gray")
    
    # Traffic Light Box
    screen.draw.filled_rect(Rect(150, 50, 100, 220), "dimgray")
    
    # Modulo Logic: 0=Red, 1=Yellow, 2=Green
    phase = (frame_count // LIGHT_DURATION) % 3
    
    # Draw Lights (Draw OFF version first, then ON version if active)
    light_off.pos = light_red.pos; light_off.draw()
    light_off.pos = light_yellow.pos; light_off.draw()
    light_off.pos = light_green.pos; light_off.draw()
    
    if phase == 0:
        light_red.draw()
        status = "STOP (Red)"
    elif phase == 1:
        light_yellow.draw()
        status = "WAIT (Yellow)"
    else:
        light_green.draw()
        status = "GO! (Green)"
        
    car.draw()
    
    # Display Info
    screen.draw.text(f"Time: {frame_count}", (20, 20), fontsize=18, color="white")
    screen.draw.text(f"Phase % 3 = {phase}", (20, 42), fontsize=18, color="yellow")
    screen.draw.text(status, (250, 150), fontsize=24, color="white")
