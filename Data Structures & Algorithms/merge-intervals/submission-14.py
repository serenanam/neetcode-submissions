class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # O(nlogn)
        res = []
        start, end = intervals[0]
        for curr_s, curr_e in intervals[1:]:
            if curr_s <= end:
                end = max(end, curr_e)
            else:
                res.append([start, end])
                start, end = curr_s, curr_e
        
        res.append([start, end])
        return res
    # Time: O(n)
    # Space: O(n)
    
