class Solution:
    def findLonelyPixel(self, picture) -> int:
        row_count = [0] * len(picture)
        col_count = [0] * len(picture[0])
        res = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row_count[i] +=1
                    col_count[j]+=1
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and row_count[i]==1 and col_count[j]==1:
                    res+=1
        return res