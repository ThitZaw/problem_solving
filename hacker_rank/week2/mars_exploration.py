def marsExploration(s):
    # Write your code here
    output = 0
    for i,j in zip(s,'SOS' * (int(len(s)/3))):
        output += i != j
    return output
print(marsExploration('SOSSPSSQSSOR'))