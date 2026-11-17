class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = defaultdict(list)
        for i in range(len(strs)):
            freq = [0] * 26
            for c in strs[i]:
                freq[ord(c) - ord('a')] += 1
            hashed[tuple(freq)].append(i)
        
        res = []
        for key in hashed:
            sub = []
            for i in hashed[key]:
                sub.append(strs[i])
            res.append(sub)
        return res

        # Time: O(n*m) where n is # strs, m is length of longest string
        # Space: O(n)