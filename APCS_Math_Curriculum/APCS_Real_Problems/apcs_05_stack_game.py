# APCS 真題 05: 數字龍捲風/堆疊遊戲 (Stack Game)
# 題目概念：模擬類似消除遊戲，這裡用一個簡化版 Stack 消除來演示
# 規則：輸入一串數字，放入 Stack，如果新數字跟 Stack 頂端一樣，則消除並得分
#
# Run: pgzrun apcs_05_stack_game.py

WIDTH = 600
HEIGHT = 400

input_stream = [1, 2, 3, 3, 2, 1, 5]
stack = []
score = 0
curr_idx = 0
timer = 0
message = ""

def draw():
    screen.fill("midnightblue")
    screen.draw.text("Stack Elimination Game", (20, 20), fontsize=30)
    
    # Draw Input Stream
    screen.draw.text("Input:", (20, 70), color="gray")
    for i, val in enumerate(input_stream):
        color = "white"
        if i == curr_idx: color = "yellow"
        elif i < curr_idx: color = "dimgray"
        screen.draw.text(str(val), (80 + i*30, 70), fontsize=30, color=color)
        
    # Draw Stack
    screen.draw.line((250, 350), (350, 350), "white")
    screen.draw.line((250, 350), (250, 100), "white")
    screen.draw.line((350, 350), (350, 100), "white")
    
    for i, val in enumerate(stack):
        y = 310 - i * 40
        screen.draw.filled_rect(Rect(260, y, 80, 30), "cyan")
        screen.draw.text(str(val), (290, y+5), color="black", fontsize=24)
        
    screen.draw.text(f"Score: {score}", (450, 100), fontsize=40, color="lime")
    screen.draw.text(message, (400, 200), color="orange")

def update():
    global curr_idx, stack, score, message, timer
    
    if curr_idx >= len(input_stream):
        message = "Done!"
        return
        
    timer += 1
    if timer % 60 == 0:
        val = input_stream[curr_idx]
        
        if stack and stack[-1] == val:
            stack.pop()
            score += 10
            message = f"Matched {val}! Pop!"
        else:
            stack.append(val)
            message = f"Push {val}"
            
        curr_idx += 1
