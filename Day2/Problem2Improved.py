import os
import regex
import math

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    total_powers = 0
    
    for line in lines:
        min_nums = {"red": 0, "green": 0, "blue": 0}

        colors = regex.findall(r"(\d*) (red|green|blue)", line)
        for pair in colors: min_nums[pair[1]] = max(int(pair[0]), min_nums[pair[1]])
    
        total_powers += math.prod(min_nums.values())
    
    print(total_powers)


if __name__ == "__main__": main()