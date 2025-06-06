# FILENAME= "name.txt"
# out_file = open(FILENAME, "w")
# user_name = input("Enter name: ")
# print(user_name, file=out_file)
# out_file.close()
# in_file = open(FILENAME, "r")
# print(f"Hi {in_file.read().strip()}!")
total = 0
with open("numbers.txt", "r") as in_file:
    for i in range(2):
        total += int(in_file.readline().strip())
print(total)
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line.strip())
print(total)
