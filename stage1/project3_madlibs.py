# =============================================================
# Stage 1 — Mini Project 3: Mad Libs
# =============================================================
# Goal: Ask for a few words then build a silly story with them.

print("📖 Mad Libs — Fill in the blanks to make a silly story!")
print()

# Ask for words
animal    = input("Give me an animal: ")
adjective = input("Give me a describing word (e.g. fluffy, smelly, giant): ")
food      = input("Give me a food: ")

# Build the story
print()
print("=== Your Story ===")
print(f"One day, a {adjective} {animal} walked into a pizza shop.")
print(f'It looked at the menu and said, "I would like a large {food} pizza, please!"')
print(f"The chef was so surprised that he fell into a vat of {food}.")
print(f"The {animal} laughed all the way home.")
print()
print("THE END 😂")
