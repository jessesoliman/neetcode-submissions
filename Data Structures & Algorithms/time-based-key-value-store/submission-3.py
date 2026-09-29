class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return""
        l, r = 0, len(self.timemap[key]) - 1
        item = self.timemap[key]
        if item[-1][1] <= timestamp:
            return item[-1][0]
        while l <= r:
            m = (l + r) // 2
            if item[m][1] == timestamp:
                return item[m][0]
            if item[m][1] > timestamp:
                r = m - 1
                if r < len(item) and item[r][1] < timestamp:
                    return item[r][0]
            else:
                l = m + 1
                if l < len(item) and item[l][1] > timestamp:
                    return item[m][0]
        return ""
        
