n,k = map(int,input().split())
a = list(map(int,input().split()))

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]

idx = 0   
for i in range(n-k+1):
    if prefix[i+k] - prefix[i] < prefix[idx+k] - prefix[idx]:
        idx = i
print(idx+1)