# 🐍 Python Adventure — Learning Plan for [Your Son's Name]

> **Goal:** Go from zero to building your very own Python games and programs!
> **Start Date:** ___________  **Age:** 9 years old

---

## 📊 Overall Progress

| Stage | Topic | Status |
|-------|-------|--------|
| 1 | Hello, Python! — The Basics | ⬜ Not Started |
| 2 | Making Decisions — If / Else | ⬜ Not Started |
| 3 | Loops — Do It Again! | ⬜ Not Started |
| 4 | Functions — Your Own Magic Spells | ⬜ Not Started |
| 5 | Lists — Keep a Collection | ⬜ Not Started |
| 6 | 🎮 Final Project — Build a Game! | ⬜ Not Started |

> **How to update:** Change ⬜ → 🔄 when working on it, → ✅ when done!

---

## 🏆 Milestone Rewards

Agree on a fun reward for each milestone to stay motivated!

| Milestone | Reward | Earned? |
|-----------|--------|---------|
| Finish Stage 1 | _______________ | ⬜ |
| Finish Stage 2 | _______________ | ⬜ |
| Finish Stage 3 | _______________ | ⬜ |
| Finish Stage 4 | _______________ | ⬜ |
| Finish Stage 5 | _______________ | ⬜ |
| Finish Final Project | 🎉 Big celebration! | ⬜ |

---

## 🛠️ Setup Checklist

Before we code, let's get everything ready!

