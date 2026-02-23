import sys
input = sys.stdin.readline
 
n = int(input())
x = 0
 
for _ in range(n):
    s = input().strip()
    if "++" in s:
        x += 1
    elif "--" in s:
        x -= 1
 
print(x)
