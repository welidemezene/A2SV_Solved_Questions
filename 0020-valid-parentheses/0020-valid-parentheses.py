class Solution:
    def isValid(self, s: str) -> bool:
        freq = {"(":")","{":"}","[":"]"}
        list1 = []
        
        for n in s:
            if n in "[({":
                list1.append(freq[n])
            else:
                if list1 and n == list1[-1]:
                    list1.pop()
                else:
                    return False
        if not list1:
            return True   
        else:
            return False                     