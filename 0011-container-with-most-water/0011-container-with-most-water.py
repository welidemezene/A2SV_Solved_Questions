class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max1 = 0
        while l < r:
            min1 = min(height[l],height[r])
            val1 = min1 * (r-l)
            if val1 > max1:

                max1 = max(max1, val1)
            elif height[l] <= height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
        return max1    



        