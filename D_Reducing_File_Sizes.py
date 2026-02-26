n,m = map(int,input().split())
sum_a = 0
sum_b = 0
diffs = []


for _ in range(n):
    a,b = map(int,input().split())
    
    sum_a += a
    sum_b += b
    diffs.append(a - b)

if sum_b > m:
    print("-1")
else:
    diffs.sort(reverse=True)
    count = 0
    current_sum = sum_a
    
    for d in diffs:
        if current_sum <= m:
            break
        current_sum -= d
        count += 1
        
    print(count)






