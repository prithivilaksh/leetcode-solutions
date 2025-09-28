class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        res,p=[],1
        while n:
            r=n%10
            n=n//10
            if r: res.append(r*p)
            p=p*10

        return res[::-1]