class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_col = 0
        r_col = len(matrix[0]) - 1
        u_row = 0
        b_row = len(matrix) - 1

        col_picker = -1
        while(u_row <= b_row):
            mid = u_row + (b_row - u_row)//2
            if(matrix[mid][l_col]<=target and matrix[mid][r_col]>=target):
                col_picker = mid
                break
            elif(matrix[mid][l_col]>=target):
                b_row = mid - 1
            else:
                u_row = mid + 1
        
        while(l_col <= r_col):
            mid = l_col + (r_col - l_col)//2
            if(matrix[col_picker][mid]>target):
                r_col = mid - 1
            elif(matrix[col_picker][mid]<target):
                l_col = mid + 1
            else:
                return True

        return False
            