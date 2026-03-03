# Grade 5 Demo 05: Fibonacci Rabbits (Sequence)
# 觀念：數列與遞迴 — 兔子生兔子模擬，費氏數列視覺化
# Run: pgzrun demo_05_fibonacci_rabbit.py

WIDTH = 600
HEIGHT = 400

months = 1
rabbits = [1] # Sequence: 1, 1, 2, 3, 5...

def draw():
    screen.fill("darkgreen")
    
    screen.draw.text(f"Month: {months}", (20, 20), fontsize=30, color="white")
    count = rabbits[-1]
    screen.draw.text(f"Pairs of Rabbits: {count}", (20, 60), fontsize=30, color="yellow")
    
    # Visualize Rabbits (Simple Circles)
    # Limit drawing to avoid crash
    draw_count = min(count, 200)
    for i in range(draw_count):
        x = (i % 20) * 25 + 50
        y = (i // 20) * 25 + 120
        screen.draw.filled_circle((x, y), 10, "white")
        screen.draw.circle((x, y), 10, "pink") # Ears
        
    if count > 200:
        screen.draw.text(f"... and {count - 200} more!", (50, 350), color="white")
        
    screen.draw.text("Press [SPACE] for Next Month", (20, 370), color="cyan")

def on_key_down(key):
    global months, rabbits
    if key == keys.SPACE:
        months += 1
        if len(rabbits) < 2:
            rabbits.append(1)
        else:
            # F(n) = F(n-1) + F(n-2)
            new_rabbits = rabbits[-1] + rabbits[-2]
            rabbits.append(new_rabbits)
