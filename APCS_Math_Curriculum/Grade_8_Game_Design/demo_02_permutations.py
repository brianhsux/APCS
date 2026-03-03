# Grade 8 Demo 02: Permutations (Backtracking)
# 觀念：排列 — 列出所有可能的順序 (ABC, ACB, BAC...)
# Run: pgzrun demo_02_permutations.py

WIDTH = 600
HEIGHT = 400

items = ["A", "B", "C"]
results = []
current_perm = []
used = [False] * 3
timer = 0

def backtrack():
    global current_perm, used, results
    if len(current_perm) == 3:
        results.append("".join(current_perm))
        return

    for i in range(3):
        if not used[i]:
            used[i] = True
            current_perm.append(items[i])
            backtrack()
            current_perm.pop()
            used[i] = False

# Pre-calculate for demo animation? 
# Actually, let's just animate the result list for simplicity in Pygame Zero
backtrack()

display_idx = 0

def draw():
    screen.fill("black")
    screen.draw.text("Permutations of [A, B, C]", (20, 20), fontsize=30, color="white")
    
    for i in range(display_idx + 1):
        if i < len(results):
            screen.draw.text(results[i], (50, 80 + i * 40), fontsize=30, color="yellow")

def update():
    global display_idx, timer
    timer += 1
    if timer % 30 == 0:
        if display_idx < len(results):
            display_idx += 1
