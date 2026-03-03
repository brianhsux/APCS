# Grade 9 Demo 01: Standard I/O Practice
# 觀念：輸入輸出 — 模擬 APCS 的 input().split() 讀取過程
# Run: pgzrun demo_01_io_practice.py

WIDTH = 600
HEIGHT = 400

raw_input = "5 10 20 15 30"
parsed_data = []
current_token = ""
state = "READING" # READING, SPLITTING, MAPPING
timer = 0

def draw():
    screen.fill("black")
    
    screen.draw.text("Input String:", (20, 50), color="gray")
    screen.draw.text(f'"{raw_input}"', (20, 80), fontsize=40, color="white")
    
    screen.draw.text("Parsed Integers (List):", (20, 200), color="gray")
    
    for i, val in enumerate(parsed_data):
        screen.draw.rect(Rect(20 + i*60, 230, 50, 50), "blue")
        screen.draw.text(str(val), (30 + i*60, 245), fontsize=30)
        
    screen.draw.text(f"State: {state}", (20, 350), color="yellow")

def update():
    global state, timer, raw_input, parsed_data
    
    timer += 1
    if timer % 60 == 0:
        if state == "READING":
            state = "SPLITTING"
        elif state == "SPLITTING":
            tokens = raw_input.split()
            # Visualize one by one? For now just bulk
            parsed_data = [int(x) for x in tokens]
            state = "DONE"
