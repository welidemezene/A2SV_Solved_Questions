import sys
from bisect import bisect_left, bisect_right


input = sys.stdin.readline

def solve():
    
    line1 = input().split()
    if not line1: return
    n, l, r = map(int, line1)
    
    
    a = list(map(int, input().split()))
    

    a.sort()
    
    total_pairs = 0
    
   
    for i in range(n):
        
        lower_bound_val = l - a[i]
        upper_bound_val = r - a[i]
        
        
        
       
        start_idx = bisect_left(a, lower_bound_val, lo=i + 1)
        
        
        end_idx = bisect_right(a, upper_bound_val, lo=i + 1)
        
        
        total_pairs += (end_idx - start_idx)
        
    print(total_pairs)


t_str = input().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()