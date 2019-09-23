# # Assignment 2 for post class
#
# # Define an empty dictionary
# empty = {}

hero = input("Enter your hero: ")
start = input("Enter the start of the story: ")
middle = input("Enter the middle of your story: ")
end = input("Enter the end of your story: ")

dictionary = {
    'Hero': hero,
    'Start': start,
    'Middle': middle,
    'End': end
}

# Print out the dictionary information in an ordered way so we can scan read the story.
for key, values in dictionary.items():
    print(key,values)

# Prompt user for input for a story
#     it should have: hero, beginning, middle, end
#      2 other things you define to be part of the story
#     add each response to the dictionary under an appropriate key
#

