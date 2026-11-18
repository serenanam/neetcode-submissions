class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ll, lr = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    ll, lr = l, r
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    ll, lr = l, r
                l -= 1
                r += 1
        return s[ll: lr+1]
            
            
