class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        list1 = []
        for n in nums:
            freq[n] +=1
        for key , value in freq.items():
            if value > len(nums)/3:
                list1.append(key)
        return list1        
                     
        