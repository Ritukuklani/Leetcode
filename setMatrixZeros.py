class Solution:
    def setZeroes(self, matrix) -> None: # Matrix is of type : List[List[int]]
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_flag = False
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            if matrix[i][0]==0:
                col_flag = True
            for j in range(1, c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1, r):
            if matrix[i][0]==0:
                for j in range(1, c):
                    matrix[i][j] = 0
        for i in range(1, c):
            if matrix[0][i]==0:
                for j in range(1, r):
                    matrix[j][i] = 0
        if matrix[0][0]==0:
            for i in range(c):
                matrix[0][i] = 0
        if col_flag:
            for i in range(r):
                matrix[i][0] = 0
                    