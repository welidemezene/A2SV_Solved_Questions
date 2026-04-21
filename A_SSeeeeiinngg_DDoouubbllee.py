# from collections import defaultdict
# n = int(input())
# le = n * 2

# freq = defaultdict(int)
# for i in range(n):
#     s = input()
#     for m in s:
#         freq[m]+=1

#     list1 = []    
#     for key,value in freq.items():
#         list1.append(key * value)
#     freq = defaultdict(int)  

#     ans = "".join(list1)
#     an1 = ans[::-1]
#     print(ans + an1)
    
n = int(input())


for i in range(n):
    s = input()
    print(s+s[::-1])






        

