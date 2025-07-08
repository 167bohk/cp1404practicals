"""
Project Management
Estimate: 2 hours
Actual:
"""
import datetime
from prac_07.project import Project
FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""
def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = read_file(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    saving_choice = input(f"Would you like to save to {FILENAME}? ").upper()
    if saving_choice == "YES":
        pass
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    """Display projects in two groups: completed and incomplete, both sorted by priority."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    completed_projects.sort()
    incomplete_projects.sort()
    print("Incomplete projects: ")
    [print(f"  {incomplete_project}") for incomplete_project in incomplete_projects]
    print("Completed projects: ")
    [print(f"  {completed_project}") for completed_project in completed_projects]


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