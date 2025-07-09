class Solution:
    def compressedString(self, word: str) -> str:

        comp,prev,cnt="","",0
        for x in word:
            if x!=prev or cnt==9:
                comp+=str(cnt)+prev
                prev=x
                cnt=1
            else: cnt+=1


        return comp[1:]+str(cnt)+prev

        