import os
import itertools
from ctypes import *

class Mapping(Structure):
    _fields_ = [
        ("dest_start", c_longlong),
        ("src_start", c_longlong),
        ("range", c_longlong)
    ]

class MappingGroup(Structure):
    _fields_ = [
        ("group_length", c_int),
        ("group_array", POINTER(Mapping))
    ]

class Groups(Structure):
    _fields_ = [
        ("groups_amount", c_int),
        ("groups_array", POINTER(POINTER(MappingGroup)))
    ]

class Seeds(Structure):
    _fields_ = [
        ("seeds_amount", c_int),
        ("seeds_array", (c_longlong * 2) * 10)
    ]

def main() -> None:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    so_file = "/home/daniel/Code Projects/AdventOfCode2023/Testing/Problem2C.so"
    MyModule = CDLL(so_file)

    with open("input.txt", "r") as f:
        groups = f.read().split("\n\n") # splits each text grouping (for each map) into their own individual strings
        seeds_ungrouped = tuple(int(seed) for seed in groups[0].split(": ")[1].split())
        seeds = tuple(zip(itertools.islice(seeds_ungrouped, 0, None, 2), itertools.islice(seeds_ungrouped, 1, None, 2)))
        groups = [group.splitlines() for group in groups[1:]] # splits each grouping string into its individual lines
        groups = tuple(tuple(tuple(int(each) for each in sub_group.split()) for sub_group in group[1:]) for group in groups) # remove the title line, since we don't need it
    
    seeds_to_pass = Seeds(10, seeds)
    
    mapping_groups_py = []
    for group_1 in groups:
        c_arr_inner = (Mapping * len(group_1))(*group_1)
        mapping_groups_py.append(pointer(MappingGroup(len(group_1), c_arr_inner)))
    
    mapping_groups_c = (POINTER(MappingGroup) * len(groups))(*mapping_groups_py)
    groups_to_pass = Groups(len(groups), mapping_groups_c)

    groups_to_pass = Groups(
        len(groups),
        (POINTER(MappingGroup) * len(groups))(*(
            pointer(
                MappingGroup(
                    len(group_1),
                    (Mapping * len(group_1))(*group_1)
                )
            )
            for group_1 in groups
        ))
    )

    result = MyModule.compute_minimum_location(pointer(groups_to_pass), pointer(seeds_to_pass))
    print(result)

    pass



if __name__ == "__main__": main()