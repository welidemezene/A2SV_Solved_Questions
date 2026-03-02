from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))
freq = defaultdict(int)
for i in range(n):
    freq[a[i]] = i
list1 =  []

ch = sorted(freq.keys())
sum1 = ch[0]
if sum1 < k:
    list1.append(freq[ch[0]]+1)

for i in range(1,len(ch)):
    if sum1 < k:
        sum1+= ch[i]
        list1.append(freq[ch[i]]+1)
print(len(list1))        
print(*list1)

   