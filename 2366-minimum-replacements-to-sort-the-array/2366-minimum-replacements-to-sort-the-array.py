class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        ans = 0
        le = len(nums)

        for i in range(le-2, -1, -1):
            if nums[i] > last:
                t = nums[i]//last
                if nums[i] % last:
                    t +=1
                last = nums[i]//t
                ans += t-1
            else:
                last = nums[i]
                
        return ans                
        