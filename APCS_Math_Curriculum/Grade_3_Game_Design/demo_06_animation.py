# Grade 3 Demo 06: Animation with Modulo
# 觀念：用 frame % 3 輪流顯示 0, 1, 2 → 三張「姿勢」輪播就像在跑步
# Run: pgzrun demo_06_animation.py

WIDTH = 500
HEIGHT = 350

# Use simple shapes for 3 poses: 0=Crouch, 1=Stand, 2=Jump
px, py = 250, 200
SPEED = 3
frame_count = 0

def update(dt=0):
    global frame_count, px, py
    frame_count += 1
    
    if keyboard.right: px = px + SPEED
    if keyboard.left:  px = px - SPEED
    if keyboard.down:  py = py + SPEED
    if keyboard.up:    py = py - SPEED
    
    px = max(25, min(WIDTH - 25, px))
    py = max(50, min(HEIGHT - 25, py))

def draw():
    global frame_count
    screen.fill("cornflowerblue")
    
    # Modulo decides the frame index: 0, 1, 2, 0, 1, 2...
    frame_index = (frame_count // 10) % 3  # Slow down animation (change every 10 frames)
    
    # Draw different poses based on frame_index
    if frame_index == 0:
        screen.draw.filled_circle((px, py + 5), 20, "orange")   # Crouch (蹲)
    elif frame_index == 1:
        screen.draw.filled_circle((px, py), 20, "orange")      # Stand (站)
    else:
        screen.draw.filled_circle((px, py - 15), 20, "orange") # Jump (跳)
        
    screen.draw.text(f"Frame Index (0-2): {frame_index}", (20, 20), fontsize=20, color="white")
    screen.draw.text("Use Arrow Keys to Run", (20, 48), fontsize=16, color="lightgray")
