# names = ["Lindsay", "Hossein", "Dmitry", "Bruce", "Alan"]
# try:
#     name_index_plus_1 = int(input(f"Enter number, up to {len(names)}: "))
#     print(names[name_index_plus_1 - 1])
# except ValueError:
#     print("Invalid number")
# except IndexError:
#     print("Number out of range")


# names = ["Ada", "John", "Alan", "Bill"]
# print(", ".join(names))
# # name_to_remove = input("Who do you what to remove? ").title()
# # while name_to_remove != "":
# #     try:
# #         names.remove(name_to_remove)
# #         print(names)
# #     except ValueError:
# #         print("Not in the list")
# #     print(", ".join(names))
# #     name_to_remove = input("Who do you what to remove? ").title()
# # print("Farewell")
from operator import itemgetter
#
# sorted(names)
# print(names)
# names.sort()
# print(names)
# print([name.upper() for name in names if name[0] == "A"])
# print(names)
# data = [[2,1],[2,0],[4,6],[9,3]]
# data.sort(key=itemgetter(1), reverse=True) #itemgetter(index number)
# print(data)
# data = sorted(data, key=itemgetter(0), reverse=True)
# print(data)
# print(["Hi "+name for name in names])
# print([name[0] for name in names])
# print(["Hi " + name for name in names if names.index(name) == 0])

# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     user_input_string = input("Enter numbers separated by commas: ")
#     numbers = sorted([float(number.strip()) for number in user_input_string.split(",")])
#     return numbers
#
# def square_numbers(numbers):
#     numbers = [number**2 for number in numbers]
#
# def display_numbers(numbers):
#     print("..".join([str(number) for number in numbers]))
#
# main()

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# max_length_0 = max([len(pair[0]) for pair in data])
# max_length_1 =max([len(str(pair[1])) for pair in data])
# string_messages = [f"{pair[0]:{max_length_0}} = {pair[1]:{max_length_1}}" for pair in sorted(data, key=itemgetter(1), reverse=True)]
# for line in string_messages:
#     print(line)
print(type(9) in (float, int))
print(True == 0)
print(isinstance(False, int))
