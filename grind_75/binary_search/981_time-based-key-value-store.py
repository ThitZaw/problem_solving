class TimeMap:
    
    def __init__(self):
        self.key_val_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_val_map:
            self.key_val_map[key] = []
        self.key_val_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.key_val_map.get(key,[])
        left , right = 0, len(value)-1
        # find value with <= timestamp in sorted timestamp list
        while left <= right:
            m = (left + right) //2
            if value[m][1] <= timestamp:
                res = value[m][0]
                left = m + 1
            else:
                right = m -1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)