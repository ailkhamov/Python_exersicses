import random


number_list = (2,10, 50,10,54,60,70,22,442)
new_list = []
for i in number_list:
    if i % 7 == 0:
        print(i)
    elif i % 5 ==0:
        new_list.append(i)

        print(i)

# Program which guesses a number between 1 to 9

while True:
    guess = input("Guess a number from 1 to 9")
    if guess == "5":
        print("Well done")
        break


print(range(5))

## Write python program to count the number
# of even and odd numbers from a series of numbers

sample_numbers = [1,2,3,4,5,6,7,9,10,8,25,43,10]
even_number = 0
odd_number = 0
for i in sample_numbers:
    if i % 2:
        even_number = even_number + 1
    else:
        odd_number = odd_number + 1
print(f'Number of even numbers {even_number} and number of odd numbers are {odd_number}')

## Wrtite a Python program that pritns all the numbers
# from 0 to 6 exept 3 and 6

count = 0
while count <6:

    if count == 3:
        break
    continue
    print(count)
    count += 1