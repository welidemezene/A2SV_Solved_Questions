class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        value = nums[0]
        numus1 = sorted(nums[1:])
      
        value += numus1[0]
        value += numus1[1]
        return value    
        