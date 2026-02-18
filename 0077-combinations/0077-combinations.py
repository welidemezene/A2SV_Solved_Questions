class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(i=1,arr=[]):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if i>n:
                return
            arr.append(i)
            backtracking(i+1 , arr)
            arr.pop()
            backtracking(i+1 , arr)
        backtracking()
        return ans






        