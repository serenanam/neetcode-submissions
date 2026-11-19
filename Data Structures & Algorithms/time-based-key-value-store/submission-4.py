class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        slot = self.times.get(key, [])
        if len(slot) == 0:
            return ""
        
        # if timestamp in slot:
        #     return slot[timestamp][0]
        
        l, r = 0, len(slot) - 1
        res = ""
        
        while l <= r:
            t = (l+r) // 2
            if slot[t][1] <= timestamp:
                res = slot[t][0]
                l = t+1
            else:
                r = t-1

        return res
                

