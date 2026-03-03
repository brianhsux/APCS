# Grade 8 Demo 01: Recursion Stack (Factorial)
# 觀念：遞迴堆疊 — 函式呼叫自己時，電腦如何一層層記住位置
# Run: pgzrun demo_01_recursion_stack.py

WIDTH = 600
HEIGHT = 400

n = 5
call_stack = [] # Visual stack
result = 0
state = "CALL" # CALL or RETURN
current_n = n
timer = 0

def draw():
    screen.fill("black")
    
    screen.draw.text(f"Calculate Factorial({n})", (20, 20), fontsize=30, color="white")
    
    # Draw Stack
    for i, val in enumerate(call_stack):
        y = 350 - i * 50
        screen.draw.filled_rect(Rect(200, y, 200, 40), "blue")
        screen.draw.text(f"fact({val})", (260, y+10), fontsize=24, color="white")
        
    if result > 0 and not call_stack:
        screen.draw.text(f"Result: {result}", (250, 200), fontsize=50, color="lime")

def update():
    global current_n, state, result, timer
    
    if result > 0 and not call_stack: return
    
    timer += 1
    if timer % 60 == 0:
        if state == "CALL":
            if current_n > 0:
                call_stack.append(current_n)
                current_n -= 1
            else:
                state = "RETURN"
                result = 1 # Base case 0! = 1
        elif state == "RETURN":
            if call_stack:
                val = call_stack.pop()
                result *= val
