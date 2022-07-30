class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = []
        for value in nums1:
            if value in nums2:
                counter.append(value)
                del nums2[nums2.index(value)]
                
        return counter
                    
sol = Solution()
sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])