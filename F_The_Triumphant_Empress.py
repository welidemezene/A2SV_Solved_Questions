import sys
from bisect import bisect_left

# Fast I/O
input = sys.stdin.read

def solve():
    data = input().split()
    if not data: return
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        q = int(next(it))
        
        a = [int(next(it)) for _ in range(n)]
        
        # Collect all queries
        queries = []
        for i in range(q):
            k, x = int(next(it)), int(next(it))
            queries.append((k, x, i)) # Store original index to print in order
            
        # 1. COORDINATE COMPRESSION
        # Collect all values of A and X to find their ranks
        all_vals = sorted(list(set(a + [q[1] for q in queries])))
        rank_map = {val: i + 1 for i, val in enumerate(all_vals)}
        num_ranks = len(all_vals)
        
        # 2. ORGANIZE QUERIES BY K
        queries_at = [[] for _ in range(n + 1)]
        for k, x, idx in queries:
            queries_at[k].append((x, idx))
            
        # 3. FENWICK TREE (BIT)
        bit = [0] * (num_ranks + 1)
        
        def update(idx, val):
            while idx <= num_ranks:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        # 4. THE WALK
        results = [0] * q
        for i in range(n):
            # Add current prisoner's skill rank to BIT
            update(rank_map[a[i]], 1)
            
            # Answer all queries for K = i + 1
            for x_val, q_idx in queries_at[i + 1]:
                # We want count of prisoners with skill < x_val
                # So we query up to rank_map[x_val] - 1
                results[q_idx] = query(rank_map[x_val] - 1)
                
        sys.stdout.write("\n".join(map(str, results)) + "\n")

solve()