cnt = 0

for i in range(5):
    list1 = list(map(int,input().split()))
    for j in range(len(list1)):
        if list1[j] == 1:
            row = abs(i-2)
            col = abs(j-2)
            cnt = row + col
            break
print(cnt)        
