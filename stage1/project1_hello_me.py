# =============================================================
# Stage 1 — Mini Project 1: Hello, Me!
# =============================================================
# Goal: Print your name, age, and favourite color.
# Then ask the user (anyone running the program) for the same info.

# --- Your own info ---
my_name = "Alex"
my_age = 9
my_favourite_color = "blue"

print("=== About Me ===")
print(f"My name is {my_name}.")
print(f"I am {my_age} years old.")
print(f"My favourite color is {my_favourite_color}.")
print()  # blank line — print() with nothing prints an empty line

# --- Now ask the user ---
print("=== About You ===")
your_name = input("What is your name? ")
your_age = input("How old are you? ")          # still text — that's fine here
your_colour = input("What is your favourite color? ")

print()
print(f"Nice to meet you, {your_name}!")
print(f"You are {your_age} years old and your favourite color is {your_colour}.")
print("We are going to be great coding friends!")
