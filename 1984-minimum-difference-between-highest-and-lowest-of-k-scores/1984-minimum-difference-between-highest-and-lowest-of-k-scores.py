class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        le = len(nums)
        if le <= 1:
            return 0
        
        min1 = float("inf")
       
        for i in range(le-k +1):
           
            dif = nums[i+k-1]-nums[i]
            min1 = min(min1,dif)
           
        return min1    
            


       



        