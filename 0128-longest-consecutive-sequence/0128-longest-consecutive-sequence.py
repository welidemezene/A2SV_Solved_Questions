class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsset = set(nums)
        len1 = len(nums)
        if len1 < 1:
            return 0

        
        max1 = 0

        for n in numsset:
            
            if n-1 not in numsset:
                cnt = 1
                m = n
                while m+1 in numsset:
                    cnt+=1
                    m+=1
                
                max1 = max(cnt, max1)
        return max1            

       