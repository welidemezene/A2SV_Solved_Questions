class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum , rightsum = 0, sum(nums)
        for idx , ele in enumerate(nums):
            rightsum -= ele
            if leftsum == rightsum:
                return idx
            leftsum+=ele
        return -1        

       