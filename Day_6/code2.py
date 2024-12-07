def part_two():
    lines = read_lines_to_maze() # type: ignore
    answer = 0
    maze = {}
    start = None
    height = len(lines)
    width = len(lines[0])

    # Initialize the maze
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            maze[(row, col)] = cell
            if cell == "^":
                start = (row, col)

    visited = set()
    
    # Simulate the movement and check for loops
    curr = start
    direction = "up"
    
    while True:
        if direction == "up":
            if curr[0] - 1 < 0:
                break
            elif maze[(curr[0] - 1, curr[1])] == "#":
                direction = "right"
            else:
                curr = (curr[0] - 1, curr[1])
                if (curr, direction) in visited:
                    answer += 1  # Loop found
                    break
                else:
                    visited.add((curr, direction))
        elif direction == "down":
            if curr[0] + 1 >= height:
                break
            elif maze[(curr[0] + 1, curr[1])] == "#":
                direction = "left"
            else:
                curr = (curr[0] + 1, curr[1])
                if (curr, direction) in visited:
                    answer += 1  # Loop found
                    break
                else:
                    visited.add((curr, direction))
        elif direction == "right":
            if curr[1] + 1 >= width:
                break
            elif maze[(curr[0], curr[1] + 1)] == "#":
                direction = "down"
            else:
                curr = (curr[0], curr[1] + 1)
                if (curr, direction) in visited:
                    answer += 1  # Loop found
                    break
                else:
                    visited.add((curr, direction))
        elif direction == "left":
            if curr[1] - 1 < 0:
                break
            elif maze[(curr[0], curr[1] - 1)] == "#":
                direction = "up"
            else:
                curr = (curr[0], curr[1] - 1)
                if (curr, direction) in visited:
                    answer += 1  # Loop found
                    break
                else:
                    visited.add((curr, direction))

    print(f"Part 2: {answer}")
