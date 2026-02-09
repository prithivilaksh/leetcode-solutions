class Solution:
    def maxA(self, n: int) -> int:
        idea/obs:
        1) 4 options - A, ctrl A, ctrl C, ctrl V
        2) state transitions:
            A               ->  l+=1
            ctrl A, ctrl C  ->  b=l
            ctrl V          ->  l+=b
        
        def dp(rem,l,b):

            dp(rem-1,l+1,b)
            dp(rem-3,2*l,l)
            dp(rem-1,l+b,b)


