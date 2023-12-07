import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    total = sum(
        int(
            mapping.get(line_digits[0], line_digits[0]) + 
            mapping.get(line_digits[-1], line_digits[-1])
        )
        for line_digits in
        (
            regex.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)', line, overlapped=True)
            for line in lines
        )
    )

    print(total)

if __name__ == "__main__": main()