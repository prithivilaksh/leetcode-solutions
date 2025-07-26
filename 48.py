# class Solution:
#     def rotate(self, mat: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         mat.reverse()
#         n=len(mat)
#         for i in range(n):
#             for j in range(i+1,n):
#                 mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
        


# class Solution:
#     def rotate(self, mat: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n=len(mat)
#         t=l=0
#         b=r=n-1
#         while l<r:
#             for i in range(r-l):
#                 tl=mat[t][l+i]
#                 tr=mat[t+i][r]
#                 br=mat[b][r-i]
#                 bl=mat[b-i][l]

#                 mat[t+i][r]=tl
#                 mat[b][r-i]=tr
#                 mat[b-i][l]=br
#                 mat[t][l+i]=bl

#             t+=1;b-=1
#             l+=1;r-=1



class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(mat)
        t=l=0
        b=r=n-1
        while l<r:
            for i in range(r-l):

                tmp=mat[t][l+i]
                mat[t][l+i]=mat[b-i][l]
                mat[b-i][l]=mat[b][r-i]
                mat[b][r-i]=mat[t+i][r]
                mat[t+i][r]=tmp

            t+=1;b-=1
            l+=1;r-=1

        
        