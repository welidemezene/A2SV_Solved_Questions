t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    x = input()
    s = input()
    cnt = 0
    list1 = []
    if x == s:
        print(0)
    for i in range(m):
        x += x
        cnt+=1
        if x in s:
            list1.append(cnt)