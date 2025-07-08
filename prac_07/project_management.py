"""
Project Management
Estimate: 2 hours
Actual:
"""
import datetime
from prac_07.project import Project
FILENAME = "projects.txt"
def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = read_file(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")


def read_file(filename):
    """Read a file and return a list of Projects"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline() #ignore headers
        lines = in_file.readlines()
        for line in lines:
            parts = line.strip().split("\t")
            # print(parts)
            # input()
            project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y"), int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects

main()