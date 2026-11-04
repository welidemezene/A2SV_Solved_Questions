class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)

        
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        p = l

        
        def bs(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid -1
            return -1

        
        if p == 0:
            return bs(0, n - 1)
        if target >= nums[0]:
            return bs(0 ,p-1)
        return bs(p,n-1)