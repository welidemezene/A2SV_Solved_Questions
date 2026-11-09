class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)
        l,r = 0,n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l=mid+1
        p = l
        def lfr(li,ri):
            while li <= ri:
                mid1 = (li+ri)//2
                if nums[mid1] == target:
                    return mid1
                elif nums[mid1] < target:
                    li=mid1+1
                else:
                    ri=mid1-1
            return -1
        if 0 == p:
            return lfr(0,n-1)
        elif target >= nums[0]:
            return lfr(0,p-1)
        else:
            return lfr(p, n-1)            




        