class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nu1 = set(nums1)
        nu2 = set(nums2)
        li = []
        for n in nu1:
            if n in nu2:
                li.append(n)
        return li        

        
      