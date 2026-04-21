t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    id1 = a[-1]
    max1 = max(a[:n-1])
    print(id1+max1)