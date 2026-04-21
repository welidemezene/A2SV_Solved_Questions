q = int(input())
for i in range(q):
    n = int(input())
    s = input()
    if n == 2 and int(s[0]) >= int(s[1]):
        print("NO")
        continue
    elif n == 2:
        print("YES")
        print(2)
        print(s[0] ,s[1])
    else:
        print("YES")
        print(2)
        print(s[0], s[1:])    