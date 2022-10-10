class Solution:
    
    # follow neetcode problem solving
    # how it solve
    
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            # 1
            # [4,8] > [1,2] # 8 is greater than 2 
            # 5
            # [3,10] < [12,16] no overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval) # append (3,10)
                return res + intervals[i:] # append rest of the greater interval [12,16]
            # 1
            # [1,2],[3,5],[6,7],[8,10],[12,16]
            #     [4,8]   greater than 2 but start = 4 is less than end = 5 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # append [1,2]
            else: # overlapped interval
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] 
                # 2
                # min(3,4),max(5,8) => [3,8],
                # 3
                # min(3,6),max(7,8) => [3,8],
                # 4
                # min(3,8),max(8,10) => [3,10]
        res.append(newInterval)
        return res
    
sol = Solution()
res = sol.insert(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]],newInterval=[4,8])