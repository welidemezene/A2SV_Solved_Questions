class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        len1 = len(nums)
        list1 = []
        for i in range(len1-2):
            if i == 0 and nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue    
            l = i+1
            r= len1-1

            while l < r:
               
                    sum1 = nums[i] + nums[l] + nums[r]

                    if sum1 < 0:
                        l+=1
                    elif sum1 > 0:
                        r-=1
                    elif sum1 == 0:
                        list1.append([nums[i],nums[l],nums[r]])    
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
        return list1            


        