class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1 = []
        le = len(nums)
        for i in range(le):
            cnt =0
            for j in range(le):
                if nums[i] > nums[j]:
                    cnt+=1
            list1.append(cnt)
        return list1            

        