# class Solution:
#     def maximalRectangle(self, mat: List[List[str]]) -> int:
        
#         m,n,res=len(mat),len(mat[0]),0
#         h=[0]*(n+1)

#         for i in range(m):
#             st=[]
#             for j in range(n): h[j] = h[j]+1 if mat[i][j]=='1' else 0
#             for j in range(n+1):
#                 while st and h[st[-1]]>h[j]:
#                     ht=h[st.pop()]
#                     wd=(j-1-st[-1]) if st else j
#                     res=max(res,ht*wd)
#                 st.append(j)   
        
#         return res

class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        
        m,n,res=len(mat),len(mat[0]),0
        h=[0]*(n+1)

        for i in range(m):
            st=[-1]
            for j in range(n): h[j] = h[j]+1 if mat[i][j]=='1' else 0
            for j in range(n+1):
                while h[st[-1]]>h[j]:
                    ht=h[st.pop()]
                    wd=j-1-st[-1]
                    res=max(res,ht*wd)
                st.append(j)   
        
        return res

# class Solution:
#     def maximalRectangle(self, mat: List[List[str]]) -> int:
        
#         m,n=len(mat),len(mat[0])
#         h=[0]*(n+1)
#         res=0

#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j]=="1": h[j]+=1
#                 else: h[j]=0
            
#             st=[-1]
#             for r,x in enumerate(h):
#                 while h[st[-1]]>x:
#                     k=st.pop()
#                     res=max(res,h[k]*(r-st[-1]-1))
#                 st.append(r)
            
#         return res

# class Solution:
#     def maximalRectangle(self, mat: List[List[str]]) -> int:
        
#         m,n=len(mat),len(mat[0])
#         h,res=[0]*(n+1),0
#         for i in range(m):
#             for j in range(n):
#                 h[j]=(h[j]+1) if mat[i][j]=="1" else 0
#             st=[]
#             for r,x in enumerate(h):
#                 while st and h[st[-1]]>=x:
#                     ht=h[st.pop()]
#                     l=st[-1] if st else -1
#                     res=max(res,(r-l-1)*ht)
#                 st.append(r)
#         return res
