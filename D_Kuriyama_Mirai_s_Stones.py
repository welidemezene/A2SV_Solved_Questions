n = int(input())
list1 = list(map(int, input().split()))
list2 = [0] * (len(list1)+1)
list3 = [0] * (len(list1)+1)
lis = sorted(list1)


for i in range(1,len(list1)+1):
    list3[i] = list3[i-1] + lis[i-1]
    list2[i] = list2[i-1] + list1[i-1]
q = int(input())
for i in range(q):
    t,l,r = map(int, input().split())
    if t == 1:
        print(list2[r] - list2[l-1])
    else:
        print(list3[r] - list3[l-1])