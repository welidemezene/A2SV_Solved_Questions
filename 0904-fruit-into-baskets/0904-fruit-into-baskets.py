class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        le = len(fruits)
        max1 = 0
        l=0
        freq1 = defaultdict(int)
        for i in range(le):
            freq1[fruits[i]]+=1
            while len(freq1) > 2:
                freq1[fruits[l]]-=1
                
                if freq1[fruits[l]] == 0:
                    del freq1[fruits[l]]
                l+=1    
            max1 = max(max1, i-l+1)
        return max1            
       
        