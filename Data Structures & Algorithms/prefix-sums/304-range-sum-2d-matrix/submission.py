class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        Prefix sum

        1 3
        4 5

        0, 0, 1, 1

        -> 0 0 0
           0 1 4
           0 5 13  

           0[a] 0 0[b]
           0    1 4
           0[c] 5 13[d]
           result = d - b - c + a 
        '''
        m, n = len(matrix), len(matrix[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for r in range(1, m+1):
            for c in range(1, n+1):
                prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - \
                    prefix[r-1][c-1] + matrix[r-1][c-1]

        self.prefix = prefix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        row1=0, col1=0, row2=1, col2=1
        self.prefix[2][2] - self.prefix[0][1] - self.prefix[1][0] + self.prefix[0][0]

        13 - 0 - 0 + 0
        '''
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - \
            self.prefix[row2 + 1][col1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)