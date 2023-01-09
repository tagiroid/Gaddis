import vehicles

def main():
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('Cars available: ')
    print('--------------')

    print('Maker: ', car.get_make())
    print('Model: ', car.get_model())
    print('Mileage: ', car.get_mileage())
    print('Price: ', car.get_price())
    print('Doors: ', car.get_doors())
    print()
    print('Maker: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print('Drive_type: ', truck.get_drive_type())
    print()
    print('Maker: ', suv.get_make())
    print('Model: ', suv.get_model())
    print('Mileage: ', suv.get_mileage())
    print('Price: ', suv.get_price())
    print('Passenger capacity: ', suv.pass_cap())
if __name__ == '__main__':
    main()