import os
import regex

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    total_sum = 0
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if not ch == "*": continue
            # so, if ch == "*", then:
            if len(numbers := look_directions(lines, i, j)) != 2: continue
            # so, if the "*" is adjacent to exactly 2 numbers:
            number_1 = build_number(lines, numbers[0][0], numbers[0][1])
            number_2 = build_number(lines, numbers[1][0], numbers[1][1])
            total_sum += number_1 * number_2

    print(total_sum)


def look_directions(lines, i, j) -> list:
    adjacents = []
    for y_offset in range(-1, 2):
        try:
            temp_result = regex.findall(r"\d+", lines[i + y_offset][j - 1 : j + 2])
            if len(temp_result) == 2:
                adjacents.append((i + y_offset, j - 1))
                adjacents.append((i + y_offset, j + 1))
            elif len(temp_result) == 1:
                for x_offset in range(-1, 2):
                    try:
                        if lines[i + y_offset][j + x_offset].isdigit():
                            adjacents.append((i + y_offset, j + x_offset))
                            break
                    except: continue
        except: continue
    return adjacents


def build_number(lines, i, j) -> int:
    number = ""
    offset = 0
    try:
        while lines[i][j + offset].isdigit():
            number = lines[i][j + offset] + number
            offset -= 1
    except: pass
    
    offset = 1
    try:
        while lines[i][j + offset].isdigit():
            number = number + lines[i][j + offset]
            offset += 1

    except: pass

    return int(number)


if __name__ == "__main__": main()