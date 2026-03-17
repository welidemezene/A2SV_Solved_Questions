class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return 
        
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        # Build the prefix sum table
        for r in range(self.rows):
            for c in range(self.cols):
                self.prefix[r+1][c+1] = (
                    matrix[r][c] 
                    + self.prefix[r][c+1]  
                    + self.prefix[r+1][c]  
                    - self.prefix[r][c]  
                )

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefix[row2+1][col2+1] 
            - self.prefix[row1][col2+1] 
            - self.prefix[row2+1][col1] 
            + self.prefix[row1][col1]
        )