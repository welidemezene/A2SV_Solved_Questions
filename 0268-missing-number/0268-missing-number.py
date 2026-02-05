class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        le = len(nums)
        for i in range(le+1):
            if i not in set(nums):
                return i
        