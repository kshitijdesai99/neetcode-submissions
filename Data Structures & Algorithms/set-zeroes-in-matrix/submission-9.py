class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # init variables
        first_row_zero = False
        first_col_zero = False

        # 1. SAVE 
        for row in range(len(matrix)):
            for cell in range(len(matrix[row])):
                if row == 0:
                    if(matrix[row][cell]==0):
                        first_row_zero = True
                if cell == 0:
                    if(matrix[row][cell]==0):
                        first_col_zero = True

        # 2. MARK
        for row in range(1,len(matrix)):
            for cell in range(1,len(matrix[row])):
                if matrix[row][cell] == 0:
                    matrix[row][0] = 0
                    matrix[0][cell] = 0     

        # 3. APPLY
        for row in range(1,len(matrix)):
            for cell in range(1,len(matrix[row])):
                if matrix[0][cell] == 0 or matrix[row][0] == 0:
                    matrix[row][cell] = 0

        # 4. Finish
        if first_row_zero:
            for cell in range(len(matrix[0])):
                matrix[0][cell] = 0

        if first_col_zero:
            for cell in range(len(matrix)):
                matrix[cell][0] = 0

        # Time complxity - O(mn)
        # Space complexity - O(1)