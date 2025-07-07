from prac_06.guitar import Guitar
CURRENT_YEAR = 2025
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another guitar", 2013, 114514)
print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age(CURRENT_YEAR)}")
print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age(CURRENT_YEAR)}")
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(CURRENT_YEAR)}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(CURRENT_YEAR)}")