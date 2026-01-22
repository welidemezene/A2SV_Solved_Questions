class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(nums , n) -> bool:
            for i in range(1,n):
                if nums[i] < nums[i-1]: return False
            return True  
        count1 = 0
        n = len(nums)
        


        while not is_sorted(nums,n) and len(nums) > 1:

    
            min_sum = float('inf')
            target_idx = -1
            
    
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum: 
                    min_sum = current_sum
                    target_idx = i
            nums[target_idx:target_idx+2] = [min_sum]
            count1+=1
            n-=1
        return count1    
           
                