class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        l = 0
        set1 = set()
        list1 = []
        max1 = 0
        for i in range(n):
            if s[i] not in set1:
                set1.add(s[i])
                
            elif s[i] in set1:    
                while s[i] in set1:
                    
                    
                    set1.discard(s[l])
                    l+=1
                set1.add(s[i])
                
            len1 = i-l+1
            if max1 < len1:
                max1 = len1

        return max1
               



        