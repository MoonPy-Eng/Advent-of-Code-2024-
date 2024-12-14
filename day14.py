import re
import numpy as np
from collections import defaultdict

# Constants
WIDTH = 101
HEIGHT = 103

# Function to parse the input data
def parse_input(file_path):
    guards = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = list(map(int, re.findall(r"-?\d+", line)))
                assert len(numbers) == 4
                position = (numbers[0], numbers[1])
                velocity = (numbers[2], numbers[3])
                guards.append((position, velocity))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return guards

# Function to simulate positions after a certain time
def simulate(guards, width, height, time):
    new_positions = []
    for pos, vel in guards:
        new_x = (pos[0] + vel[0] * time) % width
        if new_x < 0:
            new_x += width
        new_y = (pos[1] + vel[1] * time) % height
        if new_y < 0:
            new_y += height
        new_positions.append((new_x, new_y))
    return new_positions

# Function for Part 1
def do_part1(guards, width, height):
    time = 100
    quadrants = np.zeros((2, 2), dtype=int)
    simulation = simulate(guards, width, height, time)
    for x, y in simulation:
        left_right = 0 if x < width // 2 else 1
        top_bottom = 0 if y < height // 2 else 1
        quadrants[left_right, top_bottom] += 1
    answer = np.prod(quadrants)
    return answer

# Function to visualize the positions (for debugging purposes)
def visualize(time, positions, width, height):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] = '█'
    print(f"Time: {time}")
    for row in grid:
        print("".join(row))
    print(f"Time: {time}")

# Main function
def main():
    input_path = r'day14_data.txt'
    print(f"Attempting to read file from: {input_path}")
    guards = parse_input(input_path)

    if not guards:
        print("No data found. Please check the file content.")
        return

    # Part 1
    part1_answer = do_part1(guards, WIDTH, HEIGHT)
    print(f"Part 1 Answer: {part1_answer}")

    # Part 2 would require additional translation of the logic and simulation process.

if __name__ == "__main__":
    main()
