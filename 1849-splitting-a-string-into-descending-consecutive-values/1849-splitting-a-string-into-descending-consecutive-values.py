class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(index,prev):
            if index==len(s):
                return True
            for j in range(index,len(s)):
                curr=int(s[index:j+1])
                if curr+1==prev and dfs(j+1,curr):
                    return True
            return False
        for i in range(len(s)-1):
            first_num=int(s[:i+1])
            if dfs(i+1,first_num):
                return True
        return False



