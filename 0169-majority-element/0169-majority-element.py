class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        major = len(nums)//2
        major +=1
        for n in nums:
            freq[n]+=1
        for key, value in freq.items():
            if value >= major:
                return key     