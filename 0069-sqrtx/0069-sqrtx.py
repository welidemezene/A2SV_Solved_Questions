class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(x ** 0.5)
        ans = -1
        le = 0
        ri = x
        while le <= ri:
            mid = (le+ri)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                ri = mid-1
            else:
                ans = mid
                le = mid + 1
        return ans                

        