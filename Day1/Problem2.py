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
    
    total = 0
    
    for line in lines:
        line_digits = regex.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)', line, overlapped=True) # got this from Mr. CSS, it works just as well as mine above
        if line_digits: total += int( # concatenate two strings, where the strings are the digit representations of the first and last numbers on the line.
            mapping.get(line_digits[0], line_digits[0]) + # i.e. if we look up "zero", this returns "0" from the mapping dict, but if we look up "0",
            mapping.get(line_digits[-1], line_digits[-1]) # it fails and falls back on the default value for .get(), which is the key that we were looking up, so it's the correct value.
        )

    print(total)

if __name__ == "__main__": main()