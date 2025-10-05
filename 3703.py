#TLE
# class Solution:
#     def removeSubstring(self, s: str, k: int) -> str:
#         p="("*k+")"*k

#         m,n=len(s),len(p)
#         lps=[0]*n
        
#         i,j=0,1
#         while j<n:
#             if p[i]==p[j]:
#                 lps[j]=i+1
#                 i+=1;j+=1
#             elif i!=0: i=lps[i-1]
#             else : j+=1

#         i=j=0
#         while j<m:
#             if p[i]==s[j]:
#                 i+=1;j+=1
#                 if i==n: return self.removeSubstring(s[:j-n]+s[j:],k)
#             elif i!=0: i=lps[i-1]
#             else: j+=1
                
#         return s



# class Solution:
#     def removeSubstring(self, s: str, k: int) -> str:
#         open=close=0
#         st=[]
#         for x in s:
                            
#             if x=="(":
#                 if st and st[-1][0]=="(": st[-1][1]+=1
#                 else: st.append(["(",1])

#             if x==")": 
#                 if st and st[-1][0]==")": st[-1][1]+=1
#                 else: st.append([")",1])

#             if len(st)>=2 and st[-1]==[")",k] and st[-2][1]>=k:
#                 st.pop()
#                 st[-1][1]-=k
#                 if st[-1][1]==0: st.pop()

#         res=""
#         for c,t in st:
#             res+=c*t
#         return res


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        st=[]
        for x in s:
                            
            if st and st[-1][0]==x: st[-1][1]+=1
            else: st.append([x,1])

            if len(st)>=2 and st[-1]==[")",k] and st[-2][1]>=k:
                st.pop()
                st[-1][1]-=k
                if st[-1][1]==0: st.pop()

        return "".join(c*t for c,t in st)