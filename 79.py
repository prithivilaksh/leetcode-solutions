# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m,n=len(board),len(board[0])
#         l,vis=len(word),set()
#         def dfs(pos,i,j):
#             if pos==l: return True
#             if i<0 or i==m or j<0 or j==n or word[pos]!=board[i][j] or (i,j) in vis: return False
#             vis.add((i,j))
#             if dfs(pos+1,i+1,j): return True
#             if dfs(pos+1,i-1,j): return True
#             if dfs(pos+1,i,j-1): return True
#             if dfs(pos+1,i,j+1): return True
#             vis.discard((i,j))

#         for i in range(m):
#             for j in range(n):
#                 if board[i][j]==word[0]:
#                     if dfs(0,i,j): return True
#         return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        l=len(word)
        def dfs(pos,i,j):
            if pos==l: return True
            if i<0 or i==m or j<0 or j==n or word[pos]!=board[i][j] : return False
            tmp=board[i][j]
            board[i][j]="#"
            if dfs(pos+1,i+1,j): return True
            if dfs(pos+1,i-1,j): return True
            if dfs(pos+1,i,j-1): return True
            if dfs(pos+1,i,j+1): return True
            board[i][j]=tmp

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(0,i,j): return True
        return False