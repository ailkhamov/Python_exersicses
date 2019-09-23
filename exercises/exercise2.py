# I Use of operators
# Equate something

# As a user I want to be able to guess a number and know if i got it correct or not
# so that i can know if i won OR NOT.

# we should define/assign number to a variable called magic number
# Ask user for input
# I need to check if the input matches the magic number
# I need to let the user know if the user was write or not

magic_number = 10
user_number = int(input("Pick your magic number: "))

print("Your guess was :" + " " + str(magic_number == user_number))