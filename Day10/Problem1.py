import os

node_directions = {
    "S": ((-1, 0), (0, 1), (1, 0), (0, -1)), # North, East, South, West
    "F": ((0, 1), (1, 0)), # East, South
    "7": ((1, 0), (0, -1)), # South, West
    "J": ((0, -1), (-1, 0)), # West, North
    "L": ((-1, 0), (0, 1)), # North, East
    "-": ((0, 1), (0, -1)), # East, West
    "|": ((-1, 0), (1, 0)), # North, South
}
valid_connectors = {
    (-1, 0): ("|", "7", "F", "S"), # North
    (0, 1): ("-", "J", "7", "S"), # East
    (1, 0): ("|", "L", "J", "S"), # South
    (0, -1): ("-", "L", "F", "S"), # West
}

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        grid = [list(each) for each in f.read().splitlines()]
    
    S_pos = next(
        (y_pos, x_pos)
        for y_pos in range(len(grid))
        for x_pos in range(len(grid[0]))
        if grid[y_pos][x_pos] == "S"
    )

    loop_length = loop_len(grid, S_pos)
    result = loop_length // 2
    print(result)


def loop_len(grid: list[list[str]], S_pos: tuple[int]) -> int:
    prev_pos = None
    curr_pos = S_pos
    count = 0
    while 69:
        temp_pos = curr_pos
        curr_pos = find_connector(grid, curr_pos, prev_pos)
        prev_pos = temp_pos
        count += 1
        if grid[curr_pos[0]][curr_pos[1]] == "S": return count


def find_connector(grid, curr_pos, exclude_pos) -> tuple[int]:
    curr_node = grid[curr_pos[0]][curr_pos[1]]
    for offset in node_directions[curr_node]:
        testing_pos = tuple(map(lambda x, y: x + y, curr_pos, offset))
        try:
            if grid[testing_pos[0]][testing_pos[1]] in valid_connectors[offset] and testing_pos != exclude_pos: return testing_pos
        except: continue


if __name__ == "__main__": main()