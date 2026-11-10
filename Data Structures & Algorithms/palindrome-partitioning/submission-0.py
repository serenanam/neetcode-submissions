class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, sub):
            if i == len(s):
                res.append(list(sub))
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    sub.append(s[i:j+1])
                    dfs(j+1, sub)
                    sub.pop()    

        dfs(0, [])
        return res

            
