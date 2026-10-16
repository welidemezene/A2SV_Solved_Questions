class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        m = s.lower()
        for n in m:
            if n.isalnum():
                ans+=n

        dn = ans[::-1] 
        if dn == ans:
            return True
        else:
            return False           
        