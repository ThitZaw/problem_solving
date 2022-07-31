from operator import le


def characterReplacement(s,k):
    res,count = 0,{}
    l = 0
    for r in range(len(s)):
        word = s[l:r+1]
        count[s[r]] = 1 + count.get(s[r],0)
        while (r - l +1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
            word = s[l:r+1]
        res = max(res, r - l + 1)
     
    return res

print(characterReplacement(s='AABABBA',k=1))