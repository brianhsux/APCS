# Grade 4 Demo 10: RPG Battle (State Machine)
# 觀念：狀態機 (State Machine) — 玩家回合 -> 判定 -> 敵人回合 -> 判定
# Run: pgzrun demo_10_rpg_battle.py

import time

WIDTH = 600
HEIGHT = 400

# Stats
player = {"hp": 100, "max_hp": 100, "atk": 15, "name": "Hero"}
enemy = {"hp": 100, "max_hp": 100, "atk": 10, "name": "Boss"}

# Game State: "PLAYER_TURN", "ENEMY_TURN", "WIN", "LOSE"
state = "PLAYER_TURN"
log = "Battle Start! [A]ttack [H]eal"

def draw():
    screen.fill("black")
    
    # Hero
    screen.draw.filled_circle((150, 250), 40, "blue")
    screen.draw.text(f"{player['name']}\nHP: {player['hp']}/{player['max_hp']}", (100, 300), fontsize=24)
    
    # Boss
    screen.draw.filled_circle((450, 250), 50, "red")
    screen.draw.text(f"{enemy['name']}\nHP: {enemy['hp']}/{enemy['max_hp']}", (400, 300), fontsize=24)
    
    # Log
    screen.draw.text(log, (50, 50), fontsize=30, color="yellow")
    
    if state == "PLAYER_TURN":
        screen.draw.text("Your Turn: [A] Attack  [H] Heal", (150, 350), color="cyan")
    elif state == "ENEMY_TURN":
        screen.draw.text("Boss is thinking...", (200, 350), color="orange")

def on_key_down(key):
    global state, log
    
    if state != "PLAYER_TURN": return
    
    if key == keys.A:
        # Attack
        dmg = player["atk"]
        enemy["hp"] -= dmg
        log = f"You hit Boss for {dmg} dmg!"
        check_win()
        if state == "PLAYER_TURN":
            state = "ENEMY_TURN"
            clock.schedule(enemy_attack, 1.0)
            
    elif key == keys.H:
        # Heal
        heal = 20
        player["hp"] = min(player["max_hp"], player["hp"] + heal)
        log = f"You healed {heal} HP!"
        state = "ENEMY_TURN"
        clock.schedule(enemy_attack, 1.0)

def enemy_attack():
    global state, log
    if state != "ENEMY_TURN": return
    
    dmg = enemy["atk"]
    player["hp"] -= dmg
    log = f"Boss hit you for {dmg} dmg!"
    check_lose()
    if state == "ENEMY_TURN":
        state = "PLAYER_TURN"

def check_win():
    global state, log
    if enemy["hp"] <= 0:
        enemy["hp"] = 0
        state = "WIN"
        log = "VICTORY! You defeated the Boss!"

def check_lose():
    global state, log
    if player["hp"] <= 0:
        player["hp"] = 0
        state = "LOSE"
        log = "DEFEAT... Game Over"
