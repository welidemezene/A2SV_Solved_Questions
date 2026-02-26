n,s = map(int,input().split())
a = list(map(int,input().split()))

max1= 0
cnt = 0
sum1 = 0
l = 0
for n in a:
    sum1+=n
    while sum1 > s:
        sum1-= a[l]
        l+=1
        cnt-=1
    cnt+=1
    if cnt > max1:
        max1 = cnt
print(max1)            


