"""CP1404 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print("{} fuel = {}".format(limo.name, limo.fuel))
    limo.drive(115)
    print("{} odometer = {}".format(limo.name, limo.odometer))
    print(limo)


main()