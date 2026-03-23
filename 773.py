# class Solution:
#     def slidingPuzzle(self, board: List[List[int]]) -> int:
        
#         for i in range(2):
#             for j in range(3): board[i][j]=str(board[i][j])

#         def convert(board):
#             return "".join(board[0])+"".join(board[1])
        
#         def validnei(i,j):
#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<2 and 0<=vj<3: yield vi,vj

#         dq,d,vis=deque([board]),0,set()

#         while dq:
#             for _ in range(len(dq)):
#                 curr=dq.popleft()
#                 if convert(curr)=="123450": return d

#                 for i in range(2):
#                     for j in range(3):
#                         if curr[i][j]=='0':
#                             for vi,vj in validnei(i,j):
#                                 cand=[curr[0][:],curr[1][:]]
#                                 cand[i][j],cand[vi][vj]=cand[vi][vj],cand[i][j]
#                                 candstr=convert(cand)
#                                 if candstr in vis: continue
#                                 vis.add(candstr)
#                                 dq.append(cand)
#             d+=1
#         return -1


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        start = ''.join(str(num) for row in board for num in row)
        
        g = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        dq,d = deque([start]),0
        vis = set([start])
        
        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr == "123450": return d
                u=curr.index('0')
                for v in g[u]:
                    cand = list(curr)
                    cand[u], cand[v] = cand[v], cand[u]
                    candstr = ''.join(cand)
                    if candstr in vis: continue
                    vis.add(candstr)
                    dq.append(candstr)
            d+=1
        return -1