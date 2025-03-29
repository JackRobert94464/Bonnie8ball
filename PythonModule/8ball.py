import tkinter as tk
import random

# A list of 100 possible answers:
answers = [
    "It is certain.",
    "Yes, absolutely.",
    "No, definitely not.",
    "The outlook is good.",
    "Ask again later.",
    "Reply hazy, try again.",
    "Consult your intuition.",
    "Chances are high.",
    "Chances are low.",
    "The future is unclear.",
    "Focus and ask once more.",
    "Yes, but be cautious.",
    "It will require effort.",
    "Proceed without fear.",
    "Take a risk.",
    "Now is the time.",
    "Wait for a better moment.",
    "You will have to compromise.",
    "Success is guaranteed.",
    "Think it through carefully.",
    "Definitely yes.",
    "Definitely no.",
    "Consider an alternative path.",
    "Don't hesitate.",
    "Follow the signs.",
    "You already know the answer.",
    "Opportunities will arise.",
    "Be patient.",
    "Act decisively.",
    "Guard your secrets.",
    "Listen to advice.",
    "A surprise is coming.",
    "You must make the first move.",
    "Change your perspective.",
    "Let go of the past.",
    "Don't forget your priorities.",
    "Trust the process.",
    "Be cautious of hidden costs.",
    "Expect the unexpected.",
    "Now or never.",
    "Patience will pay off.",
    "Adapt to the situation.",
    "You are overthinking it.",
    "Actions speak louder than words.",
    "Listen to your heart.",
    "Take a leap of faith.",
    "You have the power.",
    "Gather more information.",
    "Timing is everything.",
    "Just say yes.",
    "Silence is golden.",
    "Don't let fear decide.",
    "Adventure awaits you.",
    "Learn from the past.",
    "Not everything is as it seems.",
    "Believe in your destiny.",
    "Focus on the present.",
    "Do what feels right.",
    "Doubts may arise.",
    "No need to rush.",
    "You have much to learn.",
    "Expect a twist.",
    "Let caution guide you.",
    "The answer is within you.",
    "Perseverance will triumph.",
    "Take the initiative.",
    "Proceed with confidence.",
    "Not a chance.",
    "Yes, but prepare carefully.",
    "Reconsider your assumptions.",
    "Trust your instincts.",
    "Stay the course.",
    "Give it some thought.",
    "You'll need expert advice.",
    "Don't overcomplicate it.",
    "You are on the right track.",
    "Anticipate resistance.",
    "Look for new perspectives.",
    "Make peace with uncertainty.",
    "Do not doubt yourself.",
    "It might surprise you.",
    "Seize the moment.",
    "Don't rely on luck alone.",
    "Look deeper for the truth.",
    "Your logic is sound.",
    "Pause and reflect.",
    "You have all you need.",
    "Release your expectations.",
    "Absolutely not.",
    "Trust is earned.",
    "A fresh start is possible.",
    "Better late than never.",
    "Wait for clarity.",
    "Persistence is key.",
    "Explore all options.",
    "Your plan will succeed.",
    "A new perspective is required.",
    "Your intuition is right.",
    "Patience is the best approach.",
    "Yes, but stay flexible.",
    "Ego = Pay the price.",
    "The bigger the wish The longer the delay The grander the consequences.",
    "Nothing is free.",
    "Don't just play. Look too."
]

def get_random_answer():
    """Pick a random answer from the list."""
    return random.choice(answers)

def start_countdown():
    """Start the 10-second countdown."""
    lbl_status.config(text="The universe is listening...")
    btn_start.config(state="disabled")
    countdown(10)

def countdown(seconds):
    """Handle the countdown and enable the Reveal button."""
    if seconds > 0:
        lbl_timer.config(text=f"{seconds} seconds remaining...")
        root.after(1000, countdown, seconds - 1)
    else:
        lbl_timer.config(text="Time's up!")
        lbl_status.config(text="Your answer is ready.")
        btn_reveal.config(state="normal")

def reveal_answer():
    """Reveal the answer when the button is clicked."""
    lbl_answer.config(text=get_random_answer())
    lbl_timer.config(text="")
    lbl_status.config(text="Here is your answer:")

# Create the main window
root = tk.Tk()
root.title("Magic 8 Ball")
root.geometry("400x400")
root.configure(bg="#2c3e50")

# Create a frame to hold the widgets
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(expand=True)

# Title Label
lbl_title = tk.Label(frame, text="Magic 8 Ball", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
lbl_title.pack(pady=10)

# Status Label
lbl_status = tk.Label(frame, text="Focus on your question and press start.", font=("Helvetica", 14), fg="#f39c12", bg="#2c3e50")
lbl_status.pack(pady=10)

# Timer Label
lbl_timer = tk.Label(frame, text="", font=("Helvetica", 14), fg="#1abc9c", bg="#2c3e50")
lbl_timer.pack(pady=10)

# Answer Label
lbl_answer = tk.Label(frame, text="", font=("Helvetica", 16), fg="#1abc9c", bg="#2c3e50", wraplength=350, justify="center")
lbl_answer.pack(pady=20)

# Start Button
btn_start = tk.Button(frame, text="Focus Your Question", command=start_countdown, font=("Helvetica", 14), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", bd=0, width=20, height=2)
btn_start.pack(pady=10)

# Reveal Button (Initially Disabled)
btn_reveal = tk.Button(frame, text="Reveal Answer", command=reveal_answer, font=("Helvetica", 14), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, width=15, height=2, state="disabled")
btn_reveal.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
