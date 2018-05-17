#coding=utf8

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
class Person():
    def __init__(self, first_name, last_name, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city

url = "https://scrapebook22.appspot.com/"
response = urlopen(url).read()

soup = BeautifulSoup(response)

csv_file = open("person_list.csv", "w")

persons = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)

        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True}).string
        email = person_soup.find("span", attrs={"class": "email"}).string
        first_name, last_name = name.split(" ")

        person = Person(first_name=first_name, last_name=last_name, email=email, city=city)
        persons.append(person)

csv_file.write("First name,Last name,Email,City\n")
for person in persons:
    csv_file.write("%s,%s,%s,%s\n" % (person.first_name, person.last_name, person.email, person.city))

csv_file.close()


