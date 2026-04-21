t = int(input())
for i in range(t):
    s = input()
    zero = s.count("0")
    one = s.count("1")
    
    if one == zero:
        print(zero-1)
    else:

        print(min(zero,one))