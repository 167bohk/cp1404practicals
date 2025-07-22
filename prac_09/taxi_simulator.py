from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    """"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(2, name="Limo", fuel=100), SilverServiceTaxi(4, name="Hummer", fuel=200)]
    current_taxi = None
    current_bill = 0.00
    total_bill = 0.00
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice!= "q":
        if choice == "c":
            for i,taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = get_valid_integer("Choose taxi: ", "Invalid taxi choice", len(taxis)-1, 0)
            current_taxi = taxis[taxi_choice]
        elif choice == "d":

        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill}")
        print(MENU)
        choice = input(">>> ").lower()




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