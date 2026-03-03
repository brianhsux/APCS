# Grade 9 Demo 10: APCS Mock Exam (Simulation)
# 觀念：模擬實作考 — 模擬一個小型的 APCS 考試介面與計時
# Run: pgzrun demo_10_mock_exam.py

WIDTH = 600
HEIGHT = 450

# Mock Questions
questions = [
    {
        "title": "Q1: Sum of Array",
        "desc": "Given N numbers, print sum.",
        "input": "1 2 3 4 5",
        "expected": "15",
        "solved": False
    },
    {
        "title": "Q2: Max Value",
        "desc": "Find max value in list.",
        "input": "10 50 30 20",
        "expected": "50",
        "solved": False
    },
    {
        "title": "Q3: String Reverse",
        "desc": "Reverse the string.",
        "input": "HELLO",
        "expected": "OLLEH",
        "solved": False
    }
]

current_q = 0
user_input = ""
message = ""
time_left = 60 * 5 # 5 minutes (in seconds, simulated)
frame_count = 0

def draw():
    screen.fill("black")
    
    # Header
    screen.draw.text("APCS Mock Exam System", (20, 20), fontsize=30, color="cyan")
    mins = time_left // 60
    secs = time_left % 60
    screen.draw.text(f"Time: {mins:02}:{secs:02}", (450, 20), fontsize=30, color="red")
    
    # Question Area
    q = questions[current_q]
    screen.draw.rect(Rect(20, 70, 560, 150), "white")
    screen.draw.text(q["title"], (40, 90), fontsize=30, color="yellow")
    screen.draw.text(q["desc"], (40, 130), fontsize=24, color="white")
    screen.draw.text(f"Sample Input: {q['input']}", (40, 170), fontsize=24, color="gray")
    
    # Status
    status_color = "lime" if q["solved"] else "red"
    status_text = "SOLVED" if q["solved"] else "UNSOLVED"
    screen.draw.text(f"Status: {status_text}", (400, 90), color=status_color)
    
    # Code Editor Area (Simulated)
    screen.draw.text("Your Output (Type Answer):", (20, 250), color="gray")
    screen.draw.rect(Rect(20, 280, 560, 50), "blue")
    screen.draw.text(user_input + "_", (30, 295), fontsize=30, color="white")
    
    screen.draw.text(message, (20, 350), color="orange", fontsize=24)
    screen.draw.text("Press [ENTER] to Submit, [TAB] Next Question", (20, 400), color="gray")

def update():
    global time_left, frame_count
    if time_left > 0:
        frame_count += 1
        if frame_count % 60 == 0: # Approx 1 sec
            time_left -= 1

def on_key_down(key, unicode):
    global user_input, message, current_q
    
    if key == keys.TAB:
        current_q = (current_q + 1) % len(questions)
        user_input = ""
        message = ""
        
    elif key == keys.RETURN:
        # Check Answer
        q = questions[current_q]
        if user_input.strip() == q["expected"]:
            q["solved"] = True
            message = "Accepted (AC)!"
        else:
            message = "Wrong Answer (WA)"
            
    elif key == keys.BACKSPACE:
        user_input = user_input[:-1]
        
    else:
        # Simple typing
        if len(unicode) > 0 and unicode.isprintable():
            user_input += unicode
