# class Node:
#     def __init__(self,prev=None,next=None):
#         self.st=set()
#         self.prev,self.next=prev,next
    
#     def add(self,x): self.st.add(x)

#     def discard(self,x): self.st.discard(x)

# class DLL:
#     def __init__(self):
#         head,tail=Node(),Node()
#         head.next,tail.prev=tail,head
#         self.head,self.tail=head,tail
    
#     @staticmethod
#     def remove(node):
#         prev,next=node.prev,node.next
#         prev.next,next.prev=next,prev
#         node.prev=node.next=None
#         del node

#     @staticmethod
#     def insertBetween(node,prev,next):
#         prev.next=next.prev=node
#         node.prev,node.next=prev,next

#     @staticmethod
#     def insertAfter(node,prev):
#         next=prev.next
#         DLL.insertBetween(node,prev,next)

#     @staticmethod
#     def insertBefore(node,next):
#         prev=next.prev
#         DLL.insertBetween(node,prev,next)      

# class AllOne:

#     def __init__(self):
#         self.dll=DLL()
#         self.k2c=defaultdict(int)
#         self.c2n=defaultdict(lambda : Node())
#         self.c2n[0]=self.dll.head

#     def inc(self, key: str) -> None:
#         k2c,c2n,dll=self.k2c,self.c2n,self.dll

#         oldcnt=k2c[key]
#         k2c[key]+=1
#         newcnt=oldcnt+1

#         if newcnt not in c2n:
#             node=c2n[newcnt]
#             dll.insertAfter(node,c2n[oldcnt])
#         c2n[newcnt].add(key)

#         if oldcnt!=0:
#             c2n[oldcnt].discard(key)
#             if len(c2n[oldcnt].st)==0: dll.remove(c2n[oldcnt]); del c2n[oldcnt]


#     def dec(self, key: str) -> None:
#         k2c,c2n,dll=self.k2c,self.c2n,self.dll

#         oldcnt=k2c[key]
#         k2c[key]-=1
#         newcnt=oldcnt-1

#         if newcnt!=0:
#             if newcnt not in c2n:
#                 node=c2n[newcnt]
#                 dll.insertBefore(node,c2n[oldcnt])
#             c2n[newcnt].add(key)

#         c2n[oldcnt].discard(key)
#         if len(c2n[oldcnt].st)==0: dll.remove(c2n[oldcnt]); del c2n[oldcnt]
        

#     def getMaxKey(self) -> str:
#         for x in self.dll.tail.prev.st: return x
#         return ""

#     def getMinKey(self) -> str:
#         for x in self.dll.head.next.st: return x
#         return ""


# # # Your AllOne object will be instantiated and called as such:
# # # obj = AllOne()
# # # obj.inc(key)
# # # obj.dec(key)
# # # param_3 = obj.getMaxKey()
# # # param_4 = obj.getMinKey()


# class Node:
#     def __init__(self,prev=None,next=None):
#         self.st=set()
#         self.prev,self.next=prev,next
    
#     def add(self,x): self.st.add(x)

#     def discard(self,x): self.st.discard(x)

# class DLL:
#     def __init__(self):
#         head,tail=Node(),Node()
#         head.next,tail.prev=tail,head
#         self.head,self.tail=head,tail
    
#     @staticmethod
#     def remove(node):
#         prev,next=node.prev,node.next
#         prev.next,next.prev=next,prev
#         node.prev=node.next=None
#         del node

#     @staticmethod
#     def insertBetween(node,prev,next):
#         prev.next=next.prev=node
#         node.prev,node.next=prev,next

#     @staticmethod
#     def insertAfter(node,prev):
#         next=prev.next
#         DLL.insertBetween(node,prev,next)

#     @staticmethod
#     def insertBefore(node,next):
#         prev=next.prev
#         DLL.insertBetween(node,prev,next)      

# class AllOne:

#     def __init__(self):
#         self.dll=DLL()
#         self.k2c=defaultdict(int)
#         self.c2n=defaultdict(lambda : Node())
#         self.c2n[0]=self.dll.head
    
#     def upd(self,key,delta) -> Node:
#         k2c,c2n,dll=self.k2c,self.c2n,self.dll

#         oldcnt=k2c[key]
#         k2c[key]+=delta
#         newcnt=oldcnt+delta

#         if newcnt!=0:
#             if newcnt not in c2n:
#                 node=c2n[newcnt]
#                 if delta==1: dll.insertAfter(node,c2n[oldcnt])
#                 else: dll.insertBefore(node,c2n[oldcnt])
#             c2n[newcnt].add(key)

#         if oldcnt!=0:
#             c2n[oldcnt].discard(key)
#             if len(c2n[oldcnt].st)==0: dll.remove(c2n[oldcnt]); del c2n[oldcnt]

#     def inc(self, key: str) -> None: self.upd(key,1)

#     def dec(self, key: str) -> None: self.upd(key,-1)
        
#     def getMaxKey(self) -> str:
#         for x in self.dll.tail.prev.st: return x
#         return ""

#     def getMinKey(self) -> str:
#         for x in self.dll.head.next.st: return x
#         return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()



class Node:
    def __init__(self,prev=None,next=None):
        self.st=set()
        self.prev,self.next=prev,next
    
    def add(self,x): self.st.add(x)

    def discard(self,x): self.st.discard(x)

class DLL:
    def __init__(self):
        head,tail=Node(),Node()
        head.next,tail.prev=tail,head
        self.head,self.tail=head,tail
    
    @staticmethod
    def remove(node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        node.prev=node.next=None
        del node

    @staticmethod
    def insertBetween(node,prev,next):
        prev.next=next.prev=node
        node.prev,node.next=prev,next

    @staticmethod
    def insertAfter(node,prev):
        next=prev.next
        DLL.insertBetween(node,prev,next)

    @staticmethod
    def insertBefore(node,next):
        prev=next.prev
        DLL.insertBetween(node,prev,next)      

class AllOne:

    def __init__(self):
        self.dll=DLL()
        self.k2c=defaultdict(int)
        self.c2n=defaultdict(lambda : Node())
        self.c2n[0]=self.dll.head

    def inc(self, key: str) -> None:
        k2c,c2n,dll=self.k2c,self.c2n,self.dll

        oldcnt=k2c[key]
        k2c[key]+=1
        newcnt=oldcnt+1

        if newcnt not in c2n:
            node=c2n[newcnt]
            dll.insertAfter(node,c2n[oldcnt])
        c2n[newcnt].add(key)

        if oldcnt!=0:
            c2n[oldcnt].discard(key)
            if len(c2n[oldcnt].st)==0: dll.remove(c2n[oldcnt]); del c2n[oldcnt]


    def dec(self, key: str) -> None:
        k2c,c2n,dll=self.k2c,self.c2n,self.dll

        oldcnt=k2c[key]
        k2c[key]-=1
        newcnt=oldcnt-1

        if newcnt!=0:
            if newcnt not in c2n:
                node=c2n[newcnt]
                dll.insertBefore(node,c2n[oldcnt])
            c2n[newcnt].add(key)

        c2n[oldcnt].discard(key)
        if len(c2n[oldcnt].st)==0: dll.remove(c2n[oldcnt]); del c2n[oldcnt]
        

    def getMaxKey(self) -> str:
        for x in self.dll.tail.prev.st: return x
        return ""

    def getMinKey(self) -> str:
        for x in self.dll.head.next.st: return x
        return ""


# # Your AllOne object will be instantiated and called as such:
# # obj = AllOne()
# # obj.inc(key)
# # obj.dec(key)
# # param_3 = obj.getMaxKey()
# # param_4 = obj.getMinKey()