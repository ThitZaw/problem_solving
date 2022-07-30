def diagonalDifference(arr):
    # Write your code here
    right_diagonal = left_diagonal = 0
    for row_index,row in enumerate(arr):
        if row_index == 0:
            continue
        left_diagonal += row[row_index-1]
        right_diagonal += row[(len(row)-1)-(row_index-1)]
    return abs(left_diagonal - right_diagonal)

output = diagonalDifference(arr=[[3],[11,2,4],[4,5,6],[10,8,-12]])
print(output)