# After becoming famous, the CodeBots decided to move into a new building together. 
# Each of the rooms has a different cost, and some of them are free, but there's a 
# rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, 
# they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the
#  room, your task is to return the total sum of all rooms that are suitable for the CodeBots
#   (ie: add up all the values that don't appear below a 0).
def matrixElementsSum(matrix):
    m,n = len(matrix), len(matrix[0])
    ghosts = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                if (i,j) not in ghosts:
                    ghosts.append((i,j))
                    for k in range(i,m-1):
                        ghosts.append((k+1,j))
    ans = 0
    for i in range(m):
        for j in range(n):
            if (i,j) not in ghosts:
                ans+=matrix[i][j]
    return ans
