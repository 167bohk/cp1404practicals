COLOUR_TO_CODE = {'bakermillerpink': '#ff91af', 'aqua': '#00ffff', 'absolutezero': '#0048ba', 'amethyst': '#9966cc',
                  'bananayellow': '#ffe135', 'dartmouthgreen': '#00703c', 'darklavender': '#734f96',
                  'crimson': '#dc143c', 'coralpink': '#f88379', 'darkolivegreen1': '#caff70'}

input_colour_name = input("Enter colour name: ").lower()
while input_colour_name != "":
    try:
        print(COLOUR_TO_CODE[input_colour_name])
    except KeyError:
        print("Invalid colour name")
    input_colour_name = input("Enter colour name: ").lower()
print("Farewell")