n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = sum(a)
sum = 0
count1 = 0
 
 
for i in range(n):
    total -= a[i]
    sum+=a[i]
    count1+=1
 
    if sum > total:
        print(count1)
        break