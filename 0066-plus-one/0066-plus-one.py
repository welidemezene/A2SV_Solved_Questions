class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = []
        for n in digits:
            list1.append(str(n))
        list2 = "".join(list1) 
        list3 = int(list2)
        list3+=1
        list4 = str(list3)
        list5 = []

        for s in list4:
            list5.append(int(s))
        return list5    


       

      
        
        