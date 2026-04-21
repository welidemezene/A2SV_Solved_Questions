t = int(input())

for i in range(t):
    sum1 = 0
    w = input()
    p = int(input())
    so = sorted(w)
    list1 = []

    for n in so:
        sum1 += ord(n)-96
        if sum1 <= p:
            list1.append(n)
    an = "".join(list1)        
            
    print(an)        




