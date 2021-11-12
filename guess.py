

import random

taking_input_from_user = input("Type a number: ")

if taking_input_from_user.isdigit():
    taking_input_from_user = int(taking_input_from_user)

    if taking_input_from_user <= 0:
        print('Invalid as the value entered less than zero')
        quit()
else:
    print("next try enter nu,mber greater than zero")
    quit()

random_number = random.randint(0, taking_input_from_user)
counter_for_guesses = 0

while True:
    counter_for_guesses += 1
    asking_user_guesses = input("Make a guess: ")
    if asking_user_guesses.isdigit():
        asking_user_guesses = int(asking_user_guesses)
    else:
        print('Please type a number next time.')
        continue

    if asking_user_guesses == random_number:
        print("You got it!")
        break
    elif asking_user_guesses > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", counter_for_guesses, "counter_for_guesses")
