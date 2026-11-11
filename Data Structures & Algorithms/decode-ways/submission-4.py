class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = [0] * len(s)
        # if s[0] == '0':
        #     return 0
        # dp[0] = 1
        # for i in range(1, len(s)):
        #     if s[i] != '0':
        #         dp[i] += dp[i-1]

        #     if 10 <= int(s[i-1:i+1]) <= 26:
        #         # if i >= 2:
        #         dp[i] += dp[i-2]
        #         # else:
        #         #     dp[i] += 1
        
        # return dp[-1]
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
        
        

