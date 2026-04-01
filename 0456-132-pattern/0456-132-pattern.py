class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        first = float("-inf")
        check = False
        for i in range(n-1, -1, -1):
            

            while stack and stack[-1]< nums[i]:
                first = stack.pop()
            if first > nums[i]:
                return True    
            stack.append(nums[i])    
        return False