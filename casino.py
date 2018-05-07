import random
from askyesno import ask_yes_or_no_question
print "=" * 30
print "Welcome to the Bella-Casino-Game!"
secret = random.randint(1,30)
counter = 0
while True:
    while True:
        while True:
            try:
                guess = int(raw_input("Guess the Number between 1 and 30: "))
                counter += 1
                break
            except ValueError:
                print "You did not enter a number!"

        if secret == guess:
            print "Congratulations! It really is " + str(secret) +"!"
            counter = 0
            break
        elif counter == 5:
            print "Sorry! You can only guess 5 times! The answer would have been " + str(secret) + "!"
            counter = 0
            break
        elif guess > secret:
            print "You guessed too high!"
        elif guess < secret:
            print "You guessed too low!"



    again = ask_yes_or_no_question("Would you like to play again?")
    if again == False:
        print "Thank you for playing!"
        print "END"
        print "=" * 30

        break