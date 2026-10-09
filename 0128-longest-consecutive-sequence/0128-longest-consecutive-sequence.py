class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        

        length = len(nums)
        if length == 1:
            return 1
        
        nums.sort()
        cnt = 1
        max1= 0
        for i in range(1, length):
            if abs(nums[i] - nums[i -1]) == 1:
                cnt+=1
            elif abs(nums[i] - nums[i -1]) != 0:
                cnt = 1
            if cnt > max1:
                max1 = cnt
        return max1                



        