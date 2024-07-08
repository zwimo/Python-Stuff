# Thanks to https://www.youtube.com/@TechWithTim for his tutorial videos.
import random

top_range = input("Please type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Try a number greater than zero next time.')
        quit()
else:
    print('You need to type a number next time.')
random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('You need to type a number next time.')   
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print ("Maybe try a lower number.")
    else:
            print("Try a higher number.")

print("You guessed", guesses, "times.")
