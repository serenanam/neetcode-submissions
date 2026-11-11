class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = dp2 = 1
        dp = 0
        if s[0] == '0':
            return 0
        for i in range(1, len(s)):
            if s[i] != '0':
                dp += dp1

            if 10 <= int(s[i-1:i+1]) <= 26:
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
        
        

