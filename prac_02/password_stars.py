minimum_length = 10
password = input(f"Enter your password(no shorter than {minimum_length} characters): ")
while len(password) < minimum_length:
    print(f"Password length cannot shorter than {minimum_length} characters")
    password = input(f"Enter your password(no shorter than {minimum_length} characters): ")
print(len(password) * "*")