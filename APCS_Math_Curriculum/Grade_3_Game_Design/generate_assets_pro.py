# Pro Asset Generator for Grade 3 Demos
# Uses Super-Sampling (Anti-aliasing) and composite shapes for better quality.
# Usage: python3 generate_assets_pro.py

import os
from PIL import Image, ImageDraw, ImageFilter

IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def draw_smooth_shape(filename, size, draw_func):
    """
    Draws at 4x resolution and resizes down for smooth anti-aliasing.
    """
    target_w, target_h = size
    scale = 4
    super_size = (target_w * scale, target_h * scale)
    
    img = Image.new("RGBA", super_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Call the custom drawing function
    draw_func(draw, super_size[0], super_size[1])
    
    # Resize down smoothly
    img = img.resize(size, resample=Image.Resampling.LANCZOS)
    
    # Save
    path = os.path.join(IMAGE_DIR, filename + ".png")
    img.save(path)
    print(f"Generated Pro Asset: {filename}.png")

# --- Drawing Functions ---

def draw_cat(d, w, h):
    # Face
    d.ellipse([w*0.1, h*0.2, w*0.9, h*0.9], fill="#FFA500", outline="#CC8400", width=8)
    # Ears
    d.polygon([w*0.15, h*0.3, w*0.1, h*0.05, w*0.35, h*0.2], fill="#FFA500", outline="#CC8400", width=8)
    d.polygon([w*0.85, h*0.3, w*0.9, h*0.05, w*0.65, h*0.2], fill="#FFA500", outline="#CC8400", width=8)
    # Eyes
    d.ellipse([w*0.25, h*0.45, w*0.4, h*0.6], fill="white")
    d.ellipse([w*0.6, h*0.45, w*0.75, h*0.6], fill="white")
    d.ellipse([w*0.3, h*0.48, w*0.35, h*0.55], fill="black")
    d.ellipse([w*0.65, h*0.48, w*0.7, h*0.55], fill="black")
    # Nose
    d.polygon([w*0.45, h*0.65, w*0.55, h*0.65, w*0.5, h*0.75], fill="pink")

def draw_penguin(d, w, h):
    # Body
    d.ellipse([w*0.15, h*0.1, w*0.85, h*0.9], fill="#333333")
    # Tummy
    d.ellipse([w*0.25, h*0.3, w*0.75, h*0.85], fill="white")
    # Eyes
    d.ellipse([w*0.35, h*0.25, w*0.45, h*0.35], fill="white")
    d.ellipse([w*0.55, h*0.25, w*0.65, h*0.35], fill="white")
    d.ellipse([w*0.38, h*0.28, w*0.42, h*0.32], fill="black")
    d.ellipse([w*0.58, h*0.28, w*0.62, h*0.32], fill="black")
    # Beak
    d.polygon([w*0.45, h*0.35, w*0.55, h*0.35, w*0.5, h*0.45], fill="orange")
    # Feet
    d.ellipse([w*0.2, h*0.85, w*0.4, h*0.95], fill="orange")
    d.ellipse([w*0.6, h*0.85, w*0.8, h*0.95], fill="orange")

def draw_dog(d, w, h):
    # Ears (Floppy)
    d.ellipse([w*0.05, h*0.2, w*0.3, h*0.6], fill="#8B4513")
    d.ellipse([w*0.7, h*0.2, w*0.95, h*0.6], fill="#8B4513")
    # Head
    d.ellipse([w*0.15, h*0.1, w*0.85, h*0.8], fill="#A0522D", outline="#8B4513", width=5)
    # Snout
    d.ellipse([w*0.3, h*0.5, w*0.7, h*0.8], fill="#DEB887")
    d.ellipse([w*0.45, h*0.55, w*0.55, h*0.65], fill="black") # Nose
    # Eyes
    d.ellipse([w*0.3, h*0.35, w*0.4, h*0.45], fill="black")
    d.ellipse([w*0.6, h*0.35, w*0.7, h*0.45], fill="black")

def draw_bone(d, w, h):
    # Bone shape
    d.rectangle([w*0.2, h*0.3, w*0.8, h*0.7], fill="#EEE8AA")
    d.ellipse([w*0.05, h*0.2, w*0.25, h*0.5], fill="#EEE8AA")
    d.ellipse([w*0.05, h*0.5, w*0.25, h*0.8], fill="#EEE8AA")
    d.ellipse([w*0.75, h*0.2, w*0.95, h*0.5], fill="#EEE8AA")
    d.ellipse([w*0.75, h*0.5, w*0.95, h*0.8], fill="#EEE8AA")

def draw_mouse(d, w, h):
    # Ears
    d.ellipse([w*0.1, h*0.1, w*0.4, h*0.4], fill="pink", outline="gray", width=5)
    d.ellipse([w*0.6, h*0.1, w*0.9, h*0.4], fill="pink", outline="gray", width=5)
    # Face
    d.ellipse([w*0.15, h*0.2, w*0.85, h*0.9], fill="gray")
    # Nose
    d.ellipse([w*0.45, h*0.75, w*0.55, h*0.85], fill="pink")
    # Eyes
    d.ellipse([w*0.3, h*0.5, w*0.4, h*0.6], fill="black")
    d.ellipse([w*0.6, h*0.5, w*0.7, h*0.6], fill="black")

def draw_car(d, w, h):
    # Top
    d.rectangle([w*0.2, h*0.1, w*0.8, h*0.5], fill="#4682B4")
    # Bottom
    d.rectangle([w*0.05, h*0.4, w*0.95, h*0.7], fill="#4682B4")
    # Windows
    d.rectangle([w*0.25, h*0.15, w*0.45, h*0.4], fill="lightblue")
    d.rectangle([w*0.55, h*0.15, w*0.75, h*0.4], fill="lightblue")
    # Wheels
    d.ellipse([w*0.15, h*0.6, w*0.35, h*0.9], fill="black")
    d.ellipse([w*0.65, h*0.6, w*0.85, h*0.9], fill="black")

def draw_light(d, w, h, color, active):
    fill = color if active else "#333333"
    outline = "white" if active else "#555555"
    d.ellipse([w*0.1, h*0.1, w*0.9, h*0.9], fill=fill, outline=outline, width=5)
    # Shine
    if active:
        d.ellipse([w*0.25, h*0.25, w*0.45, h*0.4], fill="white")

def draw_rabbit(d, w, h, jump=False):
    offset = h*0.1 if jump else 0
    # Ears
    d.ellipse([w*0.25, h*0.05-offset, w*0.4, h*0.4-offset], fill="white", outline="pink", width=5)
    d.ellipse([w*0.6, h*0.05-offset, w*0.75, h*0.4-offset], fill="white", outline="pink", width=5)
    # Head
    d.ellipse([w*0.2, h*0.3-offset, w*0.8, h*0.8-offset], fill="white")
    # Eyes
    d.ellipse([w*0.35, h*0.45-offset, w*0.45, h*0.55-offset], fill="black")
    d.ellipse([w*0.55, h*0.45-offset, w*0.65, h*0.55-offset], fill="black")
    # Nose
    d.polygon([w*0.45, h*0.6-offset, w*0.55, h*0.6-offset, w*0.5, h*0.7-offset], fill="pink")

def draw_rocket(d, w, h):
    # Fins
    d.polygon([w*0.1, h*0.7, w*0.3, h*0.5, w*0.3, h*0.9], fill="red")
    d.polygon([w*0.9, h*0.7, w*0.7, h*0.5, w*0.7, h*0.9], fill="red")
    # Body
    d.ellipse([w*0.3, h*0.1, w*0.7, h*0.9], fill="white")
    # Window
    d.ellipse([w*0.4, h*0.3, w*0.6, h*0.5], fill="cyan", outline="gray", width=3)
    # Flame
    d.polygon([w*0.4, h*0.85, w*0.6, h*0.85, w*0.5, h*1.0], fill="orange")

def draw_meteor(d, w, h):
    # Rock
    d.ellipse([w*0.2, h*0.2, w*0.8, h*0.8], fill="#8B4513")
    # Craters
    d.ellipse([w*0.3, h*0.3, w*0.45, h*0.45], fill="#654321")
    d.ellipse([w*0.5, h*0.6, w*0.7, h*0.75], fill="#654321")
    # Trail
    d.polygon([w*0.2, h*0.5, w*0.0, h*0.4, w*0.0, h*0.6], fill="orange")

def draw_chick(d, w, h):
    # Body
    d.ellipse([w*0.1, h*0.1, w*0.9, h*0.9], fill="yellow")
    # Eyes
    d.ellipse([w*0.3, h*0.35, w*0.4, h*0.45], fill="black")
    d.ellipse([w*0.6, h*0.35, w*0.7, h*0.45], fill="black")
    # Beak
    d.polygon([w*0.45, h*0.5, w*0.55, h*0.5, w*0.5, h*0.6], fill="orange")
    # Wings
    d.arc([w*0.15, h*0.5, w*0.3, h*0.7], start=90, end=270, fill="orange", width=5)
    d.arc([w*0.7, h*0.5, w*0.85, h*0.7], start=-90, end=90, fill="orange", width=5)

def draw_drop(d, w, h):
    # Teardrop shape
    d.polygon([w*0.5, h*0.0, w*0.1, h*0.7, w*0.9, h*0.7], fill="#00BFFF")
    d.ellipse([w*0.1, h*0.5, w*0.9, h*0.95], fill="#00BFFF")
    # Shine
    d.ellipse([w*0.6, h*0.6, w*0.75, h*0.75], fill="white")

def draw_frog(d, w, h):
    # Eyes (Pop out)
    d.ellipse([w*0.1, h*0.1, w*0.4, h*0.4], fill="lime")
    d.ellipse([w*0.6, h*0.1, w*0.9, h*0.4], fill="lime")
    d.ellipse([w*0.2, h*0.2, w*0.3, h*0.3], fill="black")
    d.ellipse([w*0.7, h*0.2, w*0.8, h*0.3], fill="black")
    # Body
    d.ellipse([w*0.15, h*0.3, w*0.85, h*0.9], fill="lime")
    # Mouth
    d.arc([w*0.3, h*0.5, w*0.7, h*0.7], start=0, end=180, fill="darkgreen", width=5)

def draw_coin(d, w, h):
    d.ellipse([w*0.1, h*0.1, w*0.9, h*0.9], fill="gold", outline="orange", width=5)
    d.text((w*0.35, h*0.25), "$", fill="orange", font_size=int(h*0.5))

def draw_hero(d, w, h):
    # Helmet
    d.ellipse([w*0.2, h*0.1, w*0.8, h*0.7], fill="silver", outline="gray", width=5)
    # Visor
    d.rectangle([w*0.3, h*0.3, w*0.7, h*0.4], fill="black")
    # Body
    d.rectangle([w*0.2, h*0.7, w*0.8, h*1.0], fill="blue")

def draw_chest(d, w, h):
    # Box
    d.rectangle([w*0.1, h*0.3, w*0.9, h*0.9], fill="saddlebrown")
    # Lid
    d.arc([w*0.1, h*0.1, w*0.9, h*0.5], start=180, end=0, fill="saddlebrown", width=20)
    # Lock
    d.rectangle([w*0.4, h*0.5, w*0.6, h*0.7], fill="gold")

def draw_wall(d, w, h):
    # Bricks
    d.rectangle([0, 0, w, h], fill="#8B4513")
    d.rectangle([w*0.1, h*0.1, w*0.45, h*0.45], fill="#A0522D")
    d.rectangle([w*0.55, h*0.1, w*0.9, h*0.45], fill="#A0522D")
    d.rectangle([w*0.1, h*0.55, w*0.9, h*0.9], fill="#A0522D")

# --- Execution ---

# 01
draw_smooth_shape("cat", (60, 60), draw_cat)

# 02
draw_smooth_shape("penguin", (60, 60), draw_penguin)

# 03
draw_smooth_shape("dog", (60, 60), draw_dog)
draw_smooth_shape("bone", (50, 30), draw_bone)

# 04
draw_smooth_shape("mouse", (40, 40), draw_mouse)
draw_smooth_shape("cat_face", (60, 60), draw_cat)

# 05
draw_smooth_shape("car", (80, 50), draw_car)
draw_smooth_shape("light_red", (40, 40), lambda d,w,h: draw_light(d,w,h,"red",True))
draw_smooth_shape("light_yellow", (40, 40), lambda d,w,h: draw_light(d,w,h,"yellow",True))
draw_smooth_shape("light_green", (40, 40), lambda d,w,h: draw_light(d,w,h,"lime",True))
draw_smooth_shape("light_off", (40, 40), lambda d,w,h: draw_light(d,w,h,"gray",False))

# 06
draw_smooth_shape("rabbit", (60, 60), lambda d,w,h: draw_rabbit(d,w,h,False))
draw_smooth_shape("rabbit_jump", (60, 60), lambda d,w,h: draw_rabbit(d,w,h,True))

# 07
draw_smooth_shape("rocket", (50, 70), draw_rocket)
draw_smooth_shape("meteor", (40, 40), draw_meteor)

# 08
draw_smooth_shape("chick", (50, 50), draw_chick)
draw_smooth_shape("drop", (30, 40), draw_drop)

# 09
draw_smooth_shape("frog", (50, 50), draw_frog)
draw_smooth_shape("coin", (40, 40), draw_coin)

# 10
draw_smooth_shape("hero", (50, 50), draw_hero)
draw_smooth_shape("chest", (50, 50), draw_chest)
draw_smooth_shape("wall", (58, 58), draw_wall)

print("Pro Assets Generated Successfully!")
