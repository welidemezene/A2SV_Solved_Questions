from collections import defaultdict
t = int(input())

for i in range(t):
    freq = defaultdict(int)
    s = input()
    le = len(s)
    if le % 2 == 0:
        for j in range(le//2):
            freq[s[j]]+=1
    elif le % 2 != 0:
        for j in range(le//2):
            freq[s[j]]+=1        
    
        
    if len(freq.items()) > 1:
        print("YES")
    else:
        print("NO")        
