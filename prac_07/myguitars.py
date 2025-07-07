"""
more guitars
Estimate: 30 minutes
Actual:   30 minutes
"""
import csv
from datetime import datetime

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """"""
    guitars = read_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    add_new_guitars(guitars)
    guitars.sort()
    write_to_file(FILENAME, guitars)


def add_new_guitars(guitars):
    """Get new guitars and add them to the list guitars."""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        print()
        name = input("Name: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name_width = max(len(guitar.name) for guitar in guitars)
    cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(datetime.today().year) else ""
        print(
            f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:{cost_width},.2f}{vintage_string}")


def read_file(filename):
    """Read a csv file and return a list of Guitar objects."""
    with open(filename, "r", newline="") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        guitars = []
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars

def write_to_file(filename, guitars):
    """Write Guitars to a file."""
    with open(filename, "w", newline="") as out_file:
        # for guitar in guitars:
        #     print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
        rows = []
        for guitar in guitars:
            rows.append([guitar.name, guitar.year, guitar.cost])
        writer = csv.writer(out_file)
        writer.writerows(rows)

main()
