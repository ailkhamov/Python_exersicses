# Define the following variable
# name, last_name, age, eye_color, hair_color

name = 'Abror'
last_name = 'Ilkhamov'
age = 12
eye_color = 'Blue'
hair_color = 'Black'
# Prompt user for input and re-assign these
name = input("What is your first name?")
last_name = input("What is your last name?")
age = int(input("what is your age?"))
hair_color = input("what is your hair colour?")
eye_color = input("What is your hair colour?")
# Print them back to the user as conversation
#  Hello Jack! Welcome, your age is 26, your eyes are green and your

print(f'Hello {name}! Welcome, you age is {age}, your eyes are {eye_color} and your hair colour is {hair_color}')

# Section 2 - Calculate in what year was the person born

import datetime
year = datetime.datetime.now().year
born = age - year
print(f'You said you were {age}, so you were born in {born}')
