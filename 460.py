class Node:
    def __init__(self,k=0,v=0,prev=None,next=None):
        self.k=k
        self.v=v
        self.prev=prev
        self.next=next

class DLL:
    def __init__(self):
        self.head,self.tail=Node(),Node()
        self.head.next,self.tail.prev=self.tail,self.head
    
    def pushright(self,node):
        next,prev=self.tail,self.tail.prev
        node.next,node.prev=next,prev
        next.prev=prev.next=node
    
    def popleft(self):
        node=self.head.next
        self.pop(node)
        return node
    
    def pop(self,node):
        node.prev.next,node.next.prev=node.next,node.prev
    
    def isEmpty(self): return self.head.next==self.tail


class LFUCache:

    def __init__(self, cap: int):
        self.cap=cap
        self.knode=defaultdict(lambda: Node())
        self.kcnt=defaultdict(int)
        self.cntdll=defaultdict(lambda : DLL())
        self.mincnt=0


    def get(self, k: int) -> int:
        if k not in self.kcnt: return -1
        
        node,cnt=self.knode[k],self.kcnt[k]
        dll=self.cntdll[cnt]

        dll.pop(node) 
        if dll.isEmpty() and self.mincnt==cnt: self.mincnt+=1

        self.kcnt[k]=cnt+1
        self.cntdll[cnt+1].pushright(node)

        return node.v

        

    def put(self, k: int, v: int) -> None:
        if k in self.knode:
            self.knode[k].v=v
            self.get(k)
            return
        if self.cap==len(self.knode):
            node=self.cntdll[self.mincnt].popleft()
            del self.knode[node.k]
            del self.kcnt[node.k]
            del node
        
        node=Node(k,v)
        self.cntdll[1].pushright(node)
        self.knode[k]=node
        self.kcnt[k]=self.mincnt=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# class LFUCache:

#     def __init__(self, cap: int):
#         self.kv=defaultdict(int)
#         self.kf=defaultdict(int)
#         self.fk=defaultdict(OrderedDict)
#         self.cap=cap
#         self.minf=0


#     def get(self, k: int) -> int:
#         if k not in self.kv: return -1
#         f=self.kf[k]
#         del self.fk[f][k]
#         if not self.fk[f]: 
#             del self.fk[f]
#             if self.minf==f:self.minf+=1
#         self.fk[f+1][k]=1
#         self.kf[k]=f+1
#         return self.kv[k]


#     def put(self, k: int, v: int) -> None:
#         if k in self.kv:
#             self.kv[k]=v
#             self.get(k)
#             return
        
#         if len(self.kv)==self.cap:
#             # evck=next(iter(self.fk[self.minf]))
#             # del self.fk[self.minf][evck]
#             evck,_=self.fk[self.minf].popitem(last=False)
#             if not self.fk[self.minf]: del self.fk[self.minf]
#             del self.kv[evck]
#             del self.kf[evck]
        
#         self.kv[k]=v
#         self.kf[k]=1
#         self.fk[1][k]=1
#         self.minf=1


# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


