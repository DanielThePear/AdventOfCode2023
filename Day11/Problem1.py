import os
from itertools import combinations


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f: lines = f.read().splitlines()
    
    new_map = []
    
    # Expand rows
    for i, row in enumerate(lines):
        new_map.append(row)
        if "#" not in row: new_map.append("." * len(row))

    # Expand columns
    i = 0
    while i < len(new_map[0]):
        if "#" not in (new_map[j][i] for j in range(len(new_map))):
            for j in range(len(new_map)):
                new_map[j] = new_map[j][:i] + "." + new_map[j][i:]
            i += 1
        i += 1
    
    galaxies = [
        [y, x]
        for y, row in enumerate(new_map)
        for x, col in enumerate(row)
        if col == "#"
    ]
    galaxy_pairs = combinations(galaxies, 2)
    
    result = sum(
        abs(pair_2[0] - pair_1[0]) + abs(pair_2[1] - pair_1[1])
        for pair_1, pair_2 in galaxy_pairs
    )
    
    print(result)


if __name__ == "__main__": main()