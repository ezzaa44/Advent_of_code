def process_stones(file_name, blinks):
    # Read initial arrangement of stones from input file
    with open(file_name, "r") as file:
        stones = list(map(int, file.read().strip().split()))

    # Process the stones for the given number of blinks
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                digits = str(stone)
                mid = len(digits) // 2
                left, right = int(digits[:mid]), int(digits[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)

# Specify input file and number of blinks
file_name = "input.txt"
blinks = 25

# Get the result
result = process_stones(file_name, blinks)

# Print the number of stones after 25 blinks
print(result)
