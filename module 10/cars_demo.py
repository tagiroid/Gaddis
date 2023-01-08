import cars

def main():
    model = input("What is your model: ")
    year = input("What year: ")
    my_car = cars.Cars(model, year)

    for i in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed())

    for i in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed())

if __name__ == '__main__':
    main()