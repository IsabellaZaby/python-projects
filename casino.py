secret = 11

for x in range (5):
    guess = int(raw_input("Guess the Number between 1 and 30: "))
    if secret == guess :
        print "Congratulations! It really is 11!"
        break
    elif guess > secret:
        print "You guessed too high!"
    elif guess < secret:
        print "You guessed too low!"
