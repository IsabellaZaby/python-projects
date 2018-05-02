#coding=utf8
print "Welcome to the Daily Menu Generator!"

menu = {}

while True:
     menuitem = raw_input("What is the special today? ")
     print "Your special today is " + menuitem + "."
     while True:
        try:
            itemprice = float(raw_input("How much does the %s cost? " % menuitem))
            itemprice = format(itemprice, '.2f')
            print "The price for the " + menuitem + " is " + str(itemprice) + "€."
            break
        except ValueError:
            print "You did not enter a number!"

     menu[menuitem] = itemprice
     print " "
     print "Your daily specials so far are %s" % menu
     print " "
     status = raw_input("Do you want to add more specials? Yes to continue, No to Exit ")
     status = status.lower()

     if status == "no":
         break
     elif status == "yes":
         print " "
         continue
     else:
         print "You did not enter yes or no!"

with open ("daily_specials.txt", "w+") as daily_specials_file:
    print "Your specials today are:"
    daily_specials_file.write("Daily Specials:\n")
    for item, price in menu.iteritems():
        print "- " + item + ": " + str(price) + "€."
        daily_specials_file.write("- " + item + ": " + str(price) + "€" + "\n")

print
print
print "Thank you for using the Bella-Menu-Generator! Program shutting down."
