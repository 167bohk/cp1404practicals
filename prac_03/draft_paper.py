#
# filename = input("Filename: ")
# in_file = open(filename, 'r')
# for line in in_file:
#     if line.strip()[0] == "#":
#         print(line.strip())
# in_file.close()

"""
P.
Python, Monty.
    Python,*Monty**


Python, Monty
.
"""
# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)
# print("Done")

# names = ["Lia", "Sam", "Bob"]
# for i, name in enumerate(names, 1):
#     with open(f"{name}.txt", "w") as out_file:
#         print(i, name, file=out_file)

# name = input("Filename: ")
name = "born.txt"
with open(name, "r") as in_file:
    lines = in_file.readlines()
for i in range(0, len(lines), 2):
    print(f"{lines[i].strip()} was born in {lines[i + 1].strip()}")
