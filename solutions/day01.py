"""
# [Historian Hysteria](https://adventofcode.com/2024/day/1)

##Part a:
Given two lists of numbers, you want to find the total distance between the lists.
The distance between two numbers is the absolute difference between them, so the distance between 8 and 3 is 5.

Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list,
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
For example, if you pair up a 3 from the left list with a 7 from the right list,
the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

To find the total distance between the left list and the right list, add up the distances between all of the pairs you found.
What is the total distance between your lists?

##Part b:
This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times
that number appears in the right list.

"""

from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        _left, _right = zip(*[map(int, line.split()) for line in data])
        distance = sum(abs(x - y) for x, y in zip(sorted(_left), sorted(_right)))

        return distance

    def part2(self, data):
        _left, _right = zip(*[map(int, line.split()) for line in data])
        score = sum(x * _right.count(x) for x in _left)

        return score
