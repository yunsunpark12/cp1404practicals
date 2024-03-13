FILENAME = "wimbledon.csv"

def main():

    records = get_info()
    champion_to_count, countries = process_data(records)
    display_result(champion_to_count, countries)


def display_result(champion_to_count, countries):
    """print result"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
        print(f"\nThese {len(countries)} countries have won Wimbledon: ")
        print(", ".join(country for country in sorted(countries)))


def process_data(records):
    """process data"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def get_info():
    """get info"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)  # put clean csv info into dic
    return records


main()