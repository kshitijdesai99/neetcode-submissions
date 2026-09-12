class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        output = False
        len_word = len(word)
        visited = set()

        def search(row, col, curr = [], start = 0):
            nonlocal output

            if len(curr) == len_word:
                temp = "".join(curr)
                if temp == word:
                    
                    output = True
                return

            directions = [
                (1,0),
                (-1,0),
                (0,-1),
                (0,1)
            ]


            for di, dj in directions:
                i = row + di
                j = col + dj
                if (0<=i<len(board)) and (0<=j<len(board[0])):
                    if (i,j) not in visited:
                        if board[i][j] == word[start]:
                            curr.append(board[i][j])
                            visited.add((i,j))
                            search(i,j,curr, start+1)
                            curr.pop()
                            visited.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    search(
                        row = i,
                        col = j,
                        curr = [board[i][j]],
                        start = 1
                    )
                    visited.remove((i,j))

        # Time : O(MN4^L) m = no of rows, n = no of cols, l = len of word
        # Space : O(L)


        return output