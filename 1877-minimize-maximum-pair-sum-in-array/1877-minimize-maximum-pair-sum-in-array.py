class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        le = len(nums)
        l = 0
        r = len(nums)-1
        max1 = 0
        while l < r:
            sum1 = nums[l] + nums[r]
            l+=1
            r-=1
            max1 = max(max1,sum1)
        return max1    



        