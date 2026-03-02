class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        max1 = 0
        if nums == []:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]-1:
                cnt+=1
                max1 = max(max1,cnt)
            elif nums[i-1] == nums[i]:
                cnt = cnt 

            else:
                cnt=0     
        return max1 + 1      
    

        