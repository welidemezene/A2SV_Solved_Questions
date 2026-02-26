class Solution:
    def findValidPair(self, s: str) -> str:
        stri = []
        le = len(s)
        check = False
        
        freq = defaultdict(int)
        for n in s:
            freq[n]+=1
        for i in range(1,le):
            if s[i] != s[i-1] and freq[s[i]] == int(s[i]) and freq[s[i-1]] == int(s[i-1]):
                stri.append(s[i-1])
                stri.append(s[i])
                return "".join(stri)
                
                
        return ""   
        # return freq        
        # if check:
        #     return stri
        # else:
        #     return ""            

        


               
        