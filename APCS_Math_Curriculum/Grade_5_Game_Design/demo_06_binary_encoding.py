# Grade 5 Demo 06: Binary Encoding (Base 2)
# 觀念：二進位 (Binary) — 開關燈泡代表 0/1，計算對應的十進位數字
# Run: pgzrun demo_06_binary_encoding.py

WIDTH = 600
HEIGHT = 300

# 8 Bits (0 or 1)
bits = [0, 0, 0, 0, 0, 0, 0, 0]
selected_bit = 7 # Cursor position

def draw():
    screen.fill("black")
    
    total_value = 0
    
    for i in range(8):
        # Draw Bulb
        x = 50 + i * 65
        y = 120
        is_on = bits[i] == 1
        color = "yellow" if is_on else "gray"
        
        screen.draw.filled_circle((x, y), 25, color)
        
        # Draw Bit Value (128, 64, 32...)
        place_value = 2 ** (7 - i)
        screen.draw.text(str(place_value), (x - 10, y + 40), color="white")
        
        # Draw 0 or 1
        screen.draw.text(str(bits[i]), (x - 5, y - 10), color="black", fontsize=24)
        
        # Highlight Selection
        if i == selected_bit:
            screen.draw.rect(Rect(x - 30, y - 30, 60, 60), "cyan")
            
        if is_on:
            total_value += place_value
            
    screen.draw.text(f"Decimal Value: {total_value}", (180, 250), fontsize=40, color="lime")
    screen.draw.text("Arrows to Move, [SPACE] to Toggle", (150, 20), color="gray")

def on_key_down(key):
    global selected_bit
    if key == keys.LEFT and selected_bit > 0:
        selected_bit -= 1
    if key == keys.RIGHT and selected_bit < 7:
        selected_bit += 1
    if key == keys.SPACE:
        bits[selected_bit] = 1 - bits[selected_bit] # Toggle 0/1
