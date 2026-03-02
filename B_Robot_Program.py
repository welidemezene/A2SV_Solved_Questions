import sys

def solve():
    # Read all input at once for speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx+1])
        k = int(input_data[idx+2])
        s = input_data[idx+3]
        idx += 4
        
        # Phase 1: Try to reach the origin (0) for the first time
        first_zero_time = -1
        current_x = x
        
        # We only need to check the string once or until k steps
        for i in range(min(n, k)):
            if s[i] == 'L':
                current_x -= 1
            else:
                current_x += 1
            
            if current_x == 0:
                first_zero_time = i + 1
                break
        
        # If we never hit zero in the first pass or within k steps
        if first_zero_time == -1:
            results.append(0)
            continue
        
        # Phase 2: We hit zero once. Now calculate how many more times 
        # it returns to zero in a cycle.
        ans = 1
        remaining_k = k - first_zero_time
        
        cycle_return_time = -1
        current_x = 0 # Starting from origin now
        for i in range(n):
            if s[i] == 'L':
                current_x -= 1
            else:
                current_x += 1
            
            if current_x == 0:
                cycle_return_time = i + 1
                break
        
        # If a cycle exists, add how many times that cycle fits in remaining k
        if cycle_return_time != -1:
            ans += (remaining_k // cycle_return_time)
            
        results.append(ans)

    # Print all results joined by a newline
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()