class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = defaultdict(int)
        for i in range(len(list2)):
            freq[list2[i]] = i
        st = []    

        min1 = float("inf")
        for i in range(len(list1)):
            if list1[i] in freq:
                
                if i + freq[list1[i]] < min1:
                    min1 = min(min1, i + freq[list1[i]])
                    st = [list1[i]]
                elif i + freq[list1[i]] == min1:

                    st.append(list1[i])

        return list(st)       

                

        