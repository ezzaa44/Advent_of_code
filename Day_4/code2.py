import os

def check_word(grid, x, y, dx, dy, word, rows, cols):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
            return False
    return True

def count_XMAS(grid, rows, cols):
    target_word = "XMAS"
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal-right-down
        (1, -1),  # Diagonal-left-down
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal-left-up
        (-1, 1)   # Diagonal-right-up
    ]

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if check_word(grid, r, c, dx, dy, target_word, rows, cols):
                    count += 1
    return count

def count_all_XMAS_patterns(grid, rows, cols):
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            center = grid[r][c]
            top_left = grid[r - 1][c - 1]
            top_right = grid[r - 1][c + 1]
            bottom_left = grid[r + 1][c - 1]
            bottom_right = grid[r + 1][c + 1]

            if center == 'A':
                # Pattern 1: M.S
                if top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S':
                    count += 1
                # Pattern 2: S.M
                if top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M':
                    count += 1
                # Pattern 3: M.M
                if top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S':
                    count += 1
                # Pattern 4: S.S
                if top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M':
                    count += 1

    return count

def main():
    file_path = "input.txt"  # Update this path if necessary

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} was not found.")
        return

    # Read the grid from the file
    try:
        with open(file_path, 'r') as file:
            grid = [line.strip() for line in file.readlines()]
    except PermissionError:
        print(f"Error: Permission denied when trying to open {file_path}.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    rows, cols = len(grid), len(grid[0])

    # Count occurrences of "XMAS"
    xmas_count = count_XMAS(grid, rows, cols)
    print(f"Count of XMAS: {xmas_count}")

    # Count all X-MAS patterns
    xmas_patterns = count_all_XMAS_patterns(grid, rows, cols)
    print(f"Total X-MAS patterns: {xmas_patterns}")

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
