class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        output = False
        len_word = len(word)
        visited = set()

        def search(row = 0, col = 0, curr = [], start = 0):
            nonlocal output
            row_up = row + 1, col
            row_down = row - 1, col
            row_left = row, col - 1
            row_right = row, col + 1
            row_curr = row, col


            if len(curr) == len_word:
                temp = "".join(curr)
                if temp == word:
                    
                    output = True
                return

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (i,j) in (row_up, row_down, row_left, row_right) and (i,j) not in visited:
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

        return output