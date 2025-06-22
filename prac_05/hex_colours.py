COLOUR_TO_CODE = {'bakermillerpink': '#ff91af', 'aqua': '#00ffff', 'absolutezero': '#0048ba', 'amethyst': '#9966cc',
                  'bananayellow': '#ffe135', 'dartmouthgreen': '#00703c', 'darklavender': '#734f96',
                  'crimson': '#dc143c', 'coralpink': '#f88379', 'darkolivegreen1': '#caff70'}

colour_name_searched = input("Enter colour name: ").lower()
while colour_name_searched != "":
    try:
        print(COLOUR_TO_CODE[colour_name_searched])
    except KeyError:
        print("Invalid colour name")
    colour_name_searched = input("Enter colour name: ").lower()
print("Farewell")