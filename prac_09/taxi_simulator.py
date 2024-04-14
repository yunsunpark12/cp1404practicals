from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    driving_taxi = -1
    bill_to_date = 0

    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            driving_taxi = choose_taxi(taxis)
            calculate_bill_to_date(bill_to_date)

        elif menu_choice == 'd':
            if driving_taxi == -1:
                print("You need to choose a taxi before you can drive")
                calculate_bill_to_date(bill_to_date)

            else:
                new_bill = drive_chosen_taxi(taxis, driving_taxi)
                bill_to_date = bill_to_date + new_bill
                calculate_bill_to_date(bill_to_date)
        else:
            print("Invalid option")
            calculate_bill_to_date(bill_to_date)

        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i]))


def choose_taxi(taxis):
    print("Taxis available: ")
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i]))
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("Invalid taxi choice")
        else:
            return taxi_choice

    except ValueError:
        print("Invalid taxi choice")


def drive_chosen_taxi(taxis, driving_taxi):
    distance = int(input("Drive how far? "))
    taxis[driving_taxi].drive(distance)
    new_bill = taxis[driving_taxi].get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxis[driving_taxi].name, new_bill))
    taxis[driving_taxi].start_fare()
    return new_bill


def calculate_bill_to_date(bill_to_date):
    print("Bill to date: ${:.2f}".format(bill_to_date))


if __name__ == '__main__':
    main()