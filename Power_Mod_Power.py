# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
m = int(input().strip())
k = int(input().strip())

s = pow(n,m)
p = s%k
print(s)
print(p)