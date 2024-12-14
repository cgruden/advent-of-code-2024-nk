"""
[--- Day 11: Plutonian Pebbles ---](https://adventofcode.com/2024/day/11)

Input is a list of numbers.
Iterate (blink) over the list, a given number of times. During an iteration perform one of the following actions on each of the numbers in the list, 
considering them in order.

1. Replace a 0 with a 1.
2. If the length of the number is even, split the number into two separate numbers. High order numbers first, lower oder second.
3. If neither of the above conditions are met, replace the number with the number multiplied by 2024.

Preserve the order of the numbers in the list.

Part 1: how many stones are left after 25 iterations?
Part 2: how many stones are left after 100 iterations?
"""

from utils.solution_base import SolutionBase
from math import log, floor

class Solution(SolutionBase):

    def num_digits(self, n):
        """
        Returns the number of digits in an base-10 integer.
        """
        if abs(n) <= 9:
            return 1
        return floor(log( abs(n), 10)) + 1

    def split_integer(self, n):
        """
        Splits an integer with an even number of digits into two integers with an equal number of digits.
        """
        digits = self.num_digits(n)
        if digits % 2 == 0:
            half = digits // 2
            return n // 10 ** half, n % 10 ** half
        return n, 0
    
    def blink(self, stones):
        j = 0
        while j != len(stones):
            if stones[j] == 0:
                stones[j] = 1
            elif self.num_digits(stones[j]) % 2 == 0:
                stones[j:j+1] = self.split_integer(stones[j])
                j += 1
            else:
                stones[j] *= 2024
            j += 1
        return stones

    def part1(self, data):
        stones = list(map(int, data[0].split()))
        for i in range(25): 
            stones = self.blink(stones)
        return len(stones)

    def part2(self, data):
        stones = list(map(int, data[0].split()))
        print(f"Start: len(stones) = {len(stones)}")
        for i in range(75): 
            stones = self.blink(stones)
            print(f"iteration {i}: len(stones) = {len(stones)}")
        return len(stones)
