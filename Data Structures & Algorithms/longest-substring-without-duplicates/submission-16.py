class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        l = 0
        maxSub = 0
        for r in range(len(s)):
            while s[r] in sub:
                del sub[s[l]]
                l += 1
            #print(l, r)
            maxSub = max(maxSub, r - l + 1)
            sub[s[r]] = r
        return maxSub
