class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        # Compare Guitars based on their year attribute
        return self.year < other.year


# Create a list of Guitar objects
guitars = [
    Guitar("Guitar1", 1990, 500),
    Guitar("Guitar2", 1985, 450),
    Guitar("Guitar3", 2000, 600)
]

# Sort the list of Guitars by year (oldest to newest)
guitars.sort()

# Display the sorted list of Guitars
for guitar in guitars:
    print(f"{guitar.name} ({guitar.year}) - ${guitar.cost}")
