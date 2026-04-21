n = int(input())
a = list(map(int,input().split()))
a.sort()
crd = 1
for m in a:
    if m>=crd:
        crd+=1
print(crd-1)        
