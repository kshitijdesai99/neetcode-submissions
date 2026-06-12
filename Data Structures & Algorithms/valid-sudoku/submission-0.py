class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9,1):
            empty_list = [0]*10
            for j in range(0,9,1):
                if board[i][j]==".":
                    continue
                elif empty_list[int(board[i][j])] >=1:
                    return False
                else:
                    empty_list[int(board[i][j])]+=1
        
        for i in range(0,9,1):
            empty_list = [0]*10
            for j in range(0,9,1):
                if board[j][i]==".":
                    continue
                elif empty_list[int(board[j][i])] >=1:
                    return False
                else:
                    empty_list[int(board[j][i])]+=1

        for i in range(3,9,3):
            for j in range(3,9,3):
                empty_list = [0]*10
                for k in range(i-3,i):
                    for l in range(j-3,j):
                        if board[k][l]==".":
                            continue
                        elif empty_list[int(board[k][l])] >=1:
                            return False
                        else:
                            empty_list[int(board[k][l])]+=1
                    

        
        return True