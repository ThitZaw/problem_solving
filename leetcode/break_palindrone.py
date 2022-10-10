class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        for i in range(n//2): # since it was palindrome we can only look at first half of string
            if palindrome[i] != 'a': # if it was not "a" then change it to 'a'
                return palindrome[:i] +"a"+palindrome[i+1:]  

        return palindrome[:-1]+"b"  # if nothing change then change the last char to 'b' since all are a 