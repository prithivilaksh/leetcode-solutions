
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         mpt,mps=defaultdict(int),defaultdict(int)
#         for c in t: mpt[c]+=1

#         l,n,cnt=0,len(t),0
#         ires,res=len(s)+1,""
#         for r,_ in enumerate(s):
#             if mpt[s[r]]>mps[s[r]]:cnt+=1
#             mps[s[r]]+=1

#             while l<r and mpt[s[l]]<mps[s[l]]:
#                 mps[s[l]]-=1
#                 l+=1

#             if cnt==n and r-l+1<ires: 
#                 ires=r-l+1
#                 res=s[l:r+1]
        
#         return res


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         mp=defaultdict(int)
#         for c in t: mp[c]+=1

#         l,cnt=0,len(t)
#         ires,res=len(s)+1,""
#         for r,_ in enumerate(s):

#             if mp[s[r]]>0:cnt-=1
#             mp[s[r]]-=1
#             while cnt==0:
#                 if r-l+1<ires: ires,res=r-l+1,s[l:r+1]
#                 if mp[s[l]]==0: cnt+=1
#                 mp[s[l]]+=1;l+=1
            
#         return res



# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         mp=defaultdict(int)
#         for c in t: mp[c]+=1

#         l,cnt=0,len(t)
#         ires,res=len(s)+1,""
#         for r,_ in enumerate(s):

#             if mp[s[r]]>0:cnt-=1
#             mp[s[r]]-=1
#             if cnt==0:
#                 while cnt==0:
#                     if mp[s[l]]==0: cnt+=1
#                     mp[s[l]]+=1;l+=1
#                 if r-l<ires: ires,res=r-l,s[l-1:r+1]

            
#         return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need=defaultdict(int)
        for c in t: need[c]+=1

        l,cnt,ires,res=0,0,len(s)+1,""
        for r,_ in enumerate(s):
            if need[s[r]]>0: cnt+=1
            need[s[r]]-=1

            while l<r and need[s[l]]<0:
                need[s[l]]+=1
                l+=1
            
            if cnt==len(t) and r-l+1<ires:
                ires=r-l+1
                res=s[l:r+1]
        
        return res















