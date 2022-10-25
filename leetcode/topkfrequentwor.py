from cgitb import reset
import heapq
class Solution:
    def topKFrequent(self, words, k):
        output = {}
        for word in words:
           output[word] = output.get(word,0) +1
        items = []
        for key,val in output.items():
            heapq.heappush(items,(-val,key))
        res = [heapq.heappop(items)[1] for i in range(k)]
        return res
        
sol = Solution()
res = sol.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)
print(res)