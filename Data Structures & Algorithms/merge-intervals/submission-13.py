class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
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
            
        # for i in range(len(intervals)-1):
        #     curr_s, curr_e = intervals[i]
        #     nxt_s, nxt_e = intervals[i+1]
        #     if curr_e >= nxt_s:
        #         intervals[i] = [min(curr_s, nxt_s), nxt_e]

        # return intervals 