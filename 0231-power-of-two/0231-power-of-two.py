class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
            # If n is less than or equal to 0, it cannot be a power of two
        if n <= 0:
            return False
        
        # Check if n & (n - 1) == 0 (this tells if n is a power of two)
        return n & (n - 1) == 0
        