# Grade 4 Demo 02: Inventory System (Set Logic)
# 觀念：背包 = 物品的集合；開門條件 = 有鑰匙 AND 站在門前
# Run: pgzrun demo_02_inventory_logic.py

WIDTH = 500
HEIGHT = 380

# Inventory (List/Set)
inventory = []
# Items on map: (Name, x, y)
items_on_map = [
    ("Key", 120, 150),
    ("Torch", 250, 150),
    ("Sword", 380, 150),
]
# Door
door_x, door_y = 250, 300
# Player
px, py = 250, 100
SPEED = 5
door_open = False

def draw():
    screen.fill("darkblue")
    
    # Door
    if door_open:
        screen.draw.filled_rect(Rect(door_x - 40, door_y - 50, 80, 100), "black")
        screen.draw.text("OPEN", (door_x - 20, door_y - 20), fontsize=18, color="lime")
    else:
        screen.draw.filled_rect(Rect(door_x - 40, door_y - 50, 80, 100), "sienna")
        screen.draw.rect(Rect(door_x - 40, door_y - 50, 80, 100), "gold")
        screen.draw.text("Door", (door_x - 15, door_y - 25), fontsize=24, color="white")
    
    # Items
    for name, x, y in items_on_map:
        screen.draw.filled_circle((x, y), 18, "gray")
        screen.draw.text(name[0], (x - 5, y - 8), fontsize=16, color="white")
    
    # Player
    screen.draw.filled_circle((px, py), 15, "red")
    screen.draw.text("Me", (px - 8, py - 8), fontsize=14, color="white")
    
    # HUD
    inv_text = ", ".join(inventory) if inventory else "(Empty)"
    screen.draw.text(f"Inventory: {inv_text}", (20, 20), fontsize=20, color="white")
    screen.draw.text("Press 1=Key 2=Torch 3=Sword to pick up", (20, 48), fontsize=14, color="lightgray")
    
    # Interaction Hint
    if not door_open and abs(px - door_x) < 50 and abs(py - door_y) < 50:
        if "Key" in inventory:
            screen.draw.text("Press [SPACE] to Open!", (door_x - 60, door_y - 70), fontsize=18, color="yellow")
        else:
            screen.draw.text("Need Key to Open", (door_x - 70, door_y - 70), fontsize=18, color="red")

def update():
    global px, py
    if keyboard.right: px = px + SPEED
    if keyboard.left:  px = px - SPEED
    if keyboard.down:  py = py + SPEED
    if keyboard.up:    py = py - SPEED
    px = max(20, min(WIDTH - 20, px))
    py = max(20, min(HEIGHT - 20, py))

def on_key_down(key):
    global inventory, items_on_map, door_open
    
    # Pick up items
    to_remove = None
    for i, (name, x, y) in enumerate(items_on_map):
        if abs(px - x) < 35 and abs(py - y) < 35 and name not in inventory:
            if key == keys.K_1 and name == "Key":
                inventory.append("Key")
                to_remove = i
                break
            elif key == keys.K_2 and name == "Torch":
                inventory.append("Torch")
                to_remove = i
                break
            elif key == keys.K_3 and name == "Sword":
                inventory.append("Sword")
                to_remove = i
                break
    
    if to_remove is not None:
        items_on_map.pop(to_remove)
        
    # Open Door (Logic: Near Door AND Has Key)
    if key == keys.SPACE and abs(px - door_x) < 50 and abs(py - door_y) < 50 and "Key" in inventory:
        door_open = True
