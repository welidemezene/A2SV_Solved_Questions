class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        cnt_zeros = nums.count(0)
        list1 = [0] * len(nums)
        list2 = []

        multi = 1
        for n in nums:
            if n != 0:
                multi *= n
        if cnt_zeros > 1:
            return ([0] * len(nums))

        elif cnt_zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    list1[i] = multi
            return list1
        else:
            for n in nums:
                list2.append(multi // n)  
            return list2            
        