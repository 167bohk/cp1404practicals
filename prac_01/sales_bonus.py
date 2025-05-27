"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALE_THRESHOLD = 1000.0
BONUS_RATE_LOW = 0.1
BONUS_THRESHOLD_HIGH = 0.15
user_sale = float(input("Enter sales: $"))
while user_sale >= 0:
    if user_sale >= SALE_THRESHOLD:
        bonus_rate = BONUS_THRESHOLD_HIGH
    else:
        bonus_rate = BONUS_RATE_LOW
    user_bonus = user_sale * bonus_rate
    print(f"your bonus is {user_bonus}$")
    user_sale = float(input("Enter sales: $"))