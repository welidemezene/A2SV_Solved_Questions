class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list1 = [""] * len(s)
        for i , m in enumerate(s):
            list1[indices[i]] = m
        return "".join(list1)
          
            
        