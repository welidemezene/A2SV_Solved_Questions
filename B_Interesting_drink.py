from bisect import bisect_right
n  = int(input())
list1 = list(map(int, input().split()))
list1.sort()
lis = []
q = int(input())
for i in range(q):
    m = int(input())
    ans = bisect_right(list1, m)
    lis.append(ans)
for i in lis:
    print(i)        
          
