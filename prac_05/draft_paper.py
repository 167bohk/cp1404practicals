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
name_to_age ={"Bill": 21, "Jane": 4, "Sven": 56}
new_name = input("Name: ")
new_age = int(input("Age: "))
name_to_age[new_name] = new_age
name_space = max(len(name) for name in list(name_to_age.keys()))
age_space = max([len(str(age)) for age in list(name_to_age.values())])
for name, age in name_to_age.items():
    print(f"{name:{name_space}} - {age:{age_space}}")