
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid) ,len(grid[0])
        freshcnt = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    freshcnt +=1
        if freshcnt == 0:
            return 0
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        elapsed_time = 0
        while queue:
            r ,c,time = queue.popleft()
            elapsed_time = time
            for rd , cd in direct:
                rn,cn = rd+r, cd +c
                if 0<= rn < rows and 0 <= cn < cols and grid[rn][cn] == 1:
                    grid[rn][cn] = 2
                    freshcnt -=1
                    queue.append((rn,cn,time + 1))
        if freshcnt == 0:
            return elapsed_time
        else:
            return -1                    



        