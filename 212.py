class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        Trie=lambda:defaultdict(Trie)
        
        root=Trie()
        for word in words:
            node=root
            for c in word:
                node=node[c]
            node["#"]=word
        
        m,n,res=len(board),len(board[0]),[]

        def dfs(i,j,node):
            if i<0 or i==m or j<0 or j==n or board[i][j] not in node: return 
            nextnode=node[board[i][j]]
            tmp=board[i][j]
            board[i][j]="."
            if '#' in nextnode: res.append(nextnode.pop('#'))
            dfs(i+1,j,nextnode)
            dfs(i-1,j,nextnode)
            dfs(i,j+1,nextnode)
            dfs(i,j-1,nextnode)
            board[i][j]=tmp
            if not nextnode: del node[tmp]

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i,j,root)
        return res