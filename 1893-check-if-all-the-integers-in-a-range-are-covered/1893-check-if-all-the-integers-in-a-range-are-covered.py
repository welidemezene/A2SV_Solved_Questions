class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = True
        
        for i in range(left,right+1):
            for m in ranges:
                if m[0] <= i <= m[1] :
                    check = True
                    break
                else:
                    check = False
            if not check:
                return False
        if check:
            return True                    

        