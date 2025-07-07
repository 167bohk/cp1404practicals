"""
more guitars
Estimate: 30 minutes
Actual:    minutes
"""
import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """"""
    guitars = read_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_file(filename):
    """Read a csv file and return a list of Guitar objects."""
    with open(filename, "r", newline="") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        guitars = []
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars



main()
