class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i] and stack[-1][1] + 1 == k:
                #print(i, s[i])
                for _ in range(k-1):
                    stack.pop()
                print(stack)
            else:
                print(i, s[i])
                if stack and stack[-1][0] == s[i]:
                    stack.append((s[i], stack[-1][1] + 1))
                else:
                    stack.append((s[i], 1))
        res = ""
        for c, cnt in stack:
            res += c
        return res