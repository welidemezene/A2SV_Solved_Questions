class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
      lis = []
      le = len(nums)
      for i in range(le):
        for j in range(nums[i][0], nums[i][1]+1):
            if j not in lis:
                lis.append(j)
      return len(lis)     
