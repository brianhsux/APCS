# Grade 6 Demo 05: DP Coin Change (Dynamic Programming)
# 觀念：動態規劃 (DP) — 湊錢問題：用最少硬幣湊出目標金額
# Run: pgzrun demo_05_dp_coin_change.py

WIDTH = 600
HEIGHT = 400

coins = [1, 5, 10]
target = 18
dp = [float('inf')] * (target + 1)
dp[0] = 0
history = [-1] * (target + 1) # To track which coin used

# Calculate DP
for i in range(1, target + 1):
    for c in coins:
        if i - c >= 0:
            if dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                history[i] = c

def draw():
    screen.fill("midnightblue")
    
    screen.draw.text(f"Target Amount: {target}", (20, 20), fontsize=30)
    screen.draw.text(f"Coins Available: {coins}", (20, 50), fontsize=30)
    
    # Visualize DP Array
    for i in range(target + 1):
        x = 50 + (i % 10) * 55
        y = 150 + (i // 10) * 80
        
        val = dp[i] if dp[i] != float('inf') else "X"
        screen.draw.rect(Rect(x, y, 50, 50), "white")
        screen.draw.text(str(i), (x+5, y+5), color="yellow", fontsize=14) # Index
        screen.draw.text(str(val), (x+15, y+20), color="white", fontsize=24) # Min Coins
        
    # Show Solution Path
    curr = target
    solution = []
    while curr > 0:
        c = history[curr]
        solution.append(c)
        curr -= c
        
    screen.draw.text(f"Min Coins Needed: {dp[target]}", (20, 320), fontsize=30, color="lime")
    screen.draw.text(f"Solution: {solution}", (20, 360), fontsize=30, color="cyan")
