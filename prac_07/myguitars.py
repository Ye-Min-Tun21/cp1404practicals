import csv
from prac_06.guitar import Guitar


def load_guitars_from_file(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                name, year, cost = line
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        pass  # If the file doesn't exist, just return an empty list
    return guitars


def save_guitars_to_file(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Program for Guitar using Guitar class."""
    filename = "guitars.csv"
    guitars = load_guitars_from_file(filename)

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")

    save_guitars_to_file(filename, guitars)


if __name__ == "__main__":
    main()
