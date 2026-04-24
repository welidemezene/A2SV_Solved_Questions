class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0
                while queue:
                    u = queue.popleft()
                    for neighbor in graph[u]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1-color[u]
                            queue.append(neighbor)
                        elif color[neighbor] == color[u]:
                            return False
        return True            

        