class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i,j = 0,0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            start_i , end_i = firstList[i]
            start_j , end_j = secondList[j]
            value1, value2 = max(start_i, start_j) , min(end_i, end_j)
           
            if value1 <= value2:
                 res.append([value1, value2])
                
            if end_i <= end_j:
                i +=1
            else:    
                j+=1
        return res            

        