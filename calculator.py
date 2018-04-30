print "Welcome to the Bella-Calculator!"
print " "
print " "

x = None
y = None
operation = None
while True:
    while True:
        try:
            x = float(raw_input("Enter your first number: "))
            print "You've entered " + str(x) + " " + "as your first number."
            break
        except ValueError:
            print "You did not enter a number!"

    while True:
        try:
            y = float(raw_input("Enter your second number: "))
            print "You've entered " + str(y) + " as your second number."
            break
        except ValueError:
            print "You did not enter a number!"


    while True:
        operation = raw_input("Choose math operation (+, -, *, /):")
        print "You've chosen " + operation + "."
        if operation in ["+", "-", "*", "/"]:
            break
        else:
            print "You did not enter a correct operation symbol!"

    if y == 0 and operation == "/":
        print "You can not divide by 0!"
    elif operation == "+":
        print "Your result is " + str(x + y) + "."
    elif operation == "-":
        print "Your result is " + str(x - y) + "."
    elif operation == "*":
        print "Your result is " + str(x * y) + "."
    elif operation == "/":
        print "Your result is " + str(x / y) + "."
    else:
        print "You did not choose a math operation."

    print " "
    print " "
    entry = raw_input("Want to use the Bella-Caluclator one more time? (any button to continue, n to Exit)")
    if entry == "n":
        print "Thank you for choosing the Bella-Calculator!"
        break