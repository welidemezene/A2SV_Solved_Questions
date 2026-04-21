n = int(input())

s = input()

countL = 0
countO = 0
for i in range(n):
    if s[i] == 'L':
        countL += 1
    else:
        countO += 1

minusL = 0
minusO = 0
for i in range(n-1):
    if s[i] == "L":
        countL -=1
        minusL +=1
    else:
        countO -=1
        minusO +=1
    if countL != minusL and countO != minusO:
        print(minusL + minusO)
        break
else:    
    print(-1)    
           



