
t = int(input())
ans = []
for _ in range(t):
    
    n,m = map(int, input().split())
    brand_sum = [0]*(m+1)
    for i in range(m):
        x,s = map(int,input().split())
        brand_sum[x]+=s

    brand_sum.sort(reverse=True)   
    count = 0
    ans.append(brand_sum[:n])
for i in ans:
    print(sum(i))    

        
    

