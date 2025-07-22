from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    """"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(2, name="Limo", fuel=100), SilverServiceTaxi(4, name="Hummer", fuel=200)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice!= "q":
        if choice == "c":
            for i,taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = input("Choose taxi: ")

        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()


def get_valid_integer(prompt, up, low):
    valid_integer = input(prompt)

main()