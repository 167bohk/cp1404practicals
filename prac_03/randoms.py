from random import randint

"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

What did you see on line 1?
1 random integer
What was the smallest number you could have seen, what was the largest?
min: 5, max: 20

What did you see on line 2?
1 random odd number
What was the smallest number you could have seen, what was the largest?

Could line 2 have produced a 4?
No it could not
What did you see on line 3?
1 random float
What was the smallest number you could have seen, what was the largest?
min: 2.5 max: 5.5(after rounding)
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
random_number = randint(1, 100)
print(random_number)
