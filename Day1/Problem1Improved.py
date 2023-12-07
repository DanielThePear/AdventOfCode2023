import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    total = sum(
        int(f"{line_digits[0]}{line_digits[-1]}")
        for line_digits in 
        [
            regex.findall(r"\d", line) for line in lines
        ]
    )

    print(total)

if __name__ == "__main__": main()