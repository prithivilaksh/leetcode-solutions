class Node:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class DLL:
    def __init__(self):
        head,tail=Node(),Node()
        head.next,tail.prev=tail,head
        self.head,self.tail=head,tail
    
    def popleft(self):
        return self.pop(self.head.next)
    
    def pop(self,node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        return node
    
    def pushright(self,node):
        tail=self.tail
        prev,next=tail.prev,tail
        prev.next=next.prev=node
        node.prev,node.next=prev,next

class LRUCache:

    def __init__(self, cap: int):
        self.cap=cap
        self.dll=DLL()
        self.k2n={}

    def get(self, key: int) -> int:
        if key not in self.k2n: return -1
        node=self.k2n[key]
        node=self.dll.pop(node)
        self.dll.pushright(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if self.get(key)!=-1:
            node=self.k2n[key]
            node.val=val
        else: 
            self.cap-=1
            if self.cap<0:
                self.cap+=1
                node=self.dll.popleft()
                del self.k2n[node.key]
                del node
            node=Node(key,val)
            self.k2n[key]=node
            self.dll.pushright(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)