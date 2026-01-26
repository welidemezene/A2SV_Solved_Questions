class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        length = len(arr)
        minvalue = float("inf")
        arr.sort()
        for i in range(1,length):
            diff = abs(arr[i-1]-arr[i])
            minvalue = min(minvalue,diff)
        stack  = []
        for i in range(1,length):
            diff = abs(arr[i-1]-arr[i])
            if diff == minvalue:
                stack.append([arr[i-1],arr[i]])
        return stack        




        