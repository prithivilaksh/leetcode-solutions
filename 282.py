class Solution:
    def addOperators(self, nums: str, target: int) -> List[str]:
        
        def backtrack(pos,path,prev,acc):
            if pos==n and acc==target: res.append(path)

            for i in range(pos+1,n+1):
                if i==pos+1 or nums[pos]!="0":
                    x=int(nums[pos:i])
                    if prev is None:
                        backtrack(i,nums[pos:i],x,x)
                    else:
                        backtrack(i,path+"+"+nums[pos:i],x,acc+x)
                        backtrack(i,path+"-"+nums[pos:i],-x,acc-x)
                        backtrack(i,path+"*"+nums[pos:i],prev*x,acc-prev+prev*x)
        n,res=len(nums),[]
        backtrack(0,"",None,0)
        return res
            