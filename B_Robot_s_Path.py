n,k = map(int,input().split())
b = input()
an = 0
check = True
for m in b:
    if m == ".":
        an=k
       
    elif m == "#":
        an-=1
    if m == "#" and an == 0:
        check = False
        break     
    
if check:
    print("YES")
else:
    print("NO")                