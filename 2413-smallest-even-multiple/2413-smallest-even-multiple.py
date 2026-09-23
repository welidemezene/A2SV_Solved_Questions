class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        n = lcm(n,2)
        return n