class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res_row = [0] * (len(res) +1)
            for j in range(len(res)):
                res_row[j] += res[j]
                res_row[j+1] += res[j]
            res = res_row
        return res        
        