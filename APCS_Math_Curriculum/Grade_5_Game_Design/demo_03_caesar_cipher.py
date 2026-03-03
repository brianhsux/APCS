# Grade 5 Demo 03: Caesar Cipher (Modulo)
# 觀念：凱薩密碼解謎 — 將字母位移來傳送秘密訊息 (ASCII + Mod)
# Run: pgzrun demo_03_caesar_cipher.py

WIDTH = 600
HEIGHT = 400

plaintext = "HELLO APCS"
shift = 0
ciphertext = plaintext

def encrypt(text, s):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            # A=65. (Char - 65 + shift) % 26 + 65
            code = ord(char) - 65
            new_code = (code + s) % 26
            result += chr(new_code + 65)
    return result

def draw():
    screen.fill("midnightblue")
    
    screen.draw.text("CAESAR CIPHER DECODER", (150, 30), fontsize=30, color="cyan")
    
    screen.draw.text(f"Original:  {plaintext}", (50, 100), fontsize=40, color="gray")
    screen.draw.text(f"Shift Key: {shift}", (50, 180), fontsize=40, color="yellow")
    screen.draw.text(f"Encoded:   {ciphertext}", (50, 260), fontsize=40, color="lime")
    
    screen.draw.text("Use LEFT / RIGHT arrows to change Key", (50, 350), color="white")

def update():
    pass

def on_key_down(key):
    global shift, ciphertext
    if key == keys.RIGHT:
        shift = (shift + 1) % 26
    if key == keys.LEFT:
        shift = (shift - 1) % 26
        
    ciphertext = encrypt(plaintext, shift)
