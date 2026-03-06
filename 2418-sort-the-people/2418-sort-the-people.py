class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = len(heights)
        fre1 = defaultdict(str)
        for i in range(h):
            fre1[heights[i]] = names[i]
        heights.sort(reverse=True)
        stack = []
        for num in heights:
            stack.append(fre1[num])
        return stack        