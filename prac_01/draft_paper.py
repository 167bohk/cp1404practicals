# GST_RATE = 0.1
# item_price = float(input("Enter item price:"))
# gst_type = input("Has GST or not(y/n):")
# if gst_type == "y":
#     item_price += GST_RATE
# print(f"{item_price:2f}$")
#
# number = int(input("Enter an integer:"))
# count = 0
# while count != number:
#     count += 1
#     print(count, end=" ")
# print()
# for i in range(1 ,number + 1):
#     print(i, end=" ")

# ANSWER = 6
# guess = int(input("Enter number(1-10):"))
# while guess != ANSWER:
#     print("Wrong answer, guess again.")
#     guess = int(input("Enter number(1-10):"))
# print("Congratulations!")

# user_name = input("Enter your name:")
# while user_name == "":
#     print("Invalid name")
#     user_name = input("Enter your name:")
# salary = float(input("Enter your salary:"))
# while salary < 0:
#     print("Invalid salary")
#     salary = float(input("Enter your salary:"))
# print(f"{user_name.upper()}, your salary is {salary:.2f}$")

# number_of_ages = int(input("How many ages:"))
# total = 0
# for i in range(number_of_ages):
#     age = int(input("Enter age:"))
#     total += age
# average = total / number_of_ages
# print(total, average)

# total = 0
# count = 0
# age = int(input("Enter age:"))
# while age != -1:
#     total += age
#     count += 1
#     age = int(input("Enter age:"))
# average = total / count
# print(total, average)

"""
1-3
1-6
1-9
2-4
2-7
2-10
3-5
3-8
3-11
"""

for i in range(1, 10, 4):
    print(i, i * 2, end=" ")