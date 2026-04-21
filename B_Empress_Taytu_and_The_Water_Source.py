

t = int(input())

for _ in range(t):
    
    n, k = map(int, input().split())
    demands = list(map(int, input().split()))
    times = list(map(int, input().split()))
    
   
    if sum(times) > k:
        print("-1")
        continue
    
    
    low = 1
    high = max(demands)
    ans = high
    
    while low <= high:
        mid_size = (low + high) // 2
        
        
        total_time = 0
        possible = True
        
        for i in range(n):
           
            trips = (demands[i] + mid_size - 1) // mid_size
            total_time += trips * times[i]
            
            
            if total_time > k:
                possible = False
                break
        
        
        if possible:
            ans = mid_size     
            high = mid_size - 1 
        else:
            low = mid_size + 1  
            
    print(ans)