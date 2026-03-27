class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # To handle cases when k > n
        
        # Step 1: Reverse the entire array
        nums.reverse()
        
        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Step 3: Reverse the remaining elements
        nums[k:] = reversed(nums[k:])