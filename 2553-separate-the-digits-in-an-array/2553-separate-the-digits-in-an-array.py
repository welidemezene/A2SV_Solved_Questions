class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        list1 = []
        for n in nums:
            m = str(n)
            for s in m:
                list1.append(int(s))
        return list1        


        