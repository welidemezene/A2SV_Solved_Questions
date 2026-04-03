class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        freq1 = defaultdict(list)
        freq2 = defaultdict(int)

        q = deque()
        list1 = []
        for n in prerequisites:
            freq1[n[1]].append(n[0])
            freq2[n[0]]+=1
        for i in range(numCourses):
            if freq2[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            list1.append(course)
            for n in freq1[course]:
                freq2[n] -=1
                if freq2[n] == 0:
                    q.append(n)
        if len(list1) == numCourses:
            return list1
        else:
            return []        

        return list1    

        

        