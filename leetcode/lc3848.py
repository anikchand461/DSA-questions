# 3848. Check Digitorial Permutation

import math

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        ans = 0
        m = n
        while n != 0:
            ld = n % 10
            ans += math.factorial(ld)
            n //= 10

        ans = sorted(str(ans))
        m = sorted(str(m))
        
        if ans == m:
            return True
        else:
            return False

sol = Solution()
print(sol.isDigitorialPermutation(int(input())))

