# Grade 5 Demo 08: Queue Simulator (Queue)
# 觀念：佇列 (Queue) — 飲料店排隊模擬，先進先出 (FIFO)
# Run: pgzrun demo_08_queue_customer.py

import random

WIDTH = 600
HEIGHT = 400

queue = [] # List as Queue
timer = 0
served_count = 0

def draw():
    screen.fill("black")
    
    # Counter
    screen.draw.filled_rect(Rect(450, 100, 10, 200), "gray")
    screen.draw.text("Counter", (480, 200), color="white")
    
    # Draw Customers in Queue
    for i, customer in enumerate(queue):
        x = 400 - i * 50
        y = 200
        screen.draw.filled_circle((x, y), 20, customer["color"])
        screen.draw.text(str(customer["id"]), (x-5, y-5), color="black")
        
    screen.draw.text(f"Served: {served_count}", (20, 20), fontsize=30, color="lime")
    screen.draw.text("Press [A] to Add Customer, [S] to Serve", (20, 350), color="yellow")
    screen.draw.text("Queue (FIFO): First In, First Out", (20, 370), color="gray")

def on_key_down(key):
    global served_count
    
    if key == keys.A:
        # Enqueue
        if len(queue) < 8:
            new_c = {
                "id": random.randint(10, 99),
                "color": (random.randint(50,255), random.randint(50,255), random.randint(50,255))
            }
            queue.insert(0, new_c) # Add to back (left side visually)
            
    if key == keys.S:
        # Dequeue
        if queue:
            queue.pop() # Remove from front (right side visually)
            served_count += 1
