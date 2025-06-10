"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: " ))
        incomes.append(income)

    display_income_report(incomes)


def display_income_report(incomes):
    """Display income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total = calculate_total(income, total)
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def calculate_total(income, total):
    """Calculate total income up to current month."""
    total += income
    return total


main()