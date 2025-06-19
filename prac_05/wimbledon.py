"""
wimbledon
Estimate: 35 minutes
Actual:    minutes
"""
FILENAME = "wimbledon.csv"
def main():
    lines = read_file(FILENAME)
    # print(lines)

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        lines = in_file.readlines()
    return lines

main()
