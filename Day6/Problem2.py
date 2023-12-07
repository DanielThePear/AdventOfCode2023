import os


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        time = int(lines[0].split(":")[1].replace(" ", ""))
        distance = int(lines[1].split(":")[1].replace(" ", ""))
    
    each_way = 0
    percent_indices = time // 100;
    for t in range(1, time):
        if t % percent_indices == 0: print(f"{t // percent_indices}% done")
        if (distance - (t * (time - t))) < 0: each_way += 1
        elif each_way > 0: break
    
    print(each_way)


if __name__ == "__main__": main()