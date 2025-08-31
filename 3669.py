# class Solution:
#     def minDifference(self, n: int, k: int) -> List[int]:
#         f=[]
#         for d in range(1,n+1):
#             if n%d==0: f.append(d)
#         m=len(f)
#         res,arr=[],[]
#         best=inf

#         def backtrack(pos,q,k):
#             nonlocal res,best
#             if k==0:
#                 if q==1:
#                     diff=max(arr)-min(arr)
#                     if diff<best: best,res=diff,arr[:]
#                 return
            
#             for i in range(pos,m):
#                 d=f[i]
#                 if q%d==0:
#                     arr.append(d)
#                     backtrack(i,q//d,k-1)
#                     arr.pop()
#         backtrack(0,n,k)
#         return res


# class Solution:
#     def minDifference(self, n: int, k: int) -> List[int]:

#         res,arr=[],[]
#         best=inf

#         def backtrack(l,q,k,mi,mx):
#             nonlocal res,best
#             diff=mx-mi
#             if diff>=best: return
#             if k==0:
#                 if q==1: best,res=diff,arr[:]
#                 return
            
#             for d in range(l,n+1):
#                 if q<d:break
#                 if q%d==0:
#                     arr.append(d)
#                     backtrack(l,q//d,k-1,min(mi,d),max(mx,d))
#                     arr.pop()

#         backtrack(1,n,k,inf,0)
#         return res


# class Solution:
#     def minDifference(self, n: int, k: int) -> List[int]:
#         f=[]
#         for d in range(1,n+1):
#             if n%d==0: f.append(d)
#         m=len(f)
#         res,arr=[],[]
#         best=inf

#         def backtrack(pos,q,k,mi,mx):
#             nonlocal res,best
#             diff=mx-mi
#             if diff>=best: return
#             if k==0:
#                 if q==1: best,res=diff,arr[:]
#                 return
            
#             for i in range(pos,m):
#                 d=f[i]
#                 if q<d:break
#                 if q%d==0:
#                     arr.append(d)
#                     backtrack(i,q//d,k-1,min(mi,d),max(mx,d))
#                     arr.pop()

#         backtrack(0,n,k,inf,0)
#         return res

# class Solution:
#     def minDifference(self, n: int, k: int) -> List[int]:
        
#         def factorss(n,k):
#             if k==1: return [[n]]
#             res=[]
#             for d in range(int(pow(n,1/k)+1),0,-1):
#                 if n%d==0:
#                     for rem in factorss(n//d,k-1):
#                         res.append([d]+rem)
#             return res
        
#         res,best=[],inf
#         for f in factorss(n,k):
#             mi,mx=min(f),max(f)
#             if mx-mi<best:
#                 best=mx-mi
#                 res=f
#         return res

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        
        def factorss(n,k):
            if k==1: yield [n];return
            for d in range(int(pow(n,1/k)+1),0,-1):
                if n%d==0:
                    for rem in factorss(n//d,k-1):
                        yield([d]+rem)
        
        res,best=[],inf
        for f in factorss(n,k):
            mi,mx=min(f),max(f)
            if mx-mi<best:
                best=mx-mi
                res=f
        return res
            