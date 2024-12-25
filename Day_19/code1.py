from collections import deque
import os

def read_input(file_path):
    """
    Reads input from the given file path and separates towel patterns from designs.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist. Please provide a valid file path.")
    
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
    
    if len(lines) < 2:
        raise ValueError("Invalid input format. Ensure the file contains towel patterns and designs.")
    
    # Separate towel patterns and desired designs
    towel_patterns = lines[0].split(", ")
    designs = lines[2:]  # Skip the blank line and get designs
    return towel_patterns, designs

def can_form_design(design, towel_patterns):
    """
    Performs a BFS to check if the design can be created using the towel patterns.
    """
    queue = deque([design])
    seen = set()
    while queue:
        current = queue.popleft()
        if current == "":
            return True
        if current in seen:
            continue
        seen.add(current)
        for pattern in towel_patterns:
            if current.startswith(pattern):
                queue.append(current[len(pattern):])
    return False

def count_possible_designs(file_path):
    """
    Counts the number of designs that can be formed using the towel patterns.
    """
    towel_patterns, designs = read_input(file_path)
    possible_count = 0
    for design in designs:
        if can_form_design(design, towel_patterns):
            possible_count += 1
    return possible_count

if __name__ == "__main__":
    # Input file path
    file_path = "input.txt"
    
    try:
        # Count and print the number of possible designs
        result = count_possible_designs(file_path)
        print(f"Number of possible designs: {result}")
    except Exception as e:
        print(f"Error: {e}")
