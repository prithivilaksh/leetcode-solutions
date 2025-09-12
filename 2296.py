# class TextEditor:

#     def __init__(self):
#         self.l=self.r=""

#     def addText(self, text: str) -> None:
#         self.l+=text

#     def deleteText(self, k: int) -> int:
#         l=len(self.l)
#         self.l=self.l[:max(0,l-k)]
#         return l-len(self.l)

#     def cursorLeft(self, k: int) -> str:
#         m=self.l[-k:]
#         self.r=m+self.r
#         self.l=self.l[:-k]
#         return self.l[-10:]

#     def cursorRight(self, k: int) -> str:
#         m=self.r[:k]
#         self.l+=m
#         self.r=self.r[k:]
#         return self.l[-10:]
        


# # Your TextEditor object will be instantiated and called as such:
# # obj = TextEditor()
# # obj.addText(text)
# # param_2 = obj.deleteText(k)
# # param_3 = obj.cursorLeft(k)
# # param_4 = obj.cursorRight(k)

class TextEditor:

    def __init__(self):
        self.l,self.r=[],[]

    def addText(self, text: str) -> None:
        for c in text: self.l.append(c)

    def deleteText(self, k: int) -> int:
        l,cnt=self.l,0
        while self.l and k:
            l.pop()
            k-=1;cnt+=1
        return cnt
    
    def getlast(self,k=10):
        r=len(self.l)
        l=max(0,r-k)
        return ''.join(self.l[l:r])


    def cursorLeft(self, k: int) -> str:
        l,r=self.l,self.r
        while l and k:
            r.append(l.pop())
            k-=1
        return self.getlast()
        

    def cursorRight(self, k: int) -> str:
        l,r=self.l,self.r
        while r and k:
            l.append(r.pop())
            k-=1
        return self.getlast()

        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)