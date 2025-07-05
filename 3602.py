class Solution:
    def concatHex36(self, n: int) -> str:

        m="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def helper(n,b):
            res=""
            while n>0:
                r=n%b
                n=n//b
                res=m[r]+res
            return res
                
        return helper(n**2,16)+helper(n**3,36)