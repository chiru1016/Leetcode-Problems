class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = 0
        x = abs(x)
        while x > 0:
            g = x % 10
            result = result * 10 + g
            x = x // 10
        result = result * sign 
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
