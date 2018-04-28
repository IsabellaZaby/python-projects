loop = 1

while loop == 1:

    print "Welcome to the Bella-Calculator!"
    x = int(raw_input("Enter your first number: "))
    print "You've entered " + str(x) + " " + "as your first number."
    y = int(raw_input("Enter your second number: "))
    print "You've entered " + str(y) + " as your second number."

    operation = raw_input("Choose math operation (+, -, *, /: ")
    print "You've chosen " + operation + "."

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

    print "\n"