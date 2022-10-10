class TimeMap:
    
    def __init__(self):
        self.key_time_map = {}  # {key : [[val,timestamp]]}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = []
        self.key_time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.key_time_map.get(key,[])
        l,r = 0,len(value)-1
        while l<= r:
            m = (l+r)//2
            if value[m][1] <= timestamp:
                res = value[m][0]
                l = m +1
            else:
                r = m-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)