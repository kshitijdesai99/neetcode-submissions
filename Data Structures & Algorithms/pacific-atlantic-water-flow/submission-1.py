class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if((nr,nc) in visited):
                    continue
                if(not(rows>nr>=0)):
                    continue
                if(not(cols>nc>=0)):
                    continue
                if(heights[nr][nc]<heights[r][c]):
                    continue
                dfs(nr,nc,visited)

        for c in range(cols):
            dfs(0,c,pacific)
            dfs(rows-1,c,atlantic)
        
        for r in range(rows):
            dfs(r,0,pacific)
            dfs(r,cols-1,atlantic)

        return(list(pacific.intersection(atlantic)))