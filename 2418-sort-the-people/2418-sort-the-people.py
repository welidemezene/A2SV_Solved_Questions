class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        le = len(heights)
        freq = defaultdict(str)
        for i in range(le):
            freq[heights[i]] = names[i]
        check = False
        
        for i in range(le):
            for j in range(i+1,le):
                if heights[j] > heights[i]:
                    heights[i],heights[j] = heights[j],heights[i]
                    
           
        li = []        
        for n in heights:   
            li.append(freq[n]) 
        return li                


        