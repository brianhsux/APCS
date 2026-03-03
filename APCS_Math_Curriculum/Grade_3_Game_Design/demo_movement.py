# 這是給小三學生的 Pygame Zero 範例
# 觀念：座標 (x, y) 與 移動 (加減法)

# 需安裝：pip install pgzero
# 執行方式：pgzrun demo_movement.py

WIDTH = 600
HEIGHT = 400

# 定義一個角色 (Alien)
alien = Actor('alien')
alien.pos = (100, 100) # 初始座標

def draw():
    screen.clear()
    alien.draw()
    # 顯示目前的座標 (數學觀念可視化)
    screen.draw.text(f"Position: {alien.pos}", (10, 10), color="white")

def update():
    # 這裡對應數學的「加減法移動」
    if keyboard.right:
        alien.x = alien.x + 2
    if keyboard.left:
        alien.x = alien.x - 2
    if keyboard.down:
        alien.y = alien.y + 2
    if keyboard.up:
        alien.y = alien.y - 2
