class Vehicles():
    def __init__(self, brand, model, kilometers_so_far, service_date):
        self.brand = brand
        self.model = model
        self.kilometers_so_far = kilometers_so_far
        self.service_date = service_date

    def get_brand_model(self):
        return self.brand + " " + self.model



def list_cars(carlist):
    for car in carlist:
        print "Car: " + car.get_brand_model()
        print "Mileage: "+ str(car.kilometers_so_far)
        print "Service date: " + car.service_date
        print " "


def add_new_car(carlist):
    brand = raw_input("Brand: ")
    model = raw_input("Model: ")
    kilometers_so_far = raw_input("Kilometers: ")
    service_date = raw_input("Service date: ")
    new = Vehicles(brand=brand, model=model, kilometers_so_far=kilometers_so_far, service_date=service_date)
    carlist.append(new)

def edit_kilometers(carlist):
    for index, car in enumerate(carlist):
        print "ID " + str(index) + ": " + car.get_brand_model()
    selected_index = raw_input("Type in ID-Number to edit kilometers: ")
    selected_car = carlist[int(selected_index)]
    new_kilometer = raw_input("Type in new mileage: ")
    selected_car.kilometers_so_far = new_kilometer
    print "The " + selected_car.get_brand_model() + " has " + str(selected_car.kilometers_so_far) + " as its new mileage."

def export_list(carlist):
    with open("carlist.txt", "w+") as carlist_file:
        print "Your cars are:"
        carlist_file.write("Cars:\n")
        for car in carlist:
            print "-" + " Brand: " + car.brand + "," + " Model: "+ car.model + "," + " Kilometers: "+ str(car.kilometers_so_far) + "," + " Servicedate: " + car.service_date
            carlist_file.write("-" + "Brand: " + car.brand + "," + " Model: "+ car.model + "," + " Kilometers: "+ str(car.kilometers_so_far) + "," + " Servicedate: " + car.service_date + "\n")

def main():
    car_one = Vehicles(brand="Mercedes", model="A-Klasse", kilometers_so_far=250000, service_date="12.01.2019")
    car_two = Vehicles(brand="BMW", model="M5", kilometers_so_far=100000, service_date="06.06.2019")
    car_three = Vehicles(brand="Fiat", model="Punto", kilometers_so_far=25000, service_date="05.10.2018")
    carlist = [car_one, car_two, car_three]
    print " "
    print "=" * 30
    print "Welcome to the Bella-Vehicle-Manager!"
    print " "

    while True:
        print " "
        print "Please choose one of these options:"
        print "a) See all your cars"
        print "b) Add a new car"
        print "c) Edit kilometers"
        print "d) Export list"
        print "e) Quit program"
        print ""  # empty line

        selected_option = raw_input("Enter a, b, c, d or e: ")
        if selected_option.lower() == "a":
            list_cars(carlist)
        elif selected_option.lower() == "b":
            add_new_car(carlist)
        elif selected_option.lower() == "c":
            edit_kilometers(carlist)
        elif selected_option.lower() == "d":
            export_list(carlist)
        elif selected_option.lower() == "e":
            print "Thank you for using the Bella-Vehicle-Manager!"
            print "="*30
            break
        else:
            print "You did not enter a, b, c, d or e!"
            continue

if __name__ == "__main__":
    main()