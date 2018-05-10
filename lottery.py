#coding=utf8
import random
print " "
print "=" * 30
print "Welcome to the Bella-Lottery numbers generator."
print " "
while True:

    while True:
        try:
            amount = int(raw_input("Please enter how many random numbers you would like to have: "))
            break
        except ValueError:
            print "You did not enter a number!"


    def random_numbers(quantity):
        number_list = []
        while True:
            if len(number_list) == quantity:
                break
            ra_int = random.randint(1, 50)
            if ra_int not in number_list:
                number_list.append(ra_int)

        return number_list

    print random_numbers(amount)

    from askyesno import ask_yes_or_no_question

    again = ask_yes_or_no_question("Would you like to use the Bella-lottery-generator again?")
    if again == False:
        print "Thank you!"
        print "END"
        print "=" * 30
        break

