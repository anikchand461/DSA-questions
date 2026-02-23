import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # take input of the string 
    s = input().strip()
    # check the length of the input 
    length = len(s)

    if length > 10: 
        # too long word 
        # we have to apply the changes 
        s = s[0] + f'{length-2}' + s[length-1]

    print(s)

