# DA-108 : Python Programming - Task A
# Write a python program (script) which asks for user input by showing the prompt user input.
# It reads the input, does some processing and outputs the message received as input but with the case altered

import random
import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "Task_A - Case Flipper"
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)
print(linebreak)

user_input = ""

while user_input.lower() != "q":
    user_input = input("Enter a word to see magic ('q' to quit): ")

    if user_input.lower() == "q":  # Quit immediately without processing
        print(linebreak)
        print("Goodbye! Hope to see you again soon!")
        print(linebreak)
        break
    elif any(char.isalpha() for char in user_input):  # Pass if the input contains any letters
        output = ''.join(random.choice([char.upper(), char.lower()]) for char in user_input)
        print(linebreak)
        print("Magic Output :", output)
        print(linebreak)
    elif user_input.strip() or user_input == "":  # Fail if only special characters or numbers
        print(linebreak)
        print("> Ohh :( this will work on words only... Try Again!")
        print(linebreak)
