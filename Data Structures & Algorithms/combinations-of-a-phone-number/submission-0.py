class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8": "tuv", "9":"wxyz"}
        res = []
        if len(digits) < 1:
            return res
        
        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return
            
            for j in range(len(d[digits[i]])):
                dfs(i+1, s + d[digits[i]][j])
        
        dfs(0, "")
        return res


