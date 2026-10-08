class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniq = set(nums)
        uniq_length = len(uniq)
        num_length = len(nums)
        if num_length > uniq_length:
            return True
        else:
            return False    
        