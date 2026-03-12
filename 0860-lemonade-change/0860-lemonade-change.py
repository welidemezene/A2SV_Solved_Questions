class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = defaultdict(int)
        check = True
        for n in bills:
            freq[n]+=1
            if n == 10 and freq[n-5] > 0:
                freq[n-5]-=1
            elif n == 20 and freq[n-10] > 0 and freq[n-15] > 0:
                freq[n-15]-=1
                freq[n-10]-=1
            elif n == 20 and freq[n-15] > 2:
                freq[5]-=3
            
            elif n != 5:
                return False    
                
        else:
            return True                    


        