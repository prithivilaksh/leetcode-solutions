# class Solution:
#     def addOperators(self, nums: str, target: int) -> List[str]:
        
#         def backtrack(pos,path,prev,acc):
#             if pos==n and acc==target: res.append(path)

#             for i in range(pos+1,n+1):
#                 if i==pos+1 or nums[pos]!="0":
#                     x=int(nums[pos:i])
#                     if prev is None:
#                         backtrack(i,nums[pos:i],x,x)
#                     else:
#                         backtrack(i,path+"+"+nums[pos:i],x,acc+x)
#                         backtrack(i,path+"-"+nums[pos:i],-x,acc-x)
#                         backtrack(i,path+"*"+nums[pos:i],prev*x,acc-prev+prev*x)
#         n,res=len(nums),[]
#         backtrack(0,"",None,0)
#         return res
            
class Solution:
    def addOperators(self, nums: str, t: int) -> List[str]:

        def backtrack(pos,acc,prev,path):
            if pos==n:
                if acc==t: res.append(path)
                return
            s=""
            for i in range(pos,n):
                s+=nums[i]
                curr=int(s)
                if s[0]=="0" and len(s)>1: break
                if pos==0: backtrack(i+1,curr,curr,s)
                else:
                    backtrack(i+1,acc+curr,curr,path+"+"+s)
                    backtrack(i+1,acc-curr,-curr,path+"-"+s)
                    backtrack(i+1,acc-prev+prev*curr,prev*curr,path+"*"+s)
        n,res=len(nums),[]
        backtrack(0,0,0,"")
        return res












