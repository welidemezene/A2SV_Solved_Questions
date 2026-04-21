import sys
input = sys.stdin.readline

def solve():
    # 1. Read Inputs
    recipe = input().strip()
    # Current stock: Bread, Sausage, Cheese
    nb, ns, nc = map(int, input().split())
    # Prices at shop
    pb, ps, pc = map(int, input().split())
    # Money in pocket
    money = int(input())
    
    # 2. Count requirements per 1 burger
    reqB = recipe.count('B')
    reqS = recipe.count('S')
    reqC = recipe.count('C')
    
    # 3. The "Can I?" Function
    def can_make(mid):
        # Calculate how much we need to buy
        buyB = max(0, mid * reqB - nb)
        buyS = max(0, mid * reqS - ns)
        buyC = max(0, mid * reqC - nc)
        
        total_cost = (buyB * pb) + (buyS * ps) + (buyC * pc)
        return total_cost <= money

    # 4. Binary Search for the MAXIMUM 'Yes'
    low = 0
    high = 10**14 # Set it very high to be safe
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_make(mid):
            ans = mid      # This works! Save it.
            low = mid + 1  # Try to make more.
        else:
            high = mid - 1 # Too expensive. Try to make fewer.
            
    print(ans)

solve()