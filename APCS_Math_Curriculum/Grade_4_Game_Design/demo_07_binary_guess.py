# Grade 4 Demo 07: Binary Search Guessing
# 觀念：每次猜中間，可以最快找到答案
# Run: pgzrun demo_07_binary_guess.py

WIDTH = 600
HEIGHT = 400

# Range 1~100
low = 1
high = 100
target = 57  # The Answer
guess = (low + high) // 2

def draw():
    screen.fill("black")
    
    # Draw Number Line
    for i in range(1, 101):
        x = 50 + i * 5
        color = "gray"
        
        if i < low or i > high:
            color = "dimgray" # Eliminated
        elif i == target:
            color = "gold"    # Answer
        elif i == guess:
            color = "cyan"    # Current Guess
            
        screen.draw.line((x, 100), (x, 200), color)
        
    screen.draw.text(f"Range: {low} ~ {high}", (50, 250), fontsize=30, color="white")
    screen.draw.text(f"Computer Guesses: {guess}", (50, 300), fontsize=30, color="cyan")
    screen.draw.text("Press [SPACE] for next guess", (50, 350), color="yellow")

def on_key_down(key):
    global low, high, guess
    
    if key == keys.SPACE:
        if guess == target:
            return # Found it
            
        # Binary Search Logic
        if guess < target:
            low = guess + 1 # Too small, move low up
        else:
            high = guess - 1 # Too big, move high down
            
        guess = (low + high) // 2
