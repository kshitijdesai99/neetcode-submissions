from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0
        if not grid:
            return output

        n_rows, n_cols = len(grid), len(grid[0])

        visited = set()

        def bfs(row,col):
            q = deque([(row,col)])
            while q:
                rowz, colz = q.popleft()
                
                up, down, left, right = (1,0),(-1,0),(0,-1),(0,1)

                for dr, dc in (up, down, left, right):
                    row = rowz + dr
                    col = colz + dc
                    if ((0<=row<n_rows) and
                        (0<=col<n_cols) and
                        grid[row][col] == "1" and
                        (row,col) not in visited):
                        visited.add((row,col))
                        q.append((row,col))

         
        for row in range(n_rows):
            for col in range(n_cols):
                if((row,col) not in visited and 
                grid[row][col] == "1"):
                    print(row,col)
                    visited.add((row,col))
                    output+=1
                    bfs(row,col)
        
        return output