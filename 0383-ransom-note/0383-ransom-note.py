class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = False
        freq = defaultdict(int)
        for n in magazine:
            freq[n]+=1
        for n in ransomNote:
            if n not in magazine or freq[n] == 0:
                return False
            elif freq[n] >=1:
                freq[n]-=1
                
                    
                
                check = True
            else:
                check = False    
                
        return check        

        