from random import randint
NUMBER_OF_COLUMNS = 6
MAX_RANDOM_NUMBER = 45
MIN_RANDOM_NUMBER = 1
lines = []
number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    numbers = []
    while len(numbers) < NUMBER_OF_COLUMNS:
        number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    lines.append(numbers)
[print(" ".join([f"{number:2}" for number in sorted(line)])) for line in lines]

