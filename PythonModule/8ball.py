import random
import sqlite3
import sys
import os
import time, math

# This module is sacred. Do not modify it without permission.
# Bonnie watches.

fallback_answers = [
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
    "Don't just play. Look too.",
    "You've brought this on yourself.",
    "AAAAAAAAAAAAAAAAAAAAAA",
    "Never skip breakfast on campaign day",
    "Do more with less."
]

def get_db_answers():
    try:
        db_path = os.path.join(os.path.dirname(__file__), "wisdoms.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ensure table exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Wisdoms (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Text TEXT NOT NULL
            );
        ''')
        conn.commit()

        # Query all wisdoms
        cursor.execute("SELECT Text FROM Wisdoms;")
        results = [row[0] for row in cursor.fetchall()]

        conn.close()

        return results
    except Exception as e:
        # Print to stderr if needed: print("DB error:", e, file=sys.stderr)
        return []


# Entropy system
def collect_entropy_vector(size=16):
    entropy = []
    for _ in range(size):
        t1 = time.perf_counter_ns()
        _ = sum(math.sin(i) for i in range(1, 100))
        t2 = time.perf_counter_ns()
        jitter = (t2 - t1) % 1000
        entropy.append(jitter / 1000.0)
    return entropy


# Tiny neural net: 16 inputs → 16 hidden → N outputs
def neural_choice(options):
    n_outputs = len(options)
    input_vector = collect_entropy_vector()

    # Initialize weights (static for consistency, but pseudo-random)
    def static_weight(i, j):
        return math.sin(i * 13.37 + j * 42.42) * 0.5

    # First layer: input → hidden
    hidden = []
    for h in range(16):
        val = sum(input_vector[i] * static_weight(i, h) for i in range(16))
        hidden.append(math.tanh(val))

    # Output layer
    scores = []
    for o in range(n_outputs):
        val = sum(hidden[h] * static_weight(h, o) for h in range(16))
        scores.append(val)

    # Choose index with max score
    index = scores.index(max(scores))
    return options[index]

# Magic 8 Ball
if __name__ == "__main__":
    question = sys.argv[1] if len(sys.argv) > 1 else ""

    db_answers = get_db_answers()
    available = db_answers if db_answers else fallback_answers

    print(neural_choice(available))

