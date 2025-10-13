class Solution:
    def strStr(self, s: str, p: str) -> int:
        
        m,n=len(s),len(p)
        lps=[0]*n
        i,j=0,1
        while j<n:
            if p[i]==p[j]:
                lps[j]=i+1
                i+=1;j+=1
            elif i!=0: i=lps[i-1]
            else: j+=1
        
        i=j=0
        while j<m:
            if p[i]==s[j]:
                i+=1;j+=1
                if i==n: return j-n
            elif i!=0: i=lps[i-1]
            else: j+=1
            
        return -1