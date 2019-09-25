# Story book!
# Create a dictionary with 3 stories inside! like a book :)
# each story should be it's own dictionary with:
    # beggining, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:


books = {
    'Story1': { 'start': 'I started walking to the river',
                'middle': 'After the long walk in the river, I accidentally did a ',
                'end': 'I panicked and jumped into the river and batman came and saved me',
                'hero': 'Batman'
                },
    'Story2':{  'start': 'I have finished doing my home work',
                'middle': 'Teacher said my homework was wrong',
                'end': 'I redone my homework again and passed',
                'hero': 'I was the hero of the story'

                }
}
while True:
    question = input("Enter the story you want to read or type exit if you want to quit:")
    for key in books:
        for key2 in books[key]:
            if question == 'Story1':
                print(books['Story1'][key2])
            elif question == 'Story2':
                print(books['Story2'][key2])
            elif question == 'exit':
                print("Thank you for reading our books! Bye for now!")
                break
            else:
                print("The story you have entered does not exist in our dictionary")