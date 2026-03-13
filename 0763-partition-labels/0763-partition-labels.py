class Solution(object):
    def partitionLabels(self, s):
        hashm = {}
        for i, c in enumerate(s):
            hashm[c] = i
        size = 0
        end = 0
        res = []
        for i , c in enumerate(s):
            size+=1
            end = max(end, hashm[c])
            if i ==end:
                res.append(size)
                size = 0
        return res        



        """
        :type s: str
        :rtype: List[int]
        """
        