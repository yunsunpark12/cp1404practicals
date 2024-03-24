from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r+')
    for line in in_file:
        part = line.strip().split(',')
        guitar = Guitar(part[0], part[1], part[2])
        guitars.append(guitar)
    guitars.sort()
    print(guitars)

    add_guitar(guitars, in_file)

    for guitar in guitars:
        print(guitar)


def add_guitar(guitars, in_file):
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        adding_guitar = Guitar(name, year, cost)
        guitars.append(adding_guitar)
        in_file.write(f'\n{name},{year},{cost}')
        print(adding_guitar, 'added.')
        name = input('Name: ')

    in_file.close()


main()