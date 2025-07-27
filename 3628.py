#Exclusive
# class Solution:
#     def numOfSubsequences(self, s: str) -> int:

#         n=len(s)
#         lcnt=[0]*n
#         tcnt=[0]*n

#         cnt=0
#         for i in range(n):
#             lcnt[i]=cnt
#             if s[i]=="L":cnt+=1
        
#         cnt=0
#         for i in range(n-1,-1,-1):
#             tcnt[i]=cnt
#             if s[i]=="T":cnt+=1
        
#         lres=cres=tres=c=0
#         for i in range(n):
#             if s[i]=="C":
#                 lres+=(1+lcnt[i])*tcnt[i]
#                 tres+=lcnt[i]*(tcnt[i]+1)
#                 cres+=lcnt[i]*tcnt[i]
#             if i+1<n:
#                 c=max(c,lcnt[i+1]*tcnt[i])
            
#         return max(lres,cres+c,tres)

#Inclusive
class Solution:
    def numOfSubsequences(self, s: str) -> int:

        n=len(s)
        lcnt=[0]*n
        tcnt=[0]*n

        cnt=0
        for i in range(n):
            if s[i]=="L":cnt+=1
            lcnt[i]=cnt

        cnt=0
        for i in range(n-1,-1,-1):
            if s[i]=="T":cnt+=1
            tcnt[i]=cnt
        
        lres=cres=tres=c=0
        for i in range(n):
            if s[i]=="C":
                lres+=(1+lcnt[i])*tcnt[i]
                tres+=lcnt[i]*(tcnt[i]+1)
                cres+=lcnt[i]*tcnt[i]
            c=max(c,lcnt[i]*tcnt[i])
            
        return max(lres,cres+c,tres)

        