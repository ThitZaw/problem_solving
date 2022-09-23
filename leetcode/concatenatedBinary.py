from operator import truediv


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bin_val_list = [bin(num).replace("0b", "") for num in range(1,n+1)]
        return int("".join(bin_val_list),2)%(10**9+7)
    
sol = Solution()
res = sol.concatenatedBinary(12)
print(res)