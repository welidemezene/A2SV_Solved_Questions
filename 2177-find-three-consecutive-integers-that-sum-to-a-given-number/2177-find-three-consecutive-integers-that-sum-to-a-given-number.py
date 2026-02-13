class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        list1 = []
        a = num // 3
        b = a -1
        c = a + 1
        if a + b + c == num:
            list1.append(b)
            list1.append(a)
            list1.append(c)
        else:
            return list1
        return list1       
       
       
              

        