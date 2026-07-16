from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()
        q = deque([])
        output = 0
        tracker_map = {}

        for row in range(n_rows):
            for col in range(n_cols):
                if(grid[row][col]==2):
                    visited.add((row,col))
                    q.append((row,col))
                    tracker_map[(row,col)] = 0
                elif(grid[row][col]==0):
                    visited.add((row,col))

        while q:
            up, down, left, right = (1,0), (-1,0), (0,-1), (0,1)
            row, col = q.popleft()
            for dr, dc in (up, down, left, right):
                rowz = row + dr
                colz = col + dc
                if(0<=rowz<n_rows and
                    0<=colz<n_cols and
                    (rowz,colz) not in visited and
                    grid[rowz][colz]==1):
                    q.append((rowz,colz))
                    tracker_map[(rowz,colz)] = tracker_map[(row,col)]+1
                    output = max(output, tracker_map[(rowz,colz)])
                    visited.add((rowz, colz))

        print(visited)
        print(len(visited))

        return output if len(visited)>=n_rows*n_cols else -1