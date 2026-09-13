class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        cols = len(matrix[0]) - 1
        rows = len(matrix) - 1

        top = 0
        left = 0
        bottom = rows
        right = cols

        while left<right:
            for offset in range(right-left):
                top_pos = (top, left + offset)
                right_pos = (top+offset, right)
                bottom_pos = (bottom,right-offset)
                left_pos = (bottom-offset, left)

                temp = matrix[top_pos[0]][top_pos[1]]
                matrix[top_pos[0]][top_pos[1]] = matrix[left_pos[0]][left_pos[1]]
                matrix[left_pos[0]][left_pos[1]] = matrix[bottom_pos[0]][bottom_pos[1]]
                matrix[bottom_pos[0]][bottom_pos[1]] = matrix[right_pos[0]][right_pos[1]]
                matrix[right_pos[0]][right_pos[1]] = temp
            top+=1
            left+=1
            bottom-=1
            right-=1