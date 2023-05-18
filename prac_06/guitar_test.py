from Prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson)
    Guitar.get_age(gibson)
    print(Guitar.is_vintage(gibson))

    another_guitar = Guitar("Another Guitar", 2013)
    Guitar.get_age(another_guitar)
    print(Guitar.is_vintage(another_guitar))


main()