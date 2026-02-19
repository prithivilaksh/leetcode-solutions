class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row,col,box=defaultdict(set),defaultdict(set),defaultdict(set)
        all=set("123456789")
        empty=[]

        def add(i,j,v):
            board[i][j]=v
            row[i].add(v)
            col[j].add(v)
            box[(i//3,j//3)].add(v)
        
        def discard(i,j,v):
            board[i][j]="."
            row[i].discard(v)
            col[j].discard(v)
            box[(i//3,j//3)].discard(v)

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".": add(i,j,board[i][j])
                else: empty.append((i,j))
        
        def cand(i,j):
            return all-row[i]-col[j]-box[(i//3,j//3)]
        
        def backtrack():
            if not empty: return True
            empty.sort(key=lambda ij: -len(cand(ij[0],ij[1])))
            i,j=empty.pop()
            
            for v in cand(i,j):
                add(i,j,v)
                if backtrack(): return True
                discard(i,j,v)

            empty.append((i,j))
            return False

        backtrack()


        