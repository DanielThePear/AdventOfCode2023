import os
from itertools import combinations


EMPTY_EXPANSION_MULTIPLIER = 2 # each empty row or column is replaced by this many rows/columns.


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f: galaxy_map = f.read().splitlines()
    
    # rows that must be expanded
    row_expansions = [
        i
        for i, row in enumerate(galaxy_map)
        if "#" not in row
    ]

    # columns that must be expanded
    col_expansions = [
        i
        for i in range(len(galaxy_map[0]))
        if "#" not in (
            galaxy_map[j][i]
            for j in range(len(galaxy_map))
        )
    ]
    
    galaxies = (
        (y, x)
        for y, row in enumerate(galaxy_map)
        for x, col in enumerate(row)
        if col == "#"
    )
    galaxy_pairs = combinations(galaxies, 2)

    total = 0
    for pair_1, pair_2 in galaxy_pairs: 
        min_y, max_y = min(pair_1[0], pair_2[0]), max(pair_1[0], pair_2[0])
        min_x, max_x = min(pair_1[1], pair_2[1]), max(pair_1[1], pair_2[1])

        total += sum(
            (
                abs(pair_2[0] - pair_1[0]), # Y distance between the galaxies in an un-expanded universe
                abs(pair_2[1] - pair_1[1]), # X distance between the galaxies in an un-expanded universe
                (EMPTY_EXPANSION_MULTIPLIER - 1) * len([
                    i
                    for i in row_expansions
                    if i > min_y and i < max_y
                ]), # determine how many empty rows there are between the two galaxies, calculate the distance added by universe expansion for those rows, and add to total distance
                (EMPTY_EXPANSION_MULTIPLIER - 1) * len([
                    i
                    for i in col_expansions
                    if i > min_x and i < max_x
                ]) # determine how many empty cols there are between the two galaxies, calculate the distance added by universe expansion for those cols, and add to total distance
            )
        )

    print(total)
    

if __name__ == "__main__": main()