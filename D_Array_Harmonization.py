

# Read number of test cases

t = int(input())


for _ in range(t):
   
    n, m = map(int, input().split())
    
    
    a_fixed = list(map(int, input().split()))
    
    
    b = list(map(int, input().split()))
    
    
    a_fixed.sort()
    b.sort()
    
    
    j = 0
    base_matches = 0
    used_b = [False] * n
    
    for x in a_fixed:
        
        while j < n and b[j] <= x:
            j += 1
        
        if j < n:
            used_b[j] = True
            base_matches += 1
            j += 1 
            
    
    max_free_b = 0
    for j in range(n - 1, -1, -1):
        if not used_b[j]:
            max_free_b = b[j]
            break
            
    
    num_case_a = max(0, min(m, max_free_b - 1))
    num_case_b = m - num_case_a
    
    
    ans_case_a = n - (base_matches + 1)
    ans_case_b = n - base_matches
    
    total_sum = (num_case_a * ans_case_a) + (num_case_b * ans_case_b)
    
    print(total_sum)