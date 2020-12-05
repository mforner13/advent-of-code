import numpy

with open("data.py") as f:
    data = f.readlines()


def clean_input(puzzle_input: list):
    cleaned_input = [row[:-1] for row in puzzle_input[:-1]]
    cleaned_input.append(puzzle_input[-1])
    return cleaned_input


def create_slope(cleaned_input: list):
    slope = [row * 100 for row in cleaned_input]
    return slope


def count_trees_encountered(slope: list, moves_right: int, moves_down: int):
    position = 0
    num_of_trees = 0
    target_index = 0
    for i in range(len(slope)):
        if target_index > (len(slope) - 1):
            break
        if slope[target_index][position] == "#":
            num_of_trees += 1
        position += moves_right
        target_index += moves_down
    return num_of_trees


slope = create_slope(clean_input(data))

alternatives = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees_encountered = [
    count_trees_encountered(slope, alt[0], alt[1]) for alt in alternatives
]

print(numpy.prod(trees_encountered))
