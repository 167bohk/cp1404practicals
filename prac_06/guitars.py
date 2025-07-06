from prac_06.guitar import Guitar
CURRENT_YEAR = 2025
guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.")
    print()
    name = input("Name: ")
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
name_width = max(len(guitar.name) for guitar in guitars)
cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
print()
print("... snip ...")
print()
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:{cost_width},.2f}{vintage_string}")