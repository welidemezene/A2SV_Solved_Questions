from collections import defaultdict

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = defaultdict(int)
    cnt = 0
    for n in a:
        freq[n] +=1
    for key, value in freq.items():
        if value >=3:
            cnt += value // 3
        
    print(cnt)        
        


   
