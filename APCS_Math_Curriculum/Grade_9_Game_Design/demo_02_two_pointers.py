# Grade 9 Demo 02: Two Pointers
# 觀念：雙指標 — 在陣列頭尾各放一個指標，向中間夾擠 (例如找兩數之和)
# Run: pgzrun demo_02_two_pointers.py

WIDTH = 600
HEIGHT = 400

arr = [1, 3, 5, 7, 10, 15, 20] # Sorted
target = 17
left = 0
right = len(arr) - 1
found = False
timer = 0

def draw():
    screen.fill("black")
    
    screen.draw.text(f"Find Pair Sum = {target}", (200, 20), fontsize=30, color="gold")
    
    for i, val in enumerate(arr):
        x = 50 + i * 70
        y = 200
        color = "white"
        if i == left: color = "lime"
        if i == right: color = "cyan"
        
        screen.draw.rect(Rect(x, y, 60, 60), "gray")
        screen.draw.text(str(val), (x+15, y+15), fontsize=30, color=color)
        
        if i == left: screen.draw.text("L", (x+20, y+70), color="lime")
        if i == right: screen.draw.text("R", (x+20, y+70), color="cyan")
        
    current_sum = arr[left] + arr[right]
    screen.draw.text(f"Sum: {current_sum}", (250, 300), fontsize=40, color="white")
    
    if found:
        screen.draw.text("FOUND!", (250, 350), color="lime", fontsize=40)

def update():
    global left, right, found, timer
    if found or left >= right: return
    
    timer += 1
    if timer % 60 == 0:
        s = arr[left] + arr[right]
        if s == target:
            found = True
        elif s < target:
            left += 1
        else:
            right -= 1
