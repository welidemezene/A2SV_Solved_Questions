t = int(input())
for i in range(t):
    n,h = map(int,input().split())
    cnt = 0
    for j in range(n):
        w,l = map(int,input().split())
        cnt += max(w,l)
    if cnt >= h:
        print("YES")
    else:
        print("NO")         
