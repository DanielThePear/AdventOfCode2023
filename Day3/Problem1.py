import os

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    total_sum = 0
    for i, line in enumerate(lines):
        curr_num = ""
        curr_num_adjacent = False
        for j, ch in enumerate(line):
            if ch.isnumeric():
                curr_num += ch
                curr_num_adjacent = max(curr_num_adjacent, look_directions(lines, i, j))
                try:
                    if not lines[i][j + 1].isnumeric():
                        if len(curr_num) > 0 and curr_num_adjacent:
                            total_sum += int(curr_num)
                        curr_num = ""
                        curr_num_adjacent = False
                except:
                    if len(curr_num) > 0 and curr_num_adjacent:
                        total_sum += int(curr_num)
                    curr_num = ""
                    curr_num_adjacent = False

    print(total_sum)


def look_directions(lines, i, j) -> bool:
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            try:
                if not (lines[i + y_offset][j + x_offset].isnumeric()):
                    print(f"Step 1 fine {lines[i + y_offset][j + x_offset]}")
                    if lines[i + y_offset][j + x_offset] != r'.':
                        print(f"Step 2 fine {lines[i + y_offset][j + x_offset]}")
                        return True
            except: continue
    return False

if __name__ == "__main__": main()