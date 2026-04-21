
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()
    target_sum = 0
    for char in w:
        target_sum += ord(char)
    current_window_sum = 0
    for i in range(m):
        current_window_sum += ord(s[i])
    found = False
    if current_window_sum == target_sum:
        found = True
    if not found:
        for i in range(m, n):
            current_window_sum += ord(s[i])   
            current_window_sum -= ord(s[i - m])  
            if current_window_sum == target_sum:
                found = True
                break
                
    if found:
        print("YES")
    else:
        print("NO")