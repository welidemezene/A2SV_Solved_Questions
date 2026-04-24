class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        results = []
        
        
        def find_paths(current_node, current_path):
            
            if current_node == target:
                results.append(list(current_path))
                return
            
            
            for neighbor in graph[current_node]:
                
                current_path.append(neighbor)
                
                
                find_paths(neighbor, current_path)
                
               
                current_path.pop()
        
        
        find_paths(0, [0])
        return results