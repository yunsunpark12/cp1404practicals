import csv

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

def read_guitars_from_file():
    guitars = []
    with open('guitars.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, ${guitar.cost}")

def write_guitars_to_file(guitars):
    with open('guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

guitars = read_guitars_from_file()
display_guitars(guitars)

guitars.sort()
print("\nSorted guitars by year:")
display_guitars(guitars)

# Ask the user for new guitars
new_guitars = []
while True:
    name = input("Enter guitar name (or 'q' to quit): ")
    if name == 'q':
        break
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    new_guitar = Guitar(name, year, cost)
    new_guitars.append(new_guitar)

guitars.extend(new_guitars)
write_guitars_to_file(guitars)

print("\nAll guitars (including new ones):")
display_guitars(guitars)
