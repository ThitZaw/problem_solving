class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        each magazine character count must have the same char count as ransomNote 
        if ransomNote "aa" then magazine must have character 'a' count = 2 
        """
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))
        
            
sol = Solution()
print(sol.canConstruct(ransomNote = "a", magazine = "b"))