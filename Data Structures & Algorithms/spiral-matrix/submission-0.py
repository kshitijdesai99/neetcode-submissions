class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = (-1,0)
        right = (1,0)
        up = (0,-1)
        down = (0,1)

        x = 0 
        y = 0
        upper_bound = 0
        lower_bound = len(matrix)-1
        left_bound = 0
        right_bound = len(matrix[0])-1

        output = []

        while upper_bound<=lower_bound and left_bound<=right_bound:
            for dir in ('r','d','l','u'):
                if upper_bound > lower_bound or left_bound > right_bound:
                    break
                if dir == 'r':
                    i = left_bound
                    while(i<=right_bound):
                        output.append(matrix[y][i])
                        i+=1
                    upper_bound+=1
                    x = right_bound
                elif dir == 'd':
                    j = upper_bound
                    while(j<=lower_bound):
                        output.append(matrix[j][x])
                        j+=1
                    right_bound-=1
                    y = lower_bound
                elif dir == 'l':
                    i = right_bound
                    while(i>=left_bound):
                        output.append(matrix[y][i])
                        i-=1
                    lower_bound-=1
                    x = left_bound
                else:
                    j = lower_bound
                    while(j>=upper_bound):
                        output.append(matrix[j][x])
                        j-=1
                    left_bound+=1
                    y = upper_bound
        # Time complexity - O(m*n)
        # Space complexity - O(1)
        return output