class Solution:
    
    # follow neetcode problem solving
    # how it solve
    
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            # __________         _____________________________________
            # |_(s ,e)_|    |_(s ,e)_|_(s ,e)_|_(s ,e)_|_(s ,e)_|
            #   new[1]  <   interval[i][0]
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # _____________________________________    __________
            # |_(s ,e)_|_(s ,e)_|_(s ,e)_|_(s ,e)_|    |_(s ,e)_|
            #                        interval[i][1]  <  new[0]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapped between interval
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] 
        res.append(newInterval)
        return res
    
sol = Solution()
res = sol.insert(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]],newInterval=[4,8])