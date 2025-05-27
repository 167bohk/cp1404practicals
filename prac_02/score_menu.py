"""
CP1404/CP5632 - Practical
Menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
SCORE_LOW = 0
SCORE_HIGH = 100


def main():
    user_score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            grade = determine_grade(user_score)
            print(f"Result: {grade}")
        elif choice == "S":
            print_a_line(int(user_score // 1))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score"""
    score = float(input("Enter score: "))
    while score < SCORE_LOW or score > SCORE_HIGH:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_grade(score):
    """Determine user's grade according to the score"""
    if score < 50:
        return "Bad"
    if score <= 90:
        return "Passable"
    else:
        return "Excellent"


def print_a_line(number, character="*"):
    """Print a line of character("*" by default)"""
    print(character * number)


main()
