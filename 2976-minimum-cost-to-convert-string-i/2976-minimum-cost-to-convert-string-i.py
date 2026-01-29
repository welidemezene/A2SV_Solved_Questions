class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. INITIALIZE THE "NOTEBOOK" (26x26)
        # We use a huge number (1e18) instead of float('inf') to avoid slow float math
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        # 2. FILL THE DIRECT FLIGHTS (Rules)
        for u_char, v_char, c in zip(original, changed, cost):
            u = ord(u_char) - ord('a')
            v = ord(v_char) - ord('a')
            # Keep only the cheapest direct path
            if c < dist[u][v]:
                dist[u][v] = c
                
        # 3. FLOYD-WARSHALL (The Triple Bridge Loop)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # 4. FINAL CALCULATION (The O(N) Pass)
        total_cost = 0
        for s, t in zip(source, target):
            if s == t: continue # Already correct, cost 0
            
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            res = dist[u][v]
            
            if res == inf:
                return -1 # Impossible to convert!
            total_cost += res
            
        return total_cost