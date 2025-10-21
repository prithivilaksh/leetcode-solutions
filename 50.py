# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
#         @cache
#         def pow(x,n):
#             if n==0: return 1
#             if n==1: return x
#             if n<0:
#                 n=-n
#                 if n&1: return 1/(pow(x,n//2) * pow(x,n//2 +1))
#                 return 1/(pow(x,n//2) * pow(x,n//2))
#             else:
#                 if n&1: return pow(x,n//2) * pow(x,n//2 +1)
#                 return pow(x,n//2) * pow(x,n//2)

        
#         return pow(x,n)

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
#         @cache
#         def pow(x,n):
#             if n==0: return 1
#             if n==1: return x

#             if n<0: n=-n;inverse=True
#             else: inverse=False

#             if n&1: res=pow(x,n//2) * pow(x,n//2 +1)
#             else: res=pow(x,n//2) * pow(x,n//2)

#             if inverse: return 1/res
#             return res
                
        
#         return pow(x,n)



# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
#         @cache
#         def pow(x,n):
#             if n==0: return 1
#             if n==1: return x

#             if n<0: return 1/pow(x,-n)

#             if n&1: return pow(x,n//2) * pow(x,n//2 +1)
#             return pow(x,n//2) * pow(x,n//2)
                
#         return pow(x,n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # idea/observation:
        # 1) x^n = product(x^i) where i is 1,2,4,8,16...
        # 2) for eg x^5 is x^4 * x^1
        # 3) write n in binary, for eg 5 = 101, for every set bit, multiply the pow of x to res

        if n<0: return 1/self.myPow(x,-n)
        powx,res=x,1
        while n:
            if n&1: res*=powx
            powx*=powx
            n>>=1
        return res
