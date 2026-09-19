# class Solution:
#     def numberOfWeakCharacters(self, props: list[list[int]]) -> int:
        
#         props.sort(reverse=True)
#         res=mx=0
#         for k,g in groupby(props,key=lambda x:x[0]):
#             nmx=0
#             for _,d in g:
#                 if mx>d: res+=1
#                 nmx=max(nmx,d)
#             mx=max(mx,nmx)
#         return res


# class Solution:
#     def numberOfWeakCharacters(self, props: list[list[int]]) -> int:

#         res=mx=0
#         for k,g in groupby(sorted(props,reverse=True),key=lambda x:x[0]):
#             nmx=0
#             for _,d in g:
#                 if mx>d: res+=1
#                 nmx=max(nmx,d)
#             mx=max(mx,nmx)
#         return res


class Solution:
    def numberOfWeakCharacters(self, props: list[list[int]]) -> int:

        props.sort(key=lambda x: (-x[0],x[1]))
        n=len(props)
        res=mx=0
        for i in range(n):
            if props[i][1]<mx:res+=1
            mx=max(mx,props[i][1])
        return res
