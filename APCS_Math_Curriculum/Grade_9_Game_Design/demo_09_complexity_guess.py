# Grade 9 Demo 09: Complexity Guess
# 觀念：時間複雜度估算 — 判斷 N=10^5 時 O(N^2) 會不會 TLE
# Run: pgzrun demo_09_complexity_guess.py

import random

WIDTH = 600
HEIGHT = 400

questions = [
    {"n": 1000, "algo": "O(N^2)", "ok": True},
    {"n": 100000, "algo": "O(N^2)", "ok": False},
    {"n": 100000, "algo": "O(N log N)", "ok": True},
    {"n": 20, "algo": "O(2^N)", "ok": True},
    {"n": 50, "algo": "O(2^N)", "ok": False}
]
q_idx = 0
result = ""

def draw():
    screen.fill("midnightblue")
    
    q = questions[q_idx]
    screen.draw.text(f"N = {q['n']}", (50, 50), fontsize=50)
    screen.draw.text(f"Algo: {q['algo']}", (50, 120), fontsize=50, color="yellow")
    
    screen.draw.text("Will it TLE (Time Limit Exceeded)?", (50, 200), color="white")
    screen.draw.text("Press [Y] for Yes (TLE), [N] for No (Pass)", (50, 250), color="gray")
    
    screen.draw.text(result, (50, 350), fontsize=40, color="lime")

def on_key_down(key):
    global q_idx, result
    q = questions[q_idx]
    
    is_tle = not q["ok"]
    correct = False
    
    if key == keys.Y: # User says TLE
        correct = is_tle
    elif key == keys.N: # User says Pass
        correct = not is_tle
    else:
        return
        
    if correct:
        result = "Correct!"
        clock.schedule(next_q, 1.0)
    else:
        result = "Wrong!"

def next_q():
    global q_idx, result
    q_idx = (q_idx + 1) % len(questions)
    result = ""
