class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0]*n
        for i in range(m):
            new_rows = [1]*n
            for j in range(n-2, -1, -1):
                new_rows[j] = new_rows[j+1] + row[j]
            row = new_rows
        return row[0]