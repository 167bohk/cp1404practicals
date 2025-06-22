"""
wimbledon
Estimate: 35 minutes
Actual:   40 minutes
"""
INDEX_FOR_COUNTRY = 1
INDEX_FOR_CHAMPION_NAME = 2
FILENAME = "wimbledon.csv"
def main():
    """Extract champion data from FILENAME then display them."""
    lines = read_file(FILENAME)
    print(lines)
    champion_countries, champion_to_win = extract_data(lines)
    display_champions_and_countries(champion_countries, champion_to_win)


def display_champions_and_countries(champion_countries, champion_to_win):
    """Display champions with wins and sorted countries."""
    print("Wimbledon Champions: ")
    for champion, win in champion_to_win.items():
        print(champion, win)
    print()
    print(f"These {len(champion_countries)} countries have won Wimbledon: \n{" ".join(champion_countries)}")


def extract_data(lines):
    """Extract a dictionary that maps from champion name to wins and a set of champion's countries."""
    champion_countries = set()
    champion_to_win = {}
    for line in lines:
        line = line.strip().split(",")
        champion_countries.add(line[INDEX_FOR_COUNTRY])
        champion_to_win[line[INDEX_FOR_CHAMPION_NAME]] = champion_to_win.get(line[INDEX_FOR_CHAMPION_NAME], 0) + 1
    champion_countries = sorted(list(champion_countries))
    return champion_countries, champion_to_win


def read_file(filename):
    """Read a csv file and return a list of lines(string)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        lines = in_file.readlines()
    return lines

main()
