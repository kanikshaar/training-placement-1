class Solution(object):
    def isValidSudoku(self, board):
        d={}
        for i in range(len(board)):
            for j in range(len(board)):
                x=board[i][j]
                if board[i][j]!=".":
                    if board[i][j] not in d:
                        d[board[i][j]]=[]
                    else:
                        for a in d[x]:
                            m=a[0]
                            n=a[1]
                            if m==i or n==j:
                                return False
                            if (m//3==i//3) and (n//3==j//3):
                                return False                      
                    d[board[i][j]].append([i,j])
        return True
