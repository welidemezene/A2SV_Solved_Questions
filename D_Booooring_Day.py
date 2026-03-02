t = int(input())
for i in range(t):
    n,l,r = map(int,input().split())
    list1 = list(map(int,input().split()))

    
    sum1 = 0
    cnt = 0
    y = 0
    for x in range(len(list1)):
        sum1+=list1[x]

        while sum1 > r and y <= x:
            sum1-= list1[y]
            y+=1

        if l <= sum1 <= r:
            cnt+=1
            sum1 = 0
            y = x +1

    print(cnt)        

   
