print " "
print "Welcome to the Bella-Converter!"
print "This converter can convert kilometers into miles!"
print " "

while True:
    while True:
        try:
            kilometer = float(raw_input("Enter your kilometers here: "))
            print "You've entered " + str(kilometer) + " kilometers."
            result = float(kilometer * float(0.62))
            print str(kilometer) + " kilometers is " + str(result) + " miles."
            break
        except ValueError:
            print "You've not entered a number!"

    print " "
    print " "
    entry = raw_input("Do you want to convert again? (any button to continue, n to exit)")
    if entry == "n":
        print "Thank you for using the Bella-Converter!"
        print " "
        print " "
        break