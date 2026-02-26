n = int(input())
a = list(map(int,input().split()))
max1 = 0
cnt = 0
for i in range(1,n):
    if a[i] >= a[i-1]:
        cnt+=1
    else:
        cnt = 0
    max1 = max(max1,cnt)        
print(max1+1)