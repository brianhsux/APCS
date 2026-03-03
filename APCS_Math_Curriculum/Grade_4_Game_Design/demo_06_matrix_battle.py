# Grade 4 Demo 06: Matrix Battle (Index Mapping)
# 觀念：格子 (row, col) 對應陣列 grid[r][c]，選一格攻擊，打中怪物就 Hit
# Run: pgzrun demo_06_matrix_battle.py

import random

WIDTH = 400
HEIGHT = 380

ROWS, COLS = 3, 3
TILE = 100
# Monster Position
monster_r = random.randint(0, 2)
monster_c = random.randint(0, 2)

# Player Selection
selected_r, selected_c = -1, -1
hit = False
message = "Press 1-9 to Attack Grid"

def draw():
    screen.fill("darkgreen")
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * TILE + 50, r * TILE + 50
            
            # Highlight Selection
            if r == selected_r and c == selected_c:
                screen.draw.filled_rect(Rect(x, y, TILE - 4, TILE - 4), "yellow")
                screen.draw.rect(Rect(x, y, TILE - 4, TILE - 4), "white")
            else:
                screen.draw.filled_rect(Rect(x, y, TILE - 4, TILE - 4), "forestgreen")
                screen.draw.rect(Rect(x, y, TILE - 4, TILE - 4), "darkgray")
            
            # Grid Number (1~9)
            num = r * 3 + c + 1
            screen.draw.text(str(num), (x + TILE//2 - 5, y + TILE//2 - 10), fontsize=28, color="white")
            
            # Show Monster if Hit
            if hit and monster_r == r and monster_c == c:
                screen.draw.text("M", (x + TILE//2 - 10, y + 10), fontsize=36, color="red")
                
    screen.draw.text(message, (30, 355), fontsize=18, color="white")

def on_key_down(key):
    global selected_r, selected_c, hit, message
    if hit: return
    
    num = None
    if key == keys.K_1: num = 1
    elif key == keys.K_2: num = 2
    elif key == keys.K_3: num = 3
    elif key == keys.K_4: num = 4
    elif key == keys.K_5: num = 5
    elif key == keys.K_6: num = 6
    elif key == keys.K_7: num = 7
    elif key == keys.K_8: num = 8
    elif key == keys.K_9: num = 9
    
    if num is None: return
    
    # Convert 1~9 to (row, col)
    selected_r = (num - 1) // COLS
    selected_c = (num - 1) % COLS
    
    if selected_r == monster_r and selected_c == monster_c:
        hit = True
        message = "HIT! You found the monster!"
    else:
        message = f"MISS! Monster not at {num}"
