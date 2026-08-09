class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a=set()
        b=set()
        c=set()
        n=0
        k=0
        i=0
        for y in range(9):
            a=set()
            b=set()
            c=set()
            n=0
            k=0
            i=0
            for x in range(9):
                if board[x][y]!=".":
                    a.add(board[x][y])
                    n+=1
                if board[y][x]!=".":
                    b.add(board[y][x])
                    k+=1
                ya=y//3*3+x//3
                xa=y%3*3+x%3
                if board[ya][xa]!=".":
                    c.add(board[ya][xa])
                    i+=1
            if len(a)<n or len(b)<k or len(c)<i:
                return False
        return True