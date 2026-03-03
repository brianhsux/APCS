# Grade 3 Demo 05: Modulo & Traffic Light
# 觀念：用「除以 3 的餘數」決定現在是紅 / 黃 / 綠燈（0, 1, 2 循環）
# Run: pgzrun demo_05_traffic_light.py

WIDTH = 400
HEIGHT = 300

# Use frame count as time
LIGHT_DURATION = 60  # Change light every 60 frames
frame_count = 0

def update(dt=0):
    global frame_count
    frame_count += 1

def draw():
    global frame_count
    screen.fill("gray")
    
    # Traffic Light Box
    screen.draw.filled_rect(Rect(150, 50, 100, 220), "dimgray")
    
    # Modulo Logic: 0=Red, 1=Yellow, 2=Green
    t = (frame_count // LIGHT_DURATION) % 3
    
    # Red Light (y=70)
    color_red = "red" if t == 0 else "darkred"
    screen.draw.filled_circle((200, 90), 35, color_red)
    
    # Yellow Light (y=140)
    color_yellow = "yellow" if t == 1 else "darkgoldenrod"
    screen.draw.filled_circle((200, 160), 35, color_yellow)
    
    # Green Light (y=210)
    color_green = "lime" if t == 2 else "darkgreen"
    screen.draw.filled_circle((200, 230), 35, color_green)
    
    # Display Info
    screen.draw.text(f"Time Steps: {frame_count}", (20, 20), fontsize=18, color="white")
    screen.draw.text(f"Phase: {frame_count // LIGHT_DURATION}", (20, 42), fontsize=18, color="white")
    screen.draw.text(f"Remainder % 3 = {t} (0:Red 1:Yel 2:Grn)", (20, 64), fontsize=18, color="yellow")
