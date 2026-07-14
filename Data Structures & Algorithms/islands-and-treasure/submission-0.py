from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n_rows, n_cols = len(grid), len(grid[0])
        q = deque([])
        visited = set()

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))

        while q:
            up, down, left, right = (-1,0),(1,0),(0,-1),(0,1)
            row, col = q.popleft()
            for dr, dc in (up, down, left, right):
                rowz = row + dr 
                colz = col + dc
                if (0<=rowz<n_rows and
                0<=colz<n_cols and
                (rowz,colz) not in visited and
                grid[rowz][colz]!=-1):
                    grid[rowz][colz] = grid[row][col]+1
                    q.append((rowz,colz))
                    visited.add((rowz, colz))
