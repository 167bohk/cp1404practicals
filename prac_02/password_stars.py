
def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print a line of asterisks with the length of password"""
    print(len(password) * "*")


def get_password():
    """Get a valid password with a minimum length"""
    minimum_length = 10
    password = input(f"Enter your password(no shorter than {minimum_length} characters): ")
    while len(password) < minimum_length:
        print(f"Password length cannot shorter than {minimum_length} characters")
        password = input(f"Enter your password(no shorter than {minimum_length} characters): ")
    return password


main()