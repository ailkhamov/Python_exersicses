# Control flow - if statment
# Cpmtrols where the cod eis going to go
# depending on the result of the evaluations that return true or false, It runs a block of code or not.



# if <condition>:
    # BLOCK
#elif <contion> :
    # BLOCK
#else :
    #BLOCK

age = 17
driver_lisence = True

if age >= 17 and driver_lisence == True:
    print("You can vote and drive")
elif age >= 17 and driver_lisence == False:
    print("you can vote")
elif age >= 16:
    print("you can't leagally drink ")
elif age <= 15:
    print("You're too young go back to school")

movie_rating = input("Enter your movie rating: ").lower()

if movie_rating == 'universal':
    print("Everyone can watch it")
elif movie_rating == 'g#p`g':
    print(" General viewing, but scenes may unsuitable for you")
elif movie_rating == '12':
    print("Films classified 12A")
elif movie_rating == '15':
    print("no one younger than 15 can see it")
elif movie_rating == '18':
    print("no one younger than 18 can see it")
else:
    print("The movie rating you have entered is not regonised")

