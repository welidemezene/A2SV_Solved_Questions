s = input()
le = len(s)
lis = []
for i in range(1,le):
    if s[i] == s[i-1]:
        lis.append(1)
    else:
        lis.append(0)
prefix = [0] * (le)

for i in range(1,le):
    prefix[i] = prefix[i-1] + lis[i-1]


m = int(input())
for i in range(m):
    l,r = map(int,input().split())
    print(prefix[r-1] - prefix[l-1])
    # print(prefix)
