class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading whitespaces
        if not s: return 0  # return 0 if string is empty
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        result = 0
        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)
            if result > 2147483647:
                return 2147483647 if sign == 1 else -2147483648
        return sign * result
