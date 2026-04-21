# n = int(input())
# w = list(map(int, input().split()))


# l = 1

# group1 = w[0]
# while l < n:
#     if group1 >=0:
#         group1 -=w[l]
#         l+=1
#     elif group1 < 0:
#         group1+=w[l]
#         l+=1    
# print(abs(group1))        
        
import sys


n = int(input())
w = list(map(int, input().split()))

total_sum = sum(w)

ans = [float('inf')]

def solve(idx, current_sum):
    
    if idx == n:
        diff = abs((total_sum - current_sum) - current_sum)
        if diff < ans[0]:
            ans[0] = diff
        return

    
    solve(idx + 1, current_sum + w[idx])
    

    solve(idx + 1, current_sum)


solve(0, 0)
print(ans[0])




#     group1 = 0
#     group2 = 0
#     m = n//2
#     l = n-1
#     for i in range(m):
#         if i % 2 ==0:
#             group1 += w[i]
#             group1 += w[l]
#             l-=1
#         else:
#             group2 += w[i]
#             group2 += w[l]
#             l-=1
#     if group1 >= group2:
#         group2+= w[m]
#         print(abs(group1-group2))
#     else:
#         group1+= w[m]
#         print(abs(group2-group1))    





