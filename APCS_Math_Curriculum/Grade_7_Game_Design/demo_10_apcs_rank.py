# Grade 7 Demo 10: APCS Rank Logic
# 觀念：邏輯綜合 — 計算分數排名 (比我高分的人數 + 1)
# Run: pgzrun demo_10_apcs_rank.py

import random

WIDTH = 600
HEIGHT = 400

scores = [random.randint(50, 100) for _ in range(8)]
ranks = [0] * 8

def calculate_ranks():
    for i in range(8):
        rank = 1
        for j in range(8):
            if scores[j] > scores[i]:
                rank += 1
        ranks[i] = rank

calculate_ranks()

def draw():
    screen.fill("midnightblue")
    screen.draw.text("APCS Score Ranking System", (150, 20), fontsize=30, color="gold")
    
    for i in range(8):
        y = 80 + i * 40
        
        # Draw Bar
        w = scores[i] * 3
        screen.draw.filled_rect(Rect(100, y, w, 30), "blue")
        screen.draw.text(f"Student {i+1}", (20, y+5), color="white")
        screen.draw.text(str(scores[i]), (100 + w + 10, y+5), color="white")
        
        # Draw Rank
        screen.draw.text(f"Rank: {ranks[i]}", (500, y+5), color="yellow", fontsize=24)
        
    screen.draw.text("Press [R] to Randomize Scores", (150, 360), color="gray")

def on_key_down(key):
    global scores
    if key == keys.R:
        scores = [random.randint(50, 100) for _ in range(8)]
        calculate_ranks()
