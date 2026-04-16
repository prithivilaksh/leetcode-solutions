# class Solution:
#     def minCost(self, b1: List[int], b2: List[int]) -> int:
        
#         cnt=defaultdict(int)
#         for x in b1: cnt[x]+=1
#         for x in b2: cnt[x]-=1

#         l1,l2=[],[]
#         mi=min(cnt)
#         for k in sorted(cnt):
#             c=cnt[k]
#             if c%2==1: return -1
#             if c>0: l1+=[k]*c
#             elif c<0: l2+=[k]*-c
        
#         n,res=len(l1),0
#         for i in range(0,n,2):
#             res+=min(l1[i],l2[n-1-i],2*mi)

#         return res

class Solution:
    def minCost(self, b1: List[int], b2: List[int]) -> int:
        
        cnt=defaultdict(int)
        for x in b1: cnt[x]+=1
        for x in b2: cnt[x]-=1

        mi=min(cnt)
        tobe=[]
        for k in sorted(cnt):
            c=abs(cnt[k])
            if c%2==1: return -1
            tobe+=[k]*(c//2)
        

        return sum([min(2*mi,x) for x in tobe[:len(tobe)//2]])