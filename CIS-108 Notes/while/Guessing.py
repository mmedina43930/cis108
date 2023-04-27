from random import randint

number = randint(0,20)
count = 1
while count <= 5 :
    guess = int(input("I have a number between 0 and 20, Guess The number"))
    if guess == number:
        print ("you gussed right")
        break	# break out of the loop
    elif guess < number:
        print ("Guessed too low")
    elif guess > number:
        print ("Guessed too high")
    count += 1
input("Press Enter to Continue")
