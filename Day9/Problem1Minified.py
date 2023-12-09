import os
from functools import reduce
from itertools import takewhile
from sys import maxsize


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    data_lines = tuple(tuple(int(each) for each in line.split()) for line in lines)
    
    total_sum = sum(
        sum(
            (
                line[-1],
                reduce(
                    lambda x, y: x + y[-1],
                    reversed(
                        [(last_one := [line[i + 1] - line[i] for i in range(len(line) - 1)])] + 
                        list(
                            takewhile(
                                lambda x: not all(each == 0 for each in x),
                                ((last_one := [last_one[i + 1] - last_one[i] for i in range(len(last_one) - 1)]) for _ in range(maxsize))
                            )
                        )
                    ),
                    0
                )
            )
        )
        for line in data_lines
    )

    print(total_sum)


if __name__ == "__main__": main()