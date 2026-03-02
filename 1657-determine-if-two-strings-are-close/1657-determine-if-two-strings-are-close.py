class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        le = len(word1)
        le1 = len(word2)
        list1 = []
        list2 = []

        if le != le1:
            return False
        for n in word1:
            freq1[n]+=1
        for n in word2:
            freq2[n]+=1

        for key , value in freq1.items():
            list1.append(value)
        for key,value in freq2.items():
            list2.append(value)
        list1.sort()
        list2.sort()
        if set(freq1.keys()) != set(freq2.keys()): return False

        
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                return False
        return True    


        


        