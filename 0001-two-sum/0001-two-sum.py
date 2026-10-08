class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):
            for j in range(i+1,length):
                find = target - nums[i]
                if find == nums[j]:
                    return [i,j]

      