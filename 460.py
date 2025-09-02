class Node:
    def __init__(self,k=0,v=0,cnt=1,p=None,n=None):
        self.k=k
        self.v=v
        self.p=p
        self.n=n
        self.cnt=cnt

class DLL:
    def __init__(self):
        h,t=Node(),Node()
        h.n,t.p=t,h
        self.h,self.t=h,t
    
    def pop(self,node):
        p,n=node.p,node.n
        p.n,n.p=n,p
        return node
    
    def popleft(self): return self.pop(self.h.n)
    
    def pushright(self,node):
        t=self.t
        p,n=t.p,t
        p.n=n.p=node
        node.n,node.p=n,p
    
    def isempty(self): return self.h.n==self.t

class LFUCache:

    def __init__(self, cap: int):
        self.cap=cap
        self.min=1
        self.k2node={}
        self.cnt2dll=defaultdict(lambda: DLL())
    
    def poplf(self):
        dll=self.cnt2dll[self.min]
        node=dll.popleft()
        if dll.isempty(): self.min=1
        del self.k2node[node.k]
        del node


    def get(self, k: int) -> int:
        if k not in self.k2node: return -1

        node=self.k2node[k]
        cnt=node.cnt
        dll=self.cnt2dll[cnt]
        
        node=dll.pop(node)
        cnt=node.cnt=cnt+1
        if dll.isempty() and self.min==cnt-1: self.min=cnt

        dll=self.cnt2dll[cnt]
        dll.pushright(node)
        return node.v
        

    def put(self, k: int, v: int) -> None:
        if self.get(k)!=-1:
            self.k2node[k].v=v
            return
        if len(self.k2node)==self.cap: self.poplf()
        node=Node(k,v,1)
        self.min=1
        self.k2node[k]=node
        self.cnt2dll[1].pushright(node)
            


        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)