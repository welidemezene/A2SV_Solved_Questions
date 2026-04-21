import sys

def solve():
   
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    t_str = next(it, None)
    if t_str is None: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(next(it))
        num_players = 1 << n # 2^n
        
        # We store players as [strength, original_index]
        players = []
        for i in range(num_players):
            players.append([int(next(it)), i])
            
        # Iterative Merge Sort (The Tournament Stages)
        for stage in range(n):
            half = 1 << stage
            step = 1 << (stage + 1)
            
            for start in range(0, num_players, step):
                # We compete: Left [start : start+half] vs Right [start+half : start+step]
                # Both halves are sorted from the PREVIOUS stage.
                
                # 1. Count wins for Left half (against original Right half)
                left_wins = []
                r_ptr = start + half
                end_r = start + step
                for l_ptr in range(start, start + half):
                    while r_ptr < end_r and players[r_ptr][0] < players[l_ptr][0]:
                        r_ptr += 1
                    left_wins.append(r_ptr - (start + half))
                
                # 2. Count wins for Right half (against original Left half)
                right_wins = []
                l_ptr = start
                end_l = start + half
                for r_ptr in range(start + half, start + step):
                    while l_ptr < end_l and players[l_ptr][0] < players[r_ptr][0]:
                        l_ptr += 1
                    right_wins.append(l_ptr - start)
                
                # 3. Apply all wins AFTER counting is finished for this block
                for i in range(half):
                    players[start + i][0] += left_wins[i]
                    players[start + half + i][0] += right_wins[i]
                
                # 4. Sort this block to prepare for the next stage
                # Python's Timsort is O(N) on merged sorted lists
                block = players[start : start + step]
                block.sort(key=lambda x: x[0])
                players[start : start + step] = block

        # Reconstruct final strengths in the original order
        final_ans = [0] * num_players
        for strength, original_idx in players:
            final_ans[original_idx] = strength
            
        sys.stdout.write(" ".join(map(str, final_ans)) + "\n")

if __name__ == "__main__":
    solve()