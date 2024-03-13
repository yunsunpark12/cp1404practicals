FILENAME = "wimbledon.csv"

def main():

    records = []

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)       # put clean csv info into dic

    champion_to_count = {}
    countries = set()

    for record in records:
            countries.add(record[1])
            try:
                champion_to_count[record[2]] += 1
            except KeyError:
                champion_to_count[record[2]] = 1

    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
        print(f"\nThese {len(countries)} countries have won Wimbledon: ")
        print(", ".join(country for country in sorted(countries)))

main()