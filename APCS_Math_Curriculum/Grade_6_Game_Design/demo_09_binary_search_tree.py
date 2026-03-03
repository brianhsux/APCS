# Grade 6 Demo 09: Binary Search Tree (BST)
# 觀念：二元搜尋樹 (BST) — 數字大小自動分流，建立搜尋樹
# Run: pgzrun demo_09_binary_search_tree.py

WIDTH = 600
HEIGHT = 400

# Node class structure: [value, x, y, left, right]
root = None

def insert(node, val, x, y, dx):
    if node is None:
        return [val, x, y, None, None]
    
    n_val = node[0]
    if val < n_val:
        node[3] = insert(node[3], val, x - dx, y + 50, dx // 2)
    else:
        node[4] = insert(node[4], val, x + dx, y + 50, dx // 2)
    return node

def draw_tree(node):
    if node is None: return
    
    val, x, y, left, right = node
    
    if left:
        screen.draw.line((x, y), (left[1], left[2]), "white")
        draw_tree(left)
    if right:
        screen.draw.line((x, y), (right[1], right[2]), "white")
        draw_tree(right)
        
    screen.draw.filled_circle((x, y), 15, "blue")
    screen.draw.text(str(val), (x-8, y-8), color="white")

def draw():
    screen.fill("black")
    draw_tree(root)
    screen.draw.text("Press [SPACE] to Add Random Number", (10, 10), color="yellow")
    screen.draw.text("Left < Node < Right", (10, 30), color="gray")

import random
def on_key_down(key):
    global root
    if key == keys.SPACE:
        val = random.randint(1, 99)
        root = insert(root, val, 300, 50, 140)
