class Node:
    def __init__(self,k=0,v=0,prev=None,next=None):
        self.k,self.v,=k,v
        self.prev,self.next=prev,next

class DLL:
    def __init__(self):
        self.head,self.tail=Node(),Node()
        self.head.next,self.tail.prev=self.tail,self.head
    
    def pushright(self,node):
        prev,next=self.tail.prev,self.tail
        prev.next=next.prev=node
        node.next,node.prev=next,prev
    
    def pop(self,node):
        # if node==self.head or node==self.tail: raise Exception("DLL is empty, cannot pop")
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        # node.next=node.prev=None
        return node
    
    def popleft(self): return self.pop(self.head.next)
    
class LRUCache:

    def __init__(self, cap: int):
        self.cap=cap
        self.dll=DLL()
        self.k2n=defaultdict(lambda : Node())

    def get(self, k: int) -> int:
        if k not in self.k2n: return -1
        node=self.k2n[k]
        node=self.dll.pop(node)
        self.dll.pushright(node)
        return node.v

    def put(self, k: int, v: int) -> None:
        if self.get(k)!=-1:
            self.k2n[k].v=v
            return
        if self.cap==len(self.k2n):
            todel=self.dll.popleft()
            del self.k2n[todel.k]
            # del todel

        node=Node(k,v)
        self.k2n[k]=node
        self.dll.pushright(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


