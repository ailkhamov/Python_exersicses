import time
# While loops!

# keeps looping an iterating until a condian is met
# OR it comes intoa  BREAK statement


# Syntax 1
# while <condition>:
    # Block
# Syntax 1
# while <condtion>:
    # Block
    # if < condtion>:
        #Break

# counter = 0
# while True < 10:
#     print("Index")
#     print(counter)
#     counter += 1
#     time.sleep(1)
user_input = ("")

while user_input != 'exit':
    user_input = input("What's up jigglypuff? ")
    if user_input  == 'cute':
        print("Ahh Jigglypuff...")
    else:
        print("JIGGGLY PUFF!")


cars = ['volvo', 'skoda', 'ferrari']

count = 0
max_len = len(cars)

while count < max_len:
    print(cars[count])
    count += 1


