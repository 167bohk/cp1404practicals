"""
Project Management
Estimate: 2 hours
Actual:
"""
import datetime
from operator import attrgetter
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
            load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            pass
        elif choice == "U":
            for i,project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = get_valid_integer("Project choice: ", 0, len(projects)-1 )

        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    saving_choice = input(f"Would you like to save to {FILENAME}? ").upper()
    if saving_choice == "YES":
        write_file(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def filter_projects(projects):
    """Filter projects by date."""
    threshold_date = get_valid_date_object("Show projects that start after date (dd/mm/yyyy): ")
    recent_projects = sorted([project for project in projects if project.is_recent(threshold_date)],
                             key=attrgetter("start_date"))
    for recent_project in recent_projects:
        print(recent_project)


def save_projects(projects):
    """Save projects to default file or a user selected file."""
    saving_choice = input(f"Would you like to save to {FILENAME}? ").upper()
    if saving_choice == "YES":
        write_file(FILENAME, projects)
    else:
        print("Where do you want to save?")
        out_filename = input("Enter the filename: ")
        write_file(out_filename, projects)


def load_projects():
    """Load projects from default file or a user selected file."""
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

def get_valid_date_object(prompt):
    """Get a valid date object."""
    is_valid_date_string = False
    while not is_valid_date_string:
        date_string = input(prompt)
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
            is_valid_date_string = True
        except ValueError:
            print("Invalid date!")
    return date

def get_valid_integer(input_prompt, lower_limit, upper_limit):
    """Get a valid integer."""
    is_valid_number = False
    while not is_valid_number:
        try:
            integer = int(input(input_prompt).strip())
            if integer >= lower_limit and integer <= upper_limit:
                is_valid_number = True
            else:
                print(f"Number out of range.")
        except ValueError:
            print("Invalid input; enter a valid number")
    return integer

main()
