import collections
from itertools import count
class Solution:
    def majorityElement(self, nums):
        num_count = collections.Counter(nums)
        return max(num_count.keys(),key=num_count.get)