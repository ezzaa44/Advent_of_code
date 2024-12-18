directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_whole_plot(plant, pos, plots, found, limits):
    x, y = pos
    for direction in directions:
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy
        if (new_x, new_y) not in found:
            if all(p in lim for p, lim in zip([new_x, new_y], limits)):
                if plots[new_y][new_x] == plant:
                    new_pos = (new_x, new_y)
                    found.add(new_pos)
                    found.update(get_whole_plot(plant, new_pos, plots, found, limits))
    return found

if __name__ == "__main__":
    # Read the input data
    with open("input.txt", "r") as file:
        raw_input = file.read().strip()

    if not raw_input:
        print("Input is empty.")
        exit()

    plots = list(map(list, raw_input.splitlines()))
    max_x = len(plots[0])
    max_y = len(plots)
    limits = [range(max_x), range(max_y)]
    visited = set()
    plots_identified = {}

    # Identify distinct plots
    for y in limits[1]:
        for x in limits[0]:
            start = (x, y)
            if start not in visited:
                plant = plots[y][x]
                found = set()
                found.add(start)
                found = get_whole_plot(plant, (x, y), plots, found, limits)
                plots_identified[start] = found
                visited.update(found)

    # Calculate areas and perimeters
    areas_perimeters = []
    for start, plot_coords in plots_identified.items():
        num_fences = 0
        for pos in plot_coords:
            x, y = pos
            for direction in directions:
                dx, dy = direction
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) not in plot_coords or any(
                    p not in lim for p, lim in zip([new_x, new_y], limits)
                ):
                    num_fences += 1
        areas_perimeters.append((len(plot_coords), num_fences))

    # Calculate the final result
    result = sum(a * p for a, p in areas_perimeters)
    print(result)
