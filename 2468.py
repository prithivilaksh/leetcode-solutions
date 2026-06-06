# class Solution:
#     def splitMessage(self, msg: str, limit: int) -> List[str]:
        
#         n=len(msg)
#         num=k=0
#         while n+num+(3+len(str(k)))*k >k*limit:
#             k+=1
#             num+=len(str(k))
#             if 3+2*len(str(k))>=limit: return []
        
#         i,res=0,[]
#         for j in range(1,k+1):
#             l=limit-(3+len(str(j))+len(str(k)))
#             curr=msg[i:i+l]
#             res.append(curr+"<"+str(j)+"/"+str(k)+">")
#             i+=l
#         return res

class Solution:
    def splitMessage(self, msg: str, limit: int) -> List[str]:
        
        n=len(msg)
        cnt=num=0

        while n + num + (3+len(str(cnt)))*cnt > cnt*limit:
            cnt+=1
            num+=len(str(cnt))
            if 3+2*len(str(cnt))>=limit: return []
        
        l,res=0,[]
        for i in range(1,cnt+1):
            end="<"+str(i)+"/"+str(cnt)+">"
            r=l+limit-len(end)
            res.append(msg[l:r]+end)
            l=r
        return res

## there is another optimized approach finding optimal cnt

















