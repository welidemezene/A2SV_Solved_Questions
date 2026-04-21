n = int(input())
a = list(map(int,input().split()))
cnt = 0
maxcnt = 0
for i in range(1,n):
    if a[i-1] <= a[i]:
        cnt +=1
    elif a[i-1] > a[i]:
        cnt = 0    
    maxcnt = max(maxcnt, cnt)    

    


print(maxcnt+1)