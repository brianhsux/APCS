# Grade 6 Demo 03: Matrix Rotation (Tetris Logic)
# 觀念：矩陣旋轉 (Matrix) — 俄羅斯方塊的旋轉邏輯 (轉 90 度公式)
# Run: pgzrun demo_03_matrix_transform.py

WIDTH = 400
HEIGHT = 400
TILE = 40

# L-Shape
shape = [
    [1, 0],
    [1, 0],
    [1, 1]
]

offset_x = 5
offset_y = 5

def rotate(matrix):
    # Transpose + Reverse Rows = Rotate 90 deg clockwise
    # Zip(*matrix) is a python trick for transpose
    return [list(row) for row in zip(*matrix[::-1])]

def draw():
    screen.fill("black")
    
    # Draw Grid
    for r in range(10):
        for c in range(10):
            screen.draw.rect(Rect(c*TILE, r*TILE, TILE, TILE), "dimgray")
            
    # Draw Shape
    rows = len(shape)
    cols = len(shape[0])
    
    for r in range(rows):
        for c in range(cols):
            if shape[r][c] == 1:
                x = (offset_x + c) * TILE
                y = (offset_y + r) * TILE
                screen.draw.filled_rect(Rect(x, y, TILE-2, TILE-2), "cyan")
                
    screen.draw.text("Press [SPACE] to Rotate", (10, 360), color="white", fontsize=24)

def on_key_down(key):
    global shape
    if key == keys.SPACE:
        shape = rotate(shape)