- [ ] Install Python from [python.org](https://www.python.org/downloads/) (get version 3.x)
- [ ] Install VS Code (a friendly code editor) from [code.visualstudio.com](https://code.visualstudio.com/)
- [ ] Install the **Python** extension inside VS Code
- [ ] Create a folder on the desktop called `python_adventure`
- [ ] Open that folder in VS Code
- [ ] Create a file called `hello.py` and run your very first program: `print("Hello, World!")`

---

## 📚 Stage 1 — Hello, Python! (The Basics)

**What you'll learn:** How to talk to the computer and make it do stuff.
**Time estimate:** ~1–2 weeks (15–20 min per session)

### What you already know
*(Nothing yet — this is the beginning! 🎉)*

### Concepts

- [ ] **Comments (`#`)** — Notes inside code that Python ignores; great for explaining what your code does
  - Example: `# This prints a greeting` then `print("Hello!")`
- [ ] **Indentation** — Python uses spaces to group code together; getting this wrong is the #1 beginner mistake!
  - Rule: always use 4 spaces (or one Tab) when Python expects it — you'll see why in Stage 2
- [ ] **print()** — Make the screen show messages
- [ ] **Variables** — Boxes that store information
  - [ ] Storing your name: `name = "Alex"`
  - [ ] Storing your age: `age = 9`
- [ ] **Data types** — Text (strings), numbers (int/float), and True/False (bool)
- [ ] **Type conversion** — Switching between types when you need to
  - `int("9")` turns the text `"9"` into the number `9`
  - `str(9)` turns the number `9` into the text `"9"`
  - `float("3.14")` turns text into a decimal number
- [ ] **input()** — Ask the user to type something *(always gives back text/string, even if they type a number!)*
- [ ] **String joining** — Combine text with `+` and `str()`
  - Example: `print("Hello " + name + "! You are " + str(age) + " years old.")`
- [ ] ⭐ **BONUS — f-strings** — A cleaner way to mix variables into a sentence *(try this once the basics feel easy)*
  - Example: `print(f"Hello, {name}! You are {age} years old.")`

### 🐛 When Things Break (Reading Error Messages)

Errors are clues, not failures! The two most common ones:

- **SyntaxError** — Python can't understand what you wrote (check spelling, missing `:`, mismatched quotes)
- **NameError** — You used a variable name Python doesn't recognise (check you spelled it the same way everywhere)

> **Tip:** Always read the last line of the error first — it tells you *what* went wrong. The line above tells you *where*.

### 🎯 Mini Projects

- [ ] **Hello, Me!** — Print your name, age, and favourite color
- [ ] **Magic 8-Ball v1** — User types a question, you print a funny answer
- [ ] **Mad Libs** — Ask for 3 words and build a silly story with them

### 📝 Notes & Fun Discoveries
```
(Write anything cool you learned or found tricky here!)



```

---

## 📚 Stage 2 — Making Decisions (If / Else)

**What you'll learn:** How to make programs choose what to do.
**Time estimate:** ~1–2 weeks

### What you already know
- print(), variables, data types, type conversion, input()

### Concepts

- [ ] **if** statement — "If this is true, do this"
- [ ] **else** — "Otherwise, do that"
- [ ] **elif** — "Or if this other thing is true…"
- [ ] **Comparison operators** — `==`, `!=`, `>`, `<`, `>=`, `<=`
  - ⚠️ **Gotcha:** `input()` always gives back text, so `age == 10` won't work until you convert: `int(age) == 10`
- [ ] **Logical operators** — `and`, `or`, `not`
- [ ] **`random` module** — Make the computer pick something randomly
  - `import random` at the top of your file
  - `random.choice(["rock", "paper", "scissors"])` picks one at random
  - `random.randint(1, 10)` picks a random number between 1 and 10

### 🎯 Mini Projects

- [ ] **Age Checker** — Is the user old enough to ride a roller coaster? (must be >= 10)
- [ ] **Number Guesser v1** — Pick a secret number, tell the user if their guess is too high, too low, or correct
- [ ] **Rock, Paper, Scissors** — Play one round against the computer

### 📝 Notes & Fun Discoveries
```
(Write anything cool you learned or found tricky here!)



```

---

## 📚 Stage 3 — Loops (Do It Again!)

**What you'll learn:** How to make the computer repeat tasks without writing the same code over and over.
**Time estimate:** ~1–2 weeks

### What you already know
- print(), variables, type conversion, input(), if / elif / else, comparison operators, random

### Concepts

- [ ] **`range()`** — Generate a sequence of numbers
  - `range(5)` → 0, 1, 2, 3, 4
  - `range(1, 6)` → 1, 2, 3, 4, 5
  - `range(0, 10, 2)` → 0, 2, 4, 6, 8 (step by 2)
- [ ] **for loop** — Repeat a fixed number of times
  - [ ] `for i in range(10):` — Count from 0 to 9
  - [ ] Loop through a list: `for item in my_list:`
- [ ] **while loop** — Repeat until something changes
- [ ] **break** — Stop the loop early
- [ ] **continue** — Skip to the next round of the loop

### 🎯 Mini Projects

- [ ] **Countdown Timer** — Count down from 10 to BLAST OFF! 🚀
- [ ] **Multiplication Table** — Print the 7 times table automatically
- [ ] **Number Guesser v2** — Keep guessing until you get it right (add a loop to v1!)
- [ ] **Password Gate** — Keep asking for the password until the user gets it right

### 📝 Notes & Fun Discoveries
```
(Write anything cool you learned or found tricky here!)



```

---

## 📚 Stage 4 — Functions (Your Own Magic Spells)

**What you'll learn:** How to write reusable chunks of code — like teaching the computer a new trick it can do anytime you ask.
**Time estimate:** ~1–2 weeks

### What you already know
- print(), variables, type conversion, input(), if / elif / else, for loops, while loops, break, continue

### Concepts

- [ ] **def** — Define (create) a function
- [ ] **Calling** a function — Using it
- [ ] **Parameters / Arguments** — Give the function information to work with
- [ ] **return** — Get an answer back from a function
- [ ] **`None`** — What a function gives back when there is no `return` *(good to know so bugs don't surprise you!)*
- [ ] **Variable scope** — Variables created *inside* a function stay inside it; they disappear when the function finishes
  - Example: if you write `score = 0` inside a function, code outside the function can't see it
  - Fix: either `return` the value, or define the variable *before* the function
- [ ] Why functions rock: **write once, use many times!**

### 🎯 Mini Projects

- [ ] **Greeter** — A function `greet(name)` that prints a personalised hello
- [ ] **Calculator** — Functions for `add()`, `subtract()`, `multiply()`, `divide()`
- [ ] **Story Generator** — A function that builds a short adventure story from inputs
- [ ] **Rock, Paper, Scissors v2** — Refactor your old game using functions

### 📝 Notes & Fun Discoveries
```
(Write anything cool you learned or found tricky here!)



```

---

## 📚 Stage 5 — Lists (Keep a Collection)

**What you'll learn:** How to store multiple things together — like a backpack full of items.
**Time estimate:** ~1–2 weeks

### What you already know
- print(), variables, type conversion, input(), if / elif / else, for / while loops, break, continue, functions with parameters and return

### Concepts

- [ ] **Creating a list** — `fruits = ["apple", "banana", "cherry"]`
- [ ] **Accessing items** — `fruits[0]` gives `"apple"`
- [ ] **Adding items** — `.append()`, `.insert()`
- [ ] **Removing items** — `.remove()`, `.pop()`
- [ ] **Length of a list** — `len(fruits)`
- [ ] **Looping through a list** — `for fruit in fruits:`
- [ ] **Sorting a list** — `.sort()`

### 🎯 Mini Projects

- [ ] **Shopping List App** — Add, remove, and display items on a list
- [ ] **Top 5 Favourites** — Store and print your top 5 games/movies
- [ ] **Quiz Game** — A list of questions, loop through and score the answers
- [ ] **Leaderboard** — Store and sort player scores

### 📝 Notes & Fun Discoveries
```
(Write anything cool you learned or found tricky here!)



```

---

## 🎮 Stage 6 — Final Project: Build a Game!

**What you'll use:** Everything from Stages 1–5!
**Time estimate:** ~2–3 weeks

### What you already know
- print(), variables, type conversion, input(), if / elif / else, for / while loops, break, continue, functions, lists — basically everything!

Choose **one** (or invent your own!):

- [ ] 🐍 **Snake & Ladder** (text version) — Roll a die, move your piece, hit snakes and ladders
- [ ] 🃏 **Blackjack / 21** — Card game against the computer
- [ ] 🔤 **Hangman** — Guess the word letter by letter
- [ ] 🏓 **Ping Pong/Pong** — ⚠️ *Very hard — uses `pygame`, a whole new library. Best tackled with Dad side-by-side. Save this for after the course, or as a special bonus project!*

### Project Checklist

- [ ] Write down what the game does (the rules) before coding
- [ ] Draw a simple plan on paper
- [ ] Write the code in small steps — don't do it all at once!
- [ ] Test it — does it work? Fix bugs 🐛
- [ ] Add a score / win condition
- [ ] Share it with someone and demo it 🎉

### 📝 Project Notes
```
Game I chose:

Things I need to figure out:

Bugs I found and fixed:



```

---

## 📅 Session Log

Use this table to track each coding session!

| Date | Stage | What We Did | Time Spent | How It Went 😕😐😄 |
|------|-------|-------------|------------|-------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

## 💡 Tips for Dad (Teaching Notes)

- **Keep sessions short** — 20–30 minutes is perfect for a 9-year-old. Stop while it's still fun!
- **Hands-on first** — Let him type all the code himself, even if it's slow.
- **Mistakes are great** — When there's an error, say "Ooh, a puzzle! What do you think is wrong?"
- **Connect to his interests** — Swap example names/topics for his favourite games, animals, or characters.
- **Celebrate small wins** — Every working program is worth a high-five 🙌
- **Don't rush** — It's okay to spend 2 sessions on the same concept if needed.
- **Use Python Tutor** — [pythontutor.com](https://pythontutor.com) lets you see code run step by step, kids love it!
- **Reference:** [Trinket.io](https://trinket.io) is great if you want to code in the browser without installing anything.

---

## 🔗 Helpful Resources

| Resource | What It Is | Link |
|----------|-----------|------|
| Python.org | Official Python docs | https://python.org |
| Trinket.io | Run Python in the browser, no install needed | https://trinket.io |
| Python Tutor | Visualise code step by step | https://pythontutor.com |
| Automate the Boring Stuff | Free beginner book | https://automatetheboringstuff.com |
| CS Unplugged | Computer science without computers (fun!) | https://csunplugged.org |
| Real Python | Tutorials for all levels | https://realpython.com |
| PyGame | Library for making graphical games | https://pygame.org |

---

## 🚀 Bonus Stage — What's Next? (For Fast Learners!)

Finished all 6 stages and want to keep going? Here are some exciting next steps!

- [ ] **Dictionaries** — Like a list, but with labels (keys) instead of numbers
  - `player = {"name": "Alex", "score": 0}`
- [ ] **File I/O** — Save and load data from a file (make scores that survive closing the program!)
- [ ] **Turtle graphics** — Draw cool art and patterns with Python's built-in `turtle` module *(no install needed!)*
- [ ] **`pygame` library** — Build real graphical games with graphics, sound, and animation
  - Start by exploring Dad's ping pong game code 🏓
- [ ] **APIs** — Ask the internet for information (e.g., today's weather) from inside Python
- [ ] **Classes & Objects** — Group data and functions together (how big programs are built)

> 💬 **Dad's note:** If he reaches this stage, consider signing up for a real course like
> [CS50P (Harvard, free!)](https://cs50.harvard.edu/python/) or [Codecademy Python](https://www.codecademy.com/learn/learn-python-3).

---

*Last updated: 2026-04-03*
