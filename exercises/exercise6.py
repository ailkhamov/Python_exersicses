# # Assignment 2 for post class
#
# # Define an empty dictionary
# empty = {}

hero = input("Enter your hero: ")
start = input("Enter your favourite fruit ")
middle = input("Enter the your favourite country: ")
end = input("Enter your p ")

dictionary = {
    'Hero': hero,
    'Start': start,
    'Middle': middle,
    'End': end
}

# Print out the dictionary information in an ordered way so we can scan read the story.
for key, values in dictionary.items():
    print(values)

print(f'The hero of story is {}')

# Prompt user for input for a story
#     it should have: hero, beginning, middle, end
#      2 other things you define to be part of the story
#     add each response to the dictionary under an appropriate key
#

