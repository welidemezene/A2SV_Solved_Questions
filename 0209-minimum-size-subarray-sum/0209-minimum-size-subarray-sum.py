class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        le = len(nums)
        total_sum = 0
        min1 = float("inf")
        l = 0
        for i in range(le):
            total_sum += nums[i]
            while total_sum >= target:
                total_sum -= nums[l]
                l+=1
                min1 = min(min1, i - l + 2)
        if min1 == float("inf"):
            return 0
        else:
            return min1           

        