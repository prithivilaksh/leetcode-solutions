# class Solution:
#     def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
#         l=t=0
#         r,b=len(mat[0])-1,len(mat)-1
#         res=[]
#         while True:
#             if l>r: break
#             for j in range(r-l+1):
#                 res.append(mat[t][l+j])
#             t+=1
#             if t>b: break
#             for i in range(b-t+1):
#                 res.append(mat[t+i][r])
#             r-=1
#             if l>r: break
#             for j in range(r-l+1):
#                 res.append(mat[b][r-j])
#             b-=1
#             if t>b: break
#             for i in range(b-t+1):
#                 res.append(mat[b-i][l])
#             l+=1

#         return res


# class Solution:
#     def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
#         m,n=len(mat),len(mat[0])
#         res=[]
#         dir=((0,1),(1,0),(0,-1),(-1,0))
#         i=j=d=0
#         di,dj=dir[d]
#         for _ in range(m*n):
#             res.append(mat[i][j])
#             mat[i][j]=None
#             if not(0<=i+di<m and 0<=j+dj<n and mat[i+di][j+dj]!=None):
#                 d=(d+1)%4
#             di,dj=dir[d]
#             i,j=i+di,j+dj
#         return res


class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
        m,n=len(mat),len(mat[0])
        res=[]
        # dir=((0,1),(1,0),(0,-1),(-1,0))
        di,dj=0,1
        i=j=0
        for _ in range(m*n):
            res.append(mat[i][j])
            mat[i][j]=None
            if not(0<=i+di<m and 0<=j+dj<n and mat[i+di][j+dj]!=None):
                di,dj=dj,-di
            i,j=i+di,j+dj
        return res