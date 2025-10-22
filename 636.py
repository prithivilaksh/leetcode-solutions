# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
#         st,res=[],[0]*n
#         for log in logs:
#             log=log.split(":")
#             cid,ctyp,cts=int(log[0]),log[1],int(log[2])
            
#             if st:
#                 pid,pts=st[-1]
#                 res[pid]+=cts-pts
            
#             if ctyp=="end":
#                 st.pop()
#                 res[pid]+=1
#                 if st: st[-1][1]=cts+1
#             else: st.append([cid,cts])
#         return res


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        st,res=[],[0]*n
        for log in logs:
            cid,ctyp,cts=log.split(":")
            cid,cts=int(cid),int(cts)
            
            if ctyp=="end":
                res[st.pop()]+=cts-prevts+1
                prevts=cts+1
            else:
                if st: res[st[-1]]+=cts-prevts
                st.append(cid)
                prevts=cts
        return res
