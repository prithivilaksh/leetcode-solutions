from sortedcontainers import SortedList

class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val,self.prev,self.next=val,prev,next

class DLL:
    def __init__(self):
        head,tail=Node(),Node()
        head.next,tail.prev=tail,head
        self.head,self.tail=head,tail
    
    def push(self,val):
        prev,next=self.tail.prev,self.tail
        node=Node(val,prev,next)
        prev.next=next.prev=node
        return node
    
    @staticmethod
    def remove(node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        return node
    
    def pop(self): return self.remove(self.tail.prev)
    
    def top(self): return self.tail.prev
        
class MaxStack:


    def __init__(self) -> None:
        self.st=DLL()
        self.sl=SortedList(key=lambda x:x.val)


    def push(self, x: int) -> None:
        node=self.st.push(x)
        self.sl.add(node)

    def pop(self) -> int:
        node=self.st.pop()
        self.sl.remove(node)
        return node.val


    def top(self) -> int: return self.st.top().val


    def peekMax(self) -> int: return self.sl[-1].val


    def popMax(self) -> int:
        node=self.sl.pop()
        self.st.remove(node)
        return node.val