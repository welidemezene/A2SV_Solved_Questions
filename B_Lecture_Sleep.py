n,k = map(int,input().split())

a = list(map(int,input().split()))
t = list(map(int,input().split()))

prefix = [0] * (n+1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1]+ a[i-1]



max1 = 0
for i in range(n-k):
    max1 = max(max1, prefix[k+i+1]- prefix[i])
print(max1)        