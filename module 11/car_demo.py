import vehicles

def main():
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    print('Maker: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Doors: ', used_car.get_doors())

if __name__ == '__main__':
    main()