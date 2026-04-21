import sys
import math

# Use isqrt for perfect integer square roots (avoids float errors)
def get_on_count(n):
    return n - math.isqrt(n)

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    t = int(input[0])
    results = []
    
    for i in range(1, t + 1):
        k = int(input[i])
        
        # Binary Search for the minimum n
        low = 1
        high = 2 * 10**18 # k is 10^18, so n is around that
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check how many bulbs stay ON if we have 'mid' bulbs
            if get_on_count(mid) >= k:
                ans = mid      # We found enough, but can we go smaller?
                high = mid - 1
            else:
                low = mid + 1  # Not enough bulbs ON, we need a bigger n
        
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

solve()