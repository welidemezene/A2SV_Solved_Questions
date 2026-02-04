class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        le = len(intervals)
        list1 = [intervals[0]]
       
        for i in range(1,le):
            if list1[-1][1] >= intervals[i][0]:
                if list1[-1][1] < intervals[i][1]:
                    
                    list1[-1][1] = intervals[i][1]
            else:
                
                list1.append(intervals[i])
        return list1            


     

        