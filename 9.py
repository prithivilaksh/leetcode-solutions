class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0: return False
        t,y=x,0
        while t:
            y=y*10+(t%10)
            t//=10
        return x==y