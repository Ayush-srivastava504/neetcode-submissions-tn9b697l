class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n>>1
        return res

## It uses:

## Right shift (>>) to examine bits one by one.
## Modulo (% 2) to get the last bit.