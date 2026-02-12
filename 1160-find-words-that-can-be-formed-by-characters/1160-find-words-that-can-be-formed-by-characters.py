class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = defaultdict(int)
        cnt  = 0 
        for n in chars:
            freq[n] +=1
        for n in words:
            ch = freq.copy()
            for l in n:
                if l in ch and ch[l] != 0:
                    ch[l]-=1
                    
                else:
                    cnt-= len(n)
                    break
            cnt+= len(n)        

        return cnt                
                
            





        