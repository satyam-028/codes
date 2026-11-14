import sys
 
N = 5  # No of rows and column

# Function to find the row with max sum
 
 
def colMaxSum(mat):
 
    # Variable to store index of row
    # with maximum
    idx = -1
 
    # Variable to store max sum
    maxSum = -sys.maxsize
 
    # Traverse matrix row wise
    for i in range(0, N):
        sum = 0
 
        # calculate sum of row
        for j in range(0, N):
            sum += mat[i][j]
 
        # Update maxSum if it is less than
        # current sum
        if (sum > maxSum):
            maxSum = sum
 
            # store index
            idx = i
 
    res = [idx, maxSum]
 
    # return result
    return res
 
 
# Driver code
mat = [[1, 2, 3, 4, 5],
       [5, 3, 1, 4, 2],
       [5, 6, 7, 8, 9],
       [0, 6, 3, 4, 12],
       [9, 7, 12, 4, 3]]
 
ans = colMaxSum(mat)
print("Row", ans[0] + 1, "has max sum", ans[1])
 

