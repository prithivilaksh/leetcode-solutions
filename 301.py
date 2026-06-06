## TLE
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
        
#         mp=defaultdict(int,{"(":1,")":-1})
#         minremcnt,res,n=26,set(),len(s)

#         def bt(pos,accstr,cnt,remcnt):
#             nonlocal minremcnt,res
#             if cnt<0 or remcnt>minremcnt: return
#             if pos==n:
#                 if cnt==0:
#                     if remcnt==minremcnt: res.add(accstr)
#                     elif remcnt<minremcnt: minremcnt,res=remcnt,set([accstr])
#                 return
            
#             bt(pos+1,accstr+s[pos],cnt+mp[s[pos]],remcnt)

#             bt(pos+1,accstr,cnt,remcnt+1)
        
#         bt(0,"",0,0)

#         return list(res)

# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
        
#         mp=defaultdict(int,{"(":1,")":-1})
#         minremcnt,res,n=inf,set(),len(s)

#         def bt(pos,accstr,cnt,remcnt):
#             nonlocal minremcnt,res
#             if cnt<0 or remcnt>minremcnt: return
#             if pos==n:
#                 if cnt==0:
#                     minremcnt=remcnt
#                     res.add(accstr)
#                 return

#             bt(pos+1,accstr+s[pos],cnt+mp[s[pos]],remcnt)
#             if s[pos] in "()":bt(pos+1,accstr,cnt,remcnt+1)
        
#         bt(0,"",0,0)

#         return list(res)

# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
        
#         def valid(s):
#             cnt=0
#             for c in s:
#                 if c=="(": cnt+=1
#                 elif c==")": cnt-=1
#                 else: continue
#                 if cnt<0: return False
#             return cnt==0
        
#         dq,res,found=deque([s]),[],False

#         while dq:
#             vis=set()
#             for _ in range(len(dq)):
#                 curr=dq.popleft()
#                 if valid(curr):
#                     res.append(curr)
#                     found=True
                
#                 if found: continue

#                 for i in range(len(curr)):
#                     if curr[i] not in "()": continue
#                     cand=curr[:i]+curr[i+1:]
#                     if cand in vis: continue
#                     vis.add(cand)
#                     dq.append(cand)
            

#         return res


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        l,r=0,len(s)-1
        while l<r and s[l]==")":l+=1
        while l<r and s[r]=="(": r-=1
        s=s[l:r+1]

        def valid(s):
            cnt=0
            for c in s:
                if c=="(": cnt+=1
                elif c==")": cnt-=1
                else: continue
                if cnt<0: return False
            return cnt==0
        
        dq,res,found=deque([s]),[],False

        while dq:
            vis=set()
            for _ in range(len(dq)):
                curr=dq.popleft()
                if valid(curr):
                    res.append(curr)
                    found=True
                
                if found: continue

                for i in range(len(curr)):
                    if curr[i] not in "()": continue
                    cand=curr[:i]+curr[i+1:]
                    if cand in vis: continue
                    vis.add(cand)
                    dq.append(cand)

        return res

