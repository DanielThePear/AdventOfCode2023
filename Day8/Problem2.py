import os
import regex
import math


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    lr_input = lines[0]
    maps = {}
    
    for line in lines[2:]:
        result = regex.findall(r"\w\w\w", line)
        maps[result[0]] = (result[1], result[2])

    starting_points = [start_point for start_point in maps.keys() if start_point[2] == "A"]
    total_lcm = 1
    for start_point in starting_points:
        steps = 0
        curr_pos = start_point
        while curr_pos[2] != 'Z':
            for instruction in lr_input:
                curr_pos = maps[curr_pos][0 if instruction == "L" else 1]
                steps += 1
        
        total_lcm = math.lcm(total_lcm, steps)
    
    print(total_lcm)


if __name__ == "__main__": main()