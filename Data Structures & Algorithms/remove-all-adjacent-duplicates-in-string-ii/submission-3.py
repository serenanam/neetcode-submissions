class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack.append((s[i], stack[-1][1]+1))
            else:
                stack.append((s[i], 1))
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            
        res = ""
        for c, cnt in stack:
            res += c
        return res

        #Time: O(n)
        #Space: O(n)