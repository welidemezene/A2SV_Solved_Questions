# n = int(input())
# check = True
# check2 = True
# value = 0
# value1 = 0
# for i in range(n):
#     w,h = map(int,input().split())
#     min1 = min(w,h)
#     max1 = max(w,h)
#     if check:
#         if i == 0:
#             value = max1
#             value1 = min1
        
#         elif value >= min1 or value1 >= min1:
#             value = min1
            
#         elif value >= max1 or value1 >= max1:
#             value = max1
            
#         else:
#             check = False
#             break
   
        
# if check:
#     print("YES")
# else:
#     print("NO")                    


n = int(input())
limit = float('inf')
possible = True
for i in range(n):
    w, h = map(int, input().split())
    big = max(w, h)
    small = min(w, h)

    if big <= limit:
        limit = big
    elif small <= limit:
        limit = small
    else:
        possible = False
        break
if possible:
    print("YES")
else:
    print("NO")
