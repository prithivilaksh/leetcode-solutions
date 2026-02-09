# class Solution:
#     def simplifyPath(self, path: str) -> str:
        
#         ff,st=[],[]

#         for c in path+"/":
#             if c=="/":
#                 if len(st)==2 and st[-1]=="." and st[-2]==".": 
#                     if ff: ff.pop()
#                     st.clear()
#                 elif len(st)==1 and st[-1]==".": st.clear()
#                 elif st: 
#                     ff.append("".join(st))
#                     st.clear()

#             else: st.append(c)
                
#         res=""
#         for f in ff: res+="/"+f
#         return res if res else "/"


# class Solution:
#     def simplifyPath(self, path: str) -> str:
        
#         ff,st=[],[]

#         for c in path+"/":
#             if c=="/":
#                 if len(st)==2 and st[-1]=="." and st[-2]==".": 
#                     if ff: ff.pop()
#                 elif len(st)==1 and st[-1]==".": pass
#                 elif st: ff.append("".join(st))
#                 st.clear()

#             else: st.append(c)
                
#         res=""
#         for f in ff: res+="/"+f
#         return res if res else "/"


class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        for part in path.split("/"):
            if part=="" or part==".": continue
            elif part=="..":
                if st:st.pop()
            else: st.append(part)

        return "/"+"/".join(st)

