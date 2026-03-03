# Grade 8 Demo 04: Stair Climbing (1D DP)
# 觀念：一維動態規劃 — 費氏數列應用，一次走1或2階
# Run: pgzrun demo_04_stair_dp.py

WIDTH = 600
HEIGHT = 400

N = 6
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
current_step = 2
timer = 0

def draw():
    screen.fill("black")
    
    # Draw Stairs
    for i in range(N + 1):
        x = 50 + i * 80
        y = 350 - i * 40
        screen.draw.line((x, y), (x+80, y), "white")
        screen.draw.line((x+80, y), (x+80, y-40), "white")
        
        # Show DP value
        if i < current_step:
            screen.draw.text(str(dp[i]), (x+30, y-30), fontsize=24, color="yellow")
            
    screen.draw.text(f"Ways to reach Step {N}", (20, 20), fontsize=30)
    screen.draw.text("DP[i] = DP[i-1] + DP[i-2]", (20, 60), color="cyan")

def update():
    global current_step, timer
    timer += 1
    if timer % 60 == 0:
        if current_step <= N:
            dp[current_step] = dp[current_step-1] + dp[current_step-2]
            current_step += 1
