class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = sorted(s)
        t_string = sorted(t)
        if s_string == t_string:
            return True
        else:
            return False    
        