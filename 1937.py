# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         @cache
#         def dp(i,j):
#             if i==m-1: return points[i][j]
#             next=max(dp(i+1,k)-abs(j-k) for k in range(n))
#             return points[i][j]+next
        
#         m,n=len(points),len(points[0])
#         return max(dp(0,j) for j in range(n))

# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         m,n=len(points),len(points[0])

#         for i in range(1,m):
#             for j in range(n):
#                 res=0
#                 for k in range(n):
#                     res=max(res,points[i][j]+points[i-1][k]-abs(j-k))
#                 points[i][j]=res

#         return max(points[m-1])


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m,n=len(points),len(points[0])
        lmx,rmx=[0]*n,[0]*n
        for i in range(1,m):

            lmx[0]=points[i-1][0]
            for j in range(1,n):
                lmx[j]=max(lmx[j-1]-1,points[i-1][j])

            rmx[n-1]=points[i-1][n-1]
            for j in range(n-2,-1,-1):
                rmx[j]=max(rmx[j+1]-1,points[i-1][j])

            for j in range(n):
                points[i][j]+=max(lmx[j],rmx[j])

        return max(points[m-1])


# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         m,n=len(points),len(points[0])
#         lmx,rmx=[0]*n,[0]*n
#         for i in range(1,m):

#             lmx[0]=points[i-1][0]
#             for j in range(1,n):
#                 lmx[j]=max(lmx[j-1]-1,points[i-1][j])

#             rmx[n-1]=points[i-1][n-1]
#             for j in range(n-2,-1,-1):
#                 rmx[j]=max(rmx[j+1]-1,points[i-1][j])

#                 points[i][j]+=max(lmx[j],rmx[j])
            
#             points[i][n-1]+=lmx[n-1]

#         return max(points[m-1])