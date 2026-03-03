# Grade 4 Demo 01: Logic Gates (AND / OR)
# 觀念：布林運算 (Boolean) — 兩個開關同時開燈才會亮 (AND)
# Run: pgzrun demo_01_logic_gates.py

WIDTH = 500
HEIGHT = 300

switch_a = False
switch_b = False

def draw():
    screen.fill("black")
    
    # Switch A
    color_a = "lime" if switch_a else "red"
    screen.draw.filled_rect(Rect(50, 100, 60, 60), color_a)
    screen.draw.text("A (Press 1)", (55, 120), color="black")
    
    # Switch B
    color_b = "lime" if switch_b else "red"
    screen.draw.filled_rect(Rect(150, 100, 60, 60), color_b)
    screen.draw.text("B (Press 2)", (155, 120), color="black")
    
    # Logic: AND (Both must be True)
    light_on = switch_a and switch_b
    
    # Wires
    screen.draw.line((110, 130), (150, 130), "white")
    screen.draw.line((210, 130), (350, 130), "white")
    
    # Light Bulb
    bulb_color = "yellow" if light_on else "gray"
    screen.draw.filled_circle((380, 130), 40, bulb_color)
    screen.draw.text("AND", (360, 125), color="black")
    
    screen.draw.text(f"A={switch_a}  B={switch_b}  ->  Result={light_on}", (50, 250), fontsize=24, color="white")

def on_key_down(key):
    global switch_a, switch_b
    if key == keys.K_1:
        switch_a = not switch_a
    if key == keys.K_2:
        switch_b = not switch_b
