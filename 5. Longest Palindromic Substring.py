class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        max_length = 0
    
        for length in range(n):
            for i in range(n):
                j = i + length
                if j >= n:
                    break
                if length == 0:
                    dp[i][j] = True
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
    
                if dp[i][j] and length + 1 > max_length:
                    max_length = length + 1
                    ans = s[i:j+1]
    
        return ans
