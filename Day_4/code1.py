def find_xmas_in_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    count = 0

    # Directions for searching (horizontal, vertical, diagonal)
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Top-left diagonal
        (-1, 1),  # Top-right diagonal
        (1, -1),  # Bottom-left diagonal
        (1, 1)    # Bottom-right diagonal
    ]

    # Helper function to check if "XMAS" can be found starting from (r, c) in a given direction
    def search_from(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            # Check if the new position is out of bounds
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            # Check if the character matches the word
            if grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate through the grid and search for "XMAS" in all directions
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search_from(r, c, dr, dc):
                    count += 1

    return count

# Function to read grid from input.txt file
def read_grid_from_file(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))  # Remove any trailing newline and convert to list
    return grid

# Read the grid from the input file
grid = read_grid_from_file('input.txt')

# Call the function and print the result
result = find_xmas_in_grid(grid)
print(f"XMAS appears {result} times in the grid.")
