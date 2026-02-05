import sys

def solve():
    # Fast I/O is non-negotiable for N=10^5
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        
        # We store (value, original_index) to keep them linked
        pairs = []
        for i in range(1, n + 1):
            val = int(input_data[ptr])
            ptr += 1
            pairs.append((val, i))
        
        # STEP 1: SORT BY VALUE
        # This is the "Magic" that allows us to break the loop early
        pairs.sort()
        
        ans = 0
        
        # STEP 2: NESTED LOOP WITH HARMONIC BREAK
        for i in range(n):
            v1, idx1 = pairs[i]
            
            for j in range(i + 1, n):
                v2, idx2 = pairs[j]
                
                # THE BUDGET CHECK:
                # Since i + j is at most 2n - 1, if the product
                # is larger than 2n, no further v2 will work for this v1.
                if v1 * v2 >= 2 * n:
                    break
                
                # THE PLEASANT CONDITION
                if v1 * v2 == idx1 + idx2:
                    ans += 1
                    
        results.append(str(ans))
    
    # Print all results for all test cases in one go
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()