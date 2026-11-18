class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        maxSub = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            maxSub = max(maxSub, r - l + 1)
            sub.add(s[r])
        return maxSub
        #Time: O(n)
        #Space: O(n)
