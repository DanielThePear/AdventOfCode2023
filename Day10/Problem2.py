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

    all_loop_nodes = loop_nodes(grid, S_pos) # Get a set of the coords of every node in the loop
    
    # Replace S in grid with the appropriate tile
    S_conn_1 = find_connector(grid, S_pos, None)
    S_offset_1 = (S_pos[0] - S_conn_1[0], S_pos[1] - S_conn_1[1])

    S_conn_2 = find_connector(grid, S_pos, S_conn_1)
    S_offset_2 = (S_pos[0] - S_conn_2[0], S_pos[1] - S_conn_2[1])

    grid[S_pos[0]][S_pos[1]] = next(ch for ch in valid_connectors[S_offset_1] if ch in valid_connectors[S_offset_2])
    

    # count how many tiles are inside the loop
    tiles_inside_loop = count_inside_loop(grid, all_loop_nodes)

    print(tiles_inside_loop)


def count_inside_loop(grid: list[list[str]], all_loop_nodes: set[tuple[int]]) -> int:
    count = 0
    enter_F = False

    for y, row in enumerate(grid):
        in_loop = False
        for x, col in enumerate(row):
            if (y, x) in all_loop_nodes:
                curr_tile = grid[y][x]

                if curr_tile == "F": enter_F = True
                elif curr_tile == "L": enter_F = False
                elif curr_tile == "|": in_loop = not in_loop
                elif enter_F and curr_tile == "J": in_loop = not in_loop
                elif not enter_F and curr_tile == "7": in_loop = not in_loop
                
            elif in_loop: count += 1
    
    return count


def loop_nodes(grid: list[list[str]], S_pos: tuple[int]) -> set[tuple[int]]:
    prev_pos = None
    curr_pos = S_pos
    all_loop_nodes = set()
    while 69:
        temp_pos = curr_pos
        curr_pos = find_connector(grid, curr_pos, prev_pos)
        prev_pos = temp_pos
        all_loop_nodes.add(curr_pos)
        if grid[curr_pos[0]][curr_pos[1]] == "S": return all_loop_nodes


def find_connector(grid: list[list[str]], curr_pos: tuple[int], exclude_pos: tuple[int]) -> tuple[int]:
    curr_node = grid[curr_pos[0]][curr_pos[1]]
    for offset in node_directions[curr_node]:
        testing_pos = tuple(map(lambda x, y: x + y, curr_pos, offset))
        try:
            if grid[testing_pos[0]][testing_pos[1]] in valid_connectors[offset] and testing_pos != exclude_pos: return testing_pos
        except: continue


if __name__ == "__main__": main()