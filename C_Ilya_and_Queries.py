s = input()
n = int(input())
list1 = [0] * (len(s)+1)
prefix = [0] * (len(s)+1)
for i in range(2,len(s)+1):
    if s[i-1] == s[i-2]:
        list1[i] += 1
        
        
for i in range(1,len(s)+1):
    prefix[i] =  prefix[i-1] + list1[i]


for i in range(n):
    l,r = map(int,input().split())
    print(prefix[r] - prefix[l])