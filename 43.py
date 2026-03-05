# class Solution:
#     def multiply(self, a: str, b: str) -> str:
        
#         def mul(a,c):
#             if c=="0": return "0"
#             c=int(c)
#             res=""
#             n=len(a)
#             carry=0
#             for i in range(n-1,-1,-1):
#                 x=int(a[i])
#                 tot=x*c+carry
#                 res=str(tot%10)+res
#                 carry=tot//10
            
#             if carry: res=str(carry)+res

#             return res


        
#         def add(a,b):
#             res=""
#             i,j,carry=len(a)-1,len(b)-1,0
#             while 0<=i or 0<=j or carry:
#                 tot=carry
#                 if 0<=i:
#                     tot+=int(a[i])
#                     i-=1
#                 if 0<=j:
#                     tot+=int(b[j])
#                     j-=1
#                 res=str(tot%10)+res
#                 carry=tot//10
#             return res
        
#         if len(a)<len(b):a,b=b,a

#         offset,res="",""
#         for i in range(len(b)-1,-1,-1):
#             x=mul(a,b[i])
#             res=add(res,x+offset)
#             offset+="0"
#         return res


class Solution:
    def multiply(self, a: str, b: str) -> str:
        if a=="0" or b=="0": return "0"
        m,n=len(a),len(b)
        res=[0]*(m+n)
        for i in range(m-1,-1,-1):
            x=int(a[i])
            for j in range(n-1,-1,-1):
                y=int(b[j])
                res[i+j+1]+=x*y

        for i in range(m+n-1,-1,-1):
            res[i-1]+=res[i]//10
            res[i]%=10
        if res[0]==0: res=res[1:]
        return "".join(str(x) for x in res)
        


