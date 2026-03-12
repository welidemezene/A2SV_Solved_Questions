class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        le = len(nums)
        for i in range(le-2):
            sum = nums[i+1]+nums[i+2]
            if nums[i] < sum:
                return nums[i]+sum
        else:
            return 0        
        