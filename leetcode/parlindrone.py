from cgitb import reset
from gc import collect
import string
import collections
def checkIfPangram(sentence):
    ascii_sting = {i:0 for i in string.ascii_lowercase}
    output = {}
    for i in sentence:
        if i in output:
            output[i]+=1
        else:
            output[i] = 1
    return len(output) == 26
        
    
    
res = checkIfPangram(sentence="sentence")
print(res)