"""
[--- Day 8: Resonant Collinearity ---](https://adventofcode.com/2024/day/8)

Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit.
The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas.
In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency,
but only when one of the antennas is twice as far away as the other. 
This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.
Antennas with different frequencies don't create antinodes; A and a count as different frequencies. 
However, antinodes can occur at locations that contain antennas. 
Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
"""

from utils.solution_base import SolutionBase
from collections import defaultdict

# with open('/home/cgruden/src/advent-of-code-2024/data/day08/puzzle_input.txt','r') as file:
#    data = file.read().splitlines()

class Solution(SolutionBase):
    def part1(self, data):
        antennae_map = [list(line) for line in data]
        rx,ry = len(antennae_map[0]), len(antennae_map)

        antennae_coords = defaultdict(list)

        for y in range(ry):
            for x in range(rx):
                if antennae_map[y][x] != '.':
                    antennae_coords[antennae_map[y][x]].append((y,x))
                            
        antinodes = set()

        for antenna, coords in antennae_coords.items():
            for i in range(len(coords)):
                for j in range(i+1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = tuple([a + b * _dir for a, b in zip(coords[_idx], diff)])
                        if 0 <= pos[0] < ry and 0 <= pos[1] < rx:
                            antinodes.add(pos)                   
        return(len(antinodes))

    def part2(self, data):
        _map = [list(line) for line in data]
        rows, cols = len(_map), len(_map[0])

        antennas = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                if _map[row][col] != ".":
                    antennas[_map[row][col]].append((row, col))

        antinodes = set()

        for antenna, coords in antennas.items():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = coords[_idx]
                        while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)
                            pos = tuple([a + b * _dir for a, b in zip(pos, diff)])

        return len(antinodes)