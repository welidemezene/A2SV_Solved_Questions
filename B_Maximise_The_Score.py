t = int(input())
for i in range(t):
    n = int(input())
    list1 = list(map(int,input().split()))
    list1.sort()
    min1 = 0
    k = 0
    for j in range(n):
        min1+=list1[k]
        k+=2
    print(min1)    
