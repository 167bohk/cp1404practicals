
# def print_grid(row, column):
#     for i in range(row):
#         print("*" * column)
#
#
#
# print_grid(4, 6)

# def function():
#     return 1, 2.2, True
# x, y, z = function()
# print(x)
# print(type(x))
# print(y)
# print(type(y))
# print(z)
# print(type(z))
# a = [function()]
# a.append(function())
# print(a[0][0])


# x = (1, 2, 3)
# print(*x)

# from random import randint
# MENU = "(N)ame\n(P)rint a line of asterisks\n(R)andom number\n(Q)uit"
# def main():
#     print(MENU)
#     choice = input(">>> ").upper()
#     while choice != "Q":
#         if choice == "N":
#             name = get_valid_name()
#             print(f"Wellcome {name}!")
#         elif choice == "P":
#             print_a_line(5)
#         elif choice == "R":
#             print(randint(1, 10))
#         else:
#             print("Invalid choice!")
#         print(MENU)
#         choice = input(">>> ").upper()
#     print("Farewell")
#
# def get_valid_name():
#     name = input("Enter your name: ")
#     while name == "":
#         print("Invalid name")
#         name = input("Enter your name: ")
#     return name
#
# def print_a_line(length):
#     print("*" * length)

