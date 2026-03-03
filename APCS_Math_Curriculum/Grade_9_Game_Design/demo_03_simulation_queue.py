# Grade 9 Demo 03: Simulation (Queue/Stack)
# 觀念：複雜模擬 — 模擬排隊或資源分配 (APCS 常見題型)
# Run: pgzrun demo_03_simulation_queue.py

WIDTH = 600
HEIGHT = 400

queue = [10, 20, 5, 15, 30] # Job durations
processing = None
timer = 0
completed = []

def draw():
    screen.fill("black")
    
    # Draw Queue
    screen.draw.text("Waiting Queue:", (20, 50), color="gray")
    for i, job in enumerate(queue):
        screen.draw.filled_rect(Rect(20 + i*60, 80, 50, 50), "blue")
        screen.draw.text(str(job), (30 + i*60, 95), fontsize=24)
        
    # Draw Processor
    screen.draw.rect(Rect(250, 200, 100, 100), "white")
    screen.draw.text("CPU", (280, 180), color="white")
    
    if processing:
        screen.draw.filled_rect(Rect(260, 210, 80, 80), "red")
        screen.draw.text(str(processing), (280, 240), fontsize=40)
        
    # Completed
    screen.draw.text(f"Done: {len(completed)}", (20, 350), color="lime")

def update():
    global processing, timer
    
    if processing:
        processing -= 1
        if processing <= 0:
            completed.append(1)
            processing = None
    else:
        if queue:
            processing = queue.pop(0)
