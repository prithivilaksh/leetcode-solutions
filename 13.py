# class Solution:
#     def romanToInt(self, s: str) -> int:
        
#         map={
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }
#         st=[]
#         for c in s:
#             if not st or st[-1]>=map[c]: st.append(map[c])
#             else: st[-1]=map[c]-st[-1]
#         return sum(st)


map={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        
        n,res=len(s),0
        for i,c in enumerate(s):
            if i+1<n and map[c]<map[s[i+1]]: res-=map[c]
            else: res+=map[c]
        return res
