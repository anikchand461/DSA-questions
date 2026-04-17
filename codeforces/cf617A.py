import sys
input = sys.stdin.readline
write = sys.stdout.write

x = int(input())

if x <= 5:
    write(str(1) + "\n")
elif x % 5 == 0: # if x is divisible by 5
    write(str(x // 5) + "\n")
else:
    write(str(x // 5 + 1) + "\n")


