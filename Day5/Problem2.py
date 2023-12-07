import os
import sys
import itertools


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        groups = f.read().split("\n\n") # splits each text grouping (for each map) into their own individual strings
        seeds_ungrouped = tuple(int(seed) for seed in groups[0].split(": ")[1].split())
        seeds = tuple(zip(itertools.islice(seeds_ungrouped, 0, None, 2), itertools.islice(seeds_ungrouped, 1, None, 2)))
        groups = [group.splitlines() for group in groups[1:]] # splits each grouping string into its individual lines
        groups = tuple(tuple(tuple(int(each) for each in sub_group.split()) for sub_group in group[1:]) for group in groups) # remove the title line, since we don't need it
    
    seed_locations_scanned = set()
    lowest_location = sys.maxsize
    for i, seed_pair in enumerate(seeds):
        print(f"Working on seed pair {i + 1}")
        percent_indices = seed_pair[1] // 100
        for j, seed in enumerate(range(seed_pair[0], seed_pair[0] + seed_pair[1])):
            if j % percent_indices == 0: print(f"{j // percent_indices}% done")
            if seed in seed_locations_scanned: continue
            seed_locations_scanned.add(seed)
            curr_val = seed
            for group in groups: curr_val = processMapping(group, curr_val)
            lowest_location = min(lowest_location, curr_val)
            
    print(lowest_location)


#@lru_cache(maxsize=4096) # makes it slower for some reason
def processMapping(maps: tuple[tuple[int]], in_val: int) -> int:
    for ind_map in maps:
        if not (ind_map[1] <= in_val < ind_map[1] + ind_map[2]): continue # if the number is out of the range
        # if the number is in the range:
        return ind_map[0] + (in_val - ind_map[1])
    
    return in_val


if __name__ == "__main__": main()