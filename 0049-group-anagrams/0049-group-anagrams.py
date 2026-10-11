class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dif = defaultdict(list)

        for n in strs:
            key = "".join(sorted(n))
            dif[key].append(n)
        return list(dif.values())    


        