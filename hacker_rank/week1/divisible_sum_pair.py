from itertools import count


def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
    print(count)
        
        
        
divisibleSumPairs(n = 6, k = 5,ar = [1, 2, 3, 4, 5, 6])