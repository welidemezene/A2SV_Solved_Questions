class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        list1 = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                list1.append(nums[i])
        return list1        

        