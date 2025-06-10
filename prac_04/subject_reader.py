"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data from file and display subject details"""
    data = load_data()
    print(data)
    print("----------")
    display_subject_details(data)

def load_data():
    """Read data from file and return formatted nested list contain elements like: [subject, lecturer, number of students]."""
    lines_of_parts = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        lines_of_parts.append(parts)
    input_file.close()
    return lines_of_parts

def display_subject_details(lines_of_parts):
    """Display subject details like: CP1401 is taught by Ada Lovelace and has 192 students"""
    [print(f"{line_of_parts[0]} is taught by {line_of_parts[1]} and has {line_of_parts[2]} students") for line_of_parts in lines_of_parts]


main()
