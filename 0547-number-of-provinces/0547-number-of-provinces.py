class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        # The DFS Engine: Finds everyone in the same social circle
        def find_friends(city_index):
            for neighbor_index in range(n):
                # If there is a connection AND we haven't visited this neighbor yet
                if isConnected[city_index][neighbor_index] == 1 and not visited[neighbor_index]:
                    visited[neighbor_index] = True
                    # Recursively find all their friends too
                    find_friends(neighbor_index)

        # The Master Loop: Checks every city
        for i in range(n):
            if not visited[i]:
                # Found a city not yet assigned to a province
                province_count += 1
                visited[i] = True
                # Mark everyone connected to this city
                find_friends(i)
                
        return province_count