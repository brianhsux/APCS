# Asset Generator for Grade 3 Demos
# Run this once to create 'images' folder with cute pixel-art style assets.
# Usage: python3 generate_assets_g3.py

import os
from PIL import Image, ImageDraw, ImageFont

# Ensure images directory exists
IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def create_image(filename, size, color, shape="circle", text=None):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    w, h = size
    
    if shape == "circle":
        draw.ellipse([0, 0, w-1, h-1], fill=color, outline="white", width=2)
    elif shape == "rect":
        draw.rectangle([0, 0, w-1, h-1], fill=color, outline="white", width=2)
    elif shape == "triangle":
        draw.polygon([(w/2, 0), (0, h), (w, h)], fill=color, outline="white")
    elif shape == "star":
        # Simple star approximation
        draw.polygon([
            (w/2, 0), (w*0.6, h*0.4), (w, h*0.4), (w*0.7, h*0.6), 
            (w*0.8, h), (w/2, h*0.8), (w*0.2, h), (w*0.3, h*0.6), 
            (0, h*0.4), (w*0.4, h*0.4)
        ], fill=color, outline="white")
        
    # Add simple face or detail
    if text:
        # Just draw simple text/emoji if possible, or basic eyes
        pass
    else:
        # Draw eyes for cute characters
        if shape in ["circle", "rect"] and "wall" not in filename:
            eye_color = "black"
            draw.ellipse([w*0.3, h*0.3, w*0.4, h*0.4], fill=eye_color) # Left eye
            draw.ellipse([w*0.6, h*0.3, w*0.7, h*0.4], fill=eye_color) # Right eye
            
    img.save(os.path.join(IMAGE_DIR, filename + ".png"))
    print(f"Generated {filename}.png")

# --- Generate Assets ---

# 01: Cat (Orange Circle)
create_image("cat", (40, 40), "orange", "circle")

# 02: Penguin (Blue Circle)
create_image("penguin", (40, 40), "cyan", "circle")

# 03: Dog (Brown) & Bone (White Rect)
create_image("dog", (40, 40), "sienna", "circle")
create_image("bone", (30, 15), "white", "rect")

# 04: Mouse (Gray) & Cat Face (Red)
create_image("mouse", (30, 30), "gray", "circle")
create_image("cat_face", (40, 40), "red", "circle")

# 05: Car (Blue Rect) & Lights
create_image("car", (50, 30), "blue", "rect")
create_image("light_red", (30, 30), "red", "circle")
create_image("light_yellow", (30, 30), "yellow", "circle")
create_image("light_green", (30, 30), "lime", "circle")
create_image("light_off", (30, 30), "dimgray", "circle")

# 06: Rabbit (Pink)
create_image("rabbit", (40, 40), "pink", "circle")
create_image("rabbit_jump", (40, 40), "hotpink", "circle") # Slightly darker for jump

# 07: Rocket (White Triangle) & Meteor (Gray Star)
create_image("rocket", (30, 40), "white", "triangle")
create_image("meteor", (30, 30), "gray", "star")

# 08: Chick (Yellow) & Drop (Blue)
create_image("chick", (30, 30), "yellow", "circle")
create_image("drop", (20, 20), "skyblue", "circle")

# 09: Frog (Green) & Coin (Gold)
create_image("frog", (30, 30), "lime", "circle")
create_image("coin", (20, 20), "gold", "circle")

# 10: Hero (Blue), Chest (Gold), Wall (Brown)
create_image("hero", (30, 30), "dodgerblue", "circle")
create_image("chest", (30, 30), "gold", "rect")
create_image("wall", (40, 40), "saddlebrown", "rect")

print("All assets generated in 'images/' folder.")
