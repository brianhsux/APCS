# APCS 真題 03: 矩陣翻轉 (Matrix Rotation)
# 來源：2017-03-04 實作題 Q2
# 題目：給定一個 R x C 的矩陣，進行翻轉 (0:旋轉, 1:翻轉)
# 這裡視覺化「順時針旋轉 90 度」的過程
#
# Run: pgzrun apcs_03_matrix_rotation.py

WIDTH = 500
HEIGHT = 500
TILE = 60

# 3x4 Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

target_matrix = [] # Rotated
state = "ORIGINAL" # ORIGINAL, ANIMATING, ROTATED
anim_progress = 0

def rotate_logic():
    # Rotate 90 deg clockwise
    # New[c][R-1-r] = Old[r][c]
    R = len(matrix)
    C = len(matrix[0])
    new_m = [[0]*R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            new_m[c][R-1-r] = matrix[r][c]
    return new_m

target_matrix = rotate_logic()

def draw():
    screen.fill("black")
    screen.draw.text("Matrix Rotation (90 deg Clockwise)", (20, 20), fontsize=30, color="white")
    
    if state == "ORIGINAL":
        draw_matrix(matrix, 100, 100)
        screen.draw.text("Original 3x4", (100, 350), color="gray")
    elif state == "ROTATED":
        draw_matrix(target_matrix, 100, 100)
        screen.draw.text("Rotated 4x3", (100, 350), color="lime")
    elif state == "ANIMATING":
        # Simple transition effect
        draw_matrix(matrix, 100, 100, alpha=1.0-anim_progress)
        draw_matrix(target_matrix, 100, 100, alpha=anim_progress)
        
    screen.draw.text("Press [SPACE] to Rotate", (150, 450), color="yellow")

def draw_matrix(m, start_x, start_y, alpha=1.0):
    rows = len(m)
    cols = len(m[0])
    for r in range(rows):
        for c in range(cols):
            val = m[r][c]
            x = start_x + c * TILE
            y = start_y + r * TILE
            
            # Color based on value gradient
            intensity = int(50 + val * 15)
            color = (0, min(255, intensity), min(255, intensity))
            
            if alpha < 1.0: # Dim if animating
                pass 
                
            screen.draw.filled_rect(Rect(x, y, TILE-2, TILE-2), color)
            screen.draw.text(str(val), (x+20, y+20), fontsize=30, color="white")

def update():
    global state, anim_progress
    if state == "ANIMATING":
        anim_progress += 0.05
        if anim_progress >= 1.0:
            state = "ROTATED"
            anim_progress = 0

def on_key_down(key):
    global state, matrix, target_matrix
    if key == keys.SPACE:
        if state == "ORIGINAL":
            state = "ANIMATING"
        elif state == "ROTATED":
            # Reset
            state = "ORIGINAL"
