# assert isinstance(True, int)
#
#
# def main():
#     names = ["Ada", "John", "Alan", "Bill", "Ash"]
#     ages = [13, 56, 25, 6, 56]
#     name_of_the_oldest = find_oldest_person(names, ages)
#     print(name_of_the_oldest)
#
#
# def find_oldest_person(names, ages):
#     return names[ages.index(max(ages))]
#
#
# main()
# name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
# new_name = input("Name: ")
# new_age = int(input("Age: "))
# name_to_age[new_name] = new_age
# name_space = max(len(name) for name in name_to_age.keys())
# age_space = max([len(str(age)) for age in name_to_age.values()])
# for name, age in name_to_age.items():
#     print(f"{name:{name_space}} - {age:{age_space}}")
# print(type(name_to_age.keys()))

from operator import itemgetter

data = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
name_space = max(len(key) for key in data.keys())
age_space = max(len(str(value)) for value in data.values())
for key, value in sorted(data.items(), key=itemgetter(1), reverse=True):
    print(f"{key:{name_space}} = {value:{age_space}}")
print(type(data.items()))


# def main():
#     fruits = ["apple", "orange", "pear", "banana", "watermelon"]
#     fruit_to_length = convert_list_to_dictionary(fruits)
#     print(fruit_to_length)
#     # fruits[5] = "blah"
# def convert_list_to_dictionary(list_to_convert):
#     # string_to_length = {}
#     # for string in list_to_convert:
#     #     string_to_length[string] = len(string)
#     # return  string_to_length
#     return {string: len(string) for string in list_to_convert}
# main()
