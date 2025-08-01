from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    """Get taxi choice, take a taxi and print the bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(2, name="Limo", fuel=100), SilverServiceTaxi(4, name="Hummer", fuel=200)]
    current_taxi = None
    current_bill = 0.00
    total_bill = 0.00
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice!= "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_valid_integer("Choose taxi: ", "Invalid taxi choice", len(taxis)-1, 0)
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_valid_integer("Drive how far? ", "Invalid distance", 9999999999, 0) #up limit can be any number big enough
                current_taxi.start_fare()
                current_taxi.drive(distance)
                current_taxi_cost = current_taxi.get_fare()
                current_bill = current_taxi_cost
                total_bill += current_bill
                print(f"Your {current_taxi.name} trip cost you ${current_taxi_cost}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill}")
        current_bill = 0.00
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${round(total_bill,1):.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display taxis with their indexes."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_integer(prompt,error_prompt, up, low):
    """Get a valid integer."""
    is_valid_number = False
    while not is_valid_number:
        try:
            valid_integer = int(input(prompt))
            if valid_integer> up or valid_integer<low:
                print(error_prompt)
            else:
                is_valid_number = True
        except ValueError:
            print(error_prompt)
    return valid_integer

main()