"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
int(char)
2. When will a ZeroDivisionError occur?
10/0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
sure thing
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")