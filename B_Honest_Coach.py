n = int(input())
a = list(map(int,input().split()))
total_sum = 0
a.sort()
j = n-1
i = 0
while i < j:
    s = a[i] + a[j]
    
    i+=1
    j-=1
    b = s**2
    total_sum += b
print(total_sum)    