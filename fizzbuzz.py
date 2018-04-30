print "Welcome to FizzBuzz"
print " "


while True:
    try:
        yournumber = int(raw_input("Enter a number between 1 and 100: "))
        print "You've entered " + str(yournumber) + "."
        num = int(yournumber)
        if yournumber > 100:
            print "Your number was over 100!"
            continue

        for num in range(1, yournumber+1):
            if num % 3 == 0 and num % 5 == 0:
                print "fizzbuzz"
            elif num % 3 == 0:
                print "fizz"
            elif num % 5 == 0:
                print "buzz"
            else:
                print num
        break

    except ValueError:
        print "You have not entered a number!"