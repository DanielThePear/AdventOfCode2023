import os


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
        each_way = 0
        for t in range(1, time):
            if (distance - (t * (time - t))) < 0: each_way += 1
        
        all_ways *= each_way
    
    print(all_ways)


if __name__ == "__main__": main()