n,t = map(int,input().split())
a = list(map(int,input().split()))

curr = 1
while curr < t:
    curr = curr + a[curr-1]
    if curr > t:
        print("NO")
        break
    elif curr == t:
        print("YES")
        break
        
        

