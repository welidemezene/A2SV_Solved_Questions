class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        le = len(nums)
        left = 0
        n = 0
        list1 = []
        max1 = float('-inf')
        for right in range(le):
            if nums[right] ==0:
                n+=1
            while n > k:
                
                if nums[left] == 0:
                    n-=1
                left+=1    
            max1 = max(max1, right - left+1)  
        return max1          

           




        