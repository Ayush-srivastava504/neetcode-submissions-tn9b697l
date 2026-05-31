class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res

##A bit mask is a binary number used to check or modify specific bits in another number.

##It is usually combined with bitwise operators like &, |, and ^.

## Example: n & 1 uses the mask 1 (0001) to check whether the last bit of n is set.