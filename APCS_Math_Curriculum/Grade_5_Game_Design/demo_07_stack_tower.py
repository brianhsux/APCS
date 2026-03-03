# Grade 5 Demo 07: Tower of Hanoi (Stack)
# 觀念：堆疊 (Stack) — 河內塔遊戲，後進先出的概念
# Run: pgzrun demo_07_stack_tower.py

WIDTH = 600
HEIGHT = 400

# 3 Pegs (Stacks)
pegs = [[4, 3, 2, 1], [], []] # Disks: 4 is largest
selected_peg = 0
hand = None # Disk in hand

def draw():
    screen.fill("indigo")
    
    # Draw Pegs
    for i in range(3):
        x = 100 + i * 200
        screen.draw.line((x, 150), (x, 350), "white")
        screen.draw.text(f"Peg {i+1}", (x-20, 360), color="white")
        
        # Highlight Selection
        if i == selected_peg:
            screen.draw.circle((x, 370), 5, "yellow")
            
        # Draw Disks
        for j, disk_size in enumerate(pegs[i]):
            w = disk_size * 40
            h = 20
            disk_x = x - w // 2
            disk_y = 330 - j * 25
            screen.draw.filled_rect(Rect(disk_x, disk_y, w, h), "orange")
            
    # Draw Hand (Floating Disk)
    if hand is not None:
        x = 100 + selected_peg * 200
        w = hand * 40
        screen.draw.filled_rect(Rect(x - w//2, 100, w, 20), "gold")
        
    screen.draw.text("Arrows to Select, [SPACE] to Pick/Drop", (150, 20), color="white")

def on_key_down(key):
    global selected_peg, hand
    
    if key == keys.LEFT: selected_peg = (selected_peg - 1) % 3
    if key == keys.RIGHT: selected_peg = (selected_peg + 1) % 3
    
    if key == keys.SPACE:
        if hand is None:
            # Pick up
            if pegs[selected_peg]:
                hand = pegs[selected_peg].pop()
        else:
            # Drop
            # Rule: Can only drop on larger disk or empty peg
            if not pegs[selected_peg] or pegs[selected_peg][-1] > hand:
                pegs[selected_peg].append(hand)
                hand = None
            else:
                # Invalid move
                pass
