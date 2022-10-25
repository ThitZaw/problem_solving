class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            output = '11'
            for i in range(3,n+1):
                prev, count = output[0], 0
                temp = ''
                for l in output: # loop through output
                    if prev != l:
                        temp += str(count) + prev
                        prev, count = l, 1
                    else: 
                        count += 1
                        
                temp += str(count) + prev # add last char count with char
                output = temp
            return output  
    
sol = Solution()
res = sol.countAndSay(n=5)
print(res)     