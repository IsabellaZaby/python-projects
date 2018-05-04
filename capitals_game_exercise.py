#create a dictionary with 3 countries and 3 capitals
#choose one country randomly
#print the country an its capital
import random
import json

capital_json = "capitals.json"

with open(capital_json, "r") as capi_count:
    capital_countries = json.load(capi_count)


print "Welcome to the Bella-Capital-Game!"
print " "
print "We're going to ask you the capitals of certain countries."
print "You start with 10 points. For every right answer you gain one, for every wrong one, you loose one. "
print " "


#after choosing the country randomly
#ask the user to input the capital to the chosen country
#compare the input and the real value

points = 10
#for country, capital in capital_countries.items():
for x in range (10):
    country = random.choice(capital_countries.keys())
    answer = raw_input("What is the capital of " + country + "?")
    answer = answer.lower()
    capital = capital_countries[country].lower()
    capital = capital.lower()
    if answer == capital:
        points += 1
        print "Congratulations! You have " + str(points) + " points."
    else:
        points -= 1
        print "Too bad, it's " + capital_countries[country] + ", you lost a point. You have " + str(points) + " points."

print "Your final points are " + str(points) + " points."
# if correct congratulate
#if wrong say sorry