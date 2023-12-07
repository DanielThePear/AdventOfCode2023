import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    total = 0

    for line in lines:
        line_digits = regex.findall(r"\d", line)
        total += int(f"{line_digits[0]}{line_digits[-1]}")

    print(total)

if __name__ == "__main__": main()