# Advent of Code 2021 Day 1

with open("./data/input.txt") as f:
    depths = []


    for line in f:
        # Add the INTEGER to a list of depths
        depths.append(int(line))

print(depths)