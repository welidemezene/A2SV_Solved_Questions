class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        check = s[::-1]
       
        if check == s:
            return True
        else:
            return False    
        