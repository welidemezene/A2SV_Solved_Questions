import sys

# Fast I/O is important for Codeforces with 2*10^5 elements
input = sys.stdin.read

def solve():
    # Read all input at once and split by whitespace
    data = input().split()
    if not data:
        return
    
    it = iter(data)
    t = int(next(it))
    
    output = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        a = []
        for i in range(n):
            a.append(int(next(it)))
        
        
        a.sort()
        
        total_score = 0
        
        
        for i in range(n - 1, 0, -2):
            eve_item = a[i]
            noah_item = a[i-1]
            
            
            current_gap = eve_item - noah_item
            
           
            reduction = min(k, current_gap)
            
            k -= reduction
            total_score += (current_gap - reduction)
            
        
        if n % 2 == 1:
            total_score += a[0]
            
        output.append(str(total_score))
    

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()