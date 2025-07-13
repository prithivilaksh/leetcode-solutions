class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length=0
        for c in s:
            if c=="#": length*=2
            elif c.isalpha(): length+=1
            elif c=="*" and length>0: length-=1
        
        if k>=length: return '.'

        for c in s[::-1]:
            if c=="#": 
                length//=2
                if k>=length: k-=length
            elif c.isalpha(): 
                if k==length-1: return c
                length-=1
            elif c=="*": length+=1
            elif c=="%": k=length-1-k
        
        return '.'

