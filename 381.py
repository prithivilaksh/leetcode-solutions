class RandomizedCollection:

    def __init__(self):
        self.ind=defaultdict(set)
        self.arr=[]
    
    def getstate(self): return self.ind,self.arr

    def insert(self, val: int) -> bool:
        ind,arr=self.getstate()
        ind[val].add(len(arr))
        arr.append(val)
        return len(ind[val])==1

    # def remove(self, val: int) -> bool:
    #     ind,arr=self.getstate()
    #     if not ind[val]: return False
        
    #     indtbr=ind[val].pop()

    #     otherval=arr.pop()
    #     otherind=len(arr)

    #     if indtbr!=otherind:

    #         ind[otherval].discard(otherind)
    #         ind[otherval].add(indtbr)
    #         arr[indtbr]=otherval

    #     return True

    def remove(self, val: int) -> bool:
        ind,arr=self.getstate()
        if not ind[val]: return False
        
        indtbr=ind[val].pop()

        otherval,otherind=arr[-1],len(arr)-1

        ind[otherval].add(indtbr)
        ind[otherval].discard(otherind)
        arr[indtbr]=otherval
        arr.pop()

        return True
        

    def getRandom(self) -> int: return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()