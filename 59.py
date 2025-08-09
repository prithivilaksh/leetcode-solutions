# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
        
#         l=t=0
#         r,b=n-1,n-1
#         c,res=1,[[0]*n for i in range(n)]
#         while True:
#             if l>r: break
#             for j in range(r-l+1):
#                 res[t][l+j]=c;c+=1
#             t+=1
#             if t>b: break
#             for i in range(b-t+1):
#                 res[t+i][r]=c;c+=1
#             r-=1
#             if l>r: break
#             for j in range(r-l+1):
#                 res[b][r-j]=c;c+=1
#             b-=1
#             if t>b: break
#             for i in range(b-t+1):
#                 res[b-i][l]=c;c+=1
#             l+=1

#         return res

# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
        
#         res=[[0]*n for i in range(n)]
#         dir=((0,1),(1,0),(0,-1),(-1,0))
#         i=j=d=0
#         di,dj=dir[d]
#         for c in range(1,n*n+1):
#             res[i][j]=c
#             if not(0<=i+di<n and 0<=j+dj<n and res[i+di][j+dj]==0):
#                 d=(d+1)%4
#             di,dj=dir[d]
#             i,j=i+di,j+dj
#         return res


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res=[[0]*n for i in range(n)]
        di,dj=0,1
        i=j=0
        for c in range(1,n*n+1):
            res[i][j]=c
            if not(0<=i+di<n and 0<=j+dj<n and res[i+di][j+dj]==0):
                di,dj=dj,-di
            i,j=i+di,j+dj
        return res