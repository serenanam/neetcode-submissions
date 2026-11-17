class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums))]

        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        for key in freqMap:
            freqs[freqMap[key]-1].append(key)

        cnt = 0
        res = []
        for i in range(len(freqs)-1, -1, -1):
            for num in freqs[i]:
                cnt += 1
                res.append(num)
                if cnt == k:
                    return res      
        # Time: O(n)
        #Space: O(n)         
