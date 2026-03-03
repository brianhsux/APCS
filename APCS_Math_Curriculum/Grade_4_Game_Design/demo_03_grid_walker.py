# Grade 4 Demo 03: Grid Walker (2D Array)
# 觀念：二維陣列 (地圖) 與 邏輯判斷 (能不能走)
# Run: pgzrun demo_03_grid_walker.py

WIDTH = 400
HEIGHT = 400

# 0=Road, 1=Wall
game_map = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

TILE_SIZE = 80
player_row = 1
player_col = 1

def draw():
    screen.clear()
    # Draw Map (Nested Loop)
    for row in range(5):
        for col in range(5):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            
            if game_map[row][col] == 1:
                screen.draw.filled_rect(Rect(x, y, TILE_SIZE-2, TILE_SIZE-2), "gray")
            else:
                screen.draw.filled_rect(Rect(x, y, TILE_SIZE-2, TILE_SIZE-2), "black")

    # Draw Player
    player_x = player_col * TILE_SIZE + TILE_SIZE/2
    player_y = player_row * TILE_SIZE + TILE_SIZE/2
    screen.draw.circle((player_x, player_y), 20, "red")

def on_key_down(key):
    global player_row, player_col
    
    new_r = player_row
    new_c = player_col
    
    if key == keys.UP: new_r -= 1
    elif key == keys.DOWN: new_r += 1
    elif key == keys.LEFT: new_c -= 1
    elif key == keys.RIGHT: new_c += 1
    
    # Collision Check: Is it a wall (1)?
    if game_map[new_r][new_c] == 0:
        player_row = new_r
        player_col = new_c
