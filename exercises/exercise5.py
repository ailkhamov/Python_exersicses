# Assignment for post class
# Use variables and different data types
# Ask and store the following in variables:
# name, last_name. age, age_of_mother, 1 skills

name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
age_of_mother = int(input("Enter the age of your mother: "))
skill = input("Enter your three skills: ")

# Print out the information in a formatted manner
print(f'Your name is {name.lower().capitalize()} {last_name.lower().capitalize()}. Your age is {age}! Your mothers age is {age_of_mother}, your skills are {skill}!')

# Calculate age difference between response and mother
age_difference = age_of_mother - age
if age_of_mother < age:
    print('You cannot be older than your mother! Please enter the correct age')
else:
    print(f'The age diffence between you and your mother is {age_difference}')

# Store skills in a list.

# Convert string to a list
def Convert_to_string(string):
    li = list(string.split(" "))
    return li

print(Convert_to_string(skill))

# Print each skill in a formatted way (a little context text), appropriate string formatting
# like lower case or upper case etc
print(skill.upper())

