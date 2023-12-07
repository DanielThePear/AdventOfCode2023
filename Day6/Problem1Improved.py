import os
import math


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        time_distance = tuple(
            zip(
                (int(each) for each in lines[0].split(":")[1].split()),
                (int(each) for each in lines[1].split(":")[1].split())
            )
        )
    
    all_ways = 1
    for time, distance in time_distance:
        # if (distance - (t * (time - t))) < 0
        # with d = distance, time = T, we have t^2 - Tt + d < 0
        r_point, l_point = solve_quadratic(1, -time, distance) # we get the roots, but they have to be rounded because of the rules of this problem

        l_point_rounded = math.ceil(l_point) if math.ceil(l_point) != l_point else math.ceil(l_point) + 1
        r_point_rounded = math.floor(r_point) if math.floor(r_point) != r_point else math.floor(r_point) - 1

        all_ways *= (r_point_rounded - l_point_rounded) + 1
    
    print(all_ways)


def solve_quadratic(a, b, c):
    
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return root1, root2


if __name__ == "__main__": main()