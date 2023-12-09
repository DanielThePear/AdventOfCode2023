import os


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    data_lines = tuple(tuple(int(each) for each in reversed(line.split())) for line in lines)
    
    total_sum = 0
    for line in data_lines:
        all_diffs = [find_diffs(line)]
        
        while not all(each == 0 for each in all_diffs[-1]):
            all_diffs.append(find_diffs(all_diffs[-1]))
        all_diffs[-1].append(0)
        
        for each_diff_i in range(len(all_diffs) - 1, 0, -1):
            all_diffs[each_diff_i - 1].append(all_diffs[each_diff_i - 1][-1] + all_diffs[each_diff_i][-1])
        
        total_sum += line[-1] + all_diffs[0][-1]
    
    print(total_sum)


def find_diffs(line) -> list:
    return [line[i + 1] - line[i] for i in range(0, len(line) - 1)]


if __name__ == "__main__": main()