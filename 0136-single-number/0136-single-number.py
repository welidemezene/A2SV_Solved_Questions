class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for n in nums:
            freq[n]+=1
        for key,value in freq.items():
            if value == 1:
                return key
                    
        
        