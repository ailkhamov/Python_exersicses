# Mutiplies of 3 are POP
# Mutiplies of 5 are TOC

# as a user I should be asked for a number, so that i can play the game with my input
# as a player I should see the game counting up to my number and subsitute the mutiplies of 3 and 5 with
# the appropriate values, so that I can see if it is working

# As a player, I should be able to exit the game using the key word, so that i can stop playing

number = int(input("Please enter your number: "))
count = 0
while count < number:
 count += 1
 if count%3 == 0 and count%5==0:
     print('POPTOK')
 elif count % 3 == 0:
     print("POP")
 elif count% 5 ==0:
     print('TOK')
 else:
     print(f'{count}')
