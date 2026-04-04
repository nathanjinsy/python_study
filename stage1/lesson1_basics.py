# =============================================================
# Stage 1 — Lesson 1: The Basics
# =============================================================

# --- Comments ---
# Anything after a # sign is a comment. Python ignores it.
# Comments are notes for humans reading the code.

# --- print() ---
print("Hello, World!")          # Show a message on the screen
print("Python is awesome!")

# --- Variables ---
name = "Alex"                   # A string (text) variable
age = 9                         # An integer (whole number) variable
height = 1.35                   # A float (decimal number) variable
loves_games = True              # A bool (True or False) variable

print(name)
print(age)
print(height)
print(loves_games)

# --- Data Types ---
print(type(name))               # <class 'str'>
print(type(age))                # <class 'int'>
print(type(height))             # <class 'float'>
print(type(loves_games))        # <class 'bool'>

# --- String joining ---
print("Hello, " + name + "! You are " + str(age) + " years old.")

# --- f-strings (bonus — a much cleaner way!) ---
print(f"Hello, {name}! You are {age} years old and {height}m tall.")

# --- input() ---
# Uncomment the lines below to try asking the user for input:
user_name = input("What is your name? ")
print("Nice to meet you, " + user_name + "!")

# --- Type conversion ---
# input() always gives back TEXT, so if you want a number you must convert it:
user_age = int(input("How old are you? "))
print(f"Next year you will be {user_age + 1}!")
