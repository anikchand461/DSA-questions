import sys

def count_swaps(arr):
    r, c = 0, 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                r, c = i, j
                break

    # calculate the delta x and delta y 
    deltax = abs(r-2)
    deltay = abs(c-2)

    return deltax + deltay

arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))

swaps = count_swaps(arr)
print(swaps)

