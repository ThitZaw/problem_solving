class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dic = dict()
        for index, value in enumerate(nums):
            if value in index_dic and index - index_dic[value] <= k:
                return True
            index_dic[value] = index
        return False