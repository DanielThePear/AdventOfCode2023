import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    total_powers = 0
    
    for line in lines:
        line_product = 1
        min_nums = {"red": 0, "green": 0, "blue": 0}
        colors = regex.findall(r"(\d*) (red|green|blue)", line)
        for pair in colors: min_nums[pair[1]] = max(int(pair[0]), min_nums[pair[1]])
        for val in min_nums.values(): line_product *= val
        total_powers += line_product
    
    print(total_powers)
        

if __name__ == "__main__": main()