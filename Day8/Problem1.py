import os
import regex


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        lr_input = lines[0]
        
        maps = {}
        for line in lines[2:]:
            result = regex.findall(r"\w\w\w", line)
            maps[result[0]] = (result[1], result[2])

        curr_pos = "AAA"
        steps = 0
        while (curr_pos != "ZZZ"):
            for instruction in lr_input, 1:
                curr_pos = maps[curr_pos][0 if instruction == "L" else 1]
                steps += 1
                if curr_pos == "ZZZ": break;

        print(steps)


if __name__ == "__main__": main()