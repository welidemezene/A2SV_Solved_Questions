# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        # 1. SEARCH SPACE INITIALIZATION
        # We start with the full range of driver versions.
        low = 1
        high = n
        
        # 2. THE LOGARITHMIC SNIPER (O(log N) Complexity)
        while low < high:
            # THE NVIDIA STANDARD: Midpoint Calculation
            # We use 'low + (high - low) // 2' instead of '(low + high) // 2'
            # to prevent Integer Overflow in low-level memory registers.
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                # If 'mid' is bad, the FIRST bad version is either 'mid'
                # or something to its left. We 'Squeeze' the high boundary.
                high = mid
            else:
                # If 'mid' is good, we know for a fact the bad version 
                # is strictly to the right. 
                low = mid + 1
        
        # 3. CONVERGENCE
        # When low == high, the range has collapsed onto the 
        # exact transition point (The First Bad Version).
        return low