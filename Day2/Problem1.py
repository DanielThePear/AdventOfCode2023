import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    mapping = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total_id = 0

    for line in lines:
        game_id = int(regex.search(r"\d+", line).group())
        colors = regex.findall(r"(\d*) (red|green|blue)", line)
        if all(
            int(pair[0]) <= mapping[pair[1]]
            for pair in colors
        ): total_id += game_id
    
    print(total_id)
        

if __name__ == "__main__": main()