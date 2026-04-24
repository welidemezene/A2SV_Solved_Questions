import collections

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        # 1. THE PHONEBOOK (Adjacency List)
        # adj[i] = list of bombs that bomb 'i' can detonate
        adj = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j: continue # Don't check yourself
                
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                # Check if bomb i can reach bomb j
                # Distance squared logic: (x1-x2)^2 + (y1-y2)^2 <= r1^2
                d_squared = (x1 - x2)**2 + (y1 - y2)**2
                if d_squared <= r1**2:
                    adj[i].append(j)
        
        # 2. THE FIRE-SPREADER (DFS)
        def spread_fire(start_bomb, visited):
            visited.add(start_bomb)
            count = 1
            
            for neighbor in adj[start_bomb]:
                if neighbor not in visited:
                    count += spread_fire(neighbor, visited)
            
            return count

        # 3. THE MASTER SEARCH
        max_bombs = 0
        for i in range(n):
            # Try starting the explosion at bomb 'i'
            # We need a fresh 'visited' set for EVERY start!
            visited = set()
            count = spread_fire(i, visited)
            
            if count > max_bombs:
                max_bombs = count
                
        return max_bombs