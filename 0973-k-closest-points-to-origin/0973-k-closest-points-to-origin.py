class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points.sort(key=lambda x: x[0]**2 + x[1]**2)

        list1 = []
        for i in range(k):
            list1.append(points[i])
        return list1    
        