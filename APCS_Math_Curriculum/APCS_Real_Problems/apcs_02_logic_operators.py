# APCS 真題 02: 邏輯運算子 (Logic Operators)
# 來源：2016-10-29 實作題 Q2
# 題目：給定 a, b, c 三個布林值 (0或1)，計算邏輯式結果
# 範例：(a AND b) OR (NOT c)
# 這裡我們做一個簡化版視覺化：AND, OR, NOT 閘的流動
#
# Run: pgzrun apcs_02_logic_operators.py

WIDTH = 600
HEIGHT = 400

# Inputs
a = 1
b = 0
c = 1

# Gate Logic
res_and = -1
res_not = -1
res_final = -1

timer = 0
flow_step = 0 # 0:Input, 1:Gate1, 2:Gate2, 3:Output

def draw():
    screen.fill("black")
    screen.draw.text("Logic: (A AND B) OR (NOT C)", (150, 20), fontsize=30, color="white")
    
    # Inputs
    draw_node(100, 100, "A", a, flow_step >= 0)
    draw_node(100, 200, "B", b, flow_step >= 0)
    draw_node(100, 300, "C", c, flow_step >= 0)
    
    # Gate 1: AND (A, B)
    draw_gate(250, 150, "AND", flow_step >= 1)
    if flow_step >= 1:
        val = 1 if (a and b) else 0
        draw_wire(130, 100, 250, 150, a)
        draw_wire(130, 200, 250, 150, b)
        screen.draw.text(str(val), (260, 180), color="yellow")
        
    # Gate 2: NOT (C)
    draw_gate(250, 300, "NOT", flow_step >= 1)
    if flow_step >= 1:
        val = 0 if c else 1
        draw_wire(130, 300, 250, 300, c)
        screen.draw.text(str(val), (260, 330), color="yellow")

    # Gate 3: OR (Result1, Result2)
    draw_gate(400, 225, "OR", flow_step >= 2)
    if flow_step >= 2:
        v1 = 1 if (a and b) else 0
        v2 = 0 if c else 1
        res = 1 if (v1 or v2) else 0
        
        draw_wire(290, 150, 400, 225, v1)
        draw_wire(290, 300, 400, 225, v2)
        
        if flow_step >= 3:
            screen.draw.text(f"OUTPUT: {res}", (450, 220), fontsize=40, color="lime" if res else "red")

    screen.draw.text("Press [SPACE] to Toggle Inputs", (150, 370), color="gray")

def draw_node(x, y, label, val, active):
    color = "lime" if val else "red"
    if not active: color = "gray"
    screen.draw.filled_circle((x, y), 20, color)
    screen.draw.text(f"{label}:{val}", (x-15, y-10), color="black")

def draw_gate(x, y, label, active):
    color = "cyan" if active else "dimgray"
    screen.draw.rect(Rect(x, y-20, 40, 40), color)
    screen.draw.text(label, (x+5, y-10), fontsize=14)

def draw_wire(x1, y1, x2, y2, val):
    color = "lime" if val else "red"
    screen.draw.line((x1, y1), (x2, y2), color)

def update():
    global timer, flow_step
    timer += 1
    if timer % 60 == 0:
        flow_step = (flow_step + 1) % 4

def on_key_down(key):
    global a, b, c, flow_step
    if key == keys.SPACE:
        # Randomize inputs
        import random
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0, 1)
        flow_step = 0
