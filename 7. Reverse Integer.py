class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = [1,-1][x < 0]
        x *= sign
    
        while x:
            result = result*10 + x%10
            x //= 10
    
        return sign*result if result <= 0x7fffffff else 0
