import os
import sys

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        groups = f.read().split("\n\n") # splits each text grouping (for each map) into their own individual strings
        seeds = tuple(int(seed) for seed in groups[0].split(": ")[1].split()) # isolate the seeds, which are the first line of input
        groups = [group.splitlines() for group in groups[1:]] # splits each grouping string into its individual lines
        groups = [[[int(each) for each in sub_group.split()] for sub_group in group[1:]] for group in groups] # remove the title line, since we don't need it
    
    lowest_location = sys.maxsize
    for seed in seeds:
        curr_val = seed
        for group in groups: curr_val = processMapping(group, curr_val)
        lowest_location = min(lowest_location, curr_val)
    
    print(lowest_location)


def processMapping(maps: list[list[int]], in_val: int) -> int:
    for ind_map in maps:
        if not (ind_map[1] <= in_val < ind_map[1] + ind_map[2]): continue # if the number is out of the range
        # if the number is in the range:
        return ind_map[0] + (in_val - ind_map[1])
    
    return in_val


if __name__ == "__main__": main()