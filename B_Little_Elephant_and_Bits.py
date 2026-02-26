n = input()
pos = n.find("0")
if pos == -1:
    print(n[:len(n)-1])
else:
    print(n[:pos] + n[pos+1:])    