# Grade 5 Demo 01: Prime Shield (Number Theory)
# 觀念：質數 (Prime) — 只有質數盾牌能擋住攻擊，合數會碎掉
# Run: pgzrun demo_01_prime_shield.py

import random

WIDTH = 600
HEIGHT = 400

player_hp = 100
shield_num = 0
message = "Press SPACE to generate Shield"
incoming_damage = 0
timer = 0

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def draw():
    screen.fill("black")
    
    # Player
    screen.draw.filled_circle((100, 200), 30, "blue")
    screen.draw.text(f"HP: {player_hp}", (50, 250), fontsize=24)
    
    # Shield
    color = "cyan" if is_prime(shield_num) else "gray"
    screen.draw.circle((100, 200), 50, color)
    if shield_num > 0:
        screen.draw.text(str(shield_num), (90, 190), fontsize=30, color="white")
        
    # Enemy Attack
    if incoming_damage > 0:
        screen.draw.filled_circle((500 - timer*5, 200), 10, "red")
        screen.draw.text("ATTACK!", (400, 150), color="red")
        
    screen.draw.text(message, (100, 350), fontsize=24, color="yellow")
    screen.draw.text("Only PRIME numbers block damage!", (100, 380), color="gray")

def update():
    global incoming_damage, timer, player_hp, message, shield_num
    
    # Enemy attacks periodically
    if incoming_damage == 0 and random.randint(0, 100) < 2:
        incoming_damage = 20
        timer = 0
        message = "Enemy Attacking! Quick, get a Prime!"
        
    if incoming_damage > 0:
        timer += 2
        # Hit Player
        if timer > 80:
            if is_prime(shield_num):
                message = "BLOCKED! Prime Shield held!"
            else:
                player_hp -= incoming_damage
                message = "HIT! Shield broke (Not Prime)"
                shield_num = 0 # Shield breaks
            incoming_damage = 0
            timer = 0

def on_key_down(key):
    global shield_num
    if key == keys.SPACE:
        shield_num = random.randint(2, 20)
