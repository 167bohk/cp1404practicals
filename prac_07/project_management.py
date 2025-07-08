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
- (Q)uit"""


def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = read_file(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            loading_choice = input(f"Would you like to load from {FILENAME}? ").upper()
            if loading_choice == "YES":
                read_file(FILENAME)
            else:
                print("Where do you want to load from?")
                is_valid_filename = False
                loading_filename = input("Enter the filename: ")
                while not is_valid_filename:
                    try:
                        read_file(loading_filename)
                        is_valid_filename = True
                    except FileNotFoundError:
                        print(f"No such file or directory called {loading_filename}")
                        loading_filename = input("Enter the filename: ")
        elif choice == "S":
            saving_choice = input(f"Would you like to save to {FILENAME}? ").upper()
            if saving_choice == "YES":
                write_file(FILENAME, projects)
            else:
                print("Where do you want to save?")
                out_filename = input("Enter the filename: ")
                write_file(out_filename, projects)

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
        write_file(FILENAME, projects)
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
        in_file.readline()  # ignore headers
        lines = in_file.readlines()
        for line in lines:
            parts = line.strip().split("\t")
            # print(parts)
            # input()
            project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y"), int(parts[2]),
                              float(parts[3]), int(parts[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def write_file(filename, projects):
    """Write projects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            pieces = [project.name, datetime.date.strftime(project.strat_date, "%d/%m/%Y"), str(project.priority),
                      str(project.cost_estimate), str(project.completion_percentage)]
            line = "\t".join(pieces)
            print(line, file=out_file)
    print(f"Saved {len(projects)} projects to {filename}")


main()
