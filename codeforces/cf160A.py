import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

s = sum(arr)
target = s / 2

arr.sort(reverse=True)

ans = 0
temp = 0

for num in arr:
    if temp > target:
        print(ans)
        break
    else:
        temp += num
        ans += 1

if temp == s:
    print(ans)


