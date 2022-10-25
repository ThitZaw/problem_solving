class Solution:
    def intToRoman(self, num):
        num_map = {1000: "M",900: "CM",500: "D",400: "CD",100: "C",90: "XC", 50: "L",40: "XL",10: "X",9: "IX", 5: "V",4: "IV",1: "I"}
        output = ''
        for key,val in num_map.items():
            while key <= num:
                output += val
                num-=key
        return output
    
sol = Solution()
res = sol.intToRoman(58)
print(res)