# Read the input file and parse the grid
grid = {
    x + y * 1j: int(val)
    for y, line in enumerate(open("input.txt").readlines())
    for x, val in enumerate(line.strip())
}

# Identify trailheads (positions with value 0)
trailheads = [p for p, val in grid.items() if val == 0]

# Initialize metrics
p1, p2 = 0, 0

# Process each trailhead
for start in trailheads:
    target, paths, ends = 1, {(start,)}, set()
    while paths and target <= 9:
        new_paths = set()
        for path in paths:
            for d in [1, -1, 1j, -1j]:  # Four possible directions
                new_pos = path[-1] + d
                if new_pos in grid and grid[new_pos] == target:
                    new_paths.add((*path, new_pos))
                    if target == 9:
                        ends.add(new_pos)
        paths = new_paths
        target += 1
    p1 += len(ends)  # Count successful endpoints
    p2 += len(paths)  # Count remaining paths

# Print the results
print(p1)
print(p2)
