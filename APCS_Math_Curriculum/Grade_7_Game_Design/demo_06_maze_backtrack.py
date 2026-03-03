# Grade 7 Demo 06: Maze Backtracking (DFS)
# 觀念：回溯法 (Backtracking) — 走錯路就回頭，直到找到終點
# Run: pgzrun demo_06_maze_backtrack.py

WIDTH = 400
HEIGHT = 400
TILE = 80

# 0=Path, 1=Wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

path = [] # Stack for DFS
visited = set()
found = False
timer = 0

# Start DFS
path.append((0, 0))
visited.add((0, 0))

def draw():
    screen.fill("black")
    
    for r in range(5):
        for c in range(5):
            x, y = c*TILE, r*TILE
            color = "black"
            if maze[r][c] == 1: color = "gray"
            elif (r, c) in path: color = "blue" # Current Path
            elif (r, c) in visited: color = "darkblue" # Visited but backtrack
            
            if (r, c) == (0, 0): color = "lime"
            if (r, c) == (4, 4): color = "red"
            
            screen.draw.filled_rect(Rect(x, y, TILE-2, TILE-2), color)
            
    if found:
        screen.draw.text("GOAL REACHED!", (100, 180), fontsize=40, color="gold")

def update():
    global found, timer
    if found or not path: return
    
    timer += 1
    if timer % 20 == 0:
        curr = path[-1]
        r, c = curr
        
        if curr == (4, 4):
            found = True
            return
            
        # Look for neighbors (Right, Down, Left, Up)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        moved = False
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    path.append((nr, nc))
                    visited.add((nr, nc))
                    moved = True
                    break
        
        if not moved:
            path.pop() # Backtrack
