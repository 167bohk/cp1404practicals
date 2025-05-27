"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import uniform
SCORE_LOW = 0
SCORE_HIGH = 100
def main():
    user_score = float(input("Enter score: "))
    while user_score < SCORE_LOW or user_score > SCORE_HIGH:
        print("Invalid score")
        user_score = float(input("Enter score: "))
    print(f"Your score: {user_score}\nYour grade: {determine_grade(user_score)}")
    random_score = uniform(SCORE_LOW, SCORE_HIGH)
    print(f"Random score: {random_score:.1f}\nRandom grade: {determine_grade(random_score)}")

def determine_grade(score):
    """Determine user's grade according to the score"""
    if score < 50:
        return "Bad"
    if score <= 90:
        return "Passable"
    else:
        return "Excellent"

main()
