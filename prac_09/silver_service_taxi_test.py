from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    new_car = SilverServiceTaxi("Hummer", 200, 4)
    new_car.get_fare()
    print(new_car.__str__())


if __name__ == '__main__':
    main()