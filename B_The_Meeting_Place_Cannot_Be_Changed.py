import sys

# THE FIREHOSE: High-speed data ingestion
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    
    # Load coordinates (X) and speeds (V)
    x_coords = [float(val) for val in input_data[ptr : ptr + n]]
    ptr += n
    v_speeds = [float(val) for val in input_data[ptr : ptr + n]]
    ptr += n
    
    # THE SEARCH BOUNDARIES
    # Minimum time could be 0 (already at the same spot)
    # Maximum time could be 10^9 (furthest distance / slowest speed)
    low = 0.0
    high = 1e9 
    
    # THE LOGARITHMIC SNIPER (Fixed 100 iterations for precision)
    for _ in range(100):
        mid_time = (low + high) / 2.0
        
        # --- THE CHECK ENGINE (O(N)) ---
        # Find the intersection of all possible movements
        current_max_left = -2e18 # Effectively negative infinity
        current_min_right = 2e18  # Effectively positive infinity
        
        for i in range(n):
            left_reach = x_coords[i] - (v_speeds[i] * mid_time)
            right_reach = x_coords[i] + (v_speeds[i] * mid_time)
            
            # Squeeze the global intersection
            if left_reach > current_max_left:
                current_max_left = left_reach
            if right_reach < current_min_right:
                current_min_right = right_reach
        
        # VALIDATION LOGIC
        if current_max_left <= current_min_right:
            # If they can meet, try to find an even smaller time
            high = mid_time
        else:
            # If the intervals don't overlap, we need more time
            low = mid_time
            
    # THE FINAL FLUSH
    # Printing with 12 decimal places for the Codeforces judge
    print("{:.12f}".format(high))

if __name__ == "__main__":
    solve()