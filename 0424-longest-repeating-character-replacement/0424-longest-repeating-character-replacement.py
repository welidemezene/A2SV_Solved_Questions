class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len1 = len(s)
        freq = defaultdict(int)
        l = 0
        max1 = 0
        for i in range(len1):
            freq[s[i]]+=1

            max2 = max(freq.values())
            while (i-l+1) - max2 >k:
                freq[s[l]]-=1
                l+=1
            val = i-l+1
            if val>max1:
                max1 = val
        return max1            


       