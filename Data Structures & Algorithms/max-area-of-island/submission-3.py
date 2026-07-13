from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0
        if not grid:
            return output

        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()
        q = deque([])

        def bfs():
            left, right, up, down = (0,-1),(0,1),(-1,0),(1,0)
            temp = 0
            while q:
                row, col = q.popleft()
                visited.add((row,col))
                temp+=1
                for dr, dc in (left, right, up, down):
                    rowz = row + dr
                    colz = col + dc
                    if(
                        0<=rowz<n_rows and
                        0<=colz<n_cols and
                        (rowz, colz) not in visited and
                        grid[rowz][colz] == 1
                    ):
                        visited.add((rowz,colz))
                        q.append((rowz,colz))
            return temp                



        for row in range(n_rows):
            for col in range(n_cols):
                if((row,col) not in visited and
                grid[row][col]==1):
                    q.append((row, col))
                    temp = bfs()
                    output = max(temp, output)
        
        # Time complexity - O(m*n)
        # Space complexity - O(m*n)

        return output

