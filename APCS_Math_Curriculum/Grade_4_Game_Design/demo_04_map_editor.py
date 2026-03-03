# Grade 4 Demo 04: Map Editor (Modify Array)
# 觀念：點擊格子切換 0(路)/1(牆)，按 Enter 切換「編輯 / 遊玩」模式
# Run: pgzrun demo_04_map_editor.py

WIDTH = 450
HEIGHT = 480

ROWS, COLS = 6, 6
TILE = 70
# Map: 0=Road, 1=Wall
game_map = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
edit_mode = True  # True=Edit, False=Play
player_r, player_c = 0, 0
goal_r, goal_c = 5, 5

def draw():
    screen.fill("black")
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * TILE, r * TILE
            if game_map[r][c] == 1:
                screen.draw.filled_rect(Rect(x + 2, y + 2, TILE - 4, TILE - 4), "gray")
            else:
                screen.draw.filled_rect(Rect(x + 2, y + 2, TILE - 4, TILE - 4), "darkgreen")
    
    # Goal
    gx = goal_c * TILE + TILE // 2
    gy = goal_r * TILE + TILE // 2
    screen.draw.filled_circle((gx, gy), 18, "gold")
    screen.draw.text("*", (gx - 5, gy - 10), fontsize=22, color="sienna")
    
    if edit_mode:
        screen.draw.text("EDIT MODE: Click to toggle Wall/Road", (20, 425), fontsize=16, color="yellow")
        screen.draw.text("Press [ENTER] to Play", (20, 445), fontsize=16, color="yellow")
    else:
        cx = player_c * TILE + TILE // 2
        cy = player_r * TILE + TILE // 2
        screen.draw.filled_circle((cx, cy), 20, "red")
        screen.draw.text("Me", (cx - 8, cy - 8), fontsize=14, color="white")
        screen.draw.text("PLAY MODE: Arrows to Move", (20, 425), fontsize=16, color="white")
        screen.draw.text("Press [ENTER] to Edit", (20, 445), fontsize=16, color="white")
        
        if player_r == goal_r and player_c == goal_c:
            screen.draw.text("WIN!", (WIDTH // 2 - 40, 220), fontsize=60, color="gold")

def on_mouse_down(pos):
    if not edit_mode:
        return
    x, y = pos
    c = x // TILE
    r = y // TILE
    if 0 <= r < ROWS and 0 <= c < COLS:
        game_map[r][c] = 1 - game_map[r][c]  # Toggle 0/1

def on_key_down(key):
    global edit_mode, player_r, player_c
    if key == keys.RETURN or key == keys.K_RETURN:
        edit_mode = not edit_mode
        if not edit_mode:
            player_r, player_c = 0, 0
        return
        
    if edit_mode:
        return
        
    nr, nc = player_r, player_c
    if key == keys.UP:    nr -= 1
    elif key == keys.DOWN:  nr += 1
    elif key == keys.LEFT:  nc -= 1
    elif key == keys.RIGHT: nc += 1
    
    if 0 <= nr < ROWS and 0 <= nc < COLS and game_map[nr][nc] == 0:
        player_r, player_c = nr, nc
