# Grade 7 Demo 07: Bracket Checker (Stack)
# 觀念：堆疊 (Stack) — 檢查括號是否成對，左括號推入，右括號彈出
# Run: pgzrun demo_07_bracket_stack.py

WIDTH = 600
HEIGHT = 400

expr = "( ( ) [ ] ( ) )"
tokens = expr.split()
stack = []
current_idx = 0
message = "Checking..."
timer = 0
is_valid = True

def draw():
    screen.fill("black")
    
    # Draw Expression
    for i, t in enumerate(tokens):
        color = "white"
        if i == current_idx: color = "yellow"
        screen.draw.text(t, (50 + i*40, 50), fontsize=40, color=color)
        
    # Draw Stack
    screen.draw.line((100, 350), (200, 350), "white") # Base
    screen.draw.line((100, 350), (100, 150), "white") # Left
    screen.draw.line((200, 350), (200, 150), "white") # Right
    
    for i, item in enumerate(stack):
        y = 310 - i * 40
        screen.draw.filled_rect(Rect(110, y, 80, 35), "cyan")
        screen.draw.text(item, (140, y+5), color="black", fontsize=30)
        
    screen.draw.text(message, (300, 200), fontsize=30, color="white")

def update():
    global current_idx, stack, message, timer, is_valid
    
    if current_idx >= len(tokens) or not is_valid:
        if is_valid and not stack:
            message = "VALID! Stack Empty."
        elif is_valid and stack:
            message = "INVALID! Unclosed."
        return
        
    timer += 1
    if timer % 40 == 0:
        char = tokens[current_idx]
        
        if char in "([":
            stack.append(char)
            message = f"Push {char}"
        elif char in ")]":
            if not stack:
                is_valid = False
                message = "Error: Stack Empty"
            else:
                top = stack.pop()
                if (char == ")" and top == "(") or (char == "]" and top == "["):
                    message = f"Match {top} with {char}"
                else:
                    is_valid = False
                    message = f"Mismatch: {top} vs {char}"
                    
        current_idx += 1
